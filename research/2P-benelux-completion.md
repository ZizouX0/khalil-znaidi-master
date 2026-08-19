# 2P — BENELUX COMPLETION (finishing 2G)
**Agent 2P · all checks dated 2026-08-17 · target intake AUTUMN 2027**
Supplements `2G-benelux.md`. Does not repeat 2G's verified findings (FWB €5,369;
ULiège French exemption; Belgian 12-month job-search year; IND orientation year;
Utrecht pre-master exclusion). **Read 2G first.**

---

## 1. Bottom line

**Luxembourg is unblocked and the answer is a clear no for marketing.** Firecrawl
with `--proxy auto` defeated the CloudFront 403 that stopped 2G — I now have
uni.lu's own pages. The University of Luxembourg has **no marketing master, no
communication/media master, and no music master** (it has a *bachelor* en
enseignement musical only). The single tangential fit, the **Master in
Entrepreneurship & Innovation (120 ECTS)**, costs **€2,500/sem for semesters 1–2
and €1,500/sem for 3–4 (≈€8,000 total)**, demands **English C1** and states a
literal **"BA degree with 180 ECTS"** — so it is expensive-for-what-it-is and
credit-blocked. The one genuinely valuable Luxembourg datum is a **hard date**:
*"Applications for the 2027–2028 academic year will open on 1 February 2027."*
**Wallonia-Brussels remains the strongest part of Benelux** and I extended it:
**UNamur** and **UMons** both confirmed at the €5,369 FWB rate with a **31 March
visa-applicant deadline** and a **€200 file fee**, **UCLouvain's 60-credit
complementary cap is now verified on its own 2026 page** (not a search extract),
and **IHECS's Master 120 en publicité et communication commerciale** is confirmed
at €5,369 with **no entrance exam** and a syllabus containing data analytics,
social platforms, UX and influence marketing — on content-per-euro this is
arguably the best single find in Benelux for him. **Flanders is now priced**:
UAntwerpen non-EEA master = **€1,500 + €105/credit = €7,800/yr**, KU Leuven sits
in one of four bands topping out at **€9,493.92**. But Flanders' best-fit
programme, **UGent's Marketing Analysis, is confirmed BLOCKING** — it is an
*advanced master* (master-na-master) requiring a bachelor **and** a master, or a
4-year bachelor. **Dutch HBO is real but pricey**: the cheapest verified route is
AUAS's Digital Driven Business at €10,648, then NHL Stenden €11,995, Saxion
€13,644, Rotterdam UAS €14,449; The Hague's communication master is out on two
filters at once. **Music: I overturn nothing. 2G was right — zero music-business
or music-marketing master's exist anywhere in Benelux.**

---

## 2. Coverage statement — what I searched and what I found nothing on

**Languages searched:** French, Dutch, English.

**Reached and read (primary sources):** uni.lu (`/en/admissions/bachelor-master/`,
`/fdef-en/study-programs/master-in-entrepreneurship-and-innovation/admissions`,
`/fstm-en/study-programs/master-in-data-science/admissions`, plus a full site map
filtered on *master*, *marketing*, *management*, *data*, *communication culture
media music*); uclouvain.be `prog-2026-gest2m-cond_adm`; unamur.be
`/en/registration/international/masters` and `/hue/masters-conditions`;
kuleuven.be tuition-fee-breakdown; onderwijsaanbod.kuleuven.be SC_54542934;
uantwerpen.be tuition-fees-2026-2027; rotterdamuas.com programme-costs and
admission-requirements; nhlstenden.com fees-and-admissions (via firecrawl search
extract of the official page); saxion.edu total-costs; helha.be masters list.

**Tooling that mattered:** `firecrawl scrape --proxy auto` is what broke uni.lu.
Plain WebFetch, WebSearch and unproxied firecrawl all returned CloudFront 403 or
empty. **Record this for future agents: uni.lu is reachable, but only with the
stealth proxy.**

**Found NOTHING on — explicit gaps:**
1. **No music master's, anywhere in Benelux** — re-confirmed and extended.
   Luxembourg has only a *Bachelor en enseignement musical*; Flanders' PXL
   "Muziekmanagement" is a **specialisation inside a professional bachelor** in
   Pop & Rock Music, not a master. UAntwerpen Cultuurmanagement (Dutch) remains
   the single nearest thing in the whole region.
2. **KU Leuven's actual fee band for business programmes** — still not obtained.
   The four non-EEA bands are now verified but the mapping programme→band lives
   only in a JavaScript calculator that firecrawl could not execute.
3. **VUB non-EEA master fee** — the official PDF
   (`2025_Studiegeld_tarieven_NEER_2627_ENG.pdf`) **404s**; VUB's fee page is a
   JS shell. Still `NOT VERIFIED`.
4. **UHasselt non-EEA fee** — page returned no fee content. `NOT VERIFIED`.
5. **UMons's non-EU admission PDF** — `web.umons.ac.be/app/uploads/.../Master-HUE.pdf`
   returns an HTML wrapper, not the PDF, to every tool including firecrawl. I have
   its wording only via search extract.
6. **ULB's French-test exemption on a ULB-owned page** — still only a search
   extract. ULB's `www2.ulb.ac.be/temp/programme/...` pages remain 403.
7. **Breda UAS (BUas) exact non-EU fees** — behind a calculator.
8. **Fontys, Avans, HAN, Windesheim** — no English-taught HBO master in marketing,
   digital business or data-driven business surfaced for any of them. I did not
   find one; I also cannot certify none exists.
9. **Luxembourg post-study permit duration** — still unstated on guichet.lu.
   2G's gap stands.
10. **2027-28 deadlines for Belgium and the Netherlands** — not published. Only
    Luxembourg has published a 2027-28 date (1 Feb 2027 opening).

---

## 3. TASK 3 ANSWER — LUXEMBOURG (previously 100% unverified, now resolved)

### 3.1 What the University of Luxembourg actually offers

Complete master portfolio relevant to his four directions, from uni.lu's own site
map (checked 2026-08-17):

| Faculty | Master's programmes | Relevant? |
|---|---|---|
| **FDEF** (Law, Economics, Finance) | Entrepreneurship & Innovation · Wealth Management · Finance and Economics (+ tracks *Digital Transformation in Finance*, *Private Assets*) · Quantitative Economics and Finance · European Business Law · European Banking and Financial Law · Droit des fonds d'investissement | Only **Entrepreneurship & Innovation** is even adjacent |
| **FSTM** (Science, Tech, Medicine) | Data Science · High Performance Computing · Information System Security Management · Space Technologies and Business · Physics · Mathematics · biomedicine · engineering | **Data Science** is direction-1 on paper, blocked in practice |
| **FHSE** (Humanities, Education, Social Sciences) | Digital and Public History · Gérontologie · Sciences de l'éducation (2 variants) · Modern & Contemporary European Philosophy · Trinational Master in Literature, Culture and Language | None |

**NO master in marketing. NO master in communication, media or creative
industries. NO master in music or music business.** The only music provision is
a **Bachelor en enseignement musical** (FHSE) — a bachelor, therefore out of
scope under §4 of the shared brief. This is a **verified empty result**, not a
coverage gap.

### 3.2 Master in Entrepreneurship & Innovation — the only candidate

| Field | Value |
|---|---|
| University / city | University of Luxembourg (FDEF), Esch-sur-Alzette / Belval |
| Degree + ECTS | Master · **120 ECTS** (exit at 60 ECTS gives a *Certificate*, not a master) |
| Institution type | **Public university**, state-recognised, trilingual FR/DE/EN institution |
| Direction match | **2, weakly** — entrepreneurship/innovation, not marketing |
| Teaching language | English (page's language field rendered empty; **English C1 is the stated requirement**) → **Tier A** on language, but see certificate note |
| **Non-EU tuition** | **€2,500/semester for semesters 1 and 2; €1,500/semester for semesters 3 and 4** → **€5,000 in year 1, €3,000 in year 2, €8,000 total.** Same rate for non-EU as EU. **VERIFIED on uni.lu** |
| Entry requirement (exact wording) | *"Students need to have: a BA degree with **180 ECTS** in any discipline subject area and a demonstrated entrepreneurial motivation."* Alternatives: *"a 4-year BA degree (in any topic) with 240 ECTS"*; *"a 3-year BA and 1-year Masters… achieving 240 ECTS"*; **OR "180 ECTs and 3 year's work experience in a business/organizational setting."** Direct Year-2 entry needs *"60 ECTS in courses related to finance/marketing/entrepreneurship/innovation/project management"* |
| **146 ECTS verdict** | **BORDERLINE→BLOCKING.** The 180 figure is stated numerically three separate times. There is no jury-discretion or complementary-credit language anywhere on the page — unlike Belgium. The FSEG attestation is the only lever, and it must be accepted at face value with **no** bridging fallback if it isn't |
| Language requirement | **English C1** — *"Proficiency in the following language at the level indicated by the CEFR: English (C1)"*. He has **no English test**. C1 is a step above the B2 most programmes ask. This is a real obstacle, not a formality |
| Extra selection | Motivation letter on entrepreneurial intent; credit given for patents held/applied for and comparable evidence |
| Deadline | **Applications for 2027-2028 open 1 February 2027** (verified verbatim). Per-programme non-EU deadlines vary — *"check the deadline that applies to your applicant profile (EU or non-EU)"* |
| Application fee | **€100 per application**, non-refundable, **no waivers**, but **€100 is deducted from the first semester's tuition** if he enrols |
| Post-study | Luxembourg job-search permit — **duration still NOT VERIFIED** (2G's gap stands) |
| URL | https://www.uni.lu/fdef-en/study-programs/master-in-entrepreneurship-and-innovation/admissions/ |

### 3.3 Master in Data Science — direction 1 on paper, blocked in reality

120 ECTS · **€400/semester (≈€800/year — the cheapest tuition found anywhere in
this project's Benelux scope)** · English B2 (not C1). But: *"required to hold a
Bachelor's degree… with at least 180 ECTS in either mathematics, physics,
engineering, or economics, or including sufficient mathematics training… strong
emphasis is placed on the number of courses in mathematics… strong proficiency in
linear algebra and analysis is necessary."* **146 ECTS verdict: BLOCKING**, and
independently blocked on subject background — a marketing licence from FSEG will
not clear a linear-algebra prerequisite. Recorded because the €800 price tag will
tempt, and it should not.
URL: https://www.uni.lu/fstm-en/study-programs/master-in-data-science/admissions/

### 3.4 Luxembourg procedural facts (all verified 2026-08-17)

- **2027-28 application window opens 1 February 2027.** This is the only
  confirmed 2027-28 date in the whole Benelux scope.
- **€100 admin fee per application**, non-refundable, no waivers, credited against
  first-semester tuition on enrolment.
- **Multilingual programmes require proof in *every* teaching language listed** —
  *"applicants must provide proof of competence in **all** listed languages."*
  His trilingual advantage is real only where the programme lists FR.
- Non-EU admitted candidates must produce a **criminal-record extract** for the
  Ministry of Home Affairs; uni.lu advises requesting it **by early April**, before
  the admission decision arrives.
- Non-European applicants **pay enrolment and health-insurance fees in person, by
  bank card, on arrival in Luxembourg** — a cash-flow detail worth knowing.
- Source: https://www.uni.lu/en/admissions/bachelor-master/

**Verdict on Luxembourg: essentially closed for his four directions.** Cheap
tuition, high salaries and French usability do not compensate for there being no
programme to enrol in. Do not spend more research effort here.

---

## 4. TASK 1 — FRENCH-SPEAKING BELGIUM, extended

### 4.1 UNamur — NEW, previously unverified

| Field | Value |
|---|---|
| University / city | Université de Namur, Namur |
| Programmes | **Master 120 en sciences de gestion** · **Master 60 en sciences de gestion (horaire décalé)** · **Master 120 en ingénieur de gestion** · Master 60 en sciences économiques (horaire décalé) |
| Institution type | Public-funded private university (FWB-recognised, ARES register) |
| Direction match | 1–2, generalist management with marketing content |
| Language | French → **Tier A** |
| **Non-EU tuition** | **€5,369** — UNamur's own fees page states the figure for *"citizens of countries outside the European Union not listed in certain annexes"*, matching the FWB decree rate 2G verified |
| **Deadline (this is the important one)** | **31 March** for applicants **who require a visa**; 31 August for non-EU applicants who do *not* need a visa; 30 September for EU. He needs a visa → **31 March**. (2026-27 dates; 2027-28 not published — treat as indicative but the pattern is stable across ULiège, UCLouvain and UNamur) |
| Application fee | **€200 flat**, payable before the file is even reviewed |
| **Equivalence — favourable** | *"if you hold a non-Belgian degree, you do not need to provide proof of equivalence to access graduate studies"* — i.e. **no ENIC-NARIC equivalence needed for master entry**. Saves the €120 / 4-month French procedure the brief costed |
| Language requirement | *"Test de Connaissance du Français (TCF-Level B2), DALF (C1-C2), or DELF (minimum B2)."* **No exemption clause found for French-medium prior education.** ⚠️ `NOT VERIFIED — check directly`. The mandatory October diagnostic test applies only to *section 4/5 teaching* masters, not to gestion |
| **146 ECTS verdict** | **BORDERLINE.** Programme-specific conditions sit in a PDF (`Conditions admission 26-27-2ème Cycle_Mars2026bis.pdf`) that the page links but does not inline. Needs an email to the faculty |
| URLs | https://www.unamur.be/en/registration/international/masters · https://www.unamur.be/en/registration/international/hue/masters-conditions · https://www.unamur.be/en/registration/international/fees |

### 4.2 UMons (Faculté Warocqué) — NEW, partially verified

| Field | Value |
|---|---|
| University / city | Université de Mons, **Mons** and **Charleroi** campuses |
| Programmes | **Master 120 en sciences de gestion, à finalité spécialisée** (Mons, *horaire jour*) · **Master 120 en sciences de gestion, à finalité spécialisée en management et stratégie** (Charleroi, *horaire décalé* — evening, since 2004) · **Master 60 en sciences de gestion** |
| Institution type | Public university (Communauté française) |
| Direction match | 1–2. **Marketing is one of five management areas covered; there is no dedicated *finalité marketing*** — checked, does not exist |
| Language | French → **Tier A** |
| Non-EU tuition | **€5,369** (FWB decree rate; UMons is a fully subsidised FWB university, so the rate applies. ⚠️ not read on a UMons fee page — `NOT VERIFIED` at institution level) |
| Entry requirement (search extract of the official non-EU PDF) | first-cycle diploma of **"minimum 3 years of higher education and/or 180 credits"**; the diploma must have been obtained **within the last 6 years**; *"the faculty will refuse the application if the file does not contain the required diploma at the time of analysis"* and **will not accept applications "subject to the completion of the current year"** |
| **146 ECTS verdict** | **BORDERLINE, but the wording is the friendliest in FWB.** *"3 years of higher education **and/or** 180 credits"* is disjunctive — a *years* test he passes cleanly. This is materially better than ULiège's conjunctive "180 credits **plus** 75%-per-year **plus** 12/20". **If one FWB university is worth an early email, it is UMons.** |
| **6-year recency rule** | Note it. His licence must be no older than 6 years at application. For a 2027 entry that is fine if he graduated 2021 or later |
| French exemption | **NOT VERIFIED** |
| Contact | admissions.FWEG@umons.ac.be · +32 65 37 32 02 |
| URLs | https://web.umons.ac.be/fweg/en/study-programmes/2eme-cycle-master/ · https://webcontent.umons.ac.be/web/fr/pde/2025-2026/cursus/MGT1_S208.htm (Mons) · https://webcontent.umons.ac.be/web/fr/pde/2024-2025/cursus/MSG1_S207.htm (Charleroi) · non-EU conditions PDF (tool-blocked): https://web.umons.ac.be/app/uploads/2025/01/Faculte-Warocque-economie-et-gestion-Master-HUE.pdf |

### 4.3 UCLouvain — 60-credit cap now VERIFIED on a UCLouvain page

2G had this from a search extract. **Now primary.** The 2026 access-conditions
page for the Master [120] en sciences de gestion states complementary training of
**"max. 60 crédits d'enseignements complémentaires"** may be added depending on
the assessment of the applicant's background. Holders of a *"Bachelier non belge
en sciences économiques et de gestion ou équivalent issu d'une institution
universitaire reconnue"* are the addressed category — which is exactly him.

**Procedure worth knowing:** the page instructs candidates to complete a
**prerequisite-analysis form and email it to `lsm-belgian-admissions@uclouvain.be`
*before* the formal online application.** That is a free, low-stakes way to get
the 146-credit question answered by the people who decide it, months before any
deadline. **This is the single most actionable step in this whole report.**
Source: https://uclouvain.be/prog-2026-gest2m-cond_adm (checked 2026-08-17)

### 4.4 French-test exemption — status per institution (Task 1 explicit ask)

| Institution | Exemption for French-medium education? | Status |
|---|---|---|
| **ULiège** | **YES** — exempts native French speakers, nationals of French-speaking countries, **and** those who completed secondary or higher education in French | **VERIFIED** (by 2G, on `enseignement.uliege.be`) |
| **ULB** | **YES, apparently** — exemption where the applicant is a native speaker, has citizenship of a country where the language is official, **or "obtained a diploma or completed a year in higher education taught in that language"**. Also: passing ULB's special admission exam exempts from the French test | **SEARCH EXTRACT ONLY.** ULB's own pages 403 to every tool including firecrawl. Treat as probable, not proven |
| **UCLouvain** | **PARTIAL / probable** — candidates without an FWB higher-education diploma must show B2, but *"if lacking official attestation from a recognised body, a university attestation justifying instruction in French may be accepted"*. So a **free FSEG attestation that teaching was in French appears to substitute for DELF/TCF**. The mandatory October diagnostic test applies to *enseignement* (teacher-training) masters, **not** to gestion | **SEARCH EXTRACT.** Worth an email — it is the same attestation he needs for the credits question, so one email covers both |
| **UNamur** | **NO exemption found.** Page lists TCF B2 / DELF B2 / DALF C1-C2 with no dispensation clause | `NOT VERIFIED — check directly` |
| **UMons** | Not found either way | `NOT VERIFIED` |
| **ICHEC** | Not found (2G's gap stands) | `NOT VERIFIED` |
| **IHECS** | **Effectively yes** — the stated minimum is only **B1**, and teaching runs in French, English and Dutch. A native French speaker is trivially above B1 | See 4.5 |

**Practical read:** the exemption is a **regional norm in FWB, not a per-school
quirk** — ULiège states it explicitly, ULB and UCLouvain apply recognisable
variants. But because only ULiège is *proven*, he should carry a **free FSEG
attestation certifying French-medium instruction** with every FWB application.
It costs nothing and it is the document all three variants key on.

### 4.5 IHECS — Master 120 en publicité et communication commerciale ⭐ PRIORITY FIND

| Field | Value |
|---|---|
| Institution / city | **IHECS**, Brussels — *haute école* (applied, practice-oriented), FWB-recognised |
| Degree + ECTS | Master en communication appliquée, finalité **publicité et communication commerciale** — **120 ECTS** (a **Master 60 en horaire décalé** variant also exists) |
| Direction match | **HYBRID 2 + 3.** Year 2 covers *"the company's digital ecosystem (digital platforms & social media, **data analytics**, **user experience**, **influence marketing**)"* and budgeting/pre-testing of communication actions. This is closer to *digital marketing & growth* than most "marketing" masters, and the influence/audience-development content is the nearest thing in Benelux to artist promotion |
| Institution type | Haute école — **materially less selective than Solvay/LSM**, and **"no entrance exam for the Master programme"** (verified) |
| Language | Teaching units in **French, English and Dutch**; **minimum level required B1** → **Tier A**, with the lowest language bar found anywhere in Belgium |
| **Non-EU tuition** | **€1,194 + €4,175 = €5,369/yr** — IHECS's own droits-d'inscription page |
| **146 ECTS verdict** | **BORDERLINE, with the bridging mechanism already documented.** 2G verified IHECS's decree wording: complementary teaching up to **60 credits**, but **above 15 credits it becomes an *année préparatoire non diplômante*** — i.e. a real extra year with real extra cost. His 34-credit gap, if enforced, lands in that band |
| Non-EU degree-seeking procedure | **Still NOT VERIFIED** — IHECS's "admission procedure" page covers incoming exchange students. 2G's gap stands; must be obtained by email |
| URLs | https://www.ihecs.be/fr/master-en-publicite/specialisation-et-identite-professionnelle · https://www.ihecs.be/fr/s-inscrire-en-master/droits-d-inscription · https://www.ihecs.be/fr/inscriptions/procedure-d-inscription-0 |

### 4.6 The other hautes écoles — mostly an empty result, and that is the finding

I checked HELMo, HEPL, HE Vinci, HELHa, HEH and EPHEC. **The hautes écoles are
overwhelmingly bachelor-level in marketing.** HELHa, HELMo and HEPL each run a
*Bachelier en Marketing*; none runs a marketing master.

Their master portfolios, verified:

| Haute école | Masters offered | Relevant? |
|---|---|---|
| **HELHa** (Mons/Charleroi) | **Master en communication stratégique** (Mons, evening/weekend + alternance, 2 yrs) · Master en expertise comptable et fiscale (alternance) · Master ingénieur de gestion/industriel (I²) · Master ingénierie analytique · Master gestion de production · nursing, physiotherapy, teaching, social | **Communication stratégique is a NEW find** — direction 2 adjacent, applied, and delivered in *alternance* (work-linked). Details **NOT VERIFIED**: ECTS, non-EU fee, whether the evening/alternance format supports a student visa. ⚠️ Alternance formats often do not |
| **HEPL** (Liège) | **Master en Gestion publique** | Public-sector management — not his direction |
| **EPHEC** (LLN/Brussels) | **Master en Expertise Comptable et Fiscale** (co-organised with HELHa Mons and UCLouvain) | Accounting/tax — not his direction |
| **HELMo**, **HE Vinci**, **HEH** | No management or marketing master found | **Empty result** |
| **ICHEC** | Master en gestion de l'entreprise, 120 ECTS, €5,369 | Already found by 2G — remains the strongest haute-école option |

**Conclusion for Task 1's *hautes écoles* question: the "cheaper, more practical
applied route" in French Belgium reduces to exactly two institutions — ICHEC and
IHECS.** Everything else is either a bachelor or a different field. This is a
verified empty result and should stop further searching down that path.

---

## 5. TASK 2 — FLANDERS

### 5.1 Non-EEA tuition, 2026-2027 — the figures 2G never got

| University | Non-EEA master fee 2026-27 | Status |
|---|---|---|
| **UAntwerpen** | **€1,500 fixed + €105/credit = €7,800 for 60 credits** | **VERIFIED** on the official 2026-2027 tuition page |
| **KU Leuven** | Four non-EEA bands, each *fixed cost + per-credit*: **€1,181.40** (€305.40 + €14.60/cr) · **€3,093.12** (€1,305.12 + €29.80/cr) · **€5,613.12** (€1,726.92 + €64.77/cr) · **€9,493.92** (€2,376.72 + €118.62/cr) | **Bands VERIFIED**; the band that applies to Business Administration is **NOT VERIFIED** — it exists only inside a JS calculator. Budget for the €5,613–€9,494 range |
| **UGent** | €305.40 + €17.70/cr (≈€2,297) **or** €305.40 + €31/cr (≈€7,079) | 2G's figures; band still unresolved — moot, see 5.3 |
| **VUB** | Indicative €800–€3,000 quoted in secondary sources; a bachelor example computes to €2,200 + €52/cr = €5,320 | **NOT VERIFIED.** VUB's official non-EEA fee PDF **404s** and its fee page is a JS shell. VUB itself warns fees *"are subject to potential changes, in light of the budgetary proposals put forward by the Flemish Government"* |
| **UHasselt** | — | **NOT VERIFIED** |

**Correction to a premise in my brief:** Flemish non-EU tuition is **not**
reliably lower than Wallonia's. UAntwerpen at €7,800 and KU Leuven's upper bands
at €9,494 are **substantially more expensive than FWB's flat €5,369.** Only
UGent's lower band and possibly VUB undercut Wallonia. **On price, French Belgium
wins** — which reinforces rather than complicates the recommendation.

### 5.2 KU Leuven — MSc Business Administration (Brussels)

| Field | Value |
|---|---|
| Degree + ECTS | **Master of Science in Business Administration — 60 ECTS**, 1 year, Brussels campus |
| Institution type | Public university (FEB — Faculty of Economics and Business) |
| Direction match | **2** — specialisation tracks include **International Marketing Management** and **Strategic Marketing Management** (alongside Strategic Accounting and Management, Business Information Management, Corporate Finance) |
| Language | **English** → **Tier A** on language, **but he has no English certificate** |
| Non-EU tuition | Band unknown; **€5,613–€9,494** range (see 5.1) |
| Entry requirement | For non-Flemish diplomas: *"an accredited academic bachelor's or master's degree in the field of economics or business"*, equivalence assessed on *"a solid background in economics, mathematics, statistics, research methods and management courses and projects"*. Files are evaluated jointly by the admissions office **and the programme directors** |
| **Bridging route — worth noting** | KU Leuven publishes a **"Preparatory Programme: Master of Business Administration (Brussels)"** (`onderwijsaanbod.kuleuven.be/opleidingen/e/CQ_51964272.htm`). Unlike a Dutch pre-master, a Flemish *voorbereidingsprogramma* is a normal enrolment — **so the Utrecht/UvA visa problem does not transfer to Flanders.** ⚠️ Its content, length, fee and whether it independently supports a student visa are **NOT VERIFIED** |
| **146 ECTS verdict** | **BORDERLINE.** The wording is about *field and background*, not a literal credit count — no "180 ECTS" appears. That is favourable. The maths/statistics expectation is the likelier friction for a marketing licence |
| URLs | https://www.kuleuven.be/programmes/master-business-administration/brussels · https://onderwijsaanbod.kuleuven.be/opleidingen/e/SC_54542934/diploma_omschrijving · fees: https://www.kuleuven.be/english/education/student/fees/tuition-fee-breakdown |

### 5.3 UGent — Master of Marketing Analysis: **CONFIRMED BLOCKING**

2G flagged a "4 years of prior study" rule from a search extract and warned it
was unverified but fatal. **It is worse than that, and it is now confirmed.**
UGent's own study-chooser record classifies MMA as an **"MASTER IN MARKETING
ANALYSIS (ADVANCED MASTER)"** — a *master-na-master*. Applicants *"should have
obtained both a bachelor and master degree before applying… or alternatively,
graduates from a 4-year bachelor degree may also apply."* Holders of a Flemish
master or a **minimum-4-year** higher-education degree are then invited to an
**admission test** covering marketing, marketing research, basic statistics and
English.

**Verdict: BLOCKING on two independent grounds** — he holds neither a master nor
a 4-year bachelor, and the FSEG attestation cannot manufacture a fourth year or a
second degree. **Remove UGent MMA from consideration.** It was the purest
direction-1 content fit in Benelux; it is not available to him.
Source: https://studiekiezer.ugent.be/printfichescan/98791263 · https://mma.ugent.be/

### 5.4 Flemish hogescholen — a structural empty result

**The Flemish *hogescholen* do not offer business or marketing master's degrees.**
Since the 2013 *integratie*, academic master programmes moved from the hogescholen
to the associated universities; hogescholen retain **professional bachelors** and
**bachelor-na-bachelor** programmes, with master's retained only in the **arts**
(conservatoires, academies) and, in some cases, teaching.

Checked: **Artevelde, Odisee, Thomas More, AP Hogeschool, PXL, VIVES.**
- **AP Hogeschool** does list 9 masters — these are the **Royal Conservatoire and
  Royal Academy of Antwerp** arts masters (music performance, composition, visual
  arts). A *Master of Music* is a **performance degree requiring audition and
  portfolio**. Per the shared brief he is a **self-taught hobbyist with no
  portfolio** — these are **not accessible** and are recorded here only so nobody
  re-discovers them and misreads them as a music-business route.
- **PXL "Muziekmanagement"** is a **specialisation inside the professional
  bachelor Pop- en rockmuziek** — a bachelor, out of scope.
- **VIVES "Cultuurmanagement"** is likewise a **bachelor**.
- Artevelde, Odisee, Thomas More: **no relevant master found.**

**Only university-level option in the culture/creative space:** **UAntwerpen
Master Cultuurmanagement** — described by UAntwerpen as *"the only master-level
culture management programme in Flanders"*. **Dutch-taught → Tier C** for him
(Dutch to B2/C1 from a French/Arabic base is a 12–24-month commitment, per the
brief's category logic). At €7,800 non-EEA and in a language he does not have,
this is not a serious contender, but it is the honest Flemish answer to
directions 3–4.

---

## 6. TASK 4 — NETHERLANDS, HBO BRANCH (*Licence Appliquée* only)

**Framing unchanged from 2G:** this entire section is live **only if he holds a
*Licence Appliquée*** (Nuffic: 3 years of HBO). On the *Fondamentale* branch
(2 years of WO) everything below closes, and the pre-master workaround is barred
by the visa rules 2G verified. **Resolve the licence type before spending money
here.** All of these are direct master entries, so **no pre-master and therefore
no pre-master visa problem.**

| Institution | Programme | Degree / length | Language | **Non-EU tuition** | Entry / notes | Status |
|---|---|---|---|---|---|---|
| **AUAS / HvA** (Amsterdam) | **Master Digital Driven Business** | **MSc**, 1 yr, full-time | English → Tier A | **€10,648** | Best *content* fit in Benelux (2G): digital business + Marketing specialisation | Fee **VERIFIED by 2G** on AUAS's 2026-27 institutional-fee page |
| **AUAS / HvA** | Master Applied Artificial Intelligence | hbo-master, 1 yr | **Dutch only** → **Tier C** | not obtained | Direction 1 on content, closed on language | Language **VERIFIED** |
| **Rotterdam UAS** | **Master in Consultancy and Entrepreneurship** (full-time) | Master, **1 year** | English → Tier A | **€14,449** (institutional fee, 2026-27) | *"A business related Bachelor Degree"* — **he qualifies with no work experience**; non-business backgrounds need 2 yrs. **IELTS Academic 6.5 / TOEFL iBT 90 / CAE 180-184**, results **<2 years old**, **no home/online editions**. **Deadline 1 April** (fall intake); 1 October (spring) | **VERIFIED** on both official pages |
| **NHL Stenden** (Leeuwarden) | **Master International Leisure, Tourism & Events Management** | **MA** | English → Tier A | **€11,995/yr** | **Nearest thing in NL to entertainment/events marketing** — direction 3–4 adjacent. **Non-EU deadline 31 May** | Fee + deadline from the official fees-and-admissions page via firecrawl; **re-confirm before relying** |
| **Saxion** (Enschede/Deventer) | Masters generally; **MBA is part-time** | 12 months | English | **€13,644** (Sept 2026 intake; €13,200 in 2025) | ⚠️ **The MBA is a *parttime* programme** — part-time study does **not** support a Dutch student residence permit. Check format before applying | Fee **VERIFIED** on saxion.edu total-costs |
| **THUAS / The Hague** | Master International Communication Management | MA, 2 yrs | English | **€19,700** | **EXCLUDED on two filters at once**: above the €15,000 ceiling **and** requires *"two years of professional work experience"*, which he does not have | Recorded so it is not re-researched |
| **Breda UAS (BUas)** | Master **Media Innovation**; also Imagineering, Strategic Events Management, Tourism Destination Management, Games | 1 yr | English | **NOT VERIFIED** — calculator only | Media Innovation entry: *"a bachelor's degree… in Business Administration, Media Studies, Communication Studies, IT, or another media-related field"* — **a marketing licence plausibly qualifies**. **Scholarship: €3,000 off year 1, €1,500 off subsequent years**, limited number, non-EU/EEA | Worth one follow-up: fee + scholarship could land it near €8–10k |
| **Fontys, Avans, HAN, Windesheim** | — | — | — | Fontys institutional fee is set per programme (bachelor IB is €6,500) | **No English-taught HBO master in marketing, digital business or data-driven business found at any of the four.** Explicit empty result | Not found |

**Dutch HBO ranking by cost, verified figures only:**
**AUAS €10,648 → NHL Stenden €11,995 → Saxion €13,644 → Rotterdam UAS €14,449 →
THUAS €19,700 (excluded).** Everything except AUAS breaches the brief's €8,000
preference; everything except THUAS stays under the €15,000 hard ceiling. **AUAS's
Digital Driven Business remains the only Dutch option that is both affordable-ish
and a genuine content match.**

**Statutory EU rate for reference (verified):** €2,694 for 2026-27 — the gap
between that and €10,648–€14,449 is exactly what non-EEA status costs in NL.

---

## 7. Stretch options

1. **KU Leuven MSc Business Administration (Brussels)** — Tier A English, real
   marketing tracks, credit wording is qualitative rather than a literal 180, and
   a **preparatory programme** exists as an in-country bridge. Fails on: fee band
   unknown (up to €9,494), maths/statistics expectation, and an English
   certificate he does not hold. Worth a fee-tool query and an email.
2. **Breda UAS Master Media Innovation** — entry wording explicitly admits
   business-administration and communication bachelors, and the **€3,000/€1,500
   scholarship** could bring it into range. Blocked only by an unverified fee.
3. **HELHa Master en communication stratégique (Mons)** — €5,369-band applied
   master in strategic communication. Blocked on format risk: evening/alternance
   delivery may not support a student visa.
4. **University of Luxembourg, Master in Entrepreneurship & Innovation** — €8,000
   total, trilingual country, strong labour market. Blocked on a literal, thrice-
   stated 180 ECTS with **no complementary-credit fallback**, plus English C1.

---

## 8. Explicit empty results (per §7 of the shared brief)

- **Music-specific master's in Benelux: ZERO.** Confirmed across Belgium (both
  communities), Luxembourg and the Netherlands. 2G's finding stands and is now
  better evidenced: Luxembourg's only music provision is a bachelor; Flanders'
  only "muziekmanagement" is a bachelor specialisation; AP Antwerp's music masters
  are audition-based performance degrees he cannot access.
- **Marketing master at the University of Luxembourg: does not exist.**
- **Communication/media master at the University of Luxembourg: does not exist.**
- **Marketing master at any French-speaking *haute école* other than ICHEC/IHECS:
  does not exist.**
- **Business/marketing master at any Flemish *hogeschool*: does not exist**
  (structural — they are not permitted to award them outside the arts).
- **English-taught HBO master in marketing/digital business at Fontys, Avans, HAN
  or Windesheim: none found.**

---

## 9. Sources (all checked 2026-08-17)

**Luxembourg**
- https://www.uni.lu/en/admissions/bachelor-master/ — 2027-28 opening date, €100 fee, language rule, criminal-record advice
- https://www.uni.lu/fdef-en/study-programs/master-in-entrepreneurship-and-innovation/admissions/ — 120 ECTS, fees, 180-ECTS wording, English C1
- https://www.uni.lu/fstm-en/study-programs/master-in-data-science/admissions/ — €400/sem, maths prerequisites
- uni.lu site map (firecrawl, `--proxy auto`) filtered on master / marketing / management / data / communication-culture-media-music — full programme inventory

**Belgium — Wallonia-Brussels**
- https://uclouvain.be/prog-2026-gest2m-cond_adm — 60-credit complementary cap, prerequisite-analysis email route
- https://www.unamur.be/en/registration/international/masters — deadlines by visa status, €200 fee, no-equivalence-needed
- https://www.unamur.be/en/registration/international/hue/masters-conditions · https://www.unamur.be/en/registration/international/fees — €5,369, TCF/DELF/DALF
- https://web.umons.ac.be/fweg/en/study-programmes/2eme-cycle-master/ · https://webcontent.umons.ac.be/web/fr/pde/2025-2026/cursus/MGT1_S208.htm
- https://web.umons.ac.be/app/uploads/2025/01/Faculte-Warocque-economie-et-gestion-Master-HUE.pdf — non-EU conditions (**tool-blocked; search extract only**)
- https://www.ihecs.be/fr/master-en-publicite/specialisation-et-identite-professionnelle · https://www.ihecs.be/fr/s-inscrire-en-master/droits-d-inscription
- https://www.helha.be/faire-un-master-a-la-helha-cest-possible/ — HELHa master inventory
- https://www.hepl.be/fr/gestion-publique · https://www.ephec.be/formations/haute-ecole
- https://www.studyinbelgium.be/en/french-speaking-university-colleges-belgium — 19 hautes écoles, 2-cycle structure

**Belgium — Flanders**
- https://www.kuleuven.be/english/education/student/fees/tuition-fee-breakdown — four non-EEA bands
- https://onderwijsaanbod.kuleuven.be/opleidingen/e/SC_54542934/diploma_omschrijving — MSc Business Administration Brussels, 60 ECTS, marketing tracks
- https://onderwijsaanbod.kuleuven.be/opleidingen/e/CQ_51964272.htm — preparatory programme
- https://www.uantwerpen.be/en/study/admission-and-enrolment/enrolment/tuition-fees/tuition-fees-2026-2027/ — €1,500 + €105/credit
- https://studiekiezer.ugent.be/printfichescan/98791263 · https://mma.ugent.be/ — MMA is an **advanced master**
- https://www.uantwerpen.be/nl/studeren/aanbod/alle-opleidingen/cultuurmanagement-studeren/ — only culture-management master in Flanders
- https://www.pxl.be/muziekmanagement — bachelor specialisation, not a master
- https://www.vub.be/sites/default/files/2025-07/2025_Studiegeld_tarieven_NEER_2627_ENG.pdf — **404, fee NOT VERIFIED**

**Netherlands**
- https://www.rotterdamuas.com/programmes/master/master-in-consultancy-and-entrepreneurship-fulltime/programme-costs/ — €14,449
- https://www.rotterdamuas.com/programmes/master/master-in-consultancy-and-entrepreneurship-fulltime/admission-requirements/ — entry, IELTS 6.5, 1 April
- https://www.nhlstenden.com/en/courses/international-leisure-tourism-and-events-ma/fees-and-admissions — €11,995, 31 May
- https://www.saxion.edu/studying-in-the-netherlands/finance-your-studies/total-costs — €13,644 master, €2,694 statutory
- https://www.amsterdamuas.com/programmes/master-digital-driven-business · https://www.hva.nl/opleidingen/master-applied-artificial-intelligence (Dutch-taught)
- https://www.buas.nl/en/study-costs — calculator only, fees NOT VERIFIED
- https://www.thehagueuniversity.com/programmes/masters/master-in-international-communication-management-part-time/before-the-programme — 2 yrs' work experience
