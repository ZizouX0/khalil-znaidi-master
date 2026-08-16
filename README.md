# Claude Skills

60 Agent Skills installed under [`.claude/skills/`](.claude/skills). Claude Code
picks them up automatically for this project — no further wiring needed.

## Setup

Most of the skills are prose-only and work as soon as the repo is checked out.
About a dozen ship executable code and need system and language dependencies:

```bash
scripts/setup-skill-deps.sh
```

Verify the skills themselves at any time:

```bash
python3 scripts/validate-skills.py    # 60/60 skills valid
```

## What's here

| Group | Skills |
| --- | --- |
| Documents | `docx`, `pdf`, `pptx`, `xlsx` |
| Design & visuals | `algorithmic-art`, `canvas-design`, `brand-guidelines`, `frontend-design`, `theme-factory`, `web-design-guidelines`, `web-artifacts-builder`, `slack-gif-creator` |
| Web / scraping | `firecrawl` plus `firecrawl-{agent,crawl,download,interact,map,monitor,parse,scrape,search}` |
| Engineering practice | `test-driven-development-tdd`, `systematic-debugging`, `root-cause-tracing`, `verification-before-completion`, `testing-anti-patterns`, `condition-based-waiting`, `defense-in-depth-validation`, `using-git-worktrees`, `finishing-a-development-branch` |
| Planning & review | `writing-plans`, `executing-plans`, `requesting-code-review`, `code-review-reception`, `subagent-driven-development`, `dispatching-parallel-agents` |
| Thinking tools | `brainstorming-ideas-into-designs`, `collision-zone-thinking`, `inversion-exercise`, `meta-pattern-recognition`, `preserving-productive-tensions`, `scale-game`, `simplification-cascades`, `tracing-knowledge-lineages`, `when-stuck-problem-solving-dispatch` |
| Skill authoring | `skill-creator`, `writing-skills`, `find-skills`, `getting-started-with-skills`, `sharing-skills`, `gardening-skills-wiki`, `pulling-updates-from-skills-repository`, `testing-skills-with-subagents` |
| Other | `claude-api`, `mcp-builder`, `webapp-testing`, `doc-coauthoring`, `internal-comms`, `remembering-conversations` |

## Changes made to the upstream skills

The archive mixed two frontmatter dialects. Both load in Claude Code, but only
one is valid for packaging and upload, so 31 skills were normalized:

- **`name`** set to the directory slug (was Title Case, e.g. `Systematic Debugging`).
- **`when_to_use`** folded into `description` using the exact `"{description} - {when_to_use}"`
  join Claude Code applies at runtime, so the text the model sees is unchanged.
- **`version`** / **`languages`** / **`context`** moved under `metadata`, which the
  spec allows, so nothing is lost.

Three further fixes:

- `claude-api` — description trimmed from 1068 to under the 1024-char limit,
  keeping every trigger and skip rule.
- `pdf/scripts/convert_pdf_to_images.py` — created the output directory instead
  of crashing with `FileNotFoundError` when it did not already exist.
- `remembering-conversations/tool` — `getDbPath()` now honours `TEST_DB_PATH`.
  Three test files set it but nothing read it, so the suite wrote to the user's
  real conversation index at `~/.config/superpowers/conversation-index/db.sqlite`
  and orphan counts accumulated across runs (1 → 4 → 7). Tests now pass 18/18
  and leave the real index alone.

`mcp-builder/scripts/requirements.txt` was pinned to `mcp>=1.1.0,<2`: mcp 2.0
renamed `streamablehttp_client` to `streamable_http_client` and dropped the
`headers=` parameter that `connections.py` depends on.

## Known issues

- `remembering-conversations/tool` has three pre-existing TypeScript type errors
  (`npx tsc --noEmit`) caused by `^`-ranged dependencies resolving to newer
  versions. They are type-only — the tool runs through `tsx`, which strips types
  without checking, and all 18 tests pass. Left alone rather than rewriting
  against third-party API drift.
- `gardening-skills-wiki`'s lint scripts expect the upstream wiki layout
  (`skills/<category>/<skill-name>` with a `when_to_use` field), so they report
  findings against this flat, spec-normalized install. The scripts run correctly;
  the convention simply differs.
