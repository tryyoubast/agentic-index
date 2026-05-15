from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from typing import Sequence

from .catalog import CatalogError, load_catalog, recommend_projects, search_projects
from .models import Project


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    catalog = load_catalog()

    try:
        if args.command == "list":
            print_project_table(catalog.projects[: args.limit])
        elif args.command == "search":
            print_project_table(search_projects(catalog, args.query)[: args.limit])
        elif args.command == "show":
            print_project_detail(catalog.by_slug(args.slug))
        elif args.command == "recommend":
            print_project_table(
                recommend_projects(
                    catalog,
                    client=args.client,
                    goal=args.goal,
                    limit=args.limit,
                )
            )
        elif args.command == "export":
            projects = catalog.projects[: args.limit] if args.limit else catalog.projects
            if args.format == "json":
                print(json.dumps([project_to_dict(project) for project in projects], indent=2))
            else:
                print(markdown_export(projects))
        else:
            parser.print_help()
            return 1
    except CatalogError as exc:
        parser.error(str(exc))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agentic-index",
        description="Find practical AI coding-agent stack components.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List top projects by stars.")
    list_parser.add_argument("--limit", type=int, default=20)

    search_parser = subparsers.add_parser("search", help="Search the catalog.")
    search_parser.add_argument("query")
    search_parser.add_argument("--limit", type=int, default=20)

    show_parser = subparsers.add_parser("show", help="Show one project.")
    show_parser.add_argument("slug")

    recommend_parser = subparsers.add_parser("recommend", help="Recommend projects.")
    recommend_parser.add_argument("--client", help="Client such as codex, claude-code, cursor, or mcp.")
    recommend_parser.add_argument("--goal", help="Goal such as memory, skills, mcp, hud, or workflow.")
    recommend_parser.add_argument("--limit", type=int, default=10)

    export_parser = subparsers.add_parser("export", help="Export catalog data.")
    export_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    export_parser.add_argument("--limit", type=int)

    return parser


def print_project_table(projects: Sequence[Project]) -> None:
    if not projects:
        print("No projects matched.")
        return

    for project in projects:
        clients = ", ".join(project.clients[:4])
        if len(project.clients) > 4:
            clients += ", ..."
        print(f"{project.slug:32} {project.stars:>7,}  {project.category:13} {clients}")
        print(f"  {project.summary}")


def print_project_detail(project: Project) -> None:
    print(project.name)
    print("=" * len(project.name))
    print(f"Slug: {project.slug}")
    print(f"URL: {project.url}")
    print(f"Stars: {project.stars:,}")
    print(f"Category: {project.category}")
    print(f"Clients: {', '.join(project.clients)}")
    print(f"Use cases: {', '.join(project.use_cases)}")
    print()
    print(project.summary)
    print()
    print(f"Install: {project.install}")
    print(f"Why it matters: {project.why_it_matters}")
    print(f"Caveats: {project.caveats}")


def markdown_export(projects: Sequence[Project]) -> str:
    lines = [
        "# Agentic Index",
        "",
        "Structured index of practical AI coding-agent tools.",
        "",
    ]
    current_category = None
    for project in sorted(projects, key=lambda item: (item.category, -item.stars, item.slug)):
        if project.category != current_category:
            current_category = project.category
            lines.extend([f"## {project.category.title()}", ""])
        lines.extend(
            [
                f"### [{project.name}]({project.url})",
                "",
                f"- Slug: `{project.slug}`",
                f"- Stars: `{project.stars:,}`",
                f"- Clients: `{', '.join(project.clients)}`",
                f"- Use cases: `{', '.join(project.use_cases)}`",
                f"- Summary: {project.summary}",
                f"- Why it matters: {project.why_it_matters}",
                f"- Caveats: {project.caveats}",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def project_to_dict(project: Project) -> dict[str, object]:
    raw = asdict(project)
    raw["clients"] = list(project.clients)
    raw["use_cases"] = list(project.use_cases)
    raw["tags"] = list(project.tags)
    return raw


if __name__ == "__main__":
    raise SystemExit(main())
