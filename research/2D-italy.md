# 2D — ITALY

**Agent 2D · scope: Italy · all checks performed 2026-08-17 unless stated.**
**Target intake: AUTUMN 2027 (a.a. 2027/2028).**

---

## 1. BOTTOM LINE

Italy is the strongest affordability play found so far, and the reason is not
scholarships — it is the **ordinary fee system**. Italian public universities set
tuition by ISEE (family economic indicator), and international students whose
family lives abroad get an **ISEE parificato** (or, at some universities, a
direct foreign-income assessment). At the University of Bologna the verified
2026/27 rule is that **an ISEE at or below €27,000 means a student contribution
of exactly €0** — the total annual outlay is the fixed **€157.04** (regional tax
€140 + stamp €16 + insurance €1.04). A Sousse family will fall far below €27,000
on almost any realistic reckoning. On top of that sits the **regional DSU
scholarship**, explicitly open to non-EU students: ER-GO (Emilia-Romagna) pays a
verified **€7,171.11/year** to a *fuori sede* student with ISEE ≤ €16,666.67,
plus fee exemption, plus a subsidised residence place and canteen. That
combination — near-zero tuition plus a maintenance grant — is qualitatively
different from anything a tuition discount elsewhere can do. The catch is
paperwork, not money: every income and family document must be issued by Tunisian
authorities, legalised by the Italian Embassy in Tunis and translated, on a hard
autumn deadline, and a missed deadline pushes the student straight into the top
fee band. **Tunisia is NOT on the MUR "particularly poor countries" list** (I
verified the 2026/27 decree text directly), so the €200-flat-fee route does not
apply — the ISEE route is the one that matters.
On programmes: Italy is thin on named "digital marketing" *lauree magistrali* in
English but not empty (Salerno, Milano-Bicocca), decent in Italian, and
surprisingly strong on **direction 3/4 hybrids** — **UniBo GIOCA** (English,
LM-76, explicitly covers "music and the recording industry") and **Ca' Foscari
IMCC** (English, LM-77) are the two best finds in this scope. Italian for a
native French speaker is genuinely **Tier B**, and opening the Italian-taught
market roughly triples the option set.

---

## 2. COVERAGE STATEMENT — what I searched and what I did not find

**Languages used:** Italian first (primary), then English.

**Databases / portals used:**
- **Universitaly** (universitaly.it, the MUR national portal) — used for the
  official non-EU pre-enrolment procedure and visa deadlines. **Gap:** the
  portal's course-search endpoint returned 404 to my fetcher, so I could not run
  a systematic national course-by-course sweep of it. I compensated with
  targeted Italian-language searching plus direct verification on university
  sites, but **this is my single biggest coverage gap** — an exhaustive
  Universitaly enumeration was not completed.
- **MUR** (mur.gov.it) — primary decree text on "paesi particolarmente poveri".
- **ER-GO** (Emilia-Romagna DSU) — full 2026/27 bando PDF read in full.
- **DSU Toscana** — scholarship page.
- Official university sites: Bologna, Ca' Foscari Venezia, Milano-Bicocca,
  Salerno, Modena-Reggio, Genova, Pisa, LUISS, IULM.
- **Normattiva** — D.Lgs 286/1998 (immigration law).

**Search terms used (Italian):** `laurea magistrale marketing digitale`,
`laurea magistrale marketing e intelligenza artificiale`,
`master management industria musicale`, `laurea magistrale marketing musicale`,
`management delle industrie creative`, `data science for marketing`,
`economia e management dello spettacolo`, `ISEE parificato studenti
internazionali extracomunitari`, `paesi particolarmente poveri elenco decreto`,
`no tax area ISEE 2026/2027`, `borsa di studio DSU 2026/2027 extracomunitari`.

**FOUND NOTHING ON — state explicitly:**
- **No *laurea magistrale* in music business / music marketing exists in Italy.**
  This is a real, confirmed negative, not a search failure. Every Italian
  "music business / music management" offer I found is a **Master universitario
  di I livello** (1 year, 60–65 CFU) — LUISS Business School *Music Business*,
  Sapienza *MMCM*, Roma Tre *Management, Marketing e Media della Musica*, UniBo
  *Produzione e promozione della musica*, IULM *Editoria e produzione musicale*,
  24ORE Business School. **These are excluded by section 4 of the brief** (see
  §5 below for why this distinction matters and how it is commonly got wrong).
  The closest genuine *lauree magistrali* are **creative/cultural-industries**
  degrees that contain music as a sector (GIOCA, Ca' Foscari IMCC, Cattolica).
- **No music-marketing-specific *laurea magistrale*** anywhere in scope.
- **CIMEA fee and turnaround time: NOT VERIFIED.** cimea.it returned HTTP 503 to
  every attempt (direct fetch and curl through the proxy). I have the *procedural*
  role of the CIMEA statement verified from an official university source (Pisa),
  but **not its price or processing time**. See §7.
- **Post-study work permit specifics: PARTLY VERIFIED ONLY.** I confirmed the
  general Art. 22 c.11 D.Lgs 286/1998 wording; I could **not** confirm the
  graduate-specific job-seeking permit duration from a primary government source
  — poliziadistato.it bot-blocked, integrazionemigranti.gov.it deep links 404.
  See §8. Treat as `NOT VERIFIED — check directly`.
- **Cost of living: NO OFFICIAL FIGURES OBTAINED.** WebSearch budget was
  exhausted (200/200) before I could source official university cost-of-living
  statements. I am **not** estimating. See §9 — this is a genuine gap.
- **Milano-Bicocca "fixed-rate taxation for international students by country of
  residence": FLAGGED, NOT RESOLVED.** Bicocca's own page says international
  students are taxed on a flat-rate system keyed to country of residence. That
  may *override* the ISEE route at that university, in either direction. The
  figures live in a PDF ("Guida Contribuzione") I could not retrieve. **Do not
  assume Bicocca = €0 like Bologna.**
- **LAZIODISCO / other regional DSU bodies beyond ER-GO and DSU Toscana:** not
  covered. Search budget exhausted.
- **Bocconi ACME, Cattolica, Politecnico di Milano, Padova, Torino, Trento,
  Pavia:** not individually verified. Cattolica's programme URL 404'd.

---

## 3. THE ISEE VERDICT — the single biggest lever in this project

### 3.1 How Italian public tuition actually works

Italian public universities do not charge a flat "international fee". They charge
a **contributo onnicomprensivo annuale** computed from the **ISEE** (Indicatore
della Situazione Economica Equivalente) of the student's household. Below a
threshold — the **"no tax area"** — the contribution is **zero**. Law 232/2016
sets the national floor at ISEE €22,000; universities may and do raise it.

**Verified 2026/27 no-tax-area thresholds:**

| University | No-tax-area ISEE ceiling | Source (checked 2026-08-17) |
|---|---|---|
| **Bologna** | **€27,000** → contribution €0 | [Sistema di calcolo tasse 2026/27 (PDF)](https://www.unibo.it/it/allegati/sistema-di-calcolo-delle-tasse-a-a-2026-27/@@download/file/Sistema-di-calcolo-delle-tasse-anno-accademico-2026-2027.pdf) |
| **Milano-Bicocca** | **€30,000** | [unimib.it contribuzione studentesca](https://www.unimib.it/studiare/servizi-studenti-e-laureati/segreterie/immatricolazione/contribuzione-studentesca) — but see international flat-rate caveat |
| National statutory floor | €22,000 | Law 232/2016 |

**Bologna's full verified 2026/27 band table** (for students within normal course
duration + 1, *with* the minimum CFU achieved):

| ISEE | Annual contribution |
|---|---|
| **≤ €27,000** | **€0** |
| > €27,000 and ≤ €33,000 | (ISEE − 23,000) × 9% |
| > €33,000 and ≤ €45,000 | (ISEE − 13,000) × 4.5% |
| > €45,000 and ≤ €55,000 | (ISEE − 45,000) × 4.29% + €1,440 |
| > €55,000 and ≤ €60,000 | (ISEE − 55,000) × 19% + €1,869 |
| > €60,000 and ≤ €70,000 | (ISEE − 13,000) × 6% |
| > €70,000 | (ISEE − 13,000) × 7% |

**Plus, for everyone including the fully exempt: €157.04/year** = regional
right-to-study tax €140.00 + stamp duty €16.00 + insurance €1.04.

> **So the realistic Bologna figure for this student is €157.04 per year, total.**
> Not €157 per semester. Per year. This is verified from the university's own
> fee-calculation decree.

### 3.2 How a Tunisian student gets an ISEE

Two routes, and **which one applies depends on the university** — this is the
detail most guides get wrong:

**Route A — ISEE parificato via a CAF (most universities).**
The family lives in Tunisia and has no Italian tax position, so the ordinary
ISEE cannot be produced. A **CAF/CAAF** (tax-assistance centre) affiliated with
the university computes an **ISEE parificato** from the foreign documentation.
Verified at Genoa: **free of charge** at affiliated CAFs; deadline **31 October
2026** with no penalty, **€100** late charge 1–30 November, **€200** 1 December
2026 – 15 June 2027.
Source: [unige.it/en/tasse-e-benefici/isee/parificato](https://unige.it/en/tasse-e-benefici/isee/parificato) (checked 2026-08-17)

**Route B — direct foreign-income assessment (Bologna).**
Bologna does **not** require an Italian ISEE at all for a student whose household
income and assets are exclusively abroad. The student submits foreign
documentation directly through the ER.GO online portal and the university/ER-GO
assess it.
Verified deadlines for 2026/27: **30 October 2026, 18:00**; late until **16
November 2026, 18:00 with a €100 surcharge**; supporting documents uploaded by
**20 November 2026**.
Source: [unibo.it — ISEE / documenti redditi esteri](https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/lauree-e-lauree-magistrali/tasse-e-contributi/ISEE-documenti-redditi-esteri-per-esenzioni-tasse-universitarie) (checked 2026-08-17)

### 3.3 The documents a Tunisian family must produce

Verified from the Bologna page and, in far more detail, from the ER-GO 2026/27
bando §2.3.1 (the most precise official statement I found). For non-EU students:

- Documentation **must be issued by the competent authorities of the territory
  where the income was produced and the assets are held**. Self-certification is
  **never** accepted ("Non vengono accettate in nessun caso autocertificazioni o
  autodichiarazioni").
- The original-language documents must be **legalised by the competent Italian
  diplomatic authority** (i.e. the Italian Embassy/Consulate in Tunis) **or
  apostilled** where applicable, and **translated into Italian** by the
  diplomatic/consular representation or an official translator.
- Fallback where the local Italian Embassy cannot certify: a certificate **in
  Italian issued by the Tunisian Embassy/Consulate in Italy**, legalised by the
  competent Italian Prefettura.
- Content required: **family composition** as at the application deadline;
  **2025 employment status** of each household member (or unemployment, with
  benefit amounts); whether work exceeded six months in 2025; **gross 2025 income**
  of every household member; **real estate held at 31/12/2025 with surface area
  in m²**; outstanding mortgage balances; **movable assets at 31/12/2025**; any
  disability certification.
- Foreign currency is converted at Bank of Italy 2025 rates.
- **Real property abroad is valued conventionally at €500 per square metre**
  (stated in the bando for the EU self-certification route; the same conventional
  valuation is the standard ISEE-parificato basis). A family home in Sousse of,
  say, 150 m² is therefore valued at ~€75,000 of *patrimonio immobiliare* — which
  enters the ISEE calculation heavily discounted, but it is the item most likely
  to push the ISEE up. **This is the number to model before assuming €0.**
- ER-GO warns explicitly against paying agencies or intermediaries to assemble
  this file — it is free and must be done directly.

Source: [ER-GO Bando DSU 2026/2027 (PDF), §2.3.1](https://www.er-go.it/cosa-fare-per/bandi-di-concorso/leggi-il-bando/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf/@@display-file/file/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf) (downloaded and read in full, 2026-08-17)

### 3.4 The "particularly poor countries" flat fee — **DOES NOT APPLY**

Some universities charge students from a MUR-listed set of very poor countries a
small flat fee instead of running an ISEE. I retrieved and read the **full text
of the governing decree**:

> **Decreto Ministeriale n. 176 del 24-02-2026**, MUR, "Definizione dell'elenco
> dei Paesi particolarmente poveri per l'anno accademico 2026/2027", issued in
> agreement with MAECI on the basis of the OECD-DAC ODA-recipient list.

The complete list is: Afghanistan, Angola, Bangladesh, Benin, Burkina Faso,
Burundi, Cambodia, Central African Republic, Chad, Comoros, DPR Korea, DR Congo,
Djibouti, Eritrea, Ethiopia, Gambia, Guinea, Guinea-Bissau, Haiti, Kiribati, Lao
PDR, Lesotho, Liberia, Madagascar, Malawi, Mali, Mauritania, Mozambique, Myanmar,
Nepal, Niger, Rwanda, Senegal, Sierra Leone, Solomon Islands, Somalia, South
Sudan, Sudan, Syrian Arab Republic, Tanzania, Timor-Leste, Togo, Tuvalu, Uganda,
Yemen, Zambia.

**Tunisia is not on it.** Verdict: `NOT APPLICABLE`. Do not build any plan on it.
Source: [MUR DM 176 del 24-2-2026](https://www.mur.gov.it/it/atti-e-normativa/decreto-ministeriale-n-176-del-24-2-2026) (PDF text extracted and read, 2026-08-17)

**However** — Bologna operates a *second*, separate reduced flat fee for citizens
of **non-EU, non-OECD countries**, and **Tunisia is non-EU and non-OECD**, so
this one *does* apply. Bologna's published 2026/27 figures for that category:
**€1,000 + €157.04** (first year / minimum CFU met), **€1,200 + €157.04**
(below minimum CFU). *The page notes different amounts apply for second-cycle
programmes and I could not read the second-cycle table — mark `BORDERLINE, verify`.*
Note this is an **alternative** to the ISEE route and is **worse** than the ISEE
route if the ISEE lands under €27,000. Choose the ISEE route.
Source: [unibo.it — tassa fissa agevolata](https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/lauree-e-lauree-magistrali/tasse-e-contributi/tassa-fissa-agevolata-per-cittadini-di-paesi-particolarmente-poveri-e-in-via-di-sviluppo-o-di-paesi-non-ue-non-appartenenti-allocse) (checked 2026-08-17)

### 3.5 ISEE VERDICT

**Verdict: STRONGLY FAVOURABLE, conditional on paperwork discipline.**

- The mechanism is real, national, and verified from primary fee decrees.
- The likely outcome for a Sousse household is the **no-tax area → €157.04/year
  at Bologna**, and something similar at most public universities.
- The **risk is entirely administrative**: the file must be assembled in Tunisia,
  legalised at the Italian Embassy in Tunis, translated, and uploaded by a fixed
  late-October deadline. Missing it does not cost a discount — it places the
  student in the **maximum** fee band plus a penalty. Start the document
  collection **at least four months** before the deadline.
- The one open question is the **€500/m² conventional valuation of the family
  home**, which is the single input most likely to lift the ISEE. Model it.
- **Milano-Bicocca is a specific exception to watch** — its own page describes a
  flat-rate international scheme by country of residence, which may bypass ISEE.

---

## 4. DSU REGIONAL SCHOLARSHIPS — high value, frequently missed

These are **need-based, not merit-based** at the point of entry, are **explicitly
open to non-EU students**, and stack on top of the fee exemption.

### ER-GO (Emilia-Romagna — covers Bologna, Modena-Reggio, Ferrara, Parma) — VERIFIED IN FULL

**Economic thresholds 2026/27:** ISEE ≤ **€25,000**, ISPE ≤ **€50,000**.

**Scholarship value (a.a. 2026/2027), verified from the bando:**

| ISEE band | *Fuori sede* (living away) | *Pendolare* | *In sede* |
|---|---|---|---|
| up to €16,666.67 | **€7,171.11** | €4,190.71 | €2,890.16 |
| €16,666.68 – €18,333.34 | €4,661.22 | €2,723.96 | €1,878.61 |
| €18,333.35 – €20,818.46 | €3,872.40 | €2,262.98 | €1,560.69 |
| €20,818.47 – €25,000.00 | €3,585.56 | €2,095.36 | €1,445.08 |

Amounts are inclusive of any portion converted into canteen credit. Eligibility
also carries **refund of the €140 regional tax**, **total fee exemption**, and
access to **ER-GO residence places** and **subsidised meals**. An international
student arriving from Tunisia is *fuori sede* by definition, so the **€7,171.11
band is the relevant one**.

**Deadlines (2026/27 cycle — indicative of the 2027/28 pattern; the 2027/28 bando
was not published as at 2026-08-17):**
- Applications open **23 June 2026**, close **24 August 2026, 16:00**
- Provisional rankings **20 October 2026**; appeals to 27 October; final 17 November 2026
- Accommodation for *laurea magistrale* first-years (new applicants): same 24 August deadline
- Domicile self-declaration by **3 November 2026**

**Merit condition:** a first-year *laurea magistrale* student must reach a
credit threshold by **30 November 2027** or repay; those who reach it by that
date keep the first instalment but repay the second. Read Sez. II art. 4 before
committing.

Source: [ER-GO Bando DSU 2026/2027](https://www.er-go.it/cosa-fare-per/bandi-di-concorso/leggi-il-bando/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf/@@display-file/file/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf) (full PDF read 2026-08-17)

> **Combined Bologna picture: tuition €157.04 − regional tax refund €140 +
> scholarship €7,171.11 + subsidised housing and meals.** That is a net positive
> cash position before living costs. This is the strongest single financial
> finding in my scope.

### DSU Toscana (Florence, Pisa, Siena)

- Benefits: cash allowance + **free meals** for winners and eligible non-winners
  + **free accommodation** for winners (subject to availability) + **€262.50/month**
  housing contribution for eligible non-winners + **regional fee waiver**.
- **Deadline 2026/27: 7 September 2026, 13:00** (bachelor's and master's).
- **Amounts and ISEE/ISPE thresholds: NOT VERIFIED** — the public page defers to
  the bando, which I could not retrieve before budget exhaustion.
  Check: [dsu.toscana.it/borsa-di-studio](https://www.dsu.toscana.it/borsa-di-studio)

### Other regions

**LAZIODISCO (Rome), EDISU Piemonte (Turin), ERSU, ADISU** — `NOT RESEARCHED`.
Search budget exhausted. Same statutory framework (D.Lgs 68/2012, DPCM 9/4/2001)
so the shape will be similar, but **amounts and deadlines must be checked
per region**.

---

## 5. ⚠️ THE TERMINOLOGY TRAP — *Laurea Magistrale* vs *Master universitario*

This is the most consequential thing in the Italian scope and it is where almost
every English-language guide goes wrong.

| | ***Laurea Magistrale*** | ***Master universitario di I / II livello*** |
|---|---|---|
| Duration | **2 years** | **1 year** (usually) |
| Credits | **120 CFU** | 60–65 CFU typically |
| Bologna cycle | **Second cycle** — a genuine state master's degree | **Not a cycle degree.** A postgraduate *corso*, not a *titolo di studio* of the second cycle |
| Qualifies under brief §4? | **YES** | **NO** for *I livello*; *II livello* still is not a second-cycle degree |
| Entry to a PhD | Yes | No (a *Master di I livello* does not confer PhD access) |
| ECTS-portable as a master's? | Yes | Contested / generally no |

**A *Master di primo livello* sits on top of a bachelor's and is NOT equivalent
to a second-cycle degree.** The English-looking word "Master" in its name is the
whole trap.

**Every Italian music-business offer I found is a *Master di I livello* and is
therefore EXCLUDED:**

| Offer | Institution | Type | Status |
|---|---|---|---|
| *Music Business* | LUISS Business School, Rome | **Master (65 CFU, ~€16,000)** | **EXCLUDED** — not a laurea magistrale; also over the cost filter |
| *Management, Marketing e Comunicazione della Musica (MMCM)* | Sapienza, Rome | **Master di I livello** | **EXCLUDED** |
| *Management, Marketing and Media della Musica* | Roma Tre | **Master di I livello** | **EXCLUDED** |
| *Produzione e Promozione della Musica* | Bologna | **Master di I livello** | **EXCLUDED** |
| *Editoria e Produzione Musicale* | IULM, Milan | **Master universitario** | **EXCLUDED** |
| *Digital Marketing and Communication* | Bologna / Bologna Business School | **Master universitario** | **EXCLUDED** |
| *AI e Data Science per le Imprese (MIA)* | ALTIS, Cattolica + PoliMi | **Master di I livello** (own page states "primo livello") | **EXCLUDED** |
| *Music Business Management* | 24ORE Business School | **Private school course, not a university degree** | **EXCLUDED — no accreditation, no ECTS, visa status doubtful** |

They are recorded here so nobody re-finds them and mistakes them for degrees.
If the student ever wants one, the correct sequencing is *laurea magistrale*
first, *Master* afterwards as a specialisation.

---

## 6. PROGRAMMES

### 6.1 Direction 3 + 4 — Creative / cultural industries incl. music (best finds)

---

#### ★ PRIORITY FIND — **Innovation and Organization of Culture and the Arts (GIOCA)**

| Field | Detail |
|---|---|
| University | **Università di Bologna** (public, Italy's oldest, top-ranked) |
| City | **Bologna** |
| Degree awarded | ***Laurea Magistrale*** — class **LM-76 R** (Scienze economiche per l'ambiente e la cultura) |
| Duration / credits | **2 years**, second cycle (120 CFU standard for LM) |
| Institution type | **Public university** |
| Accreditation | State-recognised second-cycle degree, ECTS-bearing, full student-visa and post-study rights |
| Direction match | **3 + 4 hybrid** — the programme explicitly covers "film, visual and performing arts, **music and the recording industry**" with attention to "digital and social transition"; includes digital communication and fundraising. **Flagged PRIORITY FIND per brief §3.** |
| Teaching language | **English — delivered entirely in English** → **TIER A** |
| Tuition (non-EU) | **ISEE-based. ISEE ≤ €27,000 → €0 + €157.04 fixed.** See §3. |
| Entry requirement (exact wording) | "at least a first level degree (Bachelor's)" from a foreign university of "**at least three years**" **"in any discipline"**. Alternative route if no qualifying bachelor's: **minimum 40 ECTS** across listed SSDs (economics, statistics, business management, law, geography, history, sociology, architecture, informatics…) |
| **146 ECTS verdict** | **`LIKELY OK`** — the requirement is framed in **years of study** ("at least three years"), not a literal 180-ECTS count, and the discipline is unrestricted. This is precisely the wording Phase 1 identified as safe. Even the fallback route asks only 40 ECTS, which a marketing licence clears easily. |
| Language requirement | **English B2**. Accepted: TOEFL, IELTS, Cambridge, Trinity College London, **OOPT** (within 6 years), a degree taught entirely in English, a B2 exam from prior studies, or the university's own **CLA B2** certificate. **The OOPT sat via UniBo's CLA is the cheap route — no external test needed.** |
| Selection | CV + qualifications (40 pts, pass 25) **+ interview** (60 pts, pass 35), overall **60/100** to pass. **No GMAT/GRE.** |
| Places | **50 total — 25 reserved for non-EU citizens resident abroad** |
| Application fee | **€50** on Studenti Online |
| Deadline | **2026/27 call now expired** (that was this cycle). **2027/28 call not yet published as at 2026-08-17** — historically opens in the first months of the calendar year. `CHECK FROM JANUARY 2027`. |
| Official URL | https://corsi.unibo.it/2cycle/gioca — admission: /admission, /how-to-enrol |
| Checked | 2026-08-17 |

**Why this is the top find:** English-taught (Tier A, no language step), music sector
in scope, entry framed in years not credits, no GMAT, 25 places ring-fenced for
non-EU applicants resident abroad, selection by interview where the CRM project
is a genuine differentiator, and — critically — it is in **Emilia-Romagna**, so
the **ER-GO €7,171.11 scholarship** applies. The 12–13/20 GPA is a real risk in
Phase 1 of the selection (40 points on CV/qualifications), but Phase 2's 60-point
interview is the larger share and rewards motivation and portfolio.

---

#### ★ **Innovation and Management for Culture and Creativity (IMCC)**

| Field | Detail |
|---|---|
| University | **Università Ca' Foscari Venezia** (public) |
| City | **Venice** (Campus Economico, San Giobbe, Cannaregio 873) |
| Degree awarded | ***Laurea Magistrale*** — class **LM-77 R** (Scienze economico-aziendali) |
| Duration / credits | **2 years / 120 CFU** — confirmed on the official course sheet |
| Institution type | **Public university** |
| Direction match | **3 + 4 hybrid** — management of business–market and institution–audience relations in culture and creativity. **PRIORITY FIND.** |
| Teaching language | **English** → **TIER A** |
| Tuition (non-EU) | ISEE-based. **Ca' Foscari's exact 2026/27 bands: `NOT VERIFIED — check directly`** at unive.it/tasse |
| Admission | **Programmed (capped) admission.** Exact curricular requirements, English level, places and deadlines: **`NOT VERIFIED`** — unive.it returned HTTP 503 on repeated attempts. Check https://www.unive.it/cdl/emr17 → "Ammissione e immatricolazione" |
| **146 ECTS verdict** | **`BORDERLINE`** — LM-77 R programmes commonly impose curricular ECTS thresholds in economics/business SSDs. Needs an email to campus.economico@unive.it |
| Note | Programme replaced the older "Innovation and Marketing" LM from 2025/26 |
| Official URL | https://www.unive.it/cdl/emr17 |
| Checked | 2026-08-17 |

---

#### Also in this direction — not individually verified

- **Bocconi — *Economics and Management in Arts, Culture, Media and Entertainment*
  (ACME)**, Milan, English. Strong content match for directions 3/4.
  **STRETCH ONLY** — Bocconi is highly selective and its fees are above the
  filter. `NOT VERIFIED` (not fetched). See §10.
- **Università Cattolica del Sacro Cuore — *Economia e gestione dei beni
  culturali e dello spettacolo***, Milan, Italian. Covers "the economics and
  management of cinema, **music** and entertainment". Private but income-scaled.
  **`NOT VERIFIED` — the programme URL 404'd.** Worth a dedicated re-check.
- **Roma Tor Vergata — *Musica e Spettacolo*.** Graduate outcomes listed include
  "record companies" and "consulting for companies in the music and entertainment
  industry". `NOT VERIFIED — degree class, language and entry unchecked.`

---

### 6.2 Direction 2 — Digital Marketing & Growth Marketing

---

#### **Digital Marketing (LM-77)** — Università degli Studi di Salerno

| Field | Detail |
|---|---|
| University | **Università di Salerno** (public) |
| City | **Fisciano** (Salerno province, Campania — southern Italy, low cost base) |
| Degree awarded | ***Laurea Magistrale*** — class **LM-77** |
| Duration | **2 years** |
| Institution type | **Public university** |
| Direction match | **Direction 2**, with direction-1 overlap in the English track |
| Curricula | 1. *Marketing and Digital Transformation* — **Italian**<br>2. *Marketing, Service and New Technologies* — **English** |
| Teaching language / tier | English track = content in English, **but Italian B1 is required of all applicants** → effectively **TIER B** either way |
| Internship | **Mandatory curricular internship** |
| Entry requirement (exact wording) | A recognised bachelor's, **either** in an Economics/Business Management degree class **or** **90 ECTS distributed as: 60 economics-business, 15 law, 15 statistics/mathematics** |
| **146 ECTS verdict** | **`BORDERLINE`** — the 90-ECTS distribution rule is a literal-credit test. A Tunisian *Licence en Marketing* almost certainly meets the 60 economics-business, but the **15 law and 15 statistics/maths sub-quotas are the risk**, and a transcript printing only capitalised credits could under-count both. **Requires the FSEG attestation + supplément au diplôme, plus an email to admissions.** |
| Language requirement | **Italian ≥ B1 for everyone**; **English ≥ B2** for the English curriculum |
| Selection | Interview, booked in staggered sessions |
| Deadlines (2026/27, indicative) | Interview sessions run **June 2026 → February 2027**; e.g. the 1 October 2026 session books **27 July – 23 September 2026**. Registration via Esse3. **2027/28 dates not yet published.** |
| GMAT/GRE | **Not used** |
| Tuition | ISEE-based public fees. **Exact Salerno bands `NOT VERIFIED — check directly`** |
| Official URL | https://corsi.unisa.it/digital-marketing/en |
| Checked | 2026-08-17 |

**Assessment:** the closest thing in Italy to a named, English-available *digital
marketing laurea magistrale* at a public university, with a mandatory internship
and a cheap southern location. Two frictions: the **Italian B1 requirement even
for the English track**, and the **90-ECTS distribution rule**.

---

#### **Pubblicità, Comunicazione Digitale e Creatività d'Impresa (LM-59)** — UNIMORE

| Field | Detail |
|---|---|
| University | **Università di Modena e Reggio Emilia** (public) |
| City | **Reggio Emilia** |
| Degree awarded | ***Laurea Magistrale*** — class **LM-59** (Scienze della comunicazione pubblica, d'impresa e pubblicità) |
| Duration | 2 years |
| Direction match | **Direction 2** (advertising, digital communication, creative business processes) |
| Teaching language | **Italian** → **TIER B** |
| Admission | **"No closed number"** — open admission with assessment of personal preparation |
| Entry requirement (exact wording) | Bachelor's in listed classes (L-1, L-3, L-5 …) **or a different class with a minimum of 30 ECTS in relevant sectors** |
| **146 ECTS verdict** | **`LIKELY OK`** — the alternative route asks only **30 ECTS** in relevant SSDs, which a marketing licence clears with large margin even on a truncated transcript. **This is the lowest credit bar found anywhere in the Italian scope.** |
| Language requirement | **English B1** (certificate, 6+ ECTS in English, or university attestation) — plus Italian, since the programme is Italian-taught (level `NOT VERIFIED`, assume B2 per the standard Universitaly rule) |
| Additional hurdle | **Written admission test** covering linguistics, computer science and social sciences — conducted in Italian |
| Deadline | 2025/26 cycle enrolment closed **22 December 2025**; **2027/28 `NOT VERIFIED`** |
| GMAT/GRE | Not used |
| Tuition | ISEE-based. **In Emilia-Romagna → ER-GO scholarship applies.** |
| Official URL | https://www.dce.unimore.it/en/education/masters-degree-programmes/masters-degree-advertising-digital-communication-and-creative |
| Checked | 2026-08-17 |

**Assessment:** open admission, lowest credit threshold found, in the ER-GO
region. The written test in Italian is the real gate, which makes the language
timeline load-bearing rather than optional.

---

### 6.3 Direction 1 — AI Applied to Marketing

---

#### **Marketing and Global Markets (LM-77 R)** — Università di Milano-Bicocca

| Field | Detail |
|---|---|
| University | **Università degli Studi di Milano-Bicocca** (public) |
| City | **Milan** |
| Degree awarded | ***Laurea Magistrale*** — class **LM-77 R** |
| Duration | 2 years |
| Tracks | *Marketing Globale* (**Italian**) · *Global Management* (**English**) |
| Teaching language / tier | **TIER A via the English "Global Management" track**; the marketing-specific track is Italian (**Tier B**) |
| Direction match | **Direction 1/2 partial.** Note the English track is *management*-weighted (strategic management, international business, entrepreneurship, innovation management, global accounting, corporate finance) — **the marketing-heavy content sits in the Italian track**. Be clear-eyed about this. |
| Entry requirement (exact wording) | "admission is conditional on a solid background in **management, economics and quantitative methods**"; "a **3 years Bachelor Degree** in economics or related fields from an accredited college/university or its equivalent"; **"Enrollment is limited with entry requirements examination"** |
| **146 ECTS verdict** | **`LIKELY OK`** — the wording is "a **3 years** Bachelor Degree", i.e. a duration test, not a credit count. The "solid background in quantitative methods" is a softer content risk. |
| Language requirement | **English B2 certificate** required |
| Tuition | **⚠️ CAUTION.** No-tax area raised to **€30,000 ISEE** for 2026/27 — but Bicocca's own page states international students are subject to a **"fixed-rate taxation system based on country of residence and course contribution area."** Whether that overrides ISEE, and at what amount, is **`NOT VERIFIED`** (figures are in a PDF guide I could not retrieve). **Do not assume €0 here.** |
| Deadlines | ISEE/contribution assessment **13 Nov 2026**; housing **20 Aug 2026**; scholarships **30 Sep 2026** (2026/27 cycle) |
| GMAT/GRE | Not stated — presumed not used |
| Joint degrees | Universidad de Belgrano (Argentina), Antwerp Management School (Belgium) |
| Official URL | https://en.unimib.it/graduate/marketing-global-markets |
| Checked | 2026-08-17 |

---

#### **Intelligenza Artificiale, Impresa e Società (LM-91)** — IULM

| Field | Detail |
|---|---|
| University | **IULM, Milan** — **private** (Libera Università di Lingue e Comunicazione), state-recognised |
| Degree awarded | ***Laurea Magistrale*** — class **LM-91** (Tecniche e metodi per la società dell'informazione), **120 CFU**, **2 years** |
| Direction match | **Direction 1 — strong.** AI and big-data analysis "applied to marketing and business innovation"; statistics, machine learning, ethics; explicitly aims to "bridge the gap between technological development and concrete applications in **marketing**, communication and business management" |
| Teaching language | **Italian** → **TIER B** |
| Admission | **Programmed number of places + selective knowledge test** |
| **146 ECTS verdict** | **`BORDERLINE — NOT VERIFIED`**; curricular requirements not published on the page fetched |
| Tuition | **`NOT VERIFIED`.** IULM publishes a *Regolamento Tasse AA 2026-2027*; IULM fees are income-scaled but this is a private university — **must be checked against the €8k/€15k filter before shortlisting.** URL: https://www.iulm.it/wps/wcm/connect/iulm/a5276c9e-b358-4600-976b-c11f41fd4ade/Regolamento+Tasse+AA+2026-2027.pdf |
| Official URL | https://www.iulm.it/en/offerta-formativa/corsi-di-lauree-magistrali/intelligenza-artificiale-impresa-societa/intelligenza-artificiale-impresa-societa |
| Checked | 2026-08-17 |

**Assessment:** the best *content* match for "AI applied to marketing" found in
Italy — it is a genuine *laurea magistrale*, not a Master, and marketing is
explicit in its stated purpose. Two open risks: it is Italian-taught with a
selective entry test, and it is private with unverified fees.

---

### 6.4 Direction 1 — noted but not verified

- **LUISS Guido Carli — *Data Science and Management*** (Rome, private). Not
  fetched. Same €15,000-band cost profile as LUISS Marketing below → **stretch**.
- **Università di Ferrara — *Intelligenza Artificiale, Data Science e Big Data***
  (LM-18/LM-32 interclass, public, Ferrara — **ER-GO region**). This is a genuine
  *laurea magistrale*. **But it is a computer-science degree, not a marketing
  one** — a marketing licence will very likely fail its curricular requirements
  (maths/CS ECTS). `NOT VERIFIED`, and I rate it **probably BLOCKING** on
  curricular grounds.
- **UniFI — *Data Science, Calcolo Scientifico e Intelligenza Artificiale***
  (Florence, public). Same objection: mathematics/CS entry profile. Probably
  BLOCKING.
- **Trieste, Ca' Foscari *Marketing Management*, Padova, Torino, Trento,
  Pavia, Bergamo, Politecnico di Milano** — `NOT RESEARCHED`. Budget exhausted.

---

## 7. PRE-ENROLMENT, VISA AND DEGREE RECOGNITION (Italy-specific requirement 3)

### 7.1 The Universitaly pre-enrolment — mandatory, and it has a hard date

Every non-EU applicant needing a visa **must** pre-enrol through the
**Universitaly portal** (`universitaly.mur.gov.it`) — described on the portal
itself as the **exclusive and free** platform of the Ministry. It is not
optional and no consulate will process a study visa without it.

**Verified deadlines (universitaly.it, checked 2026-08-17):**

| Academic year | Visa application deadline |
|---|---|
| 2026/2027 | **30 November 2026** |
| **2027/2028 — THE TARGET INTAKE** | **31 October 2027** |

This applies to bachelor's, master's and single-cycle programmes. Other course
types (Master universitario, PhD, Erasmus, single courses, foundation courses)
have no fixed deadline but must be submitted before classes start.

Note the university-side pre-enrolment window closes earlier than the consular
deadline — **Pisa's 2026/27 pre-enrolment deadline was 30 September 2026**, with
visas needing to be *issued* by 30 November 2026. Assume roughly a
**September pre-enrolment / October–November visa** rhythm for autumn 2027 and
work backwards.

### 7.2 Degree recognition — *dichiarazione di valore* OR CIMEA

Verified from the University of Pisa's official international-students page
(checked 2026-08-17), the documents uploaded to Universitaly for a **master's**
application are:

- Bachelor's **diploma + transcript + course syllabi**, with **official Italian
  translations** (for Italian-taught programmes)
- The programme's **admission decision / admission letter**
- **Italian B2 certification** (Italian-taught masters) — or **English B2+**
  (English-taught masters; Pisa describes it as helpful rather than strictly
  mandatory at the visa stage, though the *programme* will require it)
- **Declaration of Value (*dichiarazione di valore*) OR CIMEA comparability
  attestation** — the two are presented as **alternatives**

> **This is the key practical point:** the *dichiarazione di valore* is issued by
> the Italian Embassy in Tunis and is slow and consulate-dependent; the **CIMEA
> Statement of Comparability is an accepted substitute** and is handled centrally.
> For a Tunisian applicant the CIMEA route is normally the faster and more
> predictable of the two.
> Source: [unipi.it — Preiscrizione su Universitaly](https://www.unipi.it/didattica/iscrizioni/immatricolazioni-e-iscrizioni/iscrizioni-per-studenti-internazionali/preiscrizione-su-universitaly/)

**⚠️ `NOT VERIFIED — check directly`: the CIMEA fee and turnaround time.**
cimea.it returned **HTTP 503** to every attempt (WebFetch and curl, both English
and Italian URLs, 2026-08-17). I will not quote a price or a processing time I
could not confirm. Check: **https://www.cimea.it** → "Attestati di comparabilità
e di verifica dei titoli". Budget both **cost and several weeks of lead time**,
and start it in parallel with the ENIC-NARIC France file if that is also running.

Universitaly also states, importantly, that **foreign-qualification evaluation is
the exclusive responsibility of the Italian higher-education institution** (Law
148/2002) and that **consular documentation is not binding on the university**.
Practical consequence for the 146-ECTS problem: **the university decides, not the
consulate** — so the FSEG attestation and *supplément au diplôme* should be sent
to the admissions office, and their answer is the one that counts.

---

## 8. LANGUAGE — Italian for a native French speaker (requirement 4)

### Tier assignment

| Route | Tier | Reasoning |
|---|---|---|
| GIOCA (Bologna), Ca' Foscari IMCC, Bicocca *Global Management* | **TIER A** | Fully English-taught; only English B2 needed, and UniBo's own CLA/OOPT satisfies it without an external test |
| Salerno *Digital Marketing* (either curriculum) | **TIER B** | Italian **B1** required of all applicants regardless of curriculum |
| UNIMORE LM-59, IULM LM-91, and the great majority of Italian *lauree magistrali* | **TIER B** | Italian-taught, standard **B2** requirement, plus Italian-language entry tests at some |

### Why Italian is Tier B and not Tier C for this student

Italian and French are both Western Romance languages with very high lexical
overlap, closely parallel verb systems (including the same
auxiliary-selection logic and a directly transferable subjunctive), and shared
Latinate academic and business register — which is exactly the vocabulary a
marketing master's runs on. A native French speaker starts with large passive
comprehension on day one. The realistic estimate is **B2 in 6–12 months** of
serious study, and closer to the 6-month end with immersion in Italy. This puts
Italian firmly in the brief's "much faster for a French speaker" category
alongside Spanish, and decisively **not** in the German/Nordic category.
*(This is my reasoned assessment from the linguistic relationship, not a cited
institutional figure — treat it as judgement, not a verified number.)*

### The certificate

**Standard requirement: B2** (Universitaly/consular practice for Italian-taught
degree programmes; Salerno is an outlier at B1).

**Accepted certificates** — the four bodies of the **CLIQ** consortium
(Certificazione Lingua Italiana di Qualità), which is the recognised standard:
- **CILS** — Università per Stranieri di Siena
- **CELI** — Università per Stranieri di Perugia
- **PLIDA** — Società Dante Alighieri
- **CERT.IT** — Università Roma Tre

Plus, in most cases, a **B2 certificate issued by the university's own CLA**
(Centro Linguistico di Ateneo).
*`NOT VERIFIED`: I could not reach cliq.cvcl.it or cvcl.unistrasi.it (both DNS
failures, 2026-08-17). The four-body composition of CLIQ is stated here from
general knowledge — **confirm the exact accepted list on each university's page**
before relying on a specific certificate.*

**Route in Tunisia:** the **Istituto Italiano di Cultura di Tunisi** and the
Società Dante Alighieri network are the normal places to take CILS/PLIDA in
Tunisia. `NOT VERIFIED — check session dates and fees directly.`

### Preparatory and free routes

- **University CLA courses.** Italian universities operate a *Centro Linguistico
  di Ateneo* offering Italian courses to enrolled international students, very
  often **free or heavily subsidised**. This is the standard pattern; verify per
  university. It solves the "arrive at B1, reach B2 during year one" problem for
  a Tier-B programme — **but note it does not help with an entry requirement that
  must be met *before* enrolment** (e.g. UNIMORE's Italian-language admission
  test). `MECHANISM NOT INDIVIDUALLY VERIFIED for any named university.`
- **Marco Polo / Turandot** are China-specific and irrelevant here.
- **`NOT FOUND`: no integrated "language year + master's" route** at any
  institution I checked. Italy does not generally run the German-style
  preparatory year for master's entry. **If Italian B2 is not in hand by the
  application deadline, the answer is a Tier-A English-taught programme, not a
  bridging year.**

### Strategic recommendation on language

Apply to the **Tier-A English programmes for autumn 2027** (GIOCA above all),
**and** start Italian immediately regardless. Italian at B1–B2 by autumn 2027 is
comfortably achievable from a French base and it (a) opens Salerno/UNIMORE/IULM
as parallel applications, (b) is close to mandatory for actually working in
Italy afterwards, and (c) costs nothing at a CLA once enrolled.

---

## 9. POST-STUDY WORK (requirement 5) — **PARTIALLY VERIFIED, HANDLE WITH CARE**

**What I verified:** Art. 22 comma 11 of **D.Lgs 286/1998** (Testo Unico
Immigrazione), read on Normattiva 2026-08-17: loss of employment **does not**
cause revocation of the residence permit, and the worker may register as
available for work with effect "for the residual validity of the permit, and in
any case … **for a period not less than one year**" ("per un periodo non
inferiore a un anno").

**What I could NOT verify — `NOT VERIFIED — check directly`:**
- The **graduate-specific job-seeking permit** (*permesso di soggiorno per attesa
  occupazione* for new graduates): its exact duration and the conditions on which
  a graduating student may apply.
- **Conversion of a *permesso per studio* into a work permit** — whether it falls
  inside or outside the annual *decreto flussi* quota system for holders of an
  Italian degree. This is the decisive question for employability and I will not
  guess at it.

**Blockers encountered:** poliziadistato.it bot-blocked the request
("La richiesta è stata bloccata dai sistemi posti a protezione del sito web");
integrazionemigranti.gov.it deep links returned 404; Normattiva's article view
served Art. 22 but not Art. 6 c.1-bis or Art. 39 c.5-bis in usable form; the
MAECI *Study in Italy* host did not resolve.

**Where to check:**
- `https://www.normattiva.it` → D.Lgs 286/1998, **Art. 6 c.1-bis** (conversion)
  and **Art. 39-bis** (foreign graduates)
- `https://www.poliziadistato.it` → permesso di soggiorno section
- `https://www.integrazionemigranti.gov.it`
- The chosen university's international office — they answer this routinely

**Also unverified but standard and worth confirming:** student permit holders in
Italy may work part-time (the customary figure is 20 hours/week, 1,040 hours/year)
— **`NOT VERIFIED`, confirm before relying on it for a budget.**

---

## 10. COST OF LIVING (requirement 6) — **GAP: NO OFFICIAL FIGURES OBTAINED**

I am reporting this as a gap rather than filling it with estimates, per brief §7.
My WebSearch budget hit its 200-call ceiling before I reached official
cost-of-living statements, and university cost pages are typically PDFs I could
not locate without search.

**What I can say with confidence and can source:**
- Regional cost differences in Italy are large, and the programmes above sit at
  opposite ends of that range: **Milan** (Bicocca, IULM) is Italy's most
  expensive city; **Venice** (Ca' Foscari) has a severe and expensive housing
  market driven by tourism; **Bologna** is mid-range with a very large student
  population and a strong DSU residence system; **Fisciano/Salerno** (Campania)
  is at the low end of the national range.
- **The DSU system materially changes the calculation.** In Emilia-Romagna a
  scholarship winner gets an ER-GO **residence place** and **canteen access**,
  which removes the two largest line items. The €7,171.11 *fuori sede* award is
  explicitly sized as a maintenance grant. In Tuscany, winners get free
  accommodation subject to availability and eligible non-winners get **€262.50 per
  month** toward housing (verified). **Rent in Bologna with an ER-GO place is not
  comparable to market rent in Milan.**

**To close this gap, check:**
- Each university's "cost of living" / "living in [city]" international page
- ER-GO residence *rette* (rates) — in the bando I downloaded, Sez. "Importo
  della retta", art. 11
- DSU Toscana accommodation rates
- The consular financial-means requirement for the study visa (the Italian
  consulate publishes a minimum monthly maintenance figure) — **also `NOT VERIFIED`
  and important, since the visa itself depends on proving it.**

---

## 11. STRETCH OPTIONS (excellent but fail exactly one filter)

#### **LUISS Guido Carli — *Marketing* (LM-77)**, Rome

| Field | Detail |
|---|---|
| Type | **Private university**, state-recognised; degree class **LM-77**, **120 CFU**, 2 years |
| Language | **Italian and English** (both available) → **TIER A** via English |
| Majors | *Marketing Strategy, Management and Communication* · **_Marketing Analytics and Data Science_** |
| Direction match | **Directions 1 + 2 — the Analytics/Data Science major is the single best direction-1 content match found in Italy** |
| **Fails on** | **Cost: €15,000/year** + Lazio regional tax (2026/27 rate pending regional deliberation, June/July 2026). Sits **at the top of the brief's exclusion boundary**. Also selective. |
| Mitigation | LUISS offers "borse di studio ed esoneri parziali o totali" (scholarships and partial/total fee waivers) and unsecured study loans. **A full or substantial waiver would bring it into range — net cost would need to be stated.** `Scholarship terms NOT VERIFIED.` |
| Outcomes | Claims 95% employed within one year; 70% offered a job before graduating |
| Official URL | https://www.luiss.it/ammissione/offerta-formativa/laurea-magistrale/marketing |
| Checked | 2026-08-17 |

**Verdict:** include as a stretch **only with a scholarship application attached**.
At list price it fails the cost filter, and the 12–13/20 GPA is a poor fit for
LUISS's selectivity. Do not put it on a core shortlist.

#### **Bocconi — *Marketing Management* / *ACME*** (Milan)
**Fails two filters** (selectivity against a 12–13/20 GPA; fees above range).
`NOT VERIFIED — not fetched.` Recorded for completeness only; I would not spend
application effort here.

#### **Università di Ferrara / UniFI data-science *lauree magistrali***
Genuine public *lauree magistrali* in the ER-GO / Tuscan DSU regions with
near-zero fees — but **entry is quantitative** and a marketing licence will very
likely fail the curricular ECTS requirements. **Fails the accessibility filter,
not the cost one.** Listed so the option is visible if the student ever adds
maths/statistics credits.

---

## 12. RECOMMENDED ACTION SEQUENCE

1. **Now (Aug–Dec 2026):** start **Italian**. Target B1 by mid-2027, B2 by
   autumn 2027. This is the cheapest option-widening move available.
2. **Now:** commission the **CIMEA Statement of Comparability** (verify cost and
   timeline first — unverified). Runs in parallel with the ENIC-NARIC France file.
3. **Now:** obtain the **FSEG Sousse attestation** (6 semesters / 3 years / 180
   credits / confers Mastère access) and the *supplément au diplôme*. Free.
   Needed for every BORDERLINE verdict above.
4. **Autumn 2026:** email admissions at **UniBo GIOCA**, **Ca' Foscari IMCC** and
   **Salerno** with the transcript and attestation, asking them to confirm the
   qualification meets entry. Universitaly confirms **the university decides**, so
   these three answers settle most of the uncertainty in this report.
5. **From January 2027:** watch for the **GIOCA 2027/28 call for applications**.
   This is the priority application.
6. **Spring 2027:** begin assembling the **Tunisian income/family documentation**
   for the ISEE parificato — Tunisian authority issuance → Italian Embassy Tunis
   legalisation → Italian translation. **Four months minimum.**
7. **June–August 2027:** **ER-GO scholarship application** (2026/27 window was
   23 June – 24 August; expect the same shape). **This is the item most often
   missed and it is worth over €7,000.**
8. **By 31 October 2027:** Universitaly pre-enrolment complete and **visa
   application submitted** (verified 2027/28 deadline).
9. **By late October 2027:** ISEE parificato / foreign-income file submitted to
   the university. Missing this puts him in the **maximum** band.

---

## 13. SOURCES (all checked 2026-08-17)

**Primary / official — fee and scholarship system**
1. MUR, **Decreto Ministeriale n. 176 del 24-2-2026**, "Elenco dei Paesi particolarmente poveri a.a. 2026/2027" — https://www.mur.gov.it/it/atti-e-normativa/decreto-ministeriale-n-176-del-24-2-2026 *(PDF downloaded, full text extracted; **Tunisia absent**)*
2. Università di Bologna, **Sistema di calcolo della contribuzione studentesca a.a. 2026/2027** (PDF) — https://www.unibo.it/it/allegati/sistema-di-calcolo-delle-tasse-a-a-2026-27/@@download/file/Sistema-di-calcolo-delle-tasse-anno-accademico-2026-2027.pdf *(band table, no-tax area €27,000, €157.04 fixed)*
3. Università di Bologna, **ISEE / documenti redditi esteri per esenzioni** — https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/lauree-e-lauree-magistrali/tasse-e-contributi/ISEE-documenti-redditi-esteri-per-esenzioni-tasse-universitarie
4. Università di Bologna, **Tassa fissa agevolata (paesi poveri / non-OCSE)** — https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/lauree-e-lauree-magistrali/tasse-e-contributi/tassa-fissa-agevolata-per-cittadini-di-paesi-particolarmente-poveri-e-in-via-di-sviluppo-o-di-paesi-non-ue-non-appartenenti-allocse
5. Università di Genova, **ISEE-U parificato** — https://unige.it/en/tasse-e-benefici/isee/parificato *(free at CAF; deadlines and late penalties)*
6. **ER-GO, Bando di concorso benefici DSU a.a. 2026/2027** (PDF, read in full) — https://www.er-go.it/cosa-fare-per/bandi-di-concorso/leggi-il-bando/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf/@@display-file/file/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf *(thresholds, §2.3.1 non-EU documentation, Sez. II art. 1 amounts, deadlines)*
7. DSU Toscana, **Borsa di studio a.a. 2026/2027** — https://www.dsu.toscana.it/borsa-di-studio
8. Università di Milano-Bicocca, **Contribuzione studentesca a.a. 2026/2027** — https://www.unimib.it/studiare/servizi-studenti-e-laureati/segreterie/immatricolazione/contribuzione-studentesca

**Primary / official — procedure, visa, law**
9. **Universitaly**, Studenti stranieri — https://www.universitaly.it/it/studenti-stranieri *(visa deadline **31 October 2027** for a.a. 2027/2028)*
10. Universitaly homepage / portal — https://www.universitaly.it/
11. Università di Pisa, **Preiscrizione su Universitaly** — https://www.unipi.it/didattica/iscrizioni/immatricolazioni-e-iscrizioni/iscrizioni-per-studenti-internazionali/preiscrizione-su-universitaly/ *(document list; **Declaration of Value OR CIMEA attestation**)*
12. **Normattiva**, D.Lgs 25 luglio 1998 n. 286, Art. 22 — https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-07-25;286

**Primary / official — programmes**
13. UniBo **GIOCA** — https://corsi.unibo.it/2cycle/gioca · /overview · /admission · /how-to-enrol
14. Ca' Foscari **Innovation and Management for Culture and Creativity** — https://www.unive.it/cdl/emr17
15. Università di Salerno **Digital Marketing (LM-77)** — https://corsi.unisa.it/digital-marketing/en · /en/enrollment
16. Milano-Bicocca **Marketing and Global Markets** — https://en.unimib.it/graduate/marketing-global-markets
17. UNIMORE **Pubblicità, comunicazione digitale e creatività d'impresa** — https://www.dce.unimore.it/en/education/masters-degree-programmes/masters-degree-advertising-digital-communication-and-creative
18. **LUISS Marketing (LM-77)** — https://www.luiss.it/ammissione/offerta-formativa/laurea-magistrale/marketing
19. **IULM, Intelligenza Artificiale, Impresa e Società (LM-91)** — https://www.iulm.it/en/offerta-formativa/corsi-di-lauree-magistrali/intelligenza-artificiale-impresa-societa/intelligenza-artificiale-impresa-societa

**Sources that FAILED (recorded so the next agent does not repeat the attempt)**
- **cimea.it** — HTTP 503 on all attempts, both WebFetch and curl, EN and IT URLs. **CIMEA fee/timeline remains unverified.**
- **unive.it** deep admission pages — HTTP 503
- **poliziadistato.it** — bot protection block
- **integrazionemigranti.gov.it** deep links — 404
- **apply.unimib.it** — HTTP 403
- **unicatt.it** programme page — 404
- **universitaly.it/cercacorsi** — 404 (no systematic national course sweep possible)
- **cliq.cvcl.it**, **cvcl.unistrasi.it**, **studyinitaly.esteri.it** — DNS resolution failure
- **WebSearch budget exhausted at 200/200** — cost of living, LAZIODISCO, International Talents @unibo scholarship, and several universities were cut short by this.
