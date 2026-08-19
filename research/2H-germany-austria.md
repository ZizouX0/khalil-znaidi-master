# 2H — AUSTRIA (primary) + GERMANY (secondary)

**Agent 2H · checked 2026-08-17 · target intake AUTUMN 2027**

---

## 1. Bottom line

**The Austrian tuition contradiction is resolved, and both earlier agents were
right about different things.** Austria charges by *sector*, not by one national
rate: **public universities** (governed by the *Universitätsgesetz*) charge
third-country nationals the **doubled** rate of **€726.72 per SEMESTER
(≈€1,453/year)** — Agent 3F's figure is correct for universities;
**Fachhochschulen** (governed by the *FH-Gesetz*) set their own third-country
policy, and FH Kufstein charges **€363.36 per semester (€726.72/YEAR)** to
everyone including Tunisians — Agent 3G's figure is correct for Kufstein. The
FH spread is enormous and nobody had measured it: I verified **€363.36/sem
(Kufstein, Salzburg, BFI Wien, CAMPUS 02) → €500 (Kärnten) → €726.72 (FH OÖ,
Joanneum) → €850 (Wiener Neustadt) → €3,000 (Technikum Wien) → €6,900 (IMC
Krems) → €8,250/sem (MCI Innsbruck)**. Choosing the wrong Austrian FH costs
**23× more** than choosing the right one. **Second, Agent 3G's §4(4) FHG
flexibility finding survives but must be narrowed: the statute is permissive,
individual FHs are not uniformly so.** IMC Krems prints *"a completed bachelor
degree with minimum 180 ECTS lasting at least six semesters"* verbatim; WU Wien
prints *"at least 180 ECTS credits… with 45 ECTS in business administration"*.
Conversely **FH Salzburg publishes the single best-worded rule I found anywhere
in this project — *"an equivalent bachelor programme of at least 3 years
duration"* — a years test with no credit count at all.** **Third, and decisive
for a student with no English test: FH Kufstein remains the ONLY Austrian
institution I could verify that accepts a plain medium-of-instruction letter
from any university in place of IELTS/TOEFL.** Every other Austrian institution
checked either demands a certificate outright, or exempts only applicants whose
*previous degree was taught in English* (which a French-taught Tunisian licence
is not), or — Uni Wien — accepts an MOI confirmation only from
EU/EEA/CH/UK/US/AU/NZ/CA institutions, explicitly excluding Tunisia. **Fourth,
Germany: I cracked anabin.** Université de Sousse is rated **H+** (state
institution, top status) and the **Tunisian *Licence Fondamentale* is rated
"Entspricht" (equivalent) to a German 3-year bachelor**, the *Licence Appliquée*
"Bedingt vergleichbar". So the credential is NOT Germany's blocker — the GPA and
the German-language requirement are, exactly as Phase 1 predicted. **No viable
German public route was found.** **Fifth: direction 3 (music marketing) is
absolutely empty in Austria, and direction 4 has exactly one true match which is
blocked three ways.**

---

## 2. Coverage statement

**Institutions swept (Austrian FH sector):** FH Kufstein, FHWien der WKW, FH
Salzburg, FH JOANNEUM (Graz), FH Vorarlberg, FH St. Pölten / USTP, FH Campus
Wien, FH Technikum Wien, FH Oberösterreich (Steyr + Hagenberg), FH Burgenland,
IMC Krems, MCI Innsbruck, FH Kärnten, FH des BFI Wien, Lauder Business School,
**plus two not on the brief's list that turned up matches: CAMPUS 02 Graz and FH
Wiener Neustadt.**

**Austrian universities swept:** WU Wien, Universität Wien, Universität
Klagenfurt (AAU), JKU Linz, Universität für Weiterbildung Krems (Danube). Uni
Graz, Uni Innsbruck, Uni Salzburg and MODUL were **not individually verified** —
declared gap, but see §5 for why the UG rule makes them low-yield.

**Search languages:** German (`Masterstudium`, `Zugangsvoraussetzungen`,
`Studiengebühren Drittstaaten`, `berufsbegleitend`, `Musikmanagement`,
`Marketing und Vertrieb`, `Musikwirtschaft`), English, plus the anabin database
queried directly in German.

**Tooling notes.** WebSearch budget was available this session (previous agents'
exhaustion did not carry over). **anabin was solved**: its public REST API is
reachable at `https://anabin.kmk.org/api/public/{institution,degree,certificates}/?search=…`
even though the front end is a JavaScript SPA — endpoint list recovered from
`/public/dist/institutions.js`. **Blocked / failed:** `ustp.at` (FH St. Pölten's
new domain) returned **403**; `make-it-in-germany.com` returned a **Radware bot
challenge**; `fhv.at` (FH Vorarlberg) master page 404'd; `donau-uni.ac.at`
German URL 404'd (English worked). Hand these to the orchestrator's Firecrawl
key if the detail matters.

### Found NOTHING on — stated explicitly

| Gap | Status |
|---|---|
| **Direction 3 — music marketing / artist promotion, ANYWHERE in Austria** | **ZERO. Not one programme, FH or university.** Confirms and extends Agent 3G's empty result. |
| **Direction 4 — music business in the Austrian FH sector** | **ZERO.** The only Austrian music-business master is at Danube University Krems (a *Weiterbildung* university) and it is triple-blocked — §4.4. |
| **Cost of living for Kufstein / Klagenfurt / Salzburg / Graz** | **NOT VERIFIED.** I refuse to estimate. Another agent must supply. |
| **Uni Graz, Uni Innsbruck, Uni Salzburg, MODUL University** | Not individually verified — coverage gap. |
| **FH Campus Wien, Lauder Business School, FH OÖ Hagenberg** | No marketing/music master identified; FH Campus Wien is health/social/tech-dominated. Not exhaustively verified. |
| **FH Vorarlberg *International Marketing & Sales*** | **Status unresolved.** 3G reported it *auslaufend* (phasing out); search results still list it; the programme URL 404'd. `NOT VERIFIED — check directly.` |
| **FH St. Pölten *Digital Marketing & Kommunikation* (Master)** | Exists, German-taught. Detail unobtainable — **ustp.at returns 403**. `NOT VERIFIED.` |

---

## 3. THE TUITION QUESTION, RESOLVED (task 3)

### 3.1 The two regimes

**Public universities — *Universitätsgesetz* §91.** Ordinary students from
third countries without equal status pay **double** the standard
`Studienbeitrag`:

| Item | Amount | Note |
|---|---|---|
| Standard `Studienbeitrag` (EU/EEA) | **€363.36 / semester** | |
| **Third-country rate** | **€726.72 / SEMESTER** | = **€1,453.44 / year**; ≈ **€2,906.88** for a 4-semester 120-ECTS master |
| ÖH (students' union) contribution | **€23.70 / semester (2026)** | **extra**, on top, paid by everyone |

Source: `studieren.univie.ac.at/studienbeitrag/hoehe-studienbeitrag/` and ÖH Uni
Wien `oeh.univie.ac.at/seite/wie-hoch-ist-die-studiengebuehr` (checked
2026-08-17). Ukraine is currently the only exception.

**→ Agent 3F was CORRECT.** Agent 3G's "€726.72/year" was correct *for FH
Kufstein* and wrong if generalised to universities.

**Fachhochschulen — *FH-Gesetz*.** The FHG caps the ordinary fee at €363.36 per
semester, but each FH is an autonomous provider (`Erhalter`) and **sets its own
third-country policy**. There is **no single Austrian FH rate.** Verified spread:

| Institution | Non-EU tuition | Per | Annual (non-EU) | Source checked 2026-08-17 |
|---|---|---|---|---|
| **FH Kufstein Tirol** | **€363.36** | semester | **€726.72** | fh-kufstein.ac.at/en/admissions/tuition-fees — *"EUR 363.36 per semester"*; non-EU pay only a **€726.72 deposit credited to year 1** |
| **FH Salzburg** | **€363.36** | semester | **€726.72** | fh-salzburg.ac.at fees page — non-EU pay a **deposit** credited to semester 1, not a surcharge |
| **FH des BFI Wien** | **€363.36** | semester | **€726.72** | fh-vie.ac.at — *"the same as for EU/EEA citizens"*; €200 deposit, credited |
| **CAMPUS 02 Graz** | **€363.36** | semester | **€726.72** | campus02.at |
| **FH Kärnten** | **€500** | semester | **€1,000** | fh-kaernten.at — *"€ 500 per semester"* for third-country nationals **from WS 2026** |
| **FH Oberösterreich** | **€726.72** | semester | **€1,453.44** | fh-ooe.at — doubled, + €79 application fee |
| **FH JOANNEUM** | **€727** | semester | **€1,454** | fh-joanneum.at — **first two semesters payable in advance (€1,454)** before the place is confirmed |
| **FH Wiener Neustadt** | **€850** | semester | **€1,700** | fhwn.ac.at — 1st sem €1,100 less €250 non-refundable registration fee |
| **FH Technikum Wien** | **€3,000** | semester | **€6,000** | technikum-wien.at — *"€3.000 je Semester"* for Drittstaaten |
| **IMC Krems** | **€6,900** | semester | **€13,800** | imc.ac.at study-fees (Business & Health band; Science & Tech €9,500/sem) + €300 registration |
| **MCI Innsbruck** | **€8,250** | semester | **€16,500** | mci.edu — **EXCLUDED on the brief's €15k filter** |

**ÖH fee is always extra and always additional**, roughly €24–27 per semester
depending on the year and institution (€23.70 quoted for 2026 by ÖH Uni Wien;
€25.20 by FH Technikum Wien; €26.20 by IMC Krems and FH Kufstein). Treat as
≈€50/year — immaterial, but do not forget it exists.

**Practical consequence:** the cheapest verified route in Austria is an FH that
does not surcharge third-country nationals — **€726.72/year at Kufstein,
Salzburg, BFI Wien or CAMPUS 02 — literally half the public-university price.**
This inverts the usual assumption that the public university is cheaper.

---

## 4. Programmes by direction

### DIRECTION 2 — Digital & growth marketing

#### ★★ #1 FIND — FH Kufstein Tirol, MA Digital Marketing (full-time)

Confirmed independently of Agent 3G and **upgraded**: the fee is now verified as
**€363.36/semester = €726.72/year including for third-country nationals** (not
the doubled rate), and the MOI-letter concession is confirmed as **unique among
the Austrian institutions I checked**.

| Field | Detail |
|---|---|
| Institution / type | Fachhochschule Kufstein Tirol, **Kufstein, Austria** — public-funded UAS, state-recognised under the FHG |
| Degree / ECTS | **MA in Business, 120 ECTS**, 4 semesters full-time |
| Direction match | **Direction 2, pure** |
| Language | **100% English — Tier A** |
| **Tuition, non-EU** | **€726.72/year** (€363.36/sem) + ÖH ≈€26/sem. **€726.72 deposit at application, credited to year 1.** |
| **Entry wording** | §4(4) FHG equivalence clause (quoted in full in 3G's report) + *"…summarily treated in a total of at least 30 ECTS"* in Marketing/Communication/Management/Business administration |
| **146 ECTS verdict** | **LIKELY OK** — no 180 count; only threshold is ≥30 ECTS in the subject core, which a Licence in Marketing clears many times over |
| **Language requirement — THE DECISIVE FEATURE** | CEFR **B2** (IELTS 6.0 / TOEFL 72 / PTE 60). *"As an alternative to the language certificates listed above, applicants can submit a certificate or an official letter (MOI) from a university/school that clearly demonstrates the language competence at CEFR level B2 or higher."* **This is the only Austrian institution verified to accept an MOI letter from a non-EU/non-Anglophone university.** Proof accepted up to programme start, not at application. |
| Deadline | Third-country: **3 March** (2027 date unpublished — indicative) |
| GMAT/GRE | Not used. Selection by interview |
| Post-study work | Austria: 12-month job-search permit → RWR Card (§6) |
| URL | https://www.fh-kufstein.ac.at/en/master/digital-marketing-ft |

#### ★ #2 — FH Salzburg (institution-level find; best-worded entry rule in the project)

FH Salzburg's master admission rule, published centrally and applying across its
master portfolio:

> *"an equivalent bachelor programme of **at least 3 years duration** at an
> accredited institution in or outside Austria has been completed"* … *"§ 4
> FHG"* … *"The degree program head makes final admission decisions"* —
> fh-salzburg.ac.at/en/prospective-students/about-to-start-studying/admission-requirements-for-master-programmes

**146 ECTS verdict: LIKELY OK — the strongest wording found anywhere.** This is
a *years* test with **no credit count of any kind**, which is exactly the ground
on which the 146/180 transcript artefact cannot bite. Tuition **€363.36/sem =
€726.72/year, non-EU pay only a deposit**. Non-EU deadline **31 March / 1 April**
depending on programme.

**Caveat that costs it the #1 slot:** FH Salzburg's business masters
(*Business Management*) state *"A proof of proper German language skills is an
entry requirement"* — **Tier B/C**. Its English-taught master is *Innovation &
Management in Tourism*, which is not a direction match. **So the excellent rule
sits behind a German-language wall for the programmes he wants.** Worth an email
asking whether any English-taught business master is planned for 2027.

#### FH Wiener Neustadt — MA Global Business Leadership (ex-Business Consultancy International)

| Field | Detail |
|---|---|
| Type / city | Fachhochschule, Wiener Neustadt |
| Language | **English — Tier A** |
| Direction match | **Direction 2** — carries a dedicated **marketing specialisation**: *"a forward-thinking marketing specialist… able to combine an in-depth understanding of strategic marketing with strong analytical skills, to convert data into customer insights"* — i.e. **a directions 1+2 hybrid** |
| **Tuition, non-EU** | **€850/semester = €1,700/year** (1st sem €1,100 less the €250 deposit). **€250 registration fee, non-refundable** |
| **Entry wording** | *"Bachelor diploma with minimum **30 ECTS credits in business-related courses** and proof of proficiency in English"* |
| **146 ECTS verdict** | **LIKELY OK** — a 30-ECTS subject threshold, no 180 total, identical architecture to Kufstein |
| Language requirement | *"Unless your previous degree programme was taught entirely in English or English is your native language, you have to submit an adequate language certificate (e.g. TOEFL iBT, IELTS Academic, CAE etc.) prior to your Skype interview."* → **a certificate IS required; no MOI concession for a French-taught degree** |
| Deadline | **31 March 2026** for visa-requiring applicants (2027 indicative) |
| URL | https://www.fhwn.ac.at/en/studyprogramme/master-business-consultancy-international |

**Verdict: the strongest Tier-A alternative to Kufstein on entry rules, at 2.3×
the tuition, and it needs a real IELTS.**

#### CAMPUS 02 Graz — MA Digital Marketing Management

**MA in Business, 120 ECTS, 4 semesters, €363.36/sem = €726.72/year.**
Entry: *"Completion of a relevant Bachelor's degree programme **or an equivalent
degree**"* + *"Proof of at least **30 ECTS** from economic subject areas"* —
**146 ECTS verdict: LIKELY OK.** Perfect direction-2 match on paper.
**Two blockers:** teaching is *"German, partly English"* with **German B2
required — Tier B/C**; and the format is *extra-occupational* (part-time,
employment not required), which weakens the residence-permit case.
https://www.campus02.at/marketing/en/digital-marketing-management/

#### FH Oberösterreich Steyr — MA Global Sales and Marketing

**English (Tier A), public UAS.** Entry: *"A completed Bachelor's or Master's
degree with a background in business administration"*; admission by **case
study + English test + interview**; a prerequisites sheet asks for **10 ECTS in
"English"** coursework. **146 ECTS verdict: LIKELY OK on credits** — no 180
figure. **But three real frictions:** tuition is the **doubled €726.72/semester
= €1,453/year**; **IELTS 6.5 / TOEFL 87 is obligatory for non-EU with no MOI
alternative**; and non-EU applicants must go through **uni-assist for a VPD**,
adding cost and 4–8 weeks. Visa-applicant deadline **31 May** (2026 cycle).
https://fh-ooe.at/en/degree-programs/global-sales-and-marketing-master

#### FH JOANNEUM Graz — MA Content Strategy (Content-Strategie und digitale Kommunikation)

English-taught; **third-country contribution €727/semester (€1,454/year), and
the first two semesters — €1,454 — must be paid in advance before the place is
confirmed.** Entry: *"documentary evidence that you have completed a relevant
Bachelor's degree **or equivalent qualification**"* — **no ECTS count →
146 ECTS verdict LIKELY OK.** English **B2**, and the accepted-proof list is
notably generous on the numbers (**IELTS only 5.0**, TOEFL 87, telc B2, FCE, PTE
59) — **but an MOI letter is not listed.** Direction-2 adjacent (content
strategy / digital communication rather than marketing proper).
https://www.fh-joanneum.at/content-strategie-und-digitale-kommunikation/master/en/admissions/application/

#### IMC Krems — MA Marketing — **EXCLUDED**

English, 120 ECTS, 4 semesters, Marketing — on paper an ideal match, and it is
the clearest counter-example to a blanket reading of §4(4) FHG:

- **Entry: *"a completed bachelor degree with minimum 180 ECTS lasting at least
  six semesters in a related subject"*** → **146 ECTS verdict: BORDERLINE,
  the artefact bites directly**; needs the FSEG attestation.
- **English: IELTS Academic 7.0 / TOEFL 94 / Cambridge C1 / Duolingo 130** —
  among the highest in the Austrian FH sector, and **the only exemption is
  70+ ECTS previously taught in English**, not an MOI letter.
- **Tuition: €6,900/semester = €13,800/year** + €300 registration → band 3 of the
  affordability ladder with no scholarship identified.

**Excluded on cost + language + credits together.** Non-EU deadline 15 April.

#### MCI Innsbruck — MA International Business & Management (Marketing / Digital Business specialisations) — **EXCLUDED**

**€8,250/semester = €16,500/year for non-EU.** Breaches the brief's €15,000
hard filter. MCI's partial scholarships *"may cover up to 50% and more"* — even
at 50% it is €8,250/year, i.e. band 3 at best. Not shortlisted.

#### FHWien der WKW — MA Marketing & Sales Management

120 ECTS, 4 semesters, **part-time, partly English but predominantly German**.
**Entry wording is excellent:** *"Admissions will only be accepted from
graduates, this means people with recognized academic Bachelor's degrees and
equivalent or higher degrees"*, with business/law degrees explicitly listed and
non-business degrees admitted *"as long as a good knowledge and understanding of
business administration and communication can be proved"* via **interview,
suitability tests, assessment center**. **No ECTS count anywhere →
146 ECTS verdict: LIKELY OK.** Third-country application deadline **9 March**.
**Tuition for third-country nationals `NOT VERIFIED` — the fees page 404'd;
the programme is described only as charging "Gesetzliche Studiengebühren"
(statutory fees), which implies €363.36/sem, but confirm.** Language
requirements not published on the requirements page — **email
servicepoint@fh-wien.ac.at**. Part-time format is a residence-permit risk.

#### FH Kärnten — MA Digital Transformation Management

**MA in Business, 120 ECTS, 4 semesters**, five curricular areas: digitisation &
management, **e-business, digital marketing, data science**, technology — a
genuine **directions 1+2 hybrid**. **Third-country tuition €500/semester
(€1,000/year) from WS 2026** — the second-cheapest verified. Entry: *"completion
of a bachelor of arts/science degree that corresponds to the respective master
degree program"* → **no ECTS count, LIKELY OK.** **Blockers: German min. B2
(Tier B/C), and a work-friendly part-time format — six on-campus weekends per
semester plus Tuesday/Thursday evening online — which almost certainly will not
support a study residence permit.** Deadlines run in four windows,
01.11.–30.09. https://www.fh-kaernten.at/en/studium/wirtschaft-management/master/digital-transformation-management

#### FH Burgenland — MA Internationale Wirtschaftsbeziehungen (International Marketing track)

120 ECTS, 4 semesters, **German-taught, part-time on 14 weekends per semester
with a high online share**. Entry is the loosest found: *"ideally… a
business-oriented bachelor's degree or **at least 14 ECTS in business studies and
6 ECTS in legal studies**"* — **146 ECTS verdict: LIKELY OK.** But
German + weekend part-time = **Tier C + visa risk**. Recorded, not recommended.

#### FH des BFI Wien — noted, no direction match

**Tuition €363.36/semester, explicitly *"the same as for EU/EEA citizens"***;
€200 deposit, credited. **English-taught masters require CEFR C1.** Its eight
masters cover business management, banking & finance, logistics, project
management, digital HR management and risk management — **no marketing, no
music.** A cheap institution with nothing he wants. Recorded so the gap is
visible.

#### FH Technikum Wien / FH Campus Wien / Lauder Business School

- **FH Technikum Wien**: **€3,000/semester (€6,000/year) for third-country
  nationals** — seven exemption categories exist, none of which he meets. Its
  *Data Science* master is being phased out (*auslaufender Studiengang*) and
  replaced by *Artificial Intelligence & Data Science*, offered part-time.
  Cost-excluded relative to Kufstein.
- **FH Campus Wien**: health/social/technology-dominated; **no marketing or
  music master identified.** Not exhaustively verified.
- **Lauder Business School**: accredited private UAS, Vienna, English-taught
  business/management/banking masters. **No marketing or music master
  identified; fees not verified.** `NOT VERIFIED.`

---

### DIRECTION 1 — AI / data applied to marketing

#### FH Kufstein Tirol — MA Data Science & Intelligent Analytics — **3G's open question is now answered**

Agent 3G flagged this as `NOT ASSESSED` pending the prerequisite threshold. **It
is: prior knowledge of mathematics and statistics (8 ECTS) and computer science
(6 ECTS).** Crucially, **FH Kufstein publishes a remedy**: applicants who lack
this *"can make up for it with our free video-based preparatory course."*

**146 ECTS verdict: LIKELY OK, with a caveat.** The credit total is not tested;
the 8+6 ECTS quantitative floor is, and a marketing licence may or may not carry
it — **but the free preparatory course is an explicit, published, zero-cost
bridge.** Same €726.72/year, same MOI-letter concession, same 3 March deadline.
**This is now a live second Kufstein application, not a dead end** — and for a
student whose single strongest asset is a self-built CRM platform, the technical
framing is defensible. https://www.fh-kufstein.ac.at/en/master/data-science-intelligent-analytics-ft

#### FH JOANNEUM — MA Data and Information Science; MA Big Data and Business Intelligence

Both exist and both sit at the **€727/semester third-country rate**. Programme
detail (ECTS, language share, exact entry wording) **NOT VERIFIED** — flagged
for follow-up. https://www.fh-joanneum.at/big-data-and-business-intelligence/master/en/admission/application-requirements/

#### JKU Linz — MSc Economic and Business Analytics; MA Digital Business Management (joint degree)

Public university → **€726.72/semester = €1,453/year**, and the *Universitäts-*
*gesetz* regime applies (see §5). Both are plausible direction-1 matches;
**entry wording and ECTS requirement NOT VERIFIED — coverage gap.**
https://www.jku.at/en/degree-programs/types-of-degree-programs/masters-degree-programs/ma-economic-and-business-analytics/

---

### DIRECTION 3 — Music marketing & artist promotion

## **NOTHING. ZERO PROGRAMMES IN AUSTRIA.**

This is a genuine, searched-for empty result, not an omission. Searched in
German across the FH sector and the university sector: `Musikmarketing`,
`Artist Development`, `Musikwirtschaft`, `Music Marketing`, `Audience
Development`. **No Austrian institution — Fachhochschule, public university,
private university or Kunstuniversität — offers a master's in music marketing,
artist promotion or audience development.** Combined with Agent 3G's identical
finding across ten other applied-sector systems, **direction 3 should now be
treated as structurally unavailable in continental Europe outside specialist
private schools.** Somebody should say this to the student plainly.

---

### DIRECTION 4 — Music business / music industry management

#### Danube University Krems (Universität für Weiterbildung Krems) — MA (CE) Music Business and Culture — **BLOCKED, three ways**

The only true music-business master in Austria. It is an exact direction-4
match — *music organisations, music entrepreneurship, music economics, IP law,
cultural management, digital transformation in the music industry* — and it is
**English-taught**. **Do not shortlist it.**

| Blocker | Evidence |
|---|---|
| **1. Explicit 180 ECTS** | *"Subject-related degree at least at Bachelor's level (**180 ECTS points**)"* — the transcript artefact bites directly. **146 ECTS verdict: BORDERLINE**, needs the FSEG attestation before it is even worth asking. |
| **2. Two years' professional experience** | *"**Two years of qualified professional experience**"* — a marketing internship is not two years. Same structural bar that closed Finland's UAS sector. **He does not meet this.** |
| **3. Format defeats the whole purpose** | *"Blended Learning"*, 5 semesters part-time, **two weeks per semester of on-site attendance**. **A low-residency degree grants no student residence permit and therefore no 12-month job-search permit and no Red-White-Red Card route.** The entire post-study-work case — Austria's single best feature — evaporates. |
| **4. Cost** | **€12,000 total.** IFPI Austria offers a partial scholarship. Even funded, blockers 1–3 stand. |

Next intake 5 October 2026; MA (CE) = *Master of Arts (Continuing Education)*,
120 ECTS, 5 semesters. https://www.donau-uni.ac.at/en/studies/ma-music-business-and-culture.html

#### University of Klagenfurt (AAU) — MSc Media and Convergence Management — **Agent 3F's "highest-value item to re-check": FOUND, and it is real**

Agent 3F could not locate this at any aau.at URL. **It exists and is live.**

| Field | Detail |
|---|---|
| Institution / type | Universität Klagenfurt — **public university** (UG regime) |
| Degree / ECTS | **Master of Science (MSc), 120 ECTS**, 4 semesters |
| Direction match | **Directions 3/4 adjacent + direction 2** — media and convergence *management*: the closest thing Austria has to a creative-industries management master. Not music, but the media-industry sector bridge |
| Language | **English — Tier A on teaching** |
| Tuition, non-EU | Public university → **€726.72/semester = €1,453/year** + ÖH. (The programme page's *"a degree programme at an Austrian state university is free"* refers to EU/EEA students — do not be misled) |
| **Entry wording** | *"a background in humanities, social or economic sciences or technical sciences"*; relevant bachelors listed include *Applied Business Administration*, *Media and Communications*, *Information Management*. **No 180 ECTS figure stated anywhere on the programme page.** Special admission procedure; selection assesses *"academic performance, motivation, relevant experience, and language skills"*, usually with an interview |
| **146 ECTS verdict** | **BORDERLINE — favourable wording, unfavourable statute.** The programme states no credit count and a Licence in Marketing sits squarely in "economic sciences". **But this is a *university*, not an FH: the flexible §4(4) FHG clause does not apply, and UG §64(3) admission conditions are set per curriculum.** Must be confirmed with the Studienabteilung. |
| **Language requirement — the real blocker** | **English C1**, proven at the time of application, per the Rectorate's language regulation. **C1 with no test taken and no MOI concession is a materially harder bar than Kufstein's B2-with-MOI-letter.** |
| Deadline | **Non-EU/EEA: 12.01.2026 – 28.02.2026** (2027 dates unpublished; expect the same window) |
| URL | https://www.aau.at/en/studien/master-media-and-convergence-management/ |

**Verdict: a genuine find and the best direction-3/4-adjacent option in Austria —
but gated on C1 English and a UG-sector credit question.** Rank it below
Kufstein, above everything else in directions 3/4.

#### FH Kufstein — MA Sports, Culture & Event Management

Stands as Agent 3G recorded it: €726.72/year, English, §4(4) + ≥30 ECTS, MOI
letter accepted, **LIKELY OK**. Honest framing unchanged — it is an events and
culture management degree in which music festivals are one application area,
not a music-business degree.

---

## 5. Austrian PUBLIC UNIVERSITIES — do they impose 180 ECTS? (task 2)

**Yes, characteristically — and the two data points are decisive.**

The *Universitätsgesetz* governs universities, **not** the FH-Gesetz, so
§4(4) FHG's equivalence-plus-supplementary-exams clause **does not apply**.
UG §64(3) frames master's admission around a completed relevant bachelor's, but
the operative `Zulassungsvoraussetzungen` are set **per curriculum**, and the
big business faculty prints the number:

> **WU Wien (Wirtschaftsuniversität Wien), MSc Marketing:** *"The bachelor's
> degree must comprise at least **180 ECTS credits** (corresponding to three
> academic years), with **45 ECTS credits earned by passing exams in the field
> of business administration**."*
> — wu.ac.at/en/programs/masters-programs/marketing/application-admission

**146 ECTS verdict at WU: BORDERLINE → effectively BLOCKING without the FSEG
attestation.** WU is also the most selective business school in Austria and runs
a 90-place cohort with three deadline rounds (8 Oct / 8 Jan / 8 Mar) — at
12–13/20 he is **outside the realistic band** and should not spend the
application effort. WU's English concession is also narrow: *"a full
English-taught bachelor's program (at least 3 years)… requires a confirmation
from the university to prove that the completed program was taught in English"*
— which does nothing for a French-taught licence.

**Universität Wien** does not accept a Tunisian MOI letter either: its
English-proficiency rule accepts a school/university confirmation only where the
prior qualification comes from **an EU/EEA country, Switzerland, the UK, USA,
Australia, New Zealand or Canada**. Tunisia is excluded by construction.

**Universität Klagenfurt** is the exception on wording (no ECTS stated) but
imposes **C1 English** — see §4.4.

**Conclusion for task 2: the Austrian university sector is materially worse for
this student than the FH sector on all three axes at once** — it costs *double*
(€1,453 vs €727/year), it prints 180-ECTS thresholds where the FHs print 30, and
it does not accept the MOI letter. **The recommendation should point at
Fachhochschulen and specifically at FH Kufstein.** Uni Graz, Uni Innsbruck, Uni
Salzburg and MODUL were **not individually verified** — but given the above,
they are low-yield and I would not spend further budget there.

---

## 6. Austria post-study, verified (task 4)

Source: migration.gv.at/en/types-of-immigration/permanent-immigration/graduates/
(checked 2026-08-17) — **primary government source, re-verified this round.**

1. **Job-search permit.** Graduates *"may renew your residence permit 'Students'
   for a period of **twelve months** for the purpose of searching for
   employment, or starting a business."* Conditions: proof of self-support and
   health insurance. (The Austrian instrument is the extension of the
   *Aufenthaltsbewilligung Studierende*, not a separately named permit.)
2. **Red-White-Red Card for graduates — no labour-market test.** *"you can apply
   for a Red-White-Red Card **without a labour market test**."* Confirmed
   verbatim.
3. **No points system.** *"**For graduates, there is no points system.**"*
   Confirmed verbatim. **This is the single most valuable feature of the
   Austrian route for a 12–13/20 candidate** — a points system is precisely the
   filter that would exclude him.
4. **Salary condition — resolve this before relying on it.** migration.gv.at
   states only the qualitative test: *"the locally customary gross minimum
   salary which comparable Austrian graduates (junior employees) would
   receive"*, **and publishes no figure.** Secondary Austrian sources
   (workinaustria.com, oesterreich.gv.at) circulate **€3,465 gross/month for
   2026** as the RWR-Card minimum — **but I could not confirm that this figure
   is the *graduate* category rather than the general skilled-worker category,
   and the official page contradicts the existence of a fixed figure for
   graduates.** `PARTIALLY VERIFIED — treat €3,465/month as an upper-bound
   working assumption and confirm with the AMS or a Landeshauptmann's office
   before relying on it.` A junior digital-marketing salary in Vienna may sit
   below it; in Tyrol, below it more often.
5. **Onward path.** After 21 months' qualifying employment within 24 →
   **Red-White-Red Card plus**, unrestricted labour-market access.

---

## 7. GERMANY — brief, and the verdict is negative (task 5)

### 7.1 anabin: SOLVED (the JS database was rendered via its public API)

The anabin front end is an Angular SPA and does not render for automated
fetchers. **However, its public REST API is open and unauthenticated.** Endpoint
list recovered from `https://anabin.kmk.org/public/dist/institutions.js`;
working query form:

```
https://anabin.kmk.org/api/public/institution/?search=<name>&limit=20
https://anabin.kmk.org/api/public/degree/?search=<degree>&limit=50
```

**Result 1 — the institution:**

| Institution | anabin classification | Status |
|---|---|---|
| **Université de Sousse** (public) | *Staatliche Hochschulen* | **H+** |
| Université Privée de Sousse (the private namesake — **not his**) | *Private Hochschulen mit staatlicher Anerkennung* | H +/− (needs a ministerial *Certificat d'Equivalence*) |

**H+ is the top rating.** Do not let anyone confuse the two Sousse institutions —
the private one carries an extra documentary burden that his public university
does not.

**Result 2 — the degree.** anabin describes and rates both Tunisian licences:

| Tunisian qualification | anabin description | German equivalent | **Equivalence class** |
|---|---|---|---|
| **Diplôme National de Licence Fondamentale** (*Ash-shahada al-wataniyya li-l-idjaza al-asasiyya*) | *"der grundständige Abschluss nach einem **dreijährigen** Studium"* in the post-2007 Tunisian system | **Bachelor 3j** (3-year bachelor, class A3) | **"Entspricht"** — **EQUIVALENT** |
| **Diplôme National de Licence Appliquée** (*…al-idjaza at-tatbiqiyya*) | *"der grundständige Abschluss eines dreijährigen **anwendungsorientierten** Studiums"* | **Bachelor 3j** (A3) | **"Bedingt vergleichbar"** — conditionally comparable (9 of 11 sampled Tunisian *Appliquée* entries) |

**Three consequences, and they matter beyond Germany:**

1. **The credential is NOT Germany's blocker.** A *Licence Fondamentale* from a
   H+ institution is rated *equivalent* to a German 3-year bachelor, and anabin
   describes it in **years, not credits** — no 180-ECTS figure appears in the
   qualification entry at all.
2. **This INVERTS the Dutch finding.** Nuffic rates *Fondamentale* **below** a
   Dutch bachelor (2 years WO) and *Appliquée* fine (3 years HBO). **Germany
   rates them the opposite way round: Fondamentale = "Entspricht", Appliquée =
   "Bedingt vergleichbar".** Whoever writes the final report must not carry the
   Dutch branch logic into Germany — **resolving which licence he holds changes
   the answer in opposite directions in the two countries.**
3. It reinforces the case for asking FSEG which licence he holds. **That single
   question now affects at least two countries' verdicts.**

### 7.2 Blocked account (Sperrkonto) — current amount

**€11,904 for twelve months = €992 per month (2026).** Payout is capped at
1/12 per month. A job-seeker/Chancenkarte visa requires 10% more: €13,092.

`VERIFIED ONLY FROM SECONDARY SOURCES` — the official
make-it-in-germany.com financial-resources page returned a **Radware bot
challenge** and could not be read. The figure is consistent across
study.eu, mygermanuniversity.com and bankdaten.de. Confirm at
https://www.make-it-in-germany.com/en/study-training/study/requirements/proof-of-financial-resources
(Firecrawl candidate). Note this is ~€11,900 of *proven funds* on top of
everything else — and Austria's equivalent requirement is materially lower.

### 7.3 Any English-taught German master's that would take him?

**Searched. The honest answer is essentially no.**

| Programme | Why it fails |
|---|---|
| **THM (Technische Hochschule Mittelhessen) — MSc Digital and International Marketing** | The closest thing to a fit: **public FH, zero tuition, ~€350/semester contribution, English-taught first semester**. **Fails three ways at once:** (i) *"First university degree with **minimum 2.3 overall grade** and **210 ECTS** in business administration"*, with 180-ECTS holders required to *"complete 30 ECTS through practical experience or additional coursework"*; (ii) **German B1 required for international applicants**; (iii) at least 5 ECTS maths/statistics. **The 2.3 grade bar is exactly the "2.5/good" threshold Phase 1 predicted he would miss.** Non-EU window 1 April – 15 July, via uni-assist. |
| **CBS University of Applied Sciences (Cologne Business School) — MSc Digital Marketing** | **Private.** Genuinely no GPA restriction — *"CBS doesn't have GPA restrictions and instead looks forward to getting to know applicants… in a personal admissions interview"* — the one German door open on grades. **But private-school tuition puts it in the brief's band 3/exclusion zone; fee `NOT VERIFIED` this round.** If anyone wants a German option, this is the only one worth pricing. |
| **Popakademie Baden-Württemberg — MA Music and Creative Industries** | Remains blocked per Agent 3G: C1 German, six months' creative-sector experience, entrance exam. |

**GERMANY VERDICT: no viable public route.** The credential clears (anabin H+,
"Entspricht"); the **grade and the German language do not**. Where a German FH
drops the GPA bar it is private and expensive; where it is free it prints 210
ECTS and 2.3. Phase 1's deprioritisation stands, now with the recognition
question closed rather than assumed. **Do not spend application effort in
Germany.** One exception worth a single email: **CBS, on the strength of its
explicit no-GPA-threshold policy** — price it, then decide.

---

## 8. Recommended Austrian shortlist

| # | Programme | Direction | Language | Tuition (non-EU) | 146 ECTS | Why |
|---|---|---|---|---|---|---|
| **1** | **FH Kufstein — MA Digital Marketing (FT)** | 2 | English, Tier A | **€726.72/yr** | LIKELY OK | Cheapest + §4(4) equivalence + ≥30 ECTS only + **MOI letter instead of IELTS** + interview-based selection |
| **2** | **FH Kufstein — MA Data Science & Intelligent Analytics (FT)** | 1 | English, Tier A | **€726.72/yr** | LIKELY OK | Same architecture; the 8+6 ECTS quantitative gap has a **free published preparatory course**; his CRM build is the argument |
| **3** | **Uni Klagenfurt — MSc Media and Convergence Management** | 3/4-adjacent + 2 | English, Tier A | €1,453/yr | BORDERLINE | Best creative-industries option in Austria; gated on **C1 English** and a UG-sector credit question |
| 4 | FH Wiener Neustadt — MA Global Business Leadership (marketing spec.) | 1+2 | English, Tier A | €1,700/yr | LIKELY OK | 30-ECTS threshold, no 180; needs a real IELTS |
| 5 | FH Kufstein — MA Sports, Culture & Event Management | 4-adjacent | English, Tier A | €726.72/yr | LIKELY OK | Sector bridge only; not a music degree |
| — | FH Salzburg | — | German wall | €726.72/yr | LIKELY OK | **Best entry wording in the project** (*"at least 3 years duration"*) attached to German-taught business masters. Email them about English provision for 2027 |
| ✗ | IMC Krems, MCI Innsbruck, FH Technikum Wien | — | — | €6,000–16,500/yr | — | Cost-excluded |
| ✗ | Danube Krems MA Music Business and Culture | 4 | English | €12,000 total | BORDERLINE | 180 ECTS + 2 yrs experience + **low-residency = no visa, no post-study work** |

**Single highest-value action:** confirm with FSEG whether the licence is
*Fondamentale* or *Appliquée* — it now moves the answer in **Germany** (opposite
direction to the Netherlands) as well as in the Netherlands.

**Second highest:** email FH Kufstein admissions confirming the MOI letter would
be accepted from **Université de Sousse specifically**, in **French-medium**
context. The published wording says *"a certificate or an official letter (MOI)
from a university/school that clearly demonstrates the language competence at
CEFR level B2 or higher"* — his university taught in French, so the letter would
have to attest his **English** competence, not the medium of instruction.
**This is the one soft spot in the #1 recommendation and it must be tested
before it is relied on.**

---

## 9. Sources, all checked 2026-08-17

**Austria — tuition**
- https://www.fh-kufstein.ac.at/en/admissions/tuition-fees
- https://studieren.univie.ac.at/studienbeitrag/hoehe-studienbeitrag/ · https://oeh.univie.ac.at/seite/wie-hoch-ist-die-studiengebuehr
- https://www.imc.ac.at/en/study/application/study-fees/
- https://www.technikum-wien.at/studieninformationen/studienbeitrage-und-studienbeihilfen/
- https://www.fh-salzburg.ac.at/en/prospective-students/about-to-start-studying/fees-and-scholarships
- https://www.fh-vie.ac.at/en/pages/studies/international-students/additonal-regulations-for-internationa-students
- https://www.fh-kaernten.at/en/studium/wirtschaft-management/master/digital-transformation-management
- https://www.mci.edu/en/study/master/international-business-management

**Austria — programmes / admission**
- https://www.fh-kufstein.ac.at/en/master/digital-marketing-ft · /data-science-intelligent-analytics-ft · /sports-culture-event-management-ft
- https://www.fh-salzburg.ac.at/en/prospective-students/about-to-start-studying/admission-requirements-for-master-programmes *(the "at least 3 years duration" wording)*
- https://www.fhwn.ac.at/en/studyprogramme/master-business-consultancy-international *(+ /faq)*
- https://www.campus02.at/marketing/en/digital-marketing-management/
- https://fh-ooe.at/en/degree-programs/global-sales-and-marketing-master *(+ /application-process)*
- https://www.fh-joanneum.at/content-strategie-und-digitale-kommunikation/master/en/admissions/application/ · /big-data-and-business-intelligence/master/en/admission/application-requirements/
- https://www.imc.ac.at/en/study/master/business/marketing/
- https://www.fh-wien.ac.at/en/study/application/requirements-master/marketing-sales-management/
- https://www.aau.at/en/studien/master-media-and-convergence-management/
- https://www.wu.ac.at/en/programs/masters-programs/marketing/application-admission
- https://www.donau-uni.ac.at/en/studies/ma-music-business-and-culture.html
- https://www.jku.at/en/degree-programs/types-of-degree-programs/masters-degree-programs/ma-economic-and-business-analytics/

**Austria — immigration**
- https://www.migration.gv.at/en/types-of-immigration/permanent-immigration/graduates/
- https://www.oesterreich.gv.at/de/themen/menschen_aus_anderen_staaten/aufenthalt/3/2/2/Seite.120229 *(RWR-Karte für Studienabsolventen; salary figure unconfirmed for the graduate category)*

**Germany**
- **anabin public API** (method note: SPA front end at https://anabin.kmk.org/db/institutionen is unrenderable; the API behind it is not):
  `https://anabin.kmk.org/api/public/institution/?search=Université%20de%20Sousse`
  `https://anabin.kmk.org/api/public/degree/?search=Licence%20Fondamentale`
  `https://anabin.kmk.org/api/public/degree/?search=Licence%20Appliquée`
- https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/10324/ *(THM MSc Digital and International Marketing)*
- https://www.uni-assist.de/en/tools/info-country-by-country/details-country/country/tn/ *(Tunisia document rules; silent on master's entry)*
- https://www.daad.tn/en/study-research-in-germany/eight-steps-to-germany/

**Blocked / failed this round (Firecrawl candidates):** `ustp.at` (403, FH St.
Pölten); `make-it-in-germany.com` (Radware challenge); `fhv.at` master pages
(404); `fh-wien.ac.at` tuition-fee page (404); `donau-uni.ac.at/de/…` (404,
English worked).
