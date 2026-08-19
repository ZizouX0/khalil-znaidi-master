# 3F — Cross-country sweep: public institutions charging little or nothing to NON-EU students

**Agent 3F · checked 2026-08-17 · target intake AUTUMN 2027**

---

## 1. Bottom line

Tuition is *not* the binding constraint people assume it is, and the cheapest
headline number is usually the worst deal. Three findings dominate. **(a) The
single highest-value question in my brief — does Tunisia qualify for Austria's
developing-country tuition waiver — is answered NO, definitively, from the
primary legal text**; the old Studienbeitragsverordnung 2004 that listed Tunisia
was *repealed*, and the regulation actually in force lists only OECD-DAC Least
Developed Countries, which Tunisia is not. He therefore pays Austria's ordinary
third-country rate of **€726.72/semester (≈€1,453/year)** — which is still, by a
distance, **the cheapest verified Tier A (English/French-ready) public route in
this whole sweep**, and Austria pairs it with the most graduate-friendly
post-study regime I verified anywhere (12-month job-search permit, then a
Red-White-Red Card for graduates with **no points system and no labour-market
test**). **(b) Czechia's zero tuition is real and I have it from the statute
itself** — Act 111/1998 Sb. §58 charges by *language of delivery*, never by
nationality — but the Czech-taught route requires an entrance exam sat in Czech,
and the preparatory year that gets him there costs **€7,167** at Charles
University's ÚJOP plus a year of living costs and a year of his life. Priced
honestly, "free" Czechia costs **more** than €1,453/year Austria. **(c) Tunisia
IS a full-degree sending partner for Hungary's Stipendium Hungaricum**, which is
genuinely fully funded (tuition exemption + stipend + accommodation + insurance)
and English-taught — the best raw economics available, but it is a competitive
scholarship, not an entitlement, and the 2027/28 call is not yet published.
Norway is now firmly **out** on cost. Germany's tuition is near-zero almost
everywhere but Phase 1's admissibility blockers make that irrelevant. My
coverage of Greece, Slovakia, Croatia, Romania, Latvia and Lithuania **failed**
this session and is declared as a gap, not glossed over.

---

## 2. Coverage statement — what I searched, and what I found nothing on

### Tooling constraint (material — read this)
The session's **WebSearch budget (200/200) was exhausted by other agents** four
searches into my scope. I completed the rest of the work with **WebFetch against
official URLs I could address directly, plus raw `curl` with a browser
user-agent** where WebFetch was refused (403/503). Fallback search engines were
also unavailable (DuckDuckGo HTML/Lite returned challenge pages; Mojeek 403).
`firecrawl` is installed at `/opt/node22/bin/firecrawl` but **no API key is set**
in the environment — the orchestrator would need to supply `FIRECRAWL_API_KEY`.

**Consequence:** I could verify *tuition law and policy* very well, because those
live at stable, guessable official URLs. I could **not** do broad *programme
discovery*, which needs a search engine or a JS-driven national portal. My
programme-level results are therefore thin by construction, and I say so
per-country rather than padding.

### Searched and verified (primary or official source)
| Country | What I verified | Source type |
|---|---|---|
| Austria | Full text of Studienbeitragsverordnung incl. its country annex; fee amounts; graduate residence permits | RIS (Austrian federal law database) + migration.gv.at + univie.ac.at |
| Czechia | Act 111/1998 Sb. §58 (fee-charging powers) in full; Masaryk fee policy; UTB Zlín programme list + admissions; ÚJOP prep-year prices | zakonyprolidi.cz + muni.cz + utb.cz + cuni.cz |
| Germany | Baden-Württemberg €1,500/semester and its exemption list | mwk.baden-wuerttemberg.de |
| Hungary | Stipendium Hungaricum 2026/27 Call for Applications PDF, full text incl. the sending-partner country list and the benefits schedule | stipendiumhungaricum.hu |
| Norway | Fee position, exempt groups, visa financial requirement | studyinnorway.no |
| Poland | Fee rules and exemptions for non-EU | study.gov.pl (official NAWA portal) |
| Slovenia | Non-EU master's fee range | studyinslovenia.si |
| Estonia | Fee range | studyinestonia.ee |

### Searched in local languages
German (`Studiengebühren`, `Studienbeitragsverordnung`, `Erlass`,
`Entwicklungsländer`, `Anlage`), Czech (`navazující magisterské studium`,
`poplatky spojené se studiem`, `marketingové komunikace`, `přijímací řízení`),
Polish (`opłaty`, `cudzoziemcy`, `zwolnienie`, `art. 324`).

### FOUND NOTHING — declared gaps
- **Greece** — the national portal (`studies.minedu.gov.gr`) is JavaScript-driven
  and its tuition page 404s. **I verified nothing about Greek master's fees.**
  Greek public *postgraduate* programmes (ΠΜΣ) generally *do* charge, unlike
  Greek bachelor's — but I could not confirm this and am not reporting it as fact.
- **Slovakia** — `studyin.sk` failed TLS (certificate name mismatch); `uniba.sk`
  returned 503. **Nothing verified.** The prize here would be confirming that
  Slovak-language study at public universities is free to all nationalities
  (as I believe Act 131/2002 provides) — **worth one search when budget allows.**
- **Croatia, Romania, Latvia, Lithuania** — **nothing verified.** The Romanian
  government scholarship for foreign citizens (incl. a funded Romanian-language
  preparatory year) is the specific item worth chasing; `studyinromania.gov.ro`
  404'd.
- **Poland's Article 324 rector-waiver mechanism** — `isap.sejm.gov.pl` served a
  CAPTCHA; alternative legal mirrors 404'd. The *general* rule is verified; the
  *discretionary waiver* is not.
- **Germany — whether any Land besides Baden-Württemberg now charges non-EU
  fees.** `study-in-germany.de/.com` returned 403/503 on every attempt.
  **NOT VERIFIED — check directly** at
  https://www.study-in-germany.de/en/plan-your-studies/requirements/tuition-fees/
- **Cost of living** — I verified only Norway's figure. Every other cost-of-living
  number in this project must come from another agent; I refuse to estimate them.
- **Programme-level matches for Hungary** — I confirmed the *funding* thoroughly
  and the *programmes* not at all. Declared gap, detailed in §3.
- **Italy / France** — deliberately not duplicated (Agents 2D / 2A).

---

## 3. Findings by country

### 3.1 AUSTRIA — the headline answer, and the best verified Tier A route

**THE HIGH-VALUE QUESTION, ANSWERED: Tunisia does NOT qualify for the
developing-country tuition waiver.**

This needs stating carefully because **the internet is wrong about it** and
several aggregator pages (and one Austrian parliamentary document) still
reproduce the old list on which Tunisia *did* appear.

What actually happened: the **Studienbeitragsverordnung 2004** had multiple
annexes; Tunisia sat in the annex granting a *partial refund* of €363.36 per
semester. That regulation was **repealed** — explicitly, by **§8 of the current
Studienbeitragsverordnung (StubeiV), BGBl. II Nr. 218/2019**. I pulled the
consolidated text in force as of **17.08.2026** directly from RIS. It contains
**one single Anlage**, headed:

> *"Anlage — Zu § 4 Abs. 2 Z 1 — Staaten gemäß § 92 Abs. 1 Z 3a UG und § 71 Z 5
> HG — englische Bezeichnung gemäß „DAC List of ODA Recipients""*

and it lists **45 states, all OECD-DAC Least Developed Countries**: Afghanistan,
Angola, Bangladesh, Benin, Bhutan, Burkina Faso, Burundi, Cambodia, Central
African Republic, Chad, Comoros, DR Congo, Djibouti, Eritrea, Ethiopia, Gambia,
Guinea, Guinea-Bissau, Haiti, Kiribati, Laos, Lesotho, Liberia, Madagascar,
Malawi, Mali, Mauritania, Mozambique, Myanmar, Nepal, Niger, Rwanda, São Tomé
and Príncipe, Senegal, Sierra Leone, Solomon Islands, Somalia, South Sudan,
Sudan, Tanzania, Timor-Leste, Togo, Tuvalu, Uganda, Yemen, Zambia.

**Tunisia is an upper-middle-income country and is not on it.** Verdict:
`NO WAIVER — verified against the statute in force`.

**What he actually pays.** Third-country nationals pay the doubled rate:

| Item | Amount | Source |
|---|---|---|
| Studienbeitrag (third-country rate) | **€726.72 / semester** | studieren.univie.ac.at/studienbeitrag/hoehe-studienbeitrag/ |
| ÖH-Beitrag (students' union) | €26.20 / semester | same |
| **Total per semester** | **€752.92** | same |
| **Total for a 120-ECTS master's (4 semesters)** | **≈ €3,012** | computed |

That is **≈€1,453/year in tuition** — comfortably inside the brief's top
affordability band, and it applies **identically to English-taught master's
programmes at public universities**, because Austria charges by residence
status, not by language. **This is the cheapest verified route in this sweep
that requires no new language.**

**Post-study work rights — verified, and unusually good** (migration.gv.at,
"Graduates of Austrian universities and universities of applied sciences",
checked 2026-08-17):
- *"you may renew your residence permit "Students" for a period of **twelve
  months** for the purpose of searching for employment, or starting a business"*
- Then the **Red-White-Red Card for graduates**: *"you can apply for a
  Red-White-Red Card **without a labour market test**"*, and *"**For graduates,
  there is no points system**."* The only substantive condition is being paid
  *"the locally customary gross minimum salary which comparable Austrian
  graduates (junior employees) would receive."*
- After 21 months' qualifying employment in 24 → **Red-White-Red Card plus**,
  unrestricted labour-market access.

For a 12–13/20 student with no elite credentials, "no points system, no labour
market test" is worth a great deal — it is precisely the kind of applicant a
points system filters out.

**146 ECTS verdict:** `BORDERLINE`. Austrian public universities admit to a
master's on the basis of a completed relevant bachelor's; §64(3) UG wording is
about the degree, not a literal credit count, which favours him. But
*Zulassungsvoraussetzungen* are set per-curriculum and some specify ECTS.
Resolve with the FSEG attestation + supplément au diplôme per Phase 1.

**Language:** Tier A *if* he picks an English-taught master's; Tier C for the
German-taught majority (C1 German, ÖSD/Goethe/ÖSD-Zertifikat; German is the
slow category for a French speaker per the brief).

**Programme-level coverage: GAP.** I attempted to verify a specific priority
target — **University of Klagenfurt, "Media and Convergence Management" (MSc,
English-taught, public)**, which on its face is a direction-3/4 hybrid at
€726.72/semester and would be a significant find. Every URL variant I tried on
`aau.at` returned 404 and I had no search engine to locate the live path.
`ACCREDITATION/DETAILS UNVERIFIED — verify before applying.` Start at
https://www.aau.at/en/ and search "Media and Convergence Management".

---

### 3.2 CZECHIA — zero tuition confirmed from the statute; the catch is priced below

**Verified against primary law.** Act No. 111/1998 Sb. on Higher Education,
**§58 "Poplatky spojené se studiem"** (retrieved from zakonyprolidi.cz,
2026-08-17). A public university may charge **only**:

- **§58(1)** an admissions-processing fee (max 20% of the statutory base);
- **§58(3)** a fee where a student exceeds *standard duration + 1 year*;
- **§58(4)** *"Uskutečňuje-li veřejná vysoká škola studijní program **v cizím
  jazyce**… stanoví poplatek za studium"* — a fee where the programme is
  **delivered in a foreign language**.

**There is no nationality-based fee anywhere in §58.** A Tunisian on a
Czech-taught master's at a public university pays **€0 tuition**, exactly as an
EU citizen does. Confirmed operationally by Masaryk University: *"programmes
taught in Czech are completely tuition free"* — with the rider *"a serious
working knowledge of Czech is required"* and advice to take *"a preliminary
language course one year prior to your enrolment."*

Note also **§58(4)(b)(1)**: even *foreign-language* programmes need not charge a
fee for students supported by Czech **government development scholarships**.
Whether Tunisia is a partner country for those — `NOT VERIFIED`.

#### PROGRAMME FIND — Direction 2 (Digital/Growth Marketing)
| Field | Detail |
|---|---|
| University | **Univerzita Tomáše Bati ve Zlíně (Tomas Bata University in Zlín)** — public |
| Faculty | Fakulta multimediálních komunikací (Faculty of Multimedia Communications) |
| Programme | **Marketingová komunikace (Mgr.)** — navazující magisterské |
| City / country | Zlín, Czechia |
| Duration / form | **2 years**, prezenční (full-time); also offered kombinovaná |
| Degree | Mgr. (master's). Total ECTS not stated on page — `assume 120, confirm` |
| Tuition, non-EU | **€0** (Czech-taught → outside §58(4)) |
| Teaching language | Czech — **Tier C** |
| Direction match | Marketing communications: consumer behaviour, advertising creativity, marketing management, brand/social-media/content careers named explicitly |
| Entry / language | Foreign applicants *"konají přijímací zkoušky v českém jazyce a prokazují tak připravenost studovat v českém jazyce"* — **the entrance exam is sat in Czech and substitutes for a B2 certificate**. So: no paper certificate needed, but real exam-grade Czech is. |
| Application fee | **740 Kč (≈€30)** |
| Deadline | 1 Jan – **30 April 2026** for the 2026 cycle. **2027 dates not yet published — treat 30 April 2027 as indicative.** |
| Entrance exam date | 29 May 2026 (2026 cycle) |
| 146 ECTS verdict | `LIKELY OK` — admission turns on holding a completed bachelor's plus the entrance exam, not on a credit audit |
| URL | https://fmk.utb.cz/studium/prijimaci-rizeni/magisterske-studium/ |

#### PRIORITY FOLLOW-UP — possible Tier A version of the same degree
The same faculty lists **"Marketing Communications (Mgr.) — 2 years, English
language, paid tuition."** The **fee amount is `NOT VERIFIED — check directly`**
(the faculty's English pages and `utb.cz/en/study/tuition-fees/` both 404'd for
me). **This matters a lot**: Czech public universities typically price
English-taught programmes at roughly €2,000–€4,000/year, and if that holds, this
is an English-taught marketing-communications master's, at a public university,
for less than the language year alone would cost — which would make it one of
the strongest finds in the entire project. **Someone should email
+420 576 034 205 / the FMK admissions office and get this number.**
Start: https://fmk.utb.cz/en/studies/study-programmes/marketing-communications/

#### Direction 4 (Creative/cultural industries management) — flagged, with a caveat
**UTB Zlín, "Arts Management" (MgA.), 2 years.** A genuine
creative-industries-management master's at a zero-tuition public university.
**Caveat: for 2025/2026 it is offered in *kombinovaná* (part-time) form only** —
full-time was not on offer. Part-time study normally does **not** support a
long-term residence permit for study purposes, which would defeat the visa and
post-study-work requirement. `BLOCKING unless a full-time cohort reopens for
2027 — verify.`

Also present at FMK, music-adjacent but **not** music business: *Teorie a praxe
audiovizuální tvorby* with a Sound Design specialisation. Not a match for
directions 3 or 4 as defined; recorded so the gap is visible.

#### The Czech language pathway — with real prices (this drives §4)
**Charles University, Institute of Language and Preparatory Studies (ÚJOP)** —
Foundation Programmes in Czech, Prague or Poděbrady, **three trimesters**, from
zero or from B1, reaching **B1/B2/C1**. Intakes **September 2026 and September
2027**. Claimed 90%+ success rate.

| Track | Intensity | Price |
|---|---|---|
| **Economics, Business and Management — COMPLEX** | 35 h/week | **CZK 167,000 ≈ €7,167** |
| Humanities — COMPLEX | 35 h/week | CZK 167,000 ≈ €7,167 |
| Humanities — PROGRESS | 25 h/week | CZK 120,000 ≈ €5,150 |
| Arts and Architecture — COMPLEX | 35 h/week | CZK 167,000 ≈ €7,167 |

Source: https://ujop.cuni.cz/UJOPEN-69.html (checked 2026-08-17). Visa
sponsorship not stated on the page — `verify`. Cheaper regional providers
(Masaryk, Palacký, Charles's own shorter courses) very likely exist; I had no
search capability to price them, so **€7,167 should be read as the
well-documented upper anchor, not the floor.**

**Realistic time to Czech at entrance-exam standard:** Czech is a Slavic
language with seven cases — for a French/Arabic speaker it is squarely the
**slow** category the brief contrasts with Spanish and Italian. **12–18 months**
of committed study; the ÚJOP year is 3 trimesters at 35 h/week precisely because
less does not work. **Tier C, firmly.**

**Post-study work rights: `NOT VERIFIED`.** Czechia implements EU Directive
2016/801, which obliges member states to allow graduates at least 9 months to
seek work, and the Czech instrument is the *long-term residence permit for the
purpose of seeking employment or commencing business activities* — but both the
old (`mvcr.cz`) and redirected (`mv.gov.cz`) pages 404'd. **Confirm before
shortlisting.**

---

### 3.3 HUNGARY — Tunisia IS a partner; fully funded; English-taught

**Verified from the primary document**: *Stipendium Hungaricum Call for
Applications 2026/2027 (BA/MA/One-tier MA)*, PDF, extracted in full.

**Tunisia's status:** the **"Tunisian Republic" appears in the sending-partner
list for FULL-DEGREE programmes** (p.7 country list), not merely in the
partial/exchange list on p.10 — so **master's degrees are open to him**. Tunisia's
sending partner is the **Ministère de l'Enseignement Supérieur**.

**What the scholarship covers (§1.3 of the Call):**
- **"Tuition-free education — exemption from the payment of tuition fee"**
- **Monthly stipend**, master's level: **HUF 43,700 ≈ €110/month**, 12 months/year
- **Accommodation**: free dormitory place (subject to capacity) **or**
  **HUF 40,000 ≈ €100/month** contribution
- **Medical insurance**: Hungarian social-security healthcare + supplementary
  cover up to **HUF 65,000 ≈ €165/year**

**Read the small print honestly.** The Call itself warns: *"these provisions are
only a contribution to the living expenses… it does not fully cover all the
living costs, and the students need to add their own financial resources"*, and
specifically that in Budapest the HUF 40,000 *"would not cover the full amount of
rental costs."* Total support ≈ **€210/month**. So this is a **tuition-free
degree with a partial living subsidy**, not a free ride — but on cost it still
beats everything else in this sweep.

**Language (§2.5):** English-taught programmes are the mainstream route →
**Tier A**. Two obligations to note:
- Every scholarship holder **must take "Hungarian as a foreign language" in year
  one and pass the exam** at the end of semester two. Fail or skip it and *"the
  monthly stipend… will be reduced to 30,000 HUF/month."* A real but modest
  condition.
- A Hungarian-taught degree route exists, requiring an **obligatory one-year
  Hungarian language preparatory course**, itself scholarship-funded — recorded
  here strictly as an entry route attached to a master's, per the brief. Hungarian
  is non-Indo-European and **Tier C**; given the English route exists, there is
  no reason to take it.

**Deadline — read carefully (brief §1 applies):**
- 2026/27 cycle: **15 January 2026, 14:00 CET — this is PAST and therefore STALE
  for our purposes.**
- **For AUTUMN 2027 he needs the 2027/28 call**, expected to open **~November
  2026** with a deadline **~mid-January 2027**. **NOT YET PUBLISHED — treat
  15 January 2027 as indicative only** and watch
  https://stipendiumhungaricum.hu/apply/. Applications are free; the Call warns
  against agencies.

**146 ECTS verdict:** `BORDERLINE` — set by each Host Institution, not by the
scholarship. **GPA reality check:** SH is competitive, but it runs on
**per-country quotas negotiated bilaterally**, so he competes against other
Tunisian applicants rather than the global pool. At 12–13/20 this is a genuine
shot, not a lottery ticket — but it is **not a plan on its own**; it must be run
in parallel with a self-funded fallback.

**Programme-level coverage: GAP — this is my main substantive shortfall.** I
confirmed the money thoroughly and matched **no specific Hungarian master's to
the four directions.** The SH study finder and `studyinhungary.hu` are both
JS-driven/503 and I had no search budget left. Two leads worth chasing:
- **Budapest University of Economics and Business (BGE/BBU)** — named as a
  participating institution; the natural home of an English-taught marketing or
  commerce master's.
- **Liszt Ferenc Academy of Music** — named as a participating institution.
  Relevant to directions 3/4 **only if** it offers a *management/business*
  master's rather than performance; his music background is a hobby with no
  portfolio, so a performance programme is out per the brief.
- **University of Pécs, Faculty of Business and Economics** — I *did* verify its
  English-taught master's list: **MSc Business Development**, **MSc International
  Economy and Business**, **MSc Management and Leadership** (EFMD accredited).
  **There is no Marketing MSc.** *Business Development* is a partial
  direction-2 match. Fees/SH-eligibility `NOT VERIFIED`.
  https://ktk.pte.hu/en/education/master-programmes

**Post-study work rights in Hungary: `NOT VERIFIED — check directly.`**

---

### 3.4 GERMANY — tuition is cheap and it does not matter

**Baden-Württemberg confirmed** (Ministerium für Wissenschaft, Forschung und
Kunst BW, checked 2026-08-17): **€1,500 per semester** for *"All future students
who are not nationals of a state of the European Union (EU) or the European
Economic Area (EEA)"*, in force since winter semester 2017/18. Second degree:
€650/semester. Exemptions include EU/EEA nationals and family members, doctoral
students, exchange/double-degree students under partnership agreements,
recognised refugees, non-EU citizens with 5+ years' legal employment in Germany,
and those who completed a prior degree in Germany — **none of which he meets**.
So in BW he would pay **€3,000/year**.

**Whether any other Land has followed: `NOT VERIFIED`** — `study-in-germany.de`
and `.com` returned 403/503 on every attempt and I had no search fallback. My
working understanding is that **BW remains the only state with a general non-EU
tuition fee**, and that everywhere else the cost is only the **Semesterbeitrag of
roughly €150–€400/semester** (which typically bundles a public-transport pass) —
**but I am flagging this as unverified rather than asserting it.** Check:
https://www.study-in-germany.de/en/plan-your-studies/requirements/tuition-fees/

**Why this is nonetheless a low-priority direction.** Phase 1 already established
Germany as **CLOSED/deprioritised**: six semesters *and* 180 ECTS are enforced,
and *"the likelier blocker is the GPA — the common 2.5/'good' threshold, which
12–13/20 probably misses."* Phase 1 also disproved the two escape hatches
(Fachhochschulen apply the same or stricter credit rules; Studienkolleg is
bachelor-entry only). **So Germany is the clearest case in this report of a
country where tuition is near-zero and completely beside the point.** Report the
tuition accurately, as instructed — then do not spend application effort there.

---

### 3.5 NORWAY — verified closed on cost

Confirmed at studyinnorway.no (checked 2026-08-17). Non-EU/EEA degree-seeking
students **pay tuition** at public institutions. The only exempt groups are:
students from Norway/Switzerland/EU/EEA; **exchange students; doctoral
candidates; and holders of Fulbright, Erasmus Mundus, NORPART, NORHED or StAR
places.** He fits none. **No fee-free Norwegian public institution was
identified**, and the page notes no 2026 fee abolition. Students admitted
*before autumn 2023* were grandfathered — irrelevant to a 2027 intake.

Everyone pays ~**NOK 1,000/semester** to the student welfare organisation.

**The decisive number is the visa requirement, not the tuition**: applicants must
show **NOK 15,488/month = NOK 170,368/year (2026–2027)** ≈ **€14,600/year** in
living costs alone, *before* fees that typically run €11,000–€33,000/year.

**Verdict: EXCLUDED.** Phase 1 listed Norway as OPEN on *credential recognition*
grounds (its year-based assessment is genuinely favourable to him) — that remains
true and is worth remembering, **but it is unaffordable**, and affordability is
the binding constraint in this project. A cheaper-fee institution may emerge for
2026/27 under the amendment permitting lower fees; even so, €14,600/year of
mandatory proven funds keeps it out of range.

---

### 3.6 POLAND — cheap, not free; the "Polish-taught is free" belief is wrong

Verified at **study.gov.pl** (the official NAWA portal), checked 2026-08-17.
Non-EU foreigners **must pay tuition**, and **Polish-language programmes are not
free to them**. Stated averages:

| Item | Cost |
|---|---|
| Bachelor's / long-cycle | €2,000 / year |
| **Postgraduate (master's)** | **€3,000 / year** |
| Polish-language preparatory course | €2,000 / year |

**Exemptions identified:** (i) foreigners who study *"on terms applicable to
Polish citizens"* — chiefly **EU/EEA nationals and holders of the Karta Polaka
(Card of the Pole)**, which he cannot obtain (it requires demonstrated Polish
ethnicity/heritage); (ii) **doctoral schools**, which are tuition-free *and*
carry a stipend — not applicable, he needs a master's.

**Not verified:** the discretionary **Article 324** rector-waiver mechanism, and
whether NAWA scholarship holders are fee-exempt. `isap.sejm.gov.pl` served a
CAPTCHA. Worth one search: the **NAWA Banach Scholarship Programme** targets
**master's** study for citizens of developing countries and covers fees plus a
stipend — **whether Tunisia is on its eligibility list is a genuinely
high-value open question I could not close.**

**Assessment:** at ~€3,000/year Poland sits inside the brief's "under €8,000"
band, English-taught programmes are plentiful, and Phase 1 rated Poland **OPEN**
on credentials. It is a solid mid-table option — just not a free one.

---

### 3.7 SLOVENIA — non-EU pay; wide range

studyinslovenia.si (checked 2026-08-17): *"Non-EU/EEA students (third-country
citizens) who do not have permanent residence in Slovenia in most cases pay
tuition fees."* Master's: **€2,000–€15,000/year**. **No language-based
exemption** was identified — i.e. unlike Czechia, studying in Slovene does not
appear to make it free. The only exemption noted is permanent residence in
Slovenia. Bilateral-agreement exemptions: not addressed on the page. At the
bottom of that range Slovenia is affordable; at the top it breaches the filter.
`Programme-level: nothing found.`

---

### 3.8 ESTONIA — mid-range, unverified language rule

studyinestonia.ee (checked 2026-08-17): *"tuition fees vary from 1500 EUR to
15000 EUR per year for Bachelor and Master programmes"*, and — directly against
us — *"Some of the more expensive specialities are medicine, law, **business
administration and social sciences**."* Doctoral study is fee-free. The page
notes only that *"Some higher education institutions may differentiate tuition
fees for students from the European Union and from outside the European Union."*
**Whether Estonian-taught programmes are free is `NOT VERIFIED`** — and Estonian
is a non-Indo-European, 14-case language, i.e. **Tier C at the extreme end**, so
even a confirmed exemption would fail the §4 test below. Not worth pursuing.

---

### 3.9 ITALY — mechanism noted only (Agent 2D owns this)

Not duplicated. Recording the mechanism because it is the one genuinely powerful
income-based lever in Europe and **it has no equivalent in any country I swept**:
Italian public universities scale the annual *contributo onnicomprensivo* to
family income via the **ISEE** (for a non-resident family, the **ISEE
parificato**, computed in Italy from consular-certified documents). A low
household income can reduce the contribution to the **no-tax area — effectively
€0 beyond a small regional tax and stamp duty.** For a Tunisian family this is
frequently the outcome. **If Agent 2D confirms it, Italy plausibly beats
everything in this report**, because it delivers near-zero tuition *without*
requiring a language he lacks — Italian is in the brief's *fast* category for a
French speaker, and Italy also offers many English-taught master's.

### 3.10 FRANCE — not duplicated (Agent 2A owns the *exonération* mechanism).

---

## 4. THE KEY JUDGEMENT — is a cheaper degree worth an extra year of language?

The brief asks this explicitly, so here is the arithmetic, then the verdict.

### The comparison, priced honestly

**Route A — Austria, English-taught public master's (Tier A, no language year):**

| Item | Cost |
|---|---|
| Tuition, 4 semesters × €752.92 | **€3,012** |
| Language preparation | **€0** |
| Years to degree | **2** (graduates summer 2029) |

**Route B — Czechia, Czech-taught public master's (Tier C, one language year):**

| Item | Cost |
|---|---|
| Tuition, 2-year master's | **€0** |
| ÚJOP preparatory year (Economics/Business COMPLEX) | **€7,167** |
| Living costs during that extra year | **≈ €7,000–9,000** *(not verified by me — Prague; use another agent's figure)* |
| Years to degree | **3** (graduates summer 2030) |
| **Cash cost before the master's even starts** | **≈ €14,000–16,000** |

### The verdict

**Route B's "free" degree costs roughly €11,000–€13,000 MORE in cash than Route
A's paid one — and then costs a year on top.** The €3,012 of Austrian tuition he
"saves" is less than half the ÚJOP fee alone. Add the forgone year: a junior
digital-marketing or CRM role in Central Europe pays on the order of
€20,000–€30,000 gross, so even discounting heavily for the chance he wouldn't
walk straight into one, the opportunity cost of the extra year is the largest
single number in this table — and it never appears in any "study free in Europe"
listicle.

**So: no. Do not buy a free Czech degree with a year of Czech.** Not on cost
grounds, which is the whole justification usually offered for it.

**Four qualifications, because the answer is not "never learn a language":**

1. **The calculus inverts if the alternative is expensive.** Against a €15,000/year
   private business school, the Czech route wins outright. It is only a bad deal
   *because* Austria at €1,453/year exists as a Tier A comparator. **Route B is the
   right answer if and only if Routes A and C both fail.**

2. **It inverts again if he wants to live there.** Czech at B2/C1 is not a cost if
   the plan is a career in Czechia — it is the single highest-return investment he
   could make, since it converts him from a foreign graduate competing for
   English-language roles into a local hire. The question is not "is Czech worth
   a year?" but "is Czech worth a year *to someone who will leave after
   graduating?*" — and the answer to that is no.

3. **Czech is the wrong language to spend the year on anyway.** The brief notes
   that Spanish and Italian are far faster for a French speaker than German or a
   Nordic language; Czech, with seven cases, is slower still. If he is going to
   spend a year on a language, **Italian buys a comparable near-zero tuition
   outcome via ISEE (§3.9) in a fraction of the study time** — and Italian is
   partly comprehensible to a French speaker from day one, which Czech is not.
   **Spending the year on Czech is the worst version of this trade.**

4. **The English-taught UTB Zlín programme could dissolve the dilemma entirely.**
   Same faculty, same marketing-communications degree, no language year — the only
   unknown is the fee. **Get that number before anyone commits to a Czech
   preparatory year**, because if it lands near €2,500/year it dominates both
   routes in this comparison.

### Ranked recommendation — by overall value, not by tuition

| # | Route | Tuition | Tier | Why it ranks here |
|---|---|---|---|---|
| **1** | **Hungary — Stipendium Hungaricum** | **€0** + ~€210/mo support | **A** (English) | Best economics available and Tunisia is a confirmed full-degree partner. **Not a plan on its own** — competitive, and the 2027/28 call isn't published. Apply, in parallel with #2. |
| **2** | **Austria — public university, English-taught master's** | **€1,453/yr** | **A** | The reliable backbone. No language year, no scholarship lottery, and the best post-study regime verified anywhere: 12-month job search → RWR Card with **no points system, no labour-market test**. |
| **3** | **Czechia — UTB Zlín, Marketing Communications (English)** | **`NOT VERIFIED`** | **A** | Could outrank #2 on cost with zero language risk. **Blocked on one missing number — chase it.** |
| **4** | **Poland — English-taught public master's** | ~€3,000/yr | **A** | Honest mid-table. Phase 1 rates Poland OPEN. Chase the NAWA Banach eligibility question. |
| **5** | **Czechia — UTB Zlín, Marketingová komunikace (Czech)** | **€0** | **C** | A genuinely good, genuinely free degree that is **the wrong purchase** at a real cost of €14–16k + a year. Fallback only. |
| **6** | **Germany** | €0–€300/sem outside BW; €3,000/yr in BW | A/C | Cheapest tuition in Europe, and almost certainly inadmissible on 180 ECTS + GPA. Do not spend effort here. |
| — | **Norway** | €11k–33k/yr + €14.6k proven funds | — | **Excluded on cost.** |
| — | **Slovenia / Estonia** | €1.5k–15k/yr | A/C | Too wide a range to act on; business fields sit at the expensive end. |

**One-line summary for the student:** *chase the Hungarian scholarship and hold
Austria as the fallback; get the Zlín English fee before considering any year of
Czech; and treat "free tuition in Germany" as a fact that will not help you.*

---

## 5. Stretch options

- **UTB Zlín, "Arts Management" (MgA.), 2 years, €0 tuition** — fails exactly one
  filter: currently **part-time only**, which likely breaks the student residence
  permit and hence post-study work rights. If a full-time cohort opens for 2027 it
  becomes a direction-4 find at zero tuition.
- **University of Klagenfurt, "Media and Convergence Management" (MSc, English)** —
  would be a direction-3/4 hybrid at €726.72/semester. Fails only on my inability
  to verify it exists at that URL. **Highest-value single item to re-check.**
- **University of Pécs, MSc Business Development (English)** — partial direction-2
  match at a Stipendium Hungaricum host institution. Fee and SH eligibility unverified.
- **NAWA Banach Scholarship (Poland)** — master's-level, developing countries, fees
  + stipend. Fails only on unverified Tunisian eligibility.

---

## 6. Sources (all checked 2026-08-17)

**Austria**
- Studienbeitragsverordnung (StubeiV), BGBl. II Nr. 218/2019, consolidated text in force 17.08.2026, incl. §8 (repeal of StubeiV 2004) and the Anlage country list — https://ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20010724
- Fee amounts (€726.72 + €26.20) — https://studieren.univie.ac.at/studienbeitrag/hoehe-studienbeitrag/
- Anlage list cross-check (35–45 LDC states, Tunisia absent) — https://www.kug.ac.at/studium/waehrend-des-studiums/kosten-stipendien-beihilfen/studien-und-studierendenbeitrag
- Graduate residence permit + Red-White-Red Card — https://www.migration.gv.at/en/types-of-immigration/permanent-immigration/graduates/

**Czechia**
- Act 111/1998 Sb. §58 (Poplatky spojené se studiem) — https://www.zakonyprolidi.cz/cs/1998-111#p58
- Masaryk University fee policy — https://www.muni.cz/en/admissions/bachelors-and-masters-studies/tuition-fees-and-financial-aid
- UTB Zlín FMK master's programme list — https://fmk.utb.cz/studium/moznosti-studia/magisterske-studium-2/
- UTB Zlín FMK master's admissions (Czech-language exam, fees, deadlines) — https://fmk.utb.cz/studium/prijimaci-rizeni/magisterske-studium/
- Charles University ÚJOP foundation-programme prices — https://ujop.cuni.cz/UJOPEN-69.html

**Germany**
- Baden-Württemberg €1,500/semester and exemptions — https://mwk.baden-wuerttemberg.de/de/hochschulen-studium/studieren-in-bw/studienfinanzierung/gebuehren-fuer-internationale-studierende-und-zweitstudium/tuition-fees-for-international-students

**Hungary**
- Stipendium Hungaricum Call for Applications 2026/2027 (BA/MA/One-tier MA), full PDF — https://stipendiumhungaricum.hu/wp-content/uploads/2025/10/BA_MA_OTM_Call_for_Applications_2026_27.pdf
- Tunisia country page — https://stipendiumhungaricum.hu/country/tunisia/
- University of Pécs FBE English master's — https://ktk.pte.hu/en/education/master-programmes

**Norway**
- Fees, exemptions, NOK 15,488/month financial requirement — https://studyinnorway.no/cost-and-requirements

**Poland**
- Tuition rules and exemptions for non-EU — https://study.gov.pl/tuition-fees

**Slovenia** — https://studyinslovenia.si/study/tuition-and-funding/
**Estonia** — https://studyinestonia.ee/tuition-fees

**Attempted and failed** (declared gaps): study-in-germany.de/.com (403/503);
studies.minedu.gov.gr (JS-driven); studyin.sk (TLS certificate mismatch);
uniba.sk (503); studyinromania.gov.ro (404); studyinlatvia.lv (no fee page);
isap.sejm.gov.pl (CAPTCHA); aau.at master's pages (404 on all variants);
mvcr.cz / mv.gov.cz post-study permit page (404); studyinhungary.hu (503);
utb.cz English tuition-fee page (404).
