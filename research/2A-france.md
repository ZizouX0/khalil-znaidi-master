# 2A — FRANCE

**Agent 2A · scope: France · all four directions · checked 2026-08-17**
**Target intake: AUTUMN 2027 = French academic year 2027/2028.**

---

## 1. Bottom line

France remains the strongest single country for this student — native French, a
huge programme pool, a real post-study work route (APS, 12 months, with
*more favourable* bilateral terms for Tunisians), and public master's programmes
that admit at M1 directly from a 3-year licence in gestion/économie. **But the
affordability premise in the brief is now out of date and this is the single most
important finding of this report.** Décret n° 2026-385 of 19 May 2026 caps how
many non-EU students a public university may exonerate: **30 % in 2026-2027,
25 % in 2027-2028 — the exact year he would enter — and 20 % thereafter.**
Baseline non-EU master's tuition for 2026/2027 is **€3,950/year + €105 CVEC**
(Campus France Tunisie's own figure), not the ~€250 standard rate. He should
plan for €3,950 and treat exoneration as a bonus, not a default. Even so, at
~€4,050/year France sits comfortably inside filter band 2–3 and beats almost
every alternative. **The binding constraint is timing, not money:** the Études en
France campaign for autumn 2027 will open around **1 October 2026** — six weeks
from now — and close around **15 January 2027**, months before the French
domestic Mon Master window. Structurally, the biggest trap is that most
French *music* master's programmes admit only at **M2 (Bac+4)**; the routes that
work for him are the ones with an **M1 entry from a licence économie-gestion**,
of which Lyon 2 is the standout.

---

## 2. Coverage statement — what I searched, and what I could not

**Languages:** French first (all primary queries), then English for the
international-facing schools.

**Databases and sources used:**
- `trouvermonmaster.gouv.fr` — **DEAD.** It now 301-redirects to
  `monmaster.gouv.fr`. Checked 2026-08-17.
- `monmaster.gouv.fr` — Angular SPA; its search API (`/api/public/formations`,
  `/api/formations`) returns **HTTP 401** to unauthenticated GET and POST.
  There is no longer a public, scriptable national master's catalogue.
  **This is a real coverage limitation and it is systematic, not incidental.**
  Note also that Mon Master is *not* his application route (see §5.3), so its
  loss costs discovery breadth, not procedure.
- `campusfrance.org` catalogue — the `/fr/catalogue-formations` search URL
  returns 404; not usable.
- `tunisie.campusfrance.org` — **used heavily and productively**, including its
  sitemap and the official procedure calendar PDF. This is the best France source
  for this student and is fully covered below.
- `service-public.gouv.fr`, `legifrance.gouv.fr` (via secondary confirmation),
  `enseignementsup-recherche.gouv.fr` (403 on direct fetch), and individual
  university / school pages for every figure quoted.
- ONISEP — **not reached** (see gaps).

**Tooling constraint that shaped this report:** the session's WebSearch budget
(200 calls) was exhausted part-way through. Alternative search engines
(DuckDuckGo HTML and Lite) return HTTP 202 challenge pages via curl; the
`firecrawl` CLI is installed but **no `FIRECRAWL_API_KEY` is set in this
environment**. From that point on I could only fetch URLs I already had or could
derive from sitemaps. Consequence: **directions 1 and 2 are under-sampled
relative to the true French pool.** There are ~30 IAE and dozens of public
universities offering a mention *Marketing-Vente* with a digital or data
parcours; I verified six and named a few more. The music directions (3 and 4)
are a small enough universe that I believe coverage there is close to complete
for the accessible tier.

**What I found NOTHING on — stated explicitly:**
- **No French *Mastère Spécialisé* (CGE label) relevant to any of the four
  directions was verified.** I did not find an MS in music business, music
  marketing, AI-marketing or growth marketing that I could confirm. Per the
  brief, none is included. The MS question is therefore *moot for France in this
  scope* rather than answered — flagged as a gap, not a null result.
- **No public French university programme dedicated to "music marketing" as
  such.** The nearest is Lyon 2's artist-career M2 and Paris 8's music-industry
  M2; both are industry-management programmes with marketing modules, not
  marketing degrees. Direction 3 in its pure form essentially does not exist in
  the French public sector.
- **No "growth marketing" master's in the public sector.** The term maps onto
  *marketing digital* / *e-marketing* parcours; there is no French public
  master's using the growth-marketing label. Private schools (IIM Digital School
  etc.) use it but I could not verify their accreditation or fees.
- **No confirmed cost-of-living figures from an official French source.**
  france-visas.gouv.fr returned 403 and the Campus France cost pages I reached
  did not carry monthly budget figures. See §5.6 — deliberately left unverified.
- **No 2027/2028 dates are published anywhere yet.** Every 2027 date in this
  report is projected from the verified 2026/2027 calendar and is labelled as
  such.

---

## 3. Programmes by direction

Language tier is **A for every programme below** — all are taught in French or
English, both of which he has. No Tier B or C programme arises in France. The
"language pathway" field is therefore not applicable anywhere in this report.

Unless stated otherwise, for public universities: **institution type = public
university**, **accreditation = diplôme national de master, state-issued, ECTS-
bearing, grants student visa and full APS rights**, **tuition for non-EU =
€3,950/yr + €105 CVEC for 2026/2027 unless exonerated**, **GMAT/GRE = not used**,
**application route = Études en France (deadline ~15 Jan 2027, projected)**.

---

### DIRECTION 1 — AI applied to marketing

#### 1.1 Master Marketing, IA et Data Science (MIADS) — IAE Lille · **PRIORITY FIND (hybrid)**
- **University / city:** IAE Lille, Université de Lille · Lille
- **Degree:** Diplôme national de master, mention *Marketing, IA et Data Science* · 120 ECTS (M1+M2), 2 years
- **Type:** IAE (public university business school)
- **Direction match:** Direction 1, squarely. Genuine AI + marketing hybrid.
- **Language:** French, "some courses taught in English" — **Tier A**
- **Entry requirement, exact wording:** *"BUT science des données, L3 marketing, L3 économie-gestion, L3 mathématique…"* — **L3 marketing is named explicitly.** M2 entry requires *"M1 marketing with professional experience in data science."*
- **146 ECTS verdict:** `LIKELY OK` — the wording is by *licence type*, not by credit count. No 180-ECTS numeral appears. This is the single most favourable entry wording I found in France.
- **Tuition:** not published on the programme page — `NOT VERIFIED — check directly`; default public rates apply (€3,950 non-EU / €254 if exonerated). URL where it should appear: iaelille.fr fees page.
- **Duration / internship:** M1 = 2 days' class + 3 days in company; M2 = 1 week class / 2 weeks company. Formation initiale option carries a 4–6 month internship.
- **Deadlines (2026/2027 cycle, verified — 2027 not yet published):** M1 follows the Mon Master calendar; M2 session 1 opened 06/03/2026, closed 16/03/2026, results 06/05/2026; session 2 27/04–11/05/2026, results 27/06/2026.
- **⚠ Major caveat:** capacity is **14 apprenticeship places + 4 formation-initiale places.** The programme is alternance-dominant, and securing a French apprenticeship contract from Tunisia before a visa is issued is close to impossible in practice. **Realistically he is competing for ~4 seats.** Treat as a stretch despite the perfect entry wording.
- **URL:** https://iaelille.fr/nos-formations/master-miads/ · checked 2026-08-17

#### 1.2 Master Marketing et Data Analytics — Montpellier Management (MOMA)
- **University / city:** Montpellier Management, Université de Montpellier · Montpellier
- **Degree:** Diplôme national de master · 60 ECTS/year, 120 total · 2 years
- **Type:** public university management school
- **Direction match:** Direction 1 (M2 includes *"Introduction au Big Data et au traitement par IA"*, SQL/Python, text mining, digital analytics)
- **Language:** French; **B2 minimum recommended for non-francophones** — Tier A, and as a native speaker he clears it
- **Entry requirement, exact wording (M1):** *"un BAC+3 en gestion, management, économie…"* — but the page glosses this as **"Bachelor's or equivalent with 180 ECTS."**
- **146 ECTS verdict:** `BORDERLINE` — the 180-ECTS numeral is stated. Per the shared brief this is exactly the case where the free FSEG attestation (6 semesters / 3 years / 180 credits / access to Mastère in Tunisia) plus the supplément au diplôme normally settles it. **Email admissions before applying.**
- **Structure:** M1 is **formation initiale only** — no apprenticeship requirement, which makes it far more visa-realistic than IAE Lille. M2 offers FI or alternance.
- **Internship:** M1 min. 308 h (March–August); M2 min. 616 h (February–August)
- **Deadlines (2026/2027, verified):** M1 17 Feb – 16 March 2026 via Mon Master; M2 3–29 April 2026 via eCandidat. **For him the Études en France deadline (~15 Jan 2027 projected) governs and falls earlier.**
- **Outcomes:** 78.6 % employment within 6 months; M1 pass rate 89.47 %
- **URL:** https://www.montpellier-management.fr/formation/master-1-2-marketing-et-data-analytics/ · checked 2026-08-17

#### 1.3 Master Marketing, vente — parcours Marketing et data science — Université de Lille
- Exists and is taught by researchers in quantitative and data-driven marketing plus practitioners from data science / big data consulting / marketing analytics.
- **`NOT VERIFIED — check directly`.** The catalogue URL (univ-lille.fr/formations/fr-00002898) resolved to a generic catalogue shell, and I had no search budget left to locate the replacement page. ECTS, entry wording, deadlines and fees all unconfirmed.
- **Where it should appear:** https://formation.univ-lille.fr/ (search "marketing data science")

#### 1.4 MSc Artificial Intelligence for Marketing Strategy (AIMS) — EPITA × EM Normandie · **STRETCH**
- **City:** Paris (EPITA campus), with an academic stay in Dublin
- **Degree:** MSc, **labellisé CGE**. RNCP level not stated on the page — `ACCREDITATION PARTIALLY UNCLEAR`. CGE-labelled MSc *is* on the list of qualifications giving APS access, so post-study rights should hold; confirm the RNCP entry before applying.
- **Type:** private grande école (engineering school + business school partnership)
- **Language:** *"entièrement en anglais"* — **Tier A**, but see the test requirement
- **Duration:** 24 months · 6-month internship
- **Entry requirement:** Bac+3 or Bac+4 **"in IT or related field"** — he is a marketing graduate with a self-built CRM platform. The CRM project is genuinely relevant but the stated profile is IT. `BORDERLINE on discipline.`
- **English test:** TOEFL ≥ 80 iBT / TOEIC ≥ 800 / IELTS ≥ 6.0 — **he has taken no test.** This is a real, dated blocker: allow 2–3 months.
- **Tuition:** application fee €60; S1–S2 €6,050; S3 €7,400; S4 €6,000 → **≈ €19,510 total ≈ €9,755/year.** Band 3.
- **Deadlines:** two admission windows per year (September and March intakes); exact dates not published — `NOT VERIFIED`.
- **146 ECTS verdict:** `BORDERLINE` (private school, discretionary).
- **URL:** https://www.epita.fr/nos-formations/master-of-science/master-intelligence-artificielle-strategie-marketing/ · checked 2026-08-17

---

### DIRECTION 2 — Digital marketing & growth marketing

#### 2.1 Master 1 e-Marketing — IAE Montpellier · **BEST DIRECTION-2 FIND**
- **University / city:** IAE Montpellier (École universitaire de management), Université de Montpellier · Montpellier
- **Degree:** Diplôme national de master, M1 e-Marketing · **60 ECTS** (30/semester), 1 year, continuing into M2
- **Type:** IAE (public)
- **Direction match:** Direction 2, with a data-analytics component
- **Language:** French with an English module — **Tier A**
- **Entry requirement, exact wording:** *"Bac+3 validé (180 ECTS) en gestion, économie, ingénierie, informatique ou disciplines connexes"*, plus interest in digital marketing and data analysis; experience in business or digital-marketing projects recommended.
- **146 ECTS verdict:** `BORDERLINE` — "(180 ECTS)" is explicit. Same remedy as 1.2: FSEG attestation + supplément au diplôme, emailed to admissions in advance.
- **Why it stands out:** the programme page **explicitly routes non-EU students through Études en France** — *"For International Students (non-EU): Apply via Études en France platform."* Very few programme pages say this. It means the pathway is established, not improvised.
- **Selection:** dossier (grades, CV, motivation letter, professional project) **followed by an oral interview.** His CRM project and Renault Kélibia internship are exactly what an interview rewards; a 12–13/20 dossier is survivable here in a way it is not at a school selecting purely on grades.
- **Internship:** mandatory 10-week internship in S2 (10 ECTS)
- **Deadlines (2026/2027 session 1, verified):** 17 Feb – 16 March 2026. **Études en France deadline governs for him (~15 Jan 2027 projected).**
- **Tuition:** `NOT VERIFIED` on the programme page; default public rates apply.
- **URL:** https://iae.umontpellier.fr/formation/master-1-e-marketing/ · checked 2026-08-17

#### 2.2 Master Marketing Stratégique et Digital — IAE Tours
- **City:** Tours · mention **Marketing-Vente** · RNCP 42353 · 780 h · M1 + M2 (2 years)
- **Type:** IAE (public) · **Language:** French — Tier A
- **Entry requirement, exact wording:** *"une licence en management/gestion"* **and a Score IAE-Message.**
- **146 ECTS verdict:** `LIKELY OK` on wording — requirement is by licence type, no credit numeral. **But the Score IAE-Message is a hard gate — see §5.4.**
- **Tuition:** **€254** stated (standard national rate; covered by the CFA des universités under an apprenticeship contract) + **CVEC €103**. Note this is the *standard* figure — as a non-EU first-time enroller he faces €3,950 unless exonerated.
- **Formats:** formation initiale, apprentissage, formation continue — all three
- **Deadlines (2026/2027, verified):** M1 17 Feb – 16 March 2026 via Mon Master; M2 dates TBC via eCandidat. Next intake September 2026.
- **Outcomes:** 94 % completion, 90 % employed at 6 months, 100 % at 30 months
- **International candidates:** not addressed on the page — `check directly`
- **URL:** https://iaetours.fr/master-marketing-strategique-et-digital · checked 2026-08-17

#### 2.3 Master Marketing, vente — parcours Marketing digital — IAE La Rochelle · **NOT RECOMMENDED**
- **City:** La Rochelle · Bac+5 · 2 years · French — Tier A
- **Entry (M1):** Bac+3 in management or economics (or equivalent); selection on record, motivation and professional experience; *"digital aptitude is expected"*; **Score IAE-Message required, less than 3 years old.**
- **146 ECTS verdict:** `LIKELY OK` on wording.
- **⚠ Decisive figure:** **19.3 applications per place (2025).** With a 12–13/20 record this is not a realistic target. Listed for completeness and because the content (SEO/SEA, UX, social, influence, AI as a performance lever) is an excellent direction-2 match.
- **Tuition:** M1 = university registration + CVEC; M2 alternance = tuition covered.
- **URL:** https://iae.univ-larochelle.fr/formations/master-marketing-vente-parcours-marketing-digital/ · checked 2026-08-17

#### 2.4 Found but NOT individually verified — real programmes, fields unconfirmed
`NOT VERIFIED — check directly` applies to all of the following. Each was
surfaced in French-language search and is genuine, but I ran out of search budget
before I could open and confirm entry wording, fees and deadlines:
- **Master Marketing Digital — IAE Paris-Est** (Créteil). Page fetch returned empty content. https://www.iae-paris-est.fr/formations/master-marketing-digital/
- **Master Marketing Direct et Digital — IAE Lille.** https://iaelille.fr/nos-formations/master-marketing-digital/
- **Master 1 & 2 Marketing Digital — IAE Lille** (distinct from MIADS)
- The wider IAE network (~30 institutes) offers a mention *Marketing-Vente* with digital parcours at Nantes, Grenoble, Toulouse, Aix-Marseille, Bordeaux, Lyon 3, Nancy and elsewhere. **This is the largest unexplored seam in this report** and the obvious place for a follow-up pass.

---

### DIRECTION 3 — Music marketing & artist promotion

**Honest framing: pure "music marketing" master's programmes do not exist in the
French public sector.** What exists is artist-career management and music-
industry management with marketing modules inside. Three options, one of them
excellent.

#### 3.1 M1 Management de l'innovation → M2 Management Carrières d'Artistes / Écosystème de la Musique — Université Lumière Lyon 2 · **★ BEST FIND IN THIS REPORT**
- **University / city:** Université Lumière Lyon 2, campus Berges du Rhône · Lyon
- **Degree:** Diplôme national de master · **60 ECTS per year, 120 total** · 2 years (M1 + M2)
- **Type:** public university
- **Direction match:** **Direction 3 + Direction 4 hybrid, with a management/innovation spine — PRIORITY FIND.** The M2 is explicitly about developing professional and entrepreneurial competencies in managing and supporting artist careers.
- **Language:** French — **Tier A**
- **Entry requirement (M1), exact wording:** *"Le M1 est accessible à des étudiants des L3 économie et/ou gestion, AES, IEP et L3 en sciences sociales."* Requires *"des bases solides en économie et en gestion"* and demonstrated interest in innovation.
- **146 ECTS verdict:** **`LIKELY OK` — the strongest verdict in this report.** The requirement is stated by licence family ("L3 économie et/ou gestion"), with **no ECTS numeral anywhere.** His Licence in Marketing from FSEG Sousse (Faculté des Sciences Économiques et de Gestion) is precisely this profile.
- **Why this is the answer to the structural problem:** almost every French music master's admits only at M2/Bac+4 (Paris 8, Saint-Étienne, EMIC all do). **Lyon 2 lets him enter at M1 from his actual licence and progress internally to the music M2.** He does not need a Bac+4, an equivalency, or a bridging year.
- **M2 entry (for reference):** M1 or equivalent in economics, management, political science, law, communication or cultural management; *"bon niveau général"* and *"bonne maîtrise du français et de l'anglais à l'écrit comme à l'oral."* Prior experience in music or culture preferred. **His self-taught music production with no portfolio is a weakness here — he should build demonstrable sector involvement during M1** (associative work, festival volunteering, a label internship).
- **Internships:** M1 mandatory 2–5 months (309–770 h), must end before September. M2 mandatory 4–6 months, late January to August, international placements possible.
- **Application:** M1 via Mon Master for French/EU. **The M2 page states explicitly that non-European students in countries with a Campus France office must use that procedure** — i.e. Études en France for him.
- **Tuition:** the M2 page still shows 2021/2022 rates (€243 + €92 CVEC) — stale. `Assume €3,950 + €105 CVEC for non-EU unless exonerated.`
- **Deadlines:** `2027 NOT PUBLISHED.` Mon Master 2026 window was 17 Feb – 16 March 2026; **his Études en France deadline (~15 Jan 2027 projected) is earlier.**
- **URLs:** M1 https://www.univ-lyon2.fr/master-1-management-de-linnovation · M2 https://www.univ-lyon2.fr/master-2-management-de-linnovation-management-carrieres-dartistes-ecosysteme-de-la-musique · both checked 2026-08-17

#### 3.2 MBA Management & Ingénierie « Industrie de la Musique » — ICART · **ACCREDITATION OK, COST UNVERIFIED**
- **City:** Paris · **Type:** private school (Groupe EDH)
- **Title awarded:** **Titre RNCP niveau 7 « Manager de l'Ingénierie Culturelle », RNCP 40674**, valid 5 years from 23 May 2025. **This is a state-registered level-7 professional title, not a diplôme national de master.** ECTS: the page cites 300 (cumulative Bac+5). `ACCREDITATION: registered, but confirm APS eligibility — a non-CGE RNCP-7 title is not automatically on the list of qualifications granting the APS.` See §5.5.
- **Language:** French — Tier A
- **Entry:** Year 1 **Bac+3 minimum (180 ECTS)**; Year 2 Bac+4 (240 ECTS). → `BORDERLINE` on 146 ECTS.
- **Duration / internship:** 2 years, **11–12 months of mandatory internship total** (5–6 months Y1, 6 months Y2) — strong for employability, and internships are compatible with a student visa.
- **Application:** online dossier, **€110 application fee** (50 % reduction for scholarship holders), dossier review then motivation interview. Next intake October 2026.
- **Tuition:** **`NOT VERIFIED — check directly`.** Not disclosed on the programme page. This is decisive and must be obtained before shortlisting. Where it should appear: icart.fr admissions/tarifs page.
- **International students:** admitted; double diploma with New York Institute of Technology and a Miami "Creativity Program" offered.
- **URL:** https://www.icart.fr/formations-mediation-culturelle/mba-mediation-culturelle/industrie-de-la-musique · checked 2026-08-17

#### 3.3 Mastère Management de la Production Musicale et Développement d'Artistes — ESG Nantes
- **City:** Nantes · **Type:** private school (ESG, title issued by ECAD Consultants / IESA arts&culture)
- **Title awarded:** **« Administrateur de projets artistiques et culturels », RNCP 39360, niveau 7**, effective 19/07/2024. Same accreditation caveat as 3.2.
- **Duration:** 2 years (469 h + 448 h) · **Language:** French — Tier A
- **Entry:** **Bac+3 (180 ECTS minimum, any discipline)** — the most open entry wording of any music programme found. `BORDERLINE` on the 180 numeral, but "any discipline" removes the subject barrier entirely.
- **Direction match:** Direction 3 in its purest available French form — *développement d'artistes* is literally artist development.
- **Tuition:** **`NOT VERIFIED — check directly`.** Not on the programme page. **Under alternance the page states *"aucun frais de scolarité n'est à la charge de l'alternant"* — zero tuition.** ⚠ But an apprenticeship contract must be signed by a French employer, which a Tunisian applicant cannot realistically secure before a visa is granted. **Treat the free-alternance route as unavailable and budget for the formation-initiale price, which is unpublished.**
- **Intakes:** October 2026, with a February 2027 alternative entry.
- **URL:** https://www.esg.fr/ecole-nantes/mastere/management-prod-musicale · checked 2026-08-17

---

### DIRECTION 4 — Music business / music industry management

#### 4.1 MSc International Music Business — Rennes School of Business · **★ PRIORITY FIND (hybrid, English)**
- **City:** Rennes · **Type:** private consular grande école · **AACSB / EQUIS / AMBA triple-accredited**, CGE member
- **Degree:** *Master of Science in International Music Business + Advanced Degree in Management of the Cultural, Creative and Luxury Industries* · **RNCP niveau 7, titre n° 39274**, certified by the Ministry of Higher Education and Research, **valid through 31/08/2028**. **Note: this is RNCP level 7, NOT a *grade de master*** — one Rennes SB page loosely says "grade de master", which applies to the Programme Grande École, not to this MSc. `ACCREDITATION: solid; CGE-label + RNCP 7 should secure APS access, but confirm in writing.`
- **ECTS:** 60 per validated year · **Duration:** 1 or 2 years, full-time
- **Language:** **entirely in English — Tier A**, but he must produce a test score
- **Direction match:** **Direction 4 + Direction 2 hybrid — PRIORITY.** Global music-industry strategy, digital distribution, IP rights, marketing, business models.
- **Entry requirement, exact wording:** M1 entry — *"Bachelor's degree or equivalent (180 ECTS)"*. M2 direct entry — completed M1 (60 ECTS) **or** a bachelor's (180 ECTS) **plus minimum 3 years' professional experience.**
- **146 ECTS verdict:** `BORDERLINE` — 180 ECTS is explicit. **He should apply for the 2-year route (M1 entry)**; the 1-year route additionally demands 3 years' experience he does not have.
- **English requirement:** admission at TOEIC 785 / IELTS 6.0 / TOEFL 80 / Cambridge B2, **or completion of the last two years of education in English** (he did not). **For graduation:** TOEIC > 800 / TOEFL > 80 / IELTS > 6.5. **He has taken no test — budget 2–3 months.** This is his main obstacle here, not his GPA.
- **GMAT/GRE:** **not required** — significant, given the brief's ~600 GMAT exclusion.
- **Selection:** CV and transcripts in English; eligible candidates invited to an **online interview with pre-recorded questions.** Not grade-only.
- **Internship:** mandatory — minimum 2 months (M1), 4 months (M2), France or abroad
- **Tuition:** **MSc M1 + M2, full-time or alternance: €28,900 total ≈ €14,450/year.** (A widely circulated €18,200 non-EU figure appears to refer to a different/older configuration — the €28,900 total is what the official fees page shows. `Confirm at application.`) **Band 3 — include only with scholarship.**
- **Scholarships (official fees page):** Talent Scholarship up to **€5,000**; Unframed Scholarship up to **€5,000**; Ambassador Scholarship **15 % reduction**; Bienvenue en France **€500**; Social and Solidarity Grants **€500–€2,000**; Eiffel (~€1,200/month). **No scholarship is designated for African or North African students.** Realistic net with a Talent scholarship: **≈ €23,900 total ≈ €11,950/year** — still band 3.
- **Deadline:** for the September 2026 intake international students had until **1 July 2026** (stale for us). `2027 NOT PUBLISHED.` Rolling admissions; apply early.
- **⚠ Note:** EMIC (Levallois-Perret) markets this same MSc as its international option — verify which campus actually delivers it before committing.
- **URLs:** https://www.rennes-sb.com/programmes/master-of-science/msc-international-music-business/ · https://www.rennes-sb.com/fees-and-scholarships/ · both checked 2026-08-17

#### 4.2 M2 Industrie de la musique : production, organisation, communication — Université Paris 8
- **City:** Saint-Denis (Paris) · **Type:** public university
- **Degree:** Diplôme national de master, **mention Industries culturelles**, parcours *Industrie de la musique*. **M2 only** — reached through the M1 *Industries culturelles et créatives* (55 places), which also feeds *Communication pour le cinéma et l'audiovisuel* and *Recherche-création et cultures numériques*.
- **Language:** French, with two courses in English (socio-economics of the CCI; cultural industries law) — Tier A
- **Entry requirement (M1 mention), exact wording:** *"Les licences permettant d'accéder à la Mention de Master Industries Culturelles (M1 et M2) sont : Arts, Arts du spectacle, Humanités, Information-communication, Lettres, Lettres et langues, Science politique, Sciences de l'Homme, anthropologie, ethnologie, Sciences sociales, Sociologie."* Also expects *"un intérêt prononcé pour le champ des médias et de la communication"* and *"une solide culture générale en Sciences humaines et sociales."*
- **146 ECTS verdict:** `BORDERLINE` on credits (no numeral stated), **but the real problem is the discipline list: économie-gestion / marketing is absent.** A Licence in Marketing is off-profile for this mention. French "licences conseillées" lists are indicative rather than legally exclusive, so an application is not barred — but he would be competing off-list for 55 places. **Realistic verdict: unlikely without a strong cultural-sector CV.**
- **M2 capacity:** 25 students; 50–75 % of the M2 cohort each year is in alternance
- **Internship:** mandatory 3–6 month professional insertion in S2 (waivable if done in M1)
- **Deadlines / tuition:** not on the programme page — `NOT VERIFIED`
- **URLs:** https://www.univ-paris8.fr/-Master-Industrie-de-la-musique-production-organisation-communication- · https://www.univ-paris8.fr/-Master-Industries-culturelles- · both checked 2026-08-17

#### 4.3 Master Industries Créatives & Management de Projets — Université Sorbonne Nouvelle Paris 3
- **City:** Paris · **Type:** public university · mention **Industries culturelles**
- **Duration:** 2 years (4 semesters) · **20 places per year per level**
- **Language:** French (some courses / guest speakers in English) — Tier A
- **Music content: yes** — *"Industrie et scènes musicales"* is a semester-8 course, alongside cinema, gaming, fashion and series.
- **Entry requirement, exact wording:** *"L3 en Sciences de l'Information et de la Communication"*; *"L3 en Sciences humaines et sociales (sociologie ; économie ; arts)"*; *"Diplômés de grandes écoles"*. Candidates must submit a research-project proposal, a professional-project statement, and demonstrate experience in cultural-project design.
- **146 ECTS verdict:** `BORDERLINE` — no credit numeral, and **"économie" is on the list**, so a FSEG marketing licence is arguably admissible. But 20 places plus a required research proposal plus demonstrated cultural-project experience makes this genuinely selective.
- **⚠ LANGUAGE TRAP:** the page requires **"niveau C2 prérequis en langue française"** for foreign students. He is a native French speaker, but **C2 is normally evidenced by a DALF C2** — the hardest French certificate there is. He must ask admissions in writing whether Tunisian French-medium higher education is accepted in lieu. **This is the one place in France where the language question could actually bite him.**
- **Deadlines (2026/2027, verified):** M1 via Mon Master 17 Feb – 16 March 2026; M2 via eCandidat 7 April – 12 May.
- **Internships:** M1 min. 150 h (Oct–Sept); M2 min. 200 h (from April)
- **URL:** https://www.sorbonne-nouvelle.fr/master-industries-creatives-management-de-projets-br-mention-industries-culturelles-535267.kjsp · checked 2026-08-17

#### 4.4 Mastère Management de la Musique — IESA arts&culture
- **City:** Paris (16 rue Claude Bernard, 75005) · **Type:** private school
- **Title awarded:** **Titre niveau 7 enregistré au RNCP, « Administrateur de projets artistiques et culturels », RNCP 42330.** Not a diplôme national de master. `ACCREDITATION: registered; confirm APS eligibility.`
- **Duration:** 2 years, 720 h total · **Language:** French — Tier A
- **Entry, exact wording:** Year 1 — bachelor's (Bac+3) **or equivalent 180 ECTS** in culture, arts, project management, communication, marketing or events. **"Marketing" is explicitly named** — good discipline fit. Year 2 — Bac+4 / 240 ECTS.
- **146 ECTS verdict:** `BORDERLINE` — 180 ECTS stated explicitly.
- **Tuition (2026-2027, published):** **Year 1 €9,700 + Year 2 €9,850 + €150 pedagogical fees ≈ €19,700 total ≈ €9,850/year.** Band 3.
- **Application window:** November 2025 – September 2026 for the October 2026 intake (rolling). `2027 equivalent: expect Nov 2026 – Sept 2027.`
- **Alternance possible; professional experience mandatory for the award.** Same alternance/visa caveat as 3.3.
- **URL:** https://www.iesa.fr/formation/mastere-management-musique · checked 2026-08-17

#### 4.5 M2 Arts, parcours Musique : administration et gestion — Université Jean Monnet Saint-Étienne
- **City:** Saint-Étienne · public · mention **Arts** · **60 ECTS, M2 only (1 year)** · French — Tier A
- **Attractive feature:** **double degree with IAE Saint-Étienne (Master MAE — Management et administration des entreprises).** Music + a general management qualification in one year is a genuinely good combination for this profile.
- **Entry, exact wording:** *"En 1ère année de master: Les étudiants doivent être titulaires d'une licence française."* Foreign degree holders must go through equivalence procedures.
- **146 ECTS verdict:** `BLOCKING as a direct entry route.` **M2 only means Bac+4 required** — he has Bac+3. Additionally the wording demands a *licence française* with equivalence for foreign degrees, which points at the ENIC-NARIC statement (€120, 4–6 months per the shared brief).
- **Internship:** mandatory, minimum 3 months in S2
- **Verdict:** **not accessible for autumn 2027.** Viable only as a *later* target after an M1 elsewhere.
- **URL:** https://www.univ-st-etienne.fr/fr/formation/master-XB/master-XB/master-arts-parcours-musique-administration-et-gestion-5_02_07_0001_FR.html · checked 2026-08-17

#### 4.6 EMIC — École de Management des Industries Musicales et Audiovisuelles
- **City:** Levallois-Perret (Paris region) · private
- Bac+5 tracks: *Manager des Industries Musicales et du Spectacle Vivant* (option Musique / option Spectacle Vivant) and *Manager des Industries Audiovisuelles*.
- **Entry: Bac+4 (M1 level), 1 year.** → `BLOCKING for direct entry` on the same M2-only logic as 4.5.
- RNCP referenced but **level and code not stated** → `ACCREDITATION UNCLEAR — verify before applying`. Tuition not published → `NOT VERIFIED`.
- 99 % of third-year students are in apprenticeship (visa caveat again); 89 % employment at six months.
- Its international option is the Rennes SB MSc at 4.1.
- **URL:** https://emic-paris.com/ · checked 2026-08-17

---

## 4. Stretch options (excellent but failing exactly one filter)

| Programme | Filter failed | Note |
|---|---|---|
| **Rennes SB MSc International Music Business** (4.1) | Cost — €14,450/yr gross, ~€11,950/yr net with a €5,000 Talent scholarship | Band 3, not excluded. The best direction-4 content in France and the only English-taught one. Worth the money if a scholarship lands. |
| **EPITA × EM Normandie MSc AIMS** (1.4) | Cost (€9,755/yr) **and** discipline fit (IT-oriented entry) | Two soft failures. His CRM build is the argument that bridges the discipline gap. |
| **IESA Mastère Management de la Musique** (4.4) | Cost (€9,850/yr) | Marketing explicitly listed as an accepted licence — the best discipline fit among the private music schools. |
| **IAE Lille MIADS** (1.1) | Accessibility — ~4 non-apprenticeship places | Perfect entry wording, near-impossible capacity. Apply, but never as the only option. |
| **IAE La Rochelle Marketing digital** (2.3) | Accessibility — 19.3 applicants/place | Excellent content, unrealistic odds at 12–13/20. |

---

## 5. Country-level notes — France

### 5.1 Études en France (EEF) — MANDATORY for Tunisian residents

**Verified from the official Campus France Tunisie calendar PDF
(*Calendrier des procédures — Rentrée universitaire 2026/2027*), read 2026-08-17.**

Verified 2026/2027 calendar (= September 2026 entry), **HORS-DAP band, which is
the one covering Master 1, Master 2, écoles d'ingénieurs and écoles de commerce**:

| Step | Verified date (2026/2027 cycle) | **Projected for autumn 2027** |
|---|---|---|
| 1. Prepare the study project | — | from summer 2026 |
| 2. Create the EEF file online | **from 01/10/2025** | **~01/10/2026** |
| 3. Submit the file **and pay the fee** | **by 15/01/2026** | **~15/01/2027** |
| 4. Campus France interview | **by 15/03/2026** | **~15/03/2027** |
| 5. Institutions respond | **by 30/04/2026** | **~30/04/2027** |
| 6. Final choice | **by 31/05/2026** | **~31/05/2027** |
| 7. Visa (TLS-Contact) | allow ~2 months | June–August 2027 |

*(The DAP band — Licence 1 / L.AS / PASS / architecture — closes earlier, on
10/12, and is irrelevant to him.)*

**The 2027/2028 calendar is NOT yet published.** The dates above are projected
from a verified prior-cycle calendar and are labelled as such. Campus France
Tunisie has historically re-opened or extended the platform (the 2025/2026
deadline of 15 January was extended to 23 January), so treat 15 January as the
working deadline and any extension as luck.

**Operational consequences he must act on now:**
1. **The EEF deadline (~15 Jan 2027) is one to two months EARLIER than the
   university deadlines quoted on programme pages** (Mon Master ran 17 Feb –
   16 March 2026; IAE M2 sessions in March–May). Reading a programme page and
   working to *its* deadline would make him miss the intake entirely.
2. The platform opens **~1 October 2026 — about six weeks from today.** Document
   gathering (FSEG attestation, supplément au diplôme, transcripts, translations,
   any language test) should start immediately.
3. **Up to 7 choices**, of which max 3 at licence level and max 2 for
   architecture schools — so effectively **7 master's choices**. He should build
   a portfolio across tiers, not bet on one programme.
4. **A mandatory Campus France interview**, in French, at Tunis, Sousse or Sfax.
   Campus France Sousse is at 15 rue Hamed el Ghazali, 4000 Sousse — his own
   city. Arrive 30 minutes early; **15–20 minutes to present and defend the
   study project.** This is where a 12–13/20 record is recoverable: the CRM
   platform and the Renault Kélibia internship are exactly the material an
   interview rewards.
5. **Fee: 400 TND** for master's applications (150 TND only for holders of a
   French bac obtained less than 4 years ago — not him). Paid online via the
   Institut français de Tunisie after the dossier is submitted. A second visa
   appointment costs an extra **100 TND**.
6. **Not every institution is "connected" to EEF.** Some private schools are
   applied to directly and then joined to the *"Je suis accepté"* pre-consular
   procedure. Rennes SB, IESA, ICART and ESG fall in this second category —
   he applies to the school, then runs the pre-consular EEF step.

**Sources:** https://www.tunisie.campusfrance.org/system/files/medias/documents/2025-09/calendrier%20EEF%2020252026%20VERSION%20OK.pdf · https://www.tunisie.campusfrance.org/la-procedure-pour-candidater-aux-etudes-en-france · https://www.tunisie.campusfrance.org/procedure-de-candidature-reglement-des-frais-de-dossier · all checked 2026-08-17

### 5.2 Tuition — **THE BRIEF'S PREMISE HAS CHANGED. Read this section.**

The brief's assumption ("~€3,770/year BUT many universities exonerate, keeping
non-EU students at ~€250") **was true until May 2026 and is no longer.**

**Current verified figures for 2026/2027, from Campus France Tunisie's own page
*Le coût des études en établissement public*:**

| Level | Non-EU differentiated rate | Standard rate |
|---|---|---|
| Licence | **€2,902** | ~€178 |
| **Master** | **€3,950** | **~€254** |
| Doctorate | **€398** (doctorate is exempt from differentiated fees) | — |
| **CVEC** (compulsory, all students) | **€105** | €105 |

Université Lyon 1 publishes €2,902 / €3,950 for the same year — the figures are
consistent and national.

**Décret n° 2026-385 of 19 May 2026** (in force the day after publication)
restricts exonérations. Each public institution may now exonerate **at most:**
- **30 %** of its non-EU students in **2026-2027**
- **25 %** in **2027-2028** ← **the year he would enrol**
- **20 %** in the long term

Exonerations may be total or partial. **Automatic (regulatory) exemptions** —
which do *not* consume the quota — cover: EU/EEA/Swiss/Andorran/Monegasque
nationals; Québec nationals; people with 2+ years' French tax residence;
**holders of a French government scholarship (BGF)**; refugees and stateless
persons; doctoral students; students on bilateral Franco-foreign agreements or
approved international mobility programmes; and students continuously enrolled in
French institutions from before 2019. **A Tunisian applying fresh from Sousse
qualifies for none of these** unless he wins a BGF.

**Institutional exemption policies vary and must be checked one by one.** Two
verified contrasting examples:
- **Université Paris 1 Panthéon-Sorbonne** adds discretionary exemptions for
  asylum seekers and for nationals of the **44 UN least-developed countries**.
  **Tunisia is not an LDC — he does not qualify at Paris 1.**
- **Université Lyon 1** runs an application-based scheme via eCandidat
  (*"Demande d'exonération des droits d'inscription différenciés pour les
  étudiants extra-communautaires"*) within the 30 % quota. **Applying is
  possible; the outcome is discretionary.**

**Planning guidance: budget €3,950 + €105 = €4,055/year and treat any
exoneration as upside.** France is still inside filter band 2 at that price and
still beats most of Europe — but the "€250 France" that circulates in guides and
older advice is, for a 2027 entrant, **wrong**.

**Sources:** https://www.tunisie.campusfrance.org/le-cout-des-etudes-en-etablissement-public · https://www.service-public.gouv.fr/particuliers/actualites/A18927 · https://www.univ-lyon1.fr/formation/inscription-et-scolarite/etudiantes-et-etudiants-internationaux-droits-dinscription-differencies-et-exonerations · https://international.pantheonsorbonne.fr/en/differentiated-tuition-fees · https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054113646 · all checked 2026-08-17

### 5.3 Mon Master vs Études en France — do not mix them up

Mon Master (monmaster.gouv.fr) is the national M1 application platform for
**EU/EEA/Swiss/Monaco/Andorra nationals and for candidates resident in the ~72
countries NOT covered by Études en France.** Tunisia **is** covered by EEF, so
**he must use Études en France, not Mon Master.**

**Explicit official warning:** a candidate resident in an EEF country who declares
a different country of residence on Mon Master **risks not obtaining a visa.**
Campus France Tunisie carries a standing alert page on this
(`/vigilance-plateforme-de-candidature-mon-master`).

Practical note: programme pages quote *Mon Master* dates (typically mid-February
to mid-March) because that is the domestic calendar. **His real deadline is the
EEF one in mid-January.** Every deadline in §3 should be read through this lens.

Also note: **trouvermonmaster.gouv.fr is dead** and monmaster.gouv.fr's search API
is authentication-gated, so there is no longer a public national catalogue to
browse. Programme discovery now has to go institution by institution or through
the EEF catalogue once the platform opens on ~1 October 2026 — **which is itself
a good reason for him to log in on day one and use the platform's own catalogue.**

### 5.4 Score IAE-Message — an under-advertised gate

Several IAEs (verified: **Tours, La Rochelle**) require the **Score IAE-Message**,
a test covering general culture, French written comprehension and expression,
logical and numerical reasoning, and written English. **Cost €42**, and one score
serves applications to multiple programmes at multiple institutions. Test centres
exist *"in France or abroad"* — but **the site does not confirm a Tunisian or
Maghreb centre, does not publish session dates, and does not say whether Études
en France candidates are exempt.** `NOT VERIFIED — he must email
contact@iae-message.fr before committing to any Score-requiring IAE.`

This matters for sequencing: if a centre or online sitting is not available from
Tunisia, Tours and La Rochelle drop out and **IAE Montpellier (which requires a
dossier + oral interview, not the Score) and Lyon 2 become the core of the
public-university list.**

**Source:** https://www.iae-message.fr/ · checked 2026-08-17

### 5.5 French language — he is NOT automatically exempt, and this surprises people

**Requirement at master level (hors-DAP):** **TCF Tout Public (TP/SO) or
DELF/DALF.** (The TCF-DAP with its written-expression component applies only to
Licence 1 / L.AS / PASS and architecture — not to him.)

**Verified exemption (dispense) cases at master level:**
- already holding a pre-registration at a French institution
- nationals of **officially French-speaking countries** — **Tunisia is NOT one.
  Tunisia's only official language is Arabic**, exactly like Algeria, Morocco and
  Lebanon. **The common assumption that a Tunisian francophone is automatically
  exempt is false.**
- holders of **DELF B2 or DALF C1/C2**
- **TEF score of 14/20** (Paris CCI)
- candidates selected via a concours or interview at a French institution
- holders of a **French baccalauréat** or a **French higher-education degree**
- candidates selected through public institutional conventions
- **French government scholarship (BGF) holders**
- doctoral candidates in France

**Critical caveat, quoted verbatim from Campus France Tunisie:** *"Même en cas de
dispense de certification de français par Campus France, il se peut que
l'établissement vous l'exige."* — an institution may demand certification even
where Campus France exempts.

**Practical verdict:** he is a native French speaker but has **no certificate**.
The cheapest, most flexible fix is a **TCF Tout Public**, sittings of which are
run by the **Institut français de Tunisie / Alliance française** in Tunisia. A
native speaker should reach C1–C2 without preparation. **He should sit it before
October 2026** so the result is in hand when the EEF platform opens. One specific
warning: **Sorbonne Nouvelle demands C2 for foreign candidates** (§4.3) — a DALF
C2 is a far heavier ask than a TCF and should be queried with admissions first.

**Source:** https://www.tunisie.campusfrance.org/les-certifications-en-langue-francaise-0 · checked 2026-08-17

### 5.6 Visa, work rights and post-study stay

**Study visa — VLS-TS mention « étudiant »:**
- Covers stays from four months to one year, renewable as a residence permit
- **Work rights during study: 964 hours per year (~20 h/week)** — a genuine
  contribution towards the €4,055 tuition
- **Processing: 15 to 45 days** after filing with **TLS-Contact**. TLS-Contact
  has run sessions at Campus France Sousse, so he may not need to travel to Tunis
- **Must be validated within 3 months of arrival** at
  administration-etrangers-en-france.interieur.gouv.fr, with an online payment of
  the residence tax. Failure to validate = irregular status and loss of VLS-TS
  rights
- Unlocks **VISALE** (free state housing guarantee — important, since he will
  have no French guarantor) and **CAF housing allowance (APL)**
- **Financial resources required per month: `NOT VERIFIED — check directly`.**
  france-visas.gouv.fr returned HTTP 403. The figure should appear at
  https://france-visas.gouv.fr/en/etudes and on the Campus France Tunisie visa
  page. **Do not quote a number without confirming it.**

**Post-study — APS (autorisation provisoire de séjour) / carte « recherche
d'emploi ou création d'entreprise » (RECE):**
- **12 months, non-renewable**
- Open to holders of a **master's or equivalent** (engineering diplomas, IEP
  diplomas, **mastères spécialisés**, **CGE-labelled MSc**, professional licences)
  and to those setting up a business
- Permits work up to 964 h/year while searching, until a substantive contract
- **Tunisia is explicitly named among the countries with a bilateral migration
  agreement granting *"conditions de délivrance plus favorables"*** — alongside
  Senegal, Gabon, Benin, Mauritius, Cape Verde, Burkina Faso and others. **This
  is a genuine, under-used advantage of his nationality in France.**
- To convert to a salaried residence card the job must pay at least **1.5× SMIC**
  (a figure of ~€2,281.82 gross/month was cited in 2026 reporting —
  `treat as indicative, verify at the time`)
- **Apply as soon as the diploma is validated — do not wait for the student
  permit to expire.**

**Accreditation implication for §3:** the APS list covers *diplôme national de
master*, *mastère spécialisé* and *CGE-labelled MSc*. **It does not obviously
cover a plain RNCP-7 title from a non-CGE school.** So ICART (RNCP 40674), IESA
(RNCP 42330) and ESG Nantes (RNCP 39360) **carry a real post-study-work risk that
Rennes SB (CGE member) and every public university programme do not.** Per the
brief's accreditation rule, these three are `VERIFY APS ELIGIBILITY IN WRITING
BEFORE APPLYING` and should stay off any shortlist until they are confirmed.

**Sources:** https://www.tunisie.campusfrance.org/visa-etudiant-vls-ts · https://www.maurice.campusfrance.org/www.campusfrance.org/fr/l-autorisation-provisoire-de-sejour-ou-aps · both checked 2026-08-17

### 5.7 Scholarships

- **Bourse du gouvernement français (BGF)** — the highest-value target, because
  **BGF holders are automatically exempt from the differentiated €3,950**, which
  makes it worth roughly €3,700/year on its own before any stipend. Campus France
  Tunisie directs applicants to the **Institut français de Tunisie and the French
  Embassy in Tunisia** for programmes matching their profile. Specific Tunisian
  BGF schemes, amounts and deadlines: `NOT VERIFIED — check directly` at
  https://www.tunisie.campusfrance.org/les-bourses-exonerations-et-aides-proposees
  and with IFT/Ambassade directly.
- **Bourse France Excellence Eiffel** — master's and doctoral level, ~€1,200/month.
  **Critical mechanism:** Eiffel is **nominated by the host institution, not
  applied for by the student.** He must ask each target institution to nominate
  him, typically in the autumn preceding entry — i.e. **autumn 2026**, in parallel
  with the EEF application. Campus France Tunisie maintains a dedicated Eiffel
  page (`/le-programme-de-bourses-france-excellence-eiffel`).
- **Campus Bourse** (campusbourse.campusfrance.org) — the official searchable
  database of French and foreign scholarships, filterable by nationality, field
  and level. **The right tool for a systematic Tunisia-filtered sweep;** I could
  not run it in this session.
- **Institutional:** Rennes SB Talent / Unframed (up to €5,000 each), Ambassador
  (15 %), Bienvenue en France (€500), Social and Solidarity (€500–€2,000).
  **None designated for African or North African students.**
- **University exoneration requests** (§5.2) are effectively a scholarship in
  disguise, worth ~€3,700/year, and are applied for on each university's own
  portal — typically after admission. **He should apply at every institution that
  offers the route.**

### 5.8 Cost of living

**`NOT VERIFIED — check directly.`** I could not confirm monthly living costs from
an official French source in this session: france-visas.gouv.fr returned 403, and
the Campus France Tunisie cost pages I reached carry tuition figures only, not
living budgets. Per the brief's rule I am **not estimating**.

Where the figures should be obtained:
- https://www.campusfrance.org — "Le coût de la vie étudiante" / budget pages
- https://www.tunisie.campusfrance.org/s-informer-sur-le-cout-et-les-bourses-d-etudes (navigation hub; follow its child articles)
- CROUS regional sites for accommodation rates in Lyon, Montpellier, Lille, Rennes, Tours

**What is verified and financially relevant:**
- **CVEC €105** for 2026/2027, compulsory
- **964 work hours/year** permitted on a student visa
- **VISALE** free state housing guarantee, available to VLS-TS holders
- **CAF/APL** housing allowance, available to VLS-TS holders
- The French state subsidises roughly **€11,000/year** of the real cost of each
  student's education — the reason even the differentiated rate stays low
- **Directional note, unverified:** every city in the shortlist (Lyon,
  Montpellier, Lille, Rennes, Tours, Saint-Étienne, La Rochelle, Nantes) is a
  regional city, materially cheaper than Paris. **Paris-based options (Paris 8,
  Sorbonne Nouvelle, IESA, ICART, EPITA) carry a significant living-cost penalty
  on top of their other drawbacks.**

---

## 6. Structural findings specific to France

1. **The M2-only trap.** Most French music-industry master's programmes admit
   only at M2 (Bac+4): Paris 8, Saint-Étienne, EMIC. With a Bac+3 licence he
   cannot enter these directly. **Only routes with an M1 entry work** —
   Lyon 2, Sorbonne Nouvelle, Rennes SB, IESA, ICART, ESG Nantes.
2. **Licence-discipline lists matter more than GPA.** French mentions publish
   lists of accepted licences. His marketing licence is *on* the list for
   Lyon 2 (économie/gestion), IAE Montpellier, IAE Tours, IAE Lille MIADS and
   IESA; **off** the list for Paris 8 (Industries culturelles) and marginal for
   Sorbonne Nouvelle. Checking that list first is a faster filter than checking
   grades.
3. **Alternance is a mirage for a visa applicant.** Several of the cheapest or
   free routes (ESG Nantes, IAE Lille MIADS, IAE Tours, EMIC) are alternance-
   based, meaning zero tuition — but they require a signed French apprenticeship
   contract, which a candidate applying from Tunisia cannot realistically obtain
   before a visa is granted. **Filter for formation-initiale places.**
4. **Interview-based selection is his friend.** IAE Montpellier (oral interview),
   Rennes SB (recorded video interview), ICART (motivation interview) and the
   mandatory Campus France interview all give weight to the CRM platform and the
   Renault internship. Programmes selecting on dossier alone are where a
   12–13/20 hurts most.
5. **No GMAT anywhere in scope.** None of the accessible French programmes
   requires GMAT or GRE. Rennes SB explicitly does not. The brief's ~600 GMAT
   exclusion never binds in France.

---

## 7. Sources, with check dates (all checked 2026-08-17)

**Government / procedure**
- Campus France Tunisie — Calendrier des procédures, rentrée 2026/2027 (PDF): https://www.tunisie.campusfrance.org/system/files/medias/documents/2025-09/calendrier%20EEF%2020252026%20VERSION%20OK.pdf
- Campus France Tunisie — la procédure pour candidater: https://www.tunisie.campusfrance.org/la-procedure-pour-candidater-aux-etudes-en-france
- Campus France Tunisie — frais de dossier (400 TND): https://www.tunisie.campusfrance.org/procedure-de-candidature-reglement-des-frais-de-dossier
- Campus France Tunisie — certifications en langue française: https://www.tunisie.campusfrance.org/les-certifications-en-langue-francaise-0
- Campus France Tunisie — coût des études en établissement public: https://www.tunisie.campusfrance.org/le-cout-des-etudes-en-etablissement-public
- Campus France Tunisie — visa étudiant VLS-TS: https://www.tunisie.campusfrance.org/visa-etudiant-vls-ts
- Campus France Tunisie — bourses, exonérations et aides: https://www.tunisie.campusfrance.org/les-bourses-exonerations-et-aides-proposees
- Campus France — l'APS: https://www.maurice.campusfrance.org/www.campusfrance.org/fr/l-autorisation-provisoire-de-sejour-ou-aps
- Service-Public — droits d'inscription étudiants étrangers: https://www.service-public.gouv.fr/particuliers/actualites/A18927
- Légifrance — Décret n° 2026-385 du 19 mai 2026: https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054113646
- Université Lyon 1 — droits différenciés et exonérations 2026/2027: https://www.univ-lyon1.fr/formation/inscription-et-scolarite/etudiantes-et-etudiants-internationaux-droits-dinscription-differencies-et-exonerations
- Paris 1 Panthéon-Sorbonne — differentiated tuition fees: https://international.pantheonsorbonne.fr/en/differentiated-tuition-fees
- Score IAE-Message: https://www.iae-message.fr/

**Programmes** — every programme URL is given inline in §3.

**Failed / blocked (recorded for the next pass)**
- trouvermonmaster.gouv.fr — 301 → monmaster.gouv.fr (catalogue discontinued)
- monmaster.gouv.fr API — HTTP 401 on all endpoints tried
- enseignementsup-recherche.gouv.fr FAQ droits différenciés — HTTP 403
- france-visas.gouv.fr/en/etudes — HTTP 403
- campusfrance.org/fr/catalogue-formations — HTTP 404
- univ-lille.fr/formations/fr-00002898 — generic catalogue shell, programme page moved
- iae-paris-est.fr Master Marketing Digital — empty response
