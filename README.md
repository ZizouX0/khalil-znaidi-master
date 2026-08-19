# khalil-znaidi-master

Two things live in this repository:

1. **[European master's programme research](#1-the-research)** — a full study of where a Tunisian marketing graduate can realistically do a master's in Europe, with costs, entry rules, funding and an application timeline.
2. **[60 Claude Agent Skills](#2-the-skills)** — installed, validated and working.

---

## 1. The research

**The question:** a Tunisian *licence* holder in Marketing (GPA ~12–13/20, native French, no English test, transcript showing 146 ECTS instead of the usual 180) wants a European master's in AI-for-marketing, digital marketing, music marketing or music business — affordably, with a realistic route to work afterwards.

### The deliverables

Read them in order. Each is written for the student directly, in plain language.

| File | What it answers | Read it if you want… |
|---|---|---|
| **[01-ects-analysis.md](output/01-ects-analysis.md)** | Is the 146-credit transcript a real problem? | The short answer: **almost certainly not** — Tunisian law fixes the licence at 180 credits, and the capitalisation rules produce transcripts that under-count by design. Includes a 7-question checklist to settle it from his own paperwork |
| **[02-country-comparison.md](output/02-country-comparison.md)** | Which countries are actually open? | Tuition, language, credential stance, post-study rights and **visa deposit** for 20 countries — plus why Norway and Luxembourg are closed and Germany is open |
| **[03-programmes.md](output/03-programmes.md)** | **The full programme list** | Every master's found that he can realistically enter and afford — by direction, by tier, with cost, entry wording and the 146 verdict. Plus everything **excluded**, and why |
| **[04-shortlist.md](output/04-shortlist.md)** | Where should he actually apply? | The twelve best bets, ranked, with the reasoning and the risks for each |
| **[05-funding.md](output/05-funding.md)** | How does he pay for it? | Every scheme he is genuinely eligible for, by deadline — and a documented list of what is **closed** to him, so he doesn't chase it |
| **[06-action-plan.md](output/06-action-plan.md)** | What does he do, and when? | A month-by-month timeline back from autumn 2027, an honest read on his profile, and a one-language strategy |

### The same content in other formats

| File | Notes |
|---|---|
| **[output/masters-research.xlsx](output/masters-research.xlsx)** | 7 sheets covering **all 81 programmes**. The **Cost calculator** is live — tuition, duration and living costs are inputs, totals are formulas, so changing an assumption updates the comparison. 99 formulas, zero errors |
| **[output/pdf/masters-research-full-report.pdf](output/pdf/masters-research-full-report.pdf)** | All six documents as one 36-page report with a cover |
| **output/pdf/01–06** | The six documents as individual PDFs |

### The five findings that matter most

| # | Finding |
|---|---|
| 1 | **The 146 credits are bookkeeping, not a missing year.** A module is only "capitalised" at ≥10/20, but students pass by compensation — so the transcript silently drops 5–8 modules. A free letter from his faculty defuses it |
| 2 | **He does not need an English test to apply.** EUBA Bratislava requires none at any stage, Corvinus assesses English in its own entrance exam, Bergamo accepts 6 ECTS of English from the bachelor's |
| 3 | **The cheapest real degrees cost €0–900 in total** — Slovakia (€0), Spain (~€886), Italy (€157–390/yr) |
| 4 | **Tuition is rarely the barrier. The visa deposit is** — €14,500 France, €14,600 Norway, €11,904 Germany |
| 5 | **Music marketing barely exists** as an affordable accredited European master's. Fifteen independent sweeps found two options on the continent |

### How it was researched, and where the limits are

Roughly 25 research agents across a phased plan: a credential-eligibility gate first, then one agent per country, thematic sweeps (Erasmus Mundus, scholarships, music, language pathways, applied sciences, job market), an independent verification pass, and consolidation.

**Being straight about the boundaries:**

- **France, Italy and Spain have no working national catalogue** — one is dead, one 404s, one is JavaScript-only. Those three are systematic institution-by-institution coverage, not a census. The **French IAE network *is* a census** (921 programmes, 37 schools).
- **Almost every 2027/28 deadline is unpublished.** Dates indicate *when in the year to look*, not deadlines to diarise.
- Figures that could not be confirmed on an official source are marked **`NOT VERIFIED`** rather than estimated.
- The verification pass **corrected three material claims**, including one this project had led with. Where a conclusion changed, the documents say so rather than quietly dropping it.

---

## Complete file map

Every file in this repository, and what it is for.

### Root

| Path | What it is |
|---|---|
| **`README.md`** | This file — the guide to everything below |
| **`.gitignore`** | Excludes `node_modules/`, `__pycache__/`, packaged `*.skill` bundles and the `.firecrawl/` cache. The Firecrawl CLI itself warns when this last one is missing |
| **`output/`** | The master's research — all six deliverables plus Excel and PDF versions |
| **`scripts/`** | Two utilities: environment setup and skill validation |
| **`.claude/skills/`** | The 60 Agent Skills |

### `output/` — the research

| File | Format | Contents |
|---|---|---|
| **`01-ects-analysis.md`** | Markdown | Whether the 146-credit transcript blocks him, why it almost certainly doesn't, and a 7-question checklist to confirm from his own paperwork |
| **`02-country-comparison.md`** | Markdown | 20 countries compared on tuition, language, credential stance, post-study rights and **visa deposit** |
| **`03-programmes.md`** | Markdown | **The full programme list** — every viable master's by direction and tier, plus everything excluded and why |
| **`04-shortlist.md`** | Markdown | The twelve strongest bets, ranked, with risks |
| **`05-funding.md`** | Markdown | Every scheme he can actually apply for, by deadline — and what is closed to him |
| **`06-action-plan.md`** | Markdown | Month-by-month timeline, profile assessment, language strategy |
| **`masters-research.xlsx`** | Excel | All of the above as data — see the sheet list below |
| **`pdf/`** | PDF | Print-ready versions |

### `output/masters-research.xlsx` — the seven sheets

| Sheet | Contents |
|---|---|
| **Read me** | How to use the workbook, what the tiers and verdicts mean, and the three things to read first |
| **Cost calculator** | 33 shortlisted programmes. **Blue cells are inputs, black are live formulas** — change tuition, duration or living cost and the totals recalculate. Yellow cells are where no official cost-of-living figure exists |
| **All programmes** | **All 81 programmes** — direction, tier, institution type, language, tuition, the exact entry wording, the 146 verdict and notes. 36 in Direction 1, 35 in Direction 2, 2 in Direction 3, 8 in Direction 4 |
| **Countries** | All 25 countries assessed — tuition, language, 146 stance, post-study rights, visa deposit and verdict |
| **Funding** | Every scheme by deadline, with odds — plus the verified-closed list and why each fails |
| **Action plan** | The timeline as a checklist, with a blank "Done?" column |
| **Excluded** | Everything checked and rejected, with the reason — so nothing gets rediscovered |

### `output/pdf/` — all seven files

| File | Pages | Contents |
|---|---|---|
| **`masters-research-full-report.pdf`** | 36 | All six documents in one, with a cover |
| **`01-ects-analysis.pdf`** | 6 | The 146-credit analysis |
| **`02-country-comparison.pdf`** | 5 | Country comparison |
| **`03-programmes.pdf`** | 9 | The full programme list |
| **`04-shortlist.pdf`** | 5 | The twelve best bets |
| **`05-funding.pdf`** | 5 | Funding by deadline |
| **`06-action-plan.pdf`** | 5 | Timeline and next steps |

### `scripts/`

| File | What it does |
|---|---|
| **`setup-skill-deps.sh`** | Installs everything the skills need — LibreOffice Writer/Impress/Calc, poppler, the Python stack, and the Firecrawl CLI with its axios fix. The container is ephemeral, so this is what makes the environment reproducible |
| **`validate-skills.py`** | Validates every skill's frontmatter against the Agent Skills spec — name format, directory match, description length, allowed keys. Exits non-zero on failure, so it works in CI |

### `.claude/skills/` — all 60

Each is a directory containing a `SKILL.md`; some ship scripts, fonts, templates or reference files as well.

| Skill | What it does | Assets |
|---|---|---|
| `algorithmic-art` | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. | 3 files |
| `brainstorming-ideas-into-designs` | Interactive idea refinement using Socratic method to develop fully-formed designs - when partner describes any feature or project idea, before… | prose only |
| `brand-guidelines` | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. | 1 files |
| `canvas-design` | Create beautiful visual art in .png and .pdf documents using design philosophy. | 82 files |
| `claude-api` | Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. | 48 files |
| `code-review-reception` | Receive and act on code review feedback with technical rigor, not performative agreement or blind implementation - when receiving code review… | prose only |
| `collision-zone-thinking` | Force unrelated concepts together to discover emergent properties - "What if we treated X like Y?" - when conventional approaches feel inadequate… | prose only |
| `condition-based-waiting` | Replace arbitrary timeouts with condition polling for reliable async tests - when tests have race conditions, timing dependencies, or inconsistent… | 1 files |
| `defense-in-depth-validation` | Validate at every layer data passes through to make bugs impossible - when invalid data causes failures deep in execution, requiring validation at… | prose only |
| `dispatching-parallel-agents` | Use multiple Claude agents to investigate and fix independent problems concurrently - when facing 3+ independent failures that can be investigated… | prose only |
| `doc-coauthoring` | Guide users through a structured workflow for co-authoring documentation. | prose only |
| `docx` | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). | 69 files |
| `executing-plans` | Execute detailed plans in batches with review checkpoints - when partner provides a complete implementation plan to execute in controlled batches… | prose only |
| `find-skills` | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...",… | prose only |
| `finishing-a-development-branch` | Complete feature development with structured options for merge, PR, or cleanup - when implementation is complete, all tests pass, and you need to… | prose only |
| `firecrawl` | Search, scrape, and interact with the web via the Firecrawl CLI. | 2 files |
| `firecrawl-agent` | AI-powered autonomous data extraction that navigates complex sites and returns structured JSON. | prose only |
| `firecrawl-crawl` | Bulk extract content from an entire website or site section. | prose only |
| `firecrawl-download` | Download an entire website as local files — markdown, screenshots, or multiple formats per page. | prose only |
| `firecrawl-interact` | Control and interact with a live browser session on any scraped page — click buttons, fill forms, navigate flows, and extract data using natural… | prose only |
| `firecrawl-map` | Discover and list all URLs on a website, with optional search filtering. | prose only |
| `firecrawl-monitor` | Detect when content on a website changes and get notified by webhook or email — no cron jobs, scrapers, or diff scripts required. | prose only |
| `firecrawl-parse` | Efficiently extract and convert the contents of any local file—such as PDF, DOCX, DOC, ODT, RTF, XLSX, XLS, or HTML—into clean, well-formatted… | prose only |
| `firecrawl-scrape` | Extract clean markdown from any URL, including JavaScript-rendered SPAs. | prose only |
| `firecrawl-search` | Web search with full page content extraction. | prose only |
| `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. | 1 files |
| `gardening-skills-wiki` | Maintain skills wiki health - check links, naming, cross-references, and coverage - when adding, removing, or reorganizing skills, or periodically… | 5 files |
| `getting-started-with-skills` | Skills wiki intro - mandatory workflows, search tool, brainstorming triggers - when starting any conversation | 2 files |
| `internal-comms` | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. | 5 files |
| `inversion-exercise` | Flip core assumptions to reveal hidden constraints and alternative approaches - "what if the opposite were true?" - when stuck on unquestioned… | prose only |
| `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. | 10 files |
| `meta-pattern-recognition` | Spot patterns appearing in 3+ domains to find universal principles - when noticing the same pattern across 3+ different domains or experiencing… | prose only |
| `pdf` | Use this skill whenever the user wants to do anything with PDF files. | 11 files |
| `pptx` | Use this skill any time a .pptx file is involved in any way — as input, output, or both. | 62 files |
| `preserving-productive-tensions` | Recognize when disagreements reveal valuable context, preserve multiple valid approaches instead of forcing premature resolution - when… | prose only |
| `pulling-updates-from-skills-repository` | Sync local skills repository with upstream changes from obra/superpowers-skills - when session start indicates new upstream skills available, or… | prose only |
| `remembering-conversations` | Search previous Claude Code conversations for facts, patterns, decisions, and context using semantic or text search - when partner mentions past… | 4790 files |
| `requesting-code-review` | Dispatch code-reviewer subagent to review implementation against plan or requirements before proceeding - when completing tasks, implementing… | 1 files |
| `root-cause-tracing` | Systematically trace bugs backward through call stack to find original trigger - when errors occur deep in execution and you need to trace back to… | 1 files |
| `scale-game` | Test at extremes (1000x bigger/smaller, instant/year-long) to expose fundamental truths hidden at normal scales - when uncertain about… | prose only |
| `sharing-skills` | Contribute skills back to upstream via branch and PR - when you've developed a broadly useful skill and want to contribute it upstream via pull… | prose only |
| `simplification-cascades` | Find one insight that eliminates multiple components - "if this is true, we don't need X, Y, or Z" - when implementing the same concept multiple… | prose only |
| `skill-creator` | Create new skills, modify and improve existing skills, and measure skill performance. | 20 files |
| `slack-gif-creator` | Knowledge and utilities for creating animated GIFs optimized for Slack. | 10 files |
| `subagent-driven-development` | Execute implementation plan by dispatching fresh subagent for each task, with code review between tasks - when executing implementation plans with… | prose only |
| `systematic-debugging` | Four-phase debugging framework that ensures root cause investigation before attempting fixes. | 5 files |
| `test-driven-development-tdd` | Write the test first, watch it fail, write minimal code to pass - when implementing any feature or bugfix, before writing implementation code | prose only |
| `testing-anti-patterns` | Never test mock behavior. | prose only |
| `testing-skills-with-subagents` | RED-GREEN-REFACTOR for process documentation - baseline without skill, write addressing failures, iterate closing loopholes - when creating or… | 1 files |
| `theme-factory` | Toolkit for styling artifacts with a theme. | 12 files |
| `tracing-knowledge-lineages` | Understand how ideas evolved over time to find old solutions for new problems and avoid repeating past failures - when questioning "why do we use… | prose only |
| `using-git-worktrees` | Create isolated git worktrees with smart directory selection and safety verification - when starting feature work that needs isolation from… | prose only |
| `verification-before-completion` | Run verification commands and confirm output before claiming success - when about to claim work is complete, fixed, or passing, before committing… | prose only |
| `web-artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS,… | 4 files |
| `web-design-guidelines` | Review UI code for Web Interface Guidelines compliance. | prose only |
| `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. | 5 files |
| `when-stuck-problem-solving-dispatch` | Dispatch to the right problem-solving technique based on how you're stuck - when stuck and unsure which problem-solving technique to apply for… | prose only |
| `writing-plans` | Create detailed implementation plans with bite-sized tasks for engineers with zero codebase context - when design is complete and you need… | prose only |
| `writing-skills` | TDD for process documentation - test with subagents before writing, iterate until bulletproof - when creating new skills, editing existing skills,… | 2 files |
| `xlsx` | Use this skill any time a spreadsheet file is the primary input or output. | 57 files |

---

## 2. The skills

60 Agent Skills under [`.claude/skills/`](.claude/skills). Claude Code picks them up automatically for this project.

### Setup

```bash
scripts/setup-skill-deps.sh      # system + language dependencies
python3 scripts/validate-skills.py   # → 60/60 skills valid
```

| File | Purpose |
|---|---|
| **[scripts/setup-skill-deps.sh](scripts/setup-skill-deps.sh)** | Installs everything the skills need — LibreOffice modules, poppler, the Python stack, the Firecrawl CLI. The container is ephemeral, so this is what makes the environment reproducible |
| **[scripts/validate-skills.py](scripts/validate-skills.py)** | Checks every skill's frontmatter against the Agent Skills spec — name, description, allowed keys, length limits |

### What's included

| Group | Skills |
|---|---|
| **Documents** | `docx`, `pdf`, `pptx`, `xlsx` |
| **Design & visuals** | `algorithmic-art`, `canvas-design`, `brand-guidelines`, `frontend-design`, `theme-factory`, `web-design-guidelines`, `web-artifacts-builder`, `slack-gif-creator` |
| **Web & scraping** | `firecrawl` + `firecrawl-{agent,crawl,download,interact,map,monitor,parse,scrape,search}` |
| **Engineering practice** | `test-driven-development-tdd`, `systematic-debugging`, `root-cause-tracing`, `verification-before-completion`, `testing-anti-patterns`, `condition-based-waiting`, `defense-in-depth-validation`, `using-git-worktrees`, `finishing-a-development-branch` |
| **Planning & review** | `writing-plans`, `executing-plans`, `requesting-code-review`, `code-review-reception`, `subagent-driven-development`, `dispatching-parallel-agents` |
| **Thinking tools** | `brainstorming-ideas-into-designs`, `collision-zone-thinking`, `inversion-exercise`, `meta-pattern-recognition`, `preserving-productive-tensions`, `scale-game`, `simplification-cascades`, `tracing-knowledge-lineages`, `when-stuck-problem-solving-dispatch` |
| **Skill authoring** | `skill-creator`, `writing-skills`, `find-skills`, `getting-started-with-skills`, `sharing-skills`, `gardening-skills-wiki`, `pulling-updates-from-skills-repository`, `testing-skills-with-subagents` |
| **Other** | `claude-api`, `mcp-builder`, `webapp-testing`, `doc-coauthoring`, `internal-comms`, `remembering-conversations` |

### Changes made to the upstream skills

The archive mixed two frontmatter dialects. Both load in Claude Code, but only one is valid for packaging, so **31 skills were normalised**: `name` set to the directory slug, `when_to_use` folded into `description` using the exact join Claude Code applies at runtime (so the text the model sees is unchanged), and `version`/`languages`/`context` moved under `metadata`.

**Four real bugs were fixed:**

| Skill | Bug |
|---|---|
| `remembering-conversations` | `getDbPath()` ignored `TEST_DB_PATH`, so the test suite wrote to the user's **real** conversation index and orphan counts accumulated across runs. Now 18/18 tests pass and the real index is untouched |
| `pdf` | `convert_pdf_to_images.py` crashed instead of creating its output directory |
| `mcp-builder` | Pinned `mcp<2`; v2 renamed `streamablehttp_client` and dropped the `headers=` parameter the code depends on |
| `claude-api` | Description trimmed under the 1024-character limit, preserving every trigger and skip rule |

### Firecrawl

The ten `firecrawl-*` skills drive the `firecrawl` CLI. Authenticate with your own key — never commit it:

```bash
export FIRECRAWL_API_KEY=fc-...
firecrawl --status
```

`firecrawl-cli` 1.19.6 and its bundled SDK both pin axios 1.15.2, which sends plain-HTTP requests. Behind an HTTPS proxy that only accepts CONNECT, every call fails with `405 Method Not Allowed`. The setup script upgrades axios in **both** copies — upgrading only the top-level one leaves the SDK's nested copy and the 405 persists.

Two usage notes: `download` is an experimental subcommand (`firecrawl x download`) and prompts for confirmation, and `crawl` is **asynchronous** — it returns a job ID, so use `--wait` or poll with `firecrawl crawl <job-id> --status`.

### Known issues

- `remembering-conversations` has three pre-existing TypeScript type errors from `^`-ranged dependency drift. Type-only — the tool runs through `tsx` and all tests pass.
- `gardening-skills-wiki`'s linters expect the upstream wiki layout, so they report findings against this flat, spec-normalised install. The scripts run correctly; the convention differs.
