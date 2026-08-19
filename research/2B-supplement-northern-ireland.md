# 2B supplement — Northern Ireland gap closed (orchestrator)

Agent 2B ran out of WebSearch budget and had no Firecrawl key, so it left
Northern Ireland `NOT VERIFIED` — flagging it as "the most plausible remaining
cheap-UK route." Closed here on **2026-08-17** using
`firecrawl scrape --proxy auto --wait-for 8000` (QUB had returned 403 to the agent).

## Result: NEITHER Northern Ireland university is affordable. Hypothesis dead.

| Institution | Programme | International fee 2026/27 | Verdict |
|---|---|---|---|
| **Queen's University Belfast** | Postgraduate taught, Fee Rate 1 (classroom-based — covers business/marketing) | **£23,000/year** | **EXCLUDED** — far above the €15,000 filter |
| **Ulster University** | MSc Digital Marketing Communication and Leadership | **£18,310/year** | **EXCLUDED** — above the filter |

Sources, both checked 2026-08-17:
- QUB: https://www.qub.ac.uk/Study/international-students/tuition-fees/ — table "Students first enrolling in 2026/27", Fee Rate 1 = £23,000 (Rate 2, laboratory, £27,600)
- Ulster: https://www.ulster.ac.uk/courses/202627/digital-marketing-communication-and-leadership-40426 — "International Fees £18,310.00" (home fee £7,490)

## Why this matters

The gap between the home fee and the international fee is the whole story. QUB
charges Northern Ireland students **£7,700** and international students
**£23,000** — three times as much. Ulster charges **£7,490** vs **£18,310**.
Northern Ireland is cheap to *live* in and cheap for *local* students; it is not
cheap for a Tunisian applicant. The intuition that NI would be a budget UK route
is wrong, and it is wrong by a wide margin.

**This confirms Agent 2B's verdict rather than softening it:** the UK is viable
only through the three specific institutions it identified (York St John,
Wrexham, and Westminster as a stretch). It is a shortlist, not a strategy.

## One useful positive detail

Ulster's English requirement is unusually low: **IELTS 6.0 overall with no band
below 5.5** (Trinity ISE Pass at level III also accepted). Most UK master's ask
6.5. That is worth remembering as a benchmark when judging whether his English
is realistically test-ready — but it does not rescue Ulster on cost.

## Still open from 2B's gap list

- TU Dublin and SETU fees — `NOT VERIFIED`
- University of West London fees — `NOT VERIFIED`
- BIMM accreditation and validating body — `NOT VERIFIED` (Agent 3D owns the
  music-school accreditation question; expect it from there)
