from __future__ import annotations

import json
from pathlib import Path

from .models import Project


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA_FILE = ROOT / "data" / "projects.json"


class CatalogError(ValueError):
    """Raised when catalog data is invalid."""


class Catalog:
    def __init__(self, projects: list[Project]) -> None:
        self.projects = sorted(projects, key=lambda project: project.stars, reverse=True)
        self._by_slug = {project.slug: project for project in self.projects}

    @classmethod
    def from_file(cls, path: Path = DEFAULT_DATA_FILE) -> "Catalog":
        try:
            raw_projects = json.loads(path.read_text(encoding="utf-8"))
        except OSError as exc:
            raise CatalogError(f"could not read catalog: {path}") from exc
        except json.JSONDecodeError as exc:
            raise CatalogError(f"invalid JSON: {exc}") from exc

        if not isinstance(raw_projects, list):
            raise CatalogError("catalog root must be a list")

        projects: list[Project] = []
        seen: set[str] = set()
        for index, raw_project in enumerate(raw_projects):
            if not isinstance(raw_project, dict):
                raise CatalogError(f"project #{index + 1} must be an object")
            try:
                project = Project.from_dict(raw_project)
            except ValueError as exc:
                raise CatalogError(f"invalid project #{index + 1}: {exc}") from exc
            if project.slug in seen:
                raise CatalogError(f"duplicate slug: {project.slug}")
            seen.add(project.slug)
            projects.append(project)

        return cls(projects)

    def by_slug(self, slug: str) -> Project:
        try:
            return self._by_slug[slug]
        except KeyError as exc:
            raise CatalogError(f"unknown project: {slug}") from exc


def load_catalog(path: Path = DEFAULT_DATA_FILE) -> Catalog:
    return Catalog.from_file(path)


def search_projects(catalog: Catalog, query: str) -> list[Project]:
    terms = [term.lower() for term in query.split() if term.strip()]
    if not terms:
        return catalog.projects

    scored: list[tuple[int, Project]] = []
    for project in catalog.projects:
        score = _match_score(project, terms)
        if score:
            scored.append((score, project))

    return [
        project
        for _, project in sorted(scored, key=lambda item: (-item[0], -item[1].stars, item[1].slug))
    ]


def recommend_projects(
    catalog: Catalog,
    *,
    client: str | None = None,
    goal: str | None = None,
    limit: int = 10,
) -> list[Project]:
    client_key = client.lower() if client else None
    goal_key = goal.lower() if goal else None
    scored: list[tuple[int, Project]] = []

    for project in catalog.projects:
        if client_key and client_key not in project.clients:
            continue
        if goal_key and goal_key not in project.use_cases and goal_key != project.category:
            continue

        score = project.stars
        if goal_key:
            if project.category == goal_key:
                score += 25_000
            if goal_key in project.use_cases:
                score += 10_000
            if goal_key in project.tags:
                score += 5_000
        if client_key and client_key in project.clients:
            score += 2_000
            if len(project.clients) == 1:
                score += 25_000
        scored.append((score, project))

    return [
        project
        for _, project in sorted(scored, key=lambda item: (-item[0], item[1].slug))[:limit]
    ]


def _match_score(project: Project, terms: list[str]) -> int:
    haystack = project.haystack()
    score = 0
    for term in terms:
        if term not in haystack:
            return 0
        if term == project.category:
            score += 100
        if term in project.use_cases:
            score += 80
        if term in project.tags:
            score += 60
        if term in project.name.lower():
            score += 40
        score += 1
    score += min(project.stars // 1_000, 100)
    return score
