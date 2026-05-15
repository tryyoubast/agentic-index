# Maintainer Notes

Agentic Index should stay useful before it gets large. The catalog is a map for
developers choosing AI coding-agent tools, not a dump of every related repo.

## Positioning

Agentic Index helps developers answer a practical question:

> Which tools should I look at for this agent client and workflow?

Keep public copy focused on that job. Avoid internal strategy language, growth
targets, or claims that the catalog is complete.

## Suggested Copy

AI coding tools now span:

- MCP servers
- Codex skills
- Claude Code tools
- memory systems
- HUDs
- subagents
- workflow kits

The hard part is choosing a stack that fits your client and goal.

Agentic Index is a structured catalog plus CLI:

```bash
agentic-index recommend --client codex --goal skills
agentic-index recommend --client claude-code --goal memory
agentic-index search mcp
```

No account. No telemetry. No paid API. Just a local catalog you can inspect,
query, and export.

## CI

The repository includes `docs/ci.example.yml`. Copy it to
`.github/workflows/ci.yml` after the GitHub token used for pushing has the
`workflow` scope.

## Audience

- Codex users looking for skills and subagents.
- Claude Code users comparing memory, HUD, and workflow tools.
- Developers entering MCP for the first time.
- Tool authors who want a structured ecosystem index.

## What Not To Claim

- Do not claim the index is complete.
- Do not claim project star counts are live unless refreshed.
- Do not claim endorsement by listed projects.
- Do not guarantee any project is safe to install.
