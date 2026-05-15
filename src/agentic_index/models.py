from __future__ import annotations

from dataclasses import dataclass


VALID_CATEGORIES = {
    "context",
    "memory",
    "skills",
    "subagents",
    "mcp",
    "hud",
    "session",
    "orchestration",
    "security",
    "workflow",
    "learning",
}


REQUIRED_FIELDS = {
    "slug",
    "name",
    "url",
    "summary",
    "category",
    "clients",
    "use_cases",
    "stars",
    "install",
    "why_it_matters",
    "caveats",
    "tags",
}


@dataclass(frozen=True)
class Project:
    slug: str
    name: str
    url: str
    summary: str
    category: str
    clients: tuple[str, ...]
    use_cases: tuple[str, ...]
    stars: int
    install: str
    why_it_matters: str
    caveats: str
    tags: tuple[str, ...]

    @classmethod
    def from_dict(cls, raw: dict[str, object]) -> "Project":
        missing = REQUIRED_FIELDS - set(raw)
        if missing:
            raise ValueError(f"missing fields: {', '.join(sorted(missing))}")

        category = _expect_str(raw["category"], "category")
        if category not in VALID_CATEGORIES:
            raise ValueError(f"unknown category: {category}")

        url = _expect_str(raw["url"], "url")
        if not url.startswith("https://github.com/"):
            raise ValueError(f"url must be a GitHub URL: {url}")

        stars = raw["stars"]
        if not isinstance(stars, int) or stars < 0:
            raise ValueError("stars must be a non-negative integer")

        return cls(
            slug=_expect_str(raw["slug"], "slug"),
            name=_expect_str(raw["name"], "name"),
            url=url,
            summary=_expect_str(raw["summary"], "summary"),
            category=category,
            clients=_expect_str_tuple(raw["clients"], "clients"),
            use_cases=_expect_str_tuple(raw["use_cases"], "use_cases"),
            stars=stars,
            install=_expect_str(raw["install"], "install"),
            why_it_matters=_expect_str(raw["why_it_matters"], "why_it_matters"),
            caveats=_expect_str(raw["caveats"], "caveats"),
            tags=_expect_str_tuple(raw["tags"], "tags"),
        )

    def haystack(self) -> str:
        parts = [
            self.slug,
            self.name,
            self.summary,
            self.category,
            *self.clients,
            *self.use_cases,
            *self.tags,
        ]
        return " ".join(parts).lower()


def _expect_str(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value


def _expect_str_tuple(value: object, field: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{field} must be a non-empty list")
    items: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"{field} must contain only non-empty strings")
        items.append(item)
    return tuple(items)
