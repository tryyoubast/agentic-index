# Agentic Index

Find practical tools for your AI coding-agent setup.

Agentic Index is a structured catalog and small CLI for comparing Codex skills,
Claude Code tools, MCP servers, memory systems, HUDs, session search, workflow
kits, and agent safety utilities.

Use it when you are building an agent stack and want a short list of relevant
projects instead of another long browser tab pile.

## Quick Start

```bash
git clone https://github.com/tryyoubast/agentic-index.git
cd agentic-index
PYTHONPATH=src python3 -m agentic_index.cli recommend --client codex --goal skills
```

Example output:

```text
awesome-codex-skills             9,728  skills        codex
  Curated practical Codex skills for automating workflows across Codex CLI and API.
codex-skill-manager              1,046  skills        codex
  macOS app for managing Codex skills.
```

## What It Helps With

- Find tools by client: Codex, Claude Code, Cursor, Gemini, MCP, and more.
- Compare projects by category, use case, install path, caveats, and stars.
- Build a starter stack for skills, memory, MCP, HUDs, session search, or orchestration.
- Export the catalog as Markdown or JSON for your own docs and tools.

The catalog is intentionally selective. It favors projects that are useful to
working developers, have public setup instructions, and solve a clear part of
the agentic coding workflow.

## Commands

```bash
PYTHONPATH=src python3 -m agentic_index.cli list --limit 10
PYTHONPATH=src python3 -m agentic_index.cli search memory
PYTHONPATH=src python3 -m agentic_index.cli show context7
PYTHONPATH=src python3 -m agentic_index.cli recommend --client claude-code --goal hud
PYTHONPATH=src python3 -m agentic_index.cli export --format markdown > AGENTIC_INDEX.md
PYTHONPATH=src python3 -m agentic_index.cli export --format json > projects.json
```

Install as a local command:

```bash
python3 -m pip install -e .
agentic-index recommend --client codex --goal skills
```

## Categories

| Category | What it covers |
| --- | --- |
| `context` | code search, retrieval, docs, context engineering |
| `memory` | persistent context and session continuity |
| `skills` | reusable agent capabilities |
| `subagents` | role-based specialist agents |
| `mcp` | Model Context Protocol servers and directories |
| `hud` | live visibility and status surfaces |
| `session` | searchable histories and replay |
| `orchestration` | parallel agents and isolated workspaces |
| `security` | scanners, hardening, and risk tools |
| `workflow` | repeatable development systems |
| `learning` | maps, guides, and field manuals |

## Repository Layout

- `data/projects.json`: the source catalog.
- `src/agentic_index/`: CLI, catalog loading, validation, and recommendation logic.
- `AGENTIC_INDEX.md`: generated Markdown export.
- `public/index.html`: generated static website.
- `docs/starter-stacks.md`: small stack suggestions by workflow.
- `docs/ci.example.yml`: GitHub Actions template.
- `tests/`: standard-library test suite.

## Add A Project

Edit `data/projects.json`, then run:

```bash
PYTHONPATH=src:. python3 -m unittest discover -s tests -v
PYTHONPATH=src:. python3 scripts/generate_site.py
PYTHONPATH=src:. python3 -m agentic_index.cli export --format markdown > AGENTIC_INDEX.md
```

Good entries explain:

- what the project does
- which clients it supports
- how to install or try it
- why a developer might choose it
- what caveats to check before adopting it

See [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar and required fields.

## Principles

- Useful beats exhaustive.
- Structured data beats hand-maintained prose.
- Caveats belong next to recommendations.
- No telemetry, no accounts, no paid API required.
- Every generated artifact should be reproducible locally.

## License

MIT
