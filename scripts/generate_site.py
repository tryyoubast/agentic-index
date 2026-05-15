from __future__ import annotations

import html
from collections import defaultdict
from pathlib import Path

from agentic_index.catalog import Catalog, load_catalog
from agentic_index.models import Project


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "public" / "index.html"


def render_site(catalog: Catalog) -> str:
    categories: dict[str, list[Project]] = defaultdict(list)
    for project in catalog.projects:
        categories[project.category].append(project)

    unique_clients = sorted({client for project in catalog.projects for client in project.clients})
    category_nav = "\n".join(
        f'<a href="#{html.escape(category)}">{html.escape(category)}</a>'
        for category in sorted(categories)
    )
    category_sections = "\n".join(
        render_category(category, projects)
        for category, projects in sorted(categories.items())
    )
    top_projects = "\n".join(
        f"<li><strong>{html.escape(project.name)}</strong><span>{project.stars:,}</span></li>"
        for project in catalog.projects[:8]
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Agentic Index - AI Coding Agent Stack Map</title>
  <meta name="description" content="Structured index and CLI for choosing AI coding-agent stacks.">
  <style>
    :root {{
      color-scheme: light;
      --ink: #161616;
      --muted: #5d646b;
      --line: #d8dde3;
      --paper: #fbfaf7;
      --panel: #ffffff;
      --accent: #0f766e;
      --accent-2: #8a4b0f;
      --code: #eef6f5;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--paper);
      color: var(--ink);
      font: 16px/1.55 ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    header {{
      border-bottom: 1px solid var(--line);
      background: #f5f1e9;
    }}
    .wrap {{
      width: min(1120px, calc(100% - 32px));
      margin: 0 auto;
    }}
    .hero {{
      display: grid;
      gap: 28px;
      grid-template-columns: minmax(0, 1.4fr) minmax(280px, 0.6fr);
      padding: 48px 0 34px;
      align-items: end;
    }}
    h1 {{
      font-size: clamp(38px, 7vw, 76px);
      line-height: 0.95;
      margin: 0 0 18px;
      letter-spacing: 0;
    }}
    .lede {{
      max-width: 760px;
      color: #2f3437;
      font-size: 20px;
      margin: 0;
    }}
    .command {{
      display: inline-flex;
      max-width: 100%;
      margin-top: 24px;
      padding: 10px 12px;
      border: 1px solid #b9c8c5;
      background: var(--code);
      color: #113b36;
      font: 14px/1.4 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      overflow-wrap: anywhere;
    }}
    .stats {{
      display: grid;
      gap: 10px;
      padding: 18px;
      border: 1px solid var(--line);
      background: var(--panel);
    }}
    .stat {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      border-bottom: 1px solid #edf0f2;
      padding-bottom: 8px;
    }}
    .stat:last-child {{ border-bottom: 0; padding-bottom: 0; }}
    nav {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      padding: 18px 0;
    }}
    nav a {{
      color: var(--accent);
      border: 1px solid #b8d5d1;
      background: #eef8f6;
      padding: 5px 9px;
      text-decoration: none;
      font-size: 14px;
    }}
    main {{ padding: 30px 0 56px; }}
    section {{ margin-top: 34px; }}
    h2 {{
      margin: 0 0 14px;
      font-size: 24px;
      text-transform: capitalize;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
    }}
    article {{
      border: 1px solid var(--line);
      background: var(--panel);
      padding: 16px;
      min-height: 220px;
    }}
    h3 {{
      margin: 0 0 8px;
      font-size: 18px;
    }}
    h3 a {{ color: var(--ink); text-decoration-color: var(--accent); }}
    p {{ margin: 0 0 10px; color: #30373b; }}
    .meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin: 12px 0;
    }}
    .pill {{
      border: 1px solid #ded8ca;
      background: #faf7ef;
      color: #473d2d;
      padding: 3px 7px;
      font-size: 12px;
    }}
    .stars {{
      color: var(--accent-2);
      font-weight: 700;
    }}
    .top-list {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    .top-list li {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      padding: 8px 0;
      border-bottom: 1px solid #edf0f2;
    }}
    footer {{
      border-top: 1px solid var(--line);
      padding: 24px 0;
      color: var(--muted);
    }}
    @media (max-width: 820px) {{
      .hero {{ grid-template-columns: 1fr; padding-top: 36px; }}
      .grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap hero">
      <div>
        <h1>Agentic Index</h1>
        <p class="lede">Stop hunting through awesome lists. Pick your agent stack in seconds: Codex skills, Claude Code workflows, MCP servers, memory layers, HUDs, and session tools.</p>
        <div class="command">python -m agentic_index.cli recommend --client codex --goal skills</div>
      </div>
      <aside class="stats" aria-label="Catalog stats">
        <div class="stat"><strong>{len(catalog.projects)}</strong><span>curated projects</span></div>
        <div class="stat"><strong>{len(unique_clients)}</strong><span>clients covered</span></div>
        <div class="stat"><strong>{len(categories)}</strong><span>categories</span></div>
        <ul class="top-list">{top_projects}</ul>
      </aside>
    </div>
  </header>
  <div class="wrap">
    <nav aria-label="Categories">
      {category_nav}
    </nav>
    <main>
      {category_sections}
    </main>
  </div>
  <footer>
    <div class="wrap">Generated from <code>data/projects.json</code>. Local-first, no account, no telemetry.</div>
  </footer>
</body>
</html>
"""


def render_category(category: str, projects: list[Project]) -> str:
    cards = "\n".join(render_project(project) for project in projects)
    return f"""<section id="{html.escape(category)}">
  <h2>{html.escape(category)}</h2>
  <div class="grid">
    {cards}
  </div>
</section>"""


def render_project(project: Project) -> str:
    tags = "".join(f'<span class="pill">{html.escape(tag)}</span>' for tag in project.tags[:5])
    clients = "".join(
        f'<span class="pill">{html.escape(client)}</span>' for client in project.clients[:5]
    )
    return f"""<article>
  <h3><a href="{html.escape(project.url)}">{html.escape(project.name)}</a></h3>
  <p class="stars">{project.stars:,} stars</p>
  <p>{html.escape(project.summary)}</p>
  <div class="meta">{clients}</div>
  <p><strong>Why:</strong> {html.escape(project.why_it_matters)}</p>
  <p><strong>Watch:</strong> {html.escape(project.caveats)}</p>
  <div class="meta">{tags}</div>
</article>"""


def write_site(catalog: Catalog, output: Path = DEFAULT_OUTPUT) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_site(catalog), encoding="utf-8")


def main() -> int:
    write_site(load_catalog())
    print(f"wrote {DEFAULT_OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
