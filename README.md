# Agentic Index

**Stop hunting through awesome lists. Pick your agent stack in seconds.**

Agentic Index is a structured, installable map of the AI coding-agent ecosystem:
Codex skills, Claude Code workflows, MCP servers, memory layers, HUDs, session
tools, orchestration, and safety utilities.

It is not another static awesome list. The repo ships a machine-readable catalog,
a zero-dependency CLI, generated Markdown, and a generated static site from the
same source of truth.

## Why This Exists

The strongest public demand signals in AI coding are ecosystem entry points and
workflow accelerators:

| Signal | Stars tracked during launch research |
| --- | ---: |
| `awesome-mcp-servers` | 86k+ |
| `claude-mem` | 75k+ |
| `get-shit-done` | 62k+ |
| `context7` | 55k+ |
| `awesome-claude-code` | 43k+ |
| `claude-hud` | 22k+ |
| `awesome-codex-skills` | 9k+ |

Those projects prove the heat. Agentic Index turns that scattered ecosystem into
a practical, queryable stack map.

## Quick Start

```bash
git clone https://github.com/tryyoubast/agentic-index.git
cd agentic-index
PYTHONPATH=src python3 -m agentic_index.cli recommend --client codex --goal skills
```

Useful commands:

```bash
PYTHONPATH=src python3 -m agentic_index.cli list --limit 10
PYTHONPATH=src python3 -m agentic_index.cli search memory
PYTHONPATH=src python3 -m agentic_index.cli show context7
PYTHONPATH=src python3 -m agentic_index.cli recommend --client claude-code --goal hud
PYTHONPATH=src python3 -m agentic_index.cli export --format markdown > AGENTIC_INDEX.md
```

## What You Get

- `data/projects.json`: structured catalog of agentic coding tools.
- `agentic-index` CLI: search, show, recommend, and export.
- `public/index.html`: generated static website.
- `scripts/generate_site.py`: reproducible site generator.
- `tests/`: standard-library test suite, no pytest required.
- `docs/starter-stacks.md`: small recommended stacks by workflow.
- `docs/ci.example.yml`: GitHub Actions workflow template.
- `AGENTIC_INDEX.md`: generated Markdown export.

## Example Recommendations

For Codex skills:

```bash
PYTHONPATH=src python3 -m agentic_index.cli recommend --client codex --goal skills
```

For Claude Code visibility:

```bash
PYTHONPATH=src python3 -m agentic_index.cli recommend --client claude-code --goal hud
```

For MCP discovery:

```bash
PYTHONPATH=src python3 -m agentic_index.cli recommend --client mcp --goal mcp
```

## Catalog Categories

- `context`: documentation, code search, retrieval
- `memory`: persistent context and session continuity
- `skills`: reusable agent capabilities
- `subagents`: role-based specialist agents
- `mcp`: Model Context Protocol servers and directories
- `hud`: live visibility and status surfaces
- `session`: searchable histories and replay
- `orchestration`: parallel agents and isolated workspaces
- `security`: scanners, hardening, and risk tools
- `workflow`: repeatable development systems
- `learning`: maps, guides, and field manuals

## Add A Project

Edit `data/projects.json`, then run:

```bash
PYTHONPATH=src:. python3 -m unittest discover -s tests -v
PYTHONPATH=src:. python3 scripts/generate_site.py
```

New entries should be useful to working developers, not just interesting demos.
Prefer projects with clear installation steps, active maintenance, and visible
community demand.

## Roadmap

- Star and freshness refresh script.
- Generated `AGENTIC_INDEX.md` export committed in releases.
- Client-specific starter stacks for Codex, Claude Code, Cursor, OpenCode, and Gemini.
- Optional GitHub Pages deployment.
- Community-maintained quality badges.

## Principles

- Useful beats exhaustive.
- Structured data beats hand-maintained prose.
- Star count is a signal, not a religion.
- No telemetry, no accounts, no paid API required.
- Every generated artifact should be reproducible locally.

## License

MIT
