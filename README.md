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
| **[output/masters-research.xlsx](output/masters-research.xlsx)** | 7 sheets. The **Cost calculator** is live — tuition, duration and living costs are inputs, totals are formulas, so changing an assumption updates the comparison. 33 shortlist rows, 99 formulas, zero errors |
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
