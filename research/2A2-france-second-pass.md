# 2A-2 — FRANCE, SECOND PASS

**Agent 2A-2 · scope: the three gaps 2A declared · all checked 2026-08-17**
**Target intake: AUTUMN 2027 = French academic year 2027/2028.**
**This file SUPPLEMENTS `2A-france.md`. It does not repeat 2A's 16 verified programmes.**

---

## 1. Bottom line

Three gaps closed, and one of them changes a project-wide number. **(a)** The IAE
sweep found **nine new Direction-1/2 programmes with a genuine M1 entry from a
licence**, of which the strongest are **iaelyon (Lyon 3) Master Marketing-Vente**
(explicitly a *relation client* degree — the closest thing in France to a CRM
master's that admits at M1 in formation initiale), **IGR-IAE Rennes M1 Marketing**
(formation initiale only, no apprenticeship trap) and **IAE Aix MSc 1 Management**
(180-ECTS entry stated for international candidates, English track available).
The sweep also exposed a **second structural trap alongside the M2-only one: the
alternance-only trap.** France's best CRM and digital-marketing parcours —
IAE Lille SMRC/MBX, IAE Caen Digital–Social Media, IAE Angers M2 Marketing
Digital, Paris-Saclay MRC — are apprenticeship-contract-mandatory, which a
candidate applying from Tunisia cannot satisfy. **Filtering for "M1 entry" alone
is not enough; the filter is "M1 entry AND formation initiale."** **(b)** The
*Mastère Spécialisé* question is now answered definitively and negatively:
**no MS is accessible to him, structurally.** The CGE label requires **Bac+5**
entry (or Bac+4 plus three years' professional experience); he holds Bac+3, so
every MS in France is out of reach regardless of subject — the APS question never
arises. **(c)** Cost of living is now sourced, and in the process I found a
change nobody in this project has: **the visa financial-resources threshold rose
from €615 to €877.50 per month on 1 August 2026** (décret n° 2026-526 of
22 June 2026), indexed to 47 % of gross SMIC and revised annually. For an autumn
2027 entry he will have to prove **at least €877.50/month ≈ €10,530/year** on top
of tuition, and probably more once the annual indexation applies. That is the
single largest financial fact in the France file and it dwarfs the tuition
question.

---

## 2. Coverage statement — what I searched, and what I found nothing on

**Languages:** French throughout for discovery; English only for IAE Aix and TSM
international pages.

**Method that worked, and is worth reusing:** the ministry open-data API at
`data.enseignementsup-recherche.gouv.fr`, dataset
`fr-esr-tmm-donnees-du-portail-dinformation-trouver-mon-master-parcours-de-format`
(the archived *Trouver Mon Master* catalogue). The Explore v2.1 API answers
unauthenticated GET. Working query form:

```
GET /api/explore/v2.1/catalog/datasets/<dataset>/records
    ?where=search(parc_intitule,"relation client")&limit=100
    &select=etab_nom,etab_ville,for_intitule,parc_intitule,for_lien_fiche
```

Note for whoever uses it next: the `like` operator is **not** supported and
silently returns `total_count: 0` — filter in post-processing instead. Records
are 2019–2021 and **every hit below was re-verified on the live institutional
page**; several had moved, been renamed, or switched to alternance since.

**Also used:** `iae-france.fr` (the IAE network's own catalogue — 30 IAEs, 106
pages of formations, facets for level/domain/admission/format; it is the single
best discovery tool for this student and 2A did not have it), individual IAE and
university pages, `cge.asso.fr`, `service-public.gouv.fr`,
`pantheonsorbonne.fr`, Campus France country sites, and the UNEF 2025
cost-of-living survey PDF.

**Still blocked:** `campusfrance.org/fr/droits-differencies` (403),
`france-visas.gouv.fr` (firecrawl reached the site but the student page returns a
404 asset — the page has moved), `iae-bordeaux.fr` (503 on two attempts),
`cge.asso.fr` MS programme directory (the label page exists; a searchable list of
accredited MS programmes is **not** published on the CGE site).

**What I found NOTHING on — stated explicitly:**
- **No CGE-accredited *Mastère Spécialisé* in music business, music marketing or
  the creative industries.** More importantly this is moot — see §4.
- **No public French university master's in "growth marketing"** — confirms 2A.
- **No CRM/relation-client master's that is simultaneously M1-entry AND formation
  initiale AND explicitly CRM-titled.** The closest is iaelyon, whose *mention*
  is Marketing-Vente but whose stated purpose is training *"spécialistes de la
  relation client"*. Every explicitly CRM-titled parcours I found (Lille SMRC,
  Caen, Paris-Saclay MRC, Clermont RMREC, Toulon cross-canal) is either
  alternance-only or M2-only. **This is a real and slightly disappointing
  finding given his CRM project, and it should be reported to him honestly.**
- **No per-city official government cost-of-living table.** France does not
  publish one. The UNEF survey is the standard reference and I have used it with
  its methodology stated — see §5.

---

## 3. NEW programmes — Directions 1 and 2

All are **Tier A** (French, or French/English). All are **public universities**:
diplôme national de master, 120 ECTS over M1+M2, ECTS-bearing, state-recognised,
student visa and full APS rights. **GMAT/GRE: not required anywhere** (accepted as
an optional alternative to the Score IAE-Message at several).
**Tuition unless stated:** the non-EU differentiated rate, **€3,950/yr + €105
CVEC** (see §6 for the corrected figures and the €2,633 answer).
**Application route: Études en France**, campaign ~1 Oct 2026 – ~15 Jan 2027.
**146-ECTS verdict for every programme in this section: `BORDERLINE`** — each
states 180 ECTS or "grade licence" explicitly, so the FSEG attestation plus the
*supplément au diplôme* is required in the dossier. None of them phrase it as
"three years of study", which would have been the easier wording.

### 3A. TIER 1 — M1 entry **and** formation initiale available (the only genuinely usable group)

#### N1. Master Marketing, Vente — **iaelyon School of Management (Université Jean Moulin Lyon 3)** · Lyon · ★ BEST NEW FIND
- **Direction:** 2, with a strong Direction-1/CRM overlap. The programme's own
  stated object is to train *"spécialistes de la relation client"* across
  marketing, sales and communication — the nearest French M1-entry equivalent to
  a CRM master's.
- **Entry point: M1.** Verbatim: *"licence ou équivalent (180 crédits)."*
- **Admission:** dossier + **Score IAE-Message (SIM)**; international candidates
  may substitute **TAGE MAGE or GMAT**. A Tunis SIM centre exists (resolved by
  the previous run) plus a remote option, so this gate is passable.
- **Format:** formation initiale **and** alternance — the FI track is the one to
  target. A Bourg-en-Bresse campus runs an alternance-only variant; avoid it.
- **Language:** French. **No French test dispense published — assume TCF required.**
- **Contact for FI:** iae-master.marketingvente@univ-lyon3.fr
- **URL:** https://iae.univ-lyon3.fr/master-marketing-vente-4 · checked 2026-08-17
- **Note:** Lyon is now in UNEF's ten most expensive student cities (§5). Weigh
  the programme fit against ~€1,324/month.

#### N2. M1 Marketing (FI) → Master Marketing, Vente — **IGR-IAE Rennes (Université de Rennes)** · Rennes
- **Direction:** 2. M1 trains in *"digital marketing, branding and marketing
  intelligence"*; M2 splits into *Management & Développement de Projets
  Marketing* and *Conseil, Études & Recherche Marketing*.
- **Entry point: M1.** Verbatim: *"diplôme de grade Licence (180 crédits ECTS)."*
- **Admission:** dossier + **Score IAE-Message (mandatory)** + interview.
- **Format: formation initiale only — no alternance pathway.** This is the single
  most important line in this report for him: it means **no apprenticeship
  contract is needed**, which removes the trap that kills Lille, Caen and Angers'
  digital M2. Internships of 2–4 months instead.
- **Capacity:** 30 places. **Language:** French; English B2 expected, business
  English taught in-programme.
- **Deadlines (2026 cycle, indicative for 2027):** last SIM sitting 17 Feb 2026
  (Rennes) / 24 Feb 2026 (national); portal opens 17 Feb 2026; **applications
  close 16 Mar 2026**; interviews 18–21 May 2026; start 4 Sep 2026.
  **Note the SIM must be sat BEFORE the application window closes.**
- **Fee shown on the page: €254/yr** — that is the *national* rate, not the
  differentiated one. `NOT VERIFIED whether IGR applies droits différenciés` —
  ask directly; if it does not, this becomes by far the cheapest option in the file.
- **URL:** https://www.igr.univ-rennes.fr/fr/formation/fi-master-1-marketing-recherche/ · checked 2026-08-17

#### N3. MSc 1 Management → MSc 2 Marketing & Brand Management — **IAE Aix-Marseille (Aix-Marseille Université)** · Aix-en-Provence
- **Direction:** 2 (brand management). **Entry point: M1.**
- **Entry wording:** *"180 ECTS obtained as part of a Bachelor's degree or a
  European diploma"*, and — unusually explicit and helpful — admission is
  *"also possible for international students holding a diploma equivalent in
  level (Bac+3) **or credits**"*. **That "or credits" wording is the most
  146-ECTS-friendly phrasing I found anywhere in France.** Verdict upgraded to
  `LIKELY OK` for this one programme.
- **Language:** M1 in **French or English** (student chooses the track); four of
  the ten MSc 2 specialisations are taught **entirely in English**, including
  Marketing & Brand Management. An English track means he could bypass the
  French-certificate question entirely — but then an English test appears instead
  (TOEFL/TOEIC/IELTS/Duolingo accepted). **He should pick the French track.**
- **Admission:** management aptitude test — TAGE MAGE, Score IAE-Message, GMAT or
  GRE. Online application on the school's site.
- **Tuition: €8,400 for the two-year MSc (€4,200/yr) at the student rate.**
  This is a school-specific programme fee. `NOT VERIFIED whether the non-EU
  differentiated right is charged on top or is replaced by it — ask, because the
  answer is a ~€4,000/yr swing.` Band 2 either way.
- **URL:** https://iae-aix.univ-amu.fr/en/programs/organization-msc/msc-1-management · checked 2026-08-17
- **Cost note:** Aix rent €603/month, above the provincial average.

#### N4. Master Marketing Digital (MKT) — **IAE Nice (Université Côte d'Azur)** · Nice
- **Direction:** 2. **Entry point: M1.** Entry requires a bac+3-level diploma with
  **a minimum of 180 ECTS**.
- **Admission:** an entrance test is **required for every national degree at IAE
  Nice** except the MAE mention — SIM, TAGE MAGE, GMAT, GRE or SAT are all
  accepted, and, valuably, **there is no eliminating minimum score.** For a
  12–13/20 student a no-floor test is materially better than a scored gate.
  Then dossier review and an interview before a jury of academics and
  practitioners — the interview format favours his CRM project.
- **Capacity:** 30 in M1, 35 in M2.
- **URLs:** https://iae.univ-cotedazur.fr/formations/je-postule-en-master-1-1 ·
  https://univ-cotedazur.fr/formation/offre-de-formation/parcours-de-master/marketing-et-digital-mkt · checked 2026-08-17
- **Serious cost caveat:** UNEF ranks **Nice the most expensive city in France
  outside Île-de-France** — rent €675/month, total ~€1,370/month. This programme
  is a good fit and a bad city; flag the trade-off rather than the programme.

#### N5. M1 Marketing → M2 Marketing digital et e-commerce / Marketing digital et consommateur connecté / Communication marketing et digitale — **Grenoble IAE-INP (Université Grenoble Alpes)** · Grenoble
- **Direction:** 2, with three digital M2 exits from one M1 — the widest digital
  choice from a single M1 entry that I found.
- **Entry point: M1**, open to holders of a bachelor's degree *"delivered by a
  European university or equivalent diploma."* The word *equivalent* carries the
  Tunisian licence; still `BORDERLINE`.
- **Format:** M1 formation initiale on the Grenoble campus, 450 hours.
- **Condition worth knowing before he commits:** FI students entering M1 **without
  prior international experience must complete an internship abroad.** For a
  Tunisian student already on a French student visa this is an administrative
  complication (a second mobility), not a blocker — but it should not be a surprise.
- **URL:** https://iae.grenoble-inp.fr/fr/nos-formations/master-1-marketing · checked 2026-08-17

#### N6. M1 Marketing (FI) → M2 Digital Marketing / Data & Innovation Marketing — **Toulouse School of Management (Université Toulouse Capitole)** · Toulouse
- **Directions 1 and 2 from one M1.** The *Data & Innovation Marketing* M2 is a
  Direction-1 target; *Digital Marketing* is Direction 2.
- **Entry point: M1**, level required **Bac+3**. (Several aggregator pages state
  "240 ECTS / bac+4" — that is the **M2** requirement being mis-attributed; the
  M1 page states bac+3. Do not let that error propagate.)
- **Format:** formation initiale, two semesters. An alternance M1 exists
  separately — target the FI one.
- **Language: French/English.** **Selection rate 28 %** — the tightest in this
  section and the one place where 12–13/20 is most at risk. Treat as a reach.
- **Contact:** m1.marketing@tsm-education.fr
- **URL:** https://tsm-education.fr/formations/masters/marketing/parcours-marketing-m1-fi · checked 2026-08-17
- **Cost:** Toulouse rent €521/month, ~€1,215/month total — among the cheapest
  large student cities. Good value if he clears the selectivity.

#### N7. Master Études et Actions Marketing (EAM) — **IAE Nantes (Nantes Université)** · Nantes
- **Direction:** 2 (studies/insight-led marketing). **Entry point: M1**, requiring
  an L3 in *sciences de gestion* or equivalent (économie-gestion, MASS).
- **Admission: Score IAE-Message mandatory** — and usefully, **IAE Nantes is
  itself an official SIM test centre**, so sitting and applying can be co-ordinated.
  Selection weighs the SIM heavily alongside licence marks, CV and motivation letter.
- **Format:** formation initiale and alternance both offered; international
  mobility possible.
- **URLs:** https://iae.univ-nantes.fr/nos-formations/offre-de-formation/master-etudes-et-actions-marketing ·
  https://iae.univ-nantes.fr/score-iae-message · checked 2026-08-17
- **Deadlines:** `NOT VERIFIED — check directly.`

#### N8. Master Marketing, Vente — **IAE Angers (Université d'Angers)** · Angers · **read the M2 warning**
- **Direction:** 2, with a Direction-1 module. **Entry point: M1**, requiring a
  **bac+3 in economics and/or management** — his licence is squarely on the list.
- **Why it looked like the best find and is not:** the **M1 is formation initiale**
  and its content is almost tailored to him — *relation client* fundamentals plus
  digital marketing, social media and search marketing, 8-week minimum internship,
  and a practical WordPress site-management assignment. The M2 *Marketing Digital*
  even contains a dedicated **"IA et marketing digital"** unit, making it a
  genuine D1/D2 hybrid.
- **The trap:** of the three M2 exits, **two (Marketing Digital, and Chef de
  Produit Responsable) are alternance-only.** The only formation-initiale M2 is
  *Pricing & Revenue Management*, which is not his direction. **So he can enter
  M1 but cannot reach the digital M2 without an apprenticeship contract.**
  Record as **M1 usable, M2 blocked** — and note he could apply out to a
  different institution's M2 after the M1.
- **Applications (2026 cycle):** via monmaster.gouv.fr, 17 Feb – 16 Mar 2026 —
  **but his route is Études en France, which closes earlier.**
- **URL:** https://iae.univ-angers.fr/fr/formations/offre/master-lmd-MLMD/droit-economie-gestion-DEG/master-marketing-vente-KV215ZXU.html · checked 2026-08-17
- **Cost warning:** Angers had the **second-largest rent rise in France outside
  Île-de-France in 2025 (+7 % / +8.01 %)**.

#### N9. Master Marketing Stratégique · Master Marketing et Communication — **IAE Bordeaux (Université de Bordeaux)** · Bordeaux
- **Direction:** 2. M1 is described as generalist across marketing and
  communication, implying **M1 entry**.
- **`NOT VERIFIED — check directly.` The site returned HTTP 503 on two attempts.**
  URLs where the detail should appear:
  https://www.iae-bordeaux.fr/programmes/etudiants-apprentis/masters-formation-initiale/master-marketing-strategique
  and `.../master-communication` · attempted 2026-08-17.
- Note the section path is literally *masters-formation-initiale*, which is a
  good sign for the alternance question.

---

### 3B. TIER 2 — M1 entry exists but **alternance-contract mandatory** (record, then exclude)

**This group is the second structural trap and it is as costly as the M2-only
one.** Each admits at M1 from a licence — which is exactly what he needs — but
requires a signed French apprenticeship or professionalisation contract *before
enrolment*, which a candidate applying from Tunisia without a visa cannot obtain.
Tuition is zero in these programmes, which is precisely why they look attractive
and precisely why he must not build a plan around them.

| Institution | Programme | Entry | Why excluded |
|---|---|---|---|
| **IAE Lille** (Univ. de Lille) | M1 Stratégie Marketing et Relation Client (SMRC) → M2 Branding et Expérience Client (MBX) | M1 from L3/bac+3, verbatim *"ayant validé une Licence 3 / bac+3 (pour le M1)"* | **Alternance exclusively**, 2 weeks company / 1 week IAE, 14 weeks on site. 60 places. Selection: dossier then interview; **SIM optional**, which would otherwise have been a real advantage. M2 sessions (2026): 6–16 Mar, results 6 May; 27 Apr–11 May, results 27 Jun. Contact master-mbx@iaelille.fr |
| **IAE Caen** (Univ. de Caen Normandie) | Master Marketing-Vente : Digital – Social Media | M1 from a 180-ECTS management bachelor's; M2 from an M1 | **"Être titulaire d'un contrat d'apprentissage ou contrat pro (à l'entrée en formation)"** — explicit and absolute. 120 ECTS / 855 h. Content would otherwise make it a top D1/D2 hybrid: digital strategy, social media, **AI and data management**, e-commerce, UX, SEO/SEM, analytics. M1 window 17 Feb – 16 Mar 2026; M2 9 Feb – 24 Apr 2026 |
| **ISM-IAE Versailles / UVSQ (Université Paris-Saclay)** | M1 Management de la Relation Client, Qualité et Digitalisation (MRC) | **M1 entry exists** | Structured around apprenticeship — **but the page also lists *formation initiale* among accepted formats.** This is the one exception worth an email: an FI place here would be the best CRM fit in France. 30 places; applications 15 Jan – 16 Mar 2026 via the Inception platform; start 31 Aug 2026; French-taught; **English B1 with a TOEIC score required**. Curriculum is explicitly CRM tools + quality + digital transformation. **`ACTION: email admissions to ask whether an FI place is open to an Études en France candidate.`** |
| **IAE Angers** | M2 Marketing Digital; M2 Chef de Produit Responsable | M2 | Alternance-only (see N8) |

### 3C. TIER 3 — M2-only entry (confirms and extends 2A's finding)

He holds Bac+3. These presume Bac+4 / 240 ECTS and are **BLOCKING** at entry:

- **Université Paris-Saclay / UVSQ — M2 Management de la Relation Client, Digital
  et Qualité (MRC).** Direct M2 entry is offered but presumes a completed M1 plus
  a 12-month apprenticeship mission. Applications 30 Jan – 30 May 2026.
- **TSM Toulouse — M2 Digital Marketing, M2 Marketing & Communication, M2
  Management Marketing.** M2 entry requires **240 ECTS / bac+4**.
- **IAE Clermont Auvergne (Université Clermont Auvergne) — M2 Marketing-Vente
  parcours Retail Management, Relation et Expérience Client (RMREC).** A strong
  CRM/retail fit, reachable only after an M1 elsewhere.
- **IAE Poitiers — M2 Marketing (formation à distance).** Note separately that
  **IAE Poitiers requires the Score IAE-Message for M1 admission across the board**
  (except M1 Communication), with the L3-holder window 4 May – 5 Jun 2026 on
  eCandidat — a later window than most, worth remembering.
- **IAE Aix — MSc 2 Marketing & Brand Management** direct entry requires an M1 or
  **240 ECTS**. Enter at MSc 1 instead (N3).

### 3D. Discovered, real, but NOT individually verified

Surfaced through the ministry dataset and confirmed to exist as programmes; entry
point, format and fees unconfirmed. `NOT VERIFIED — check directly.`

- **Université de Toulon — Marketing, vente parcours Marketing Cross-Canal et
  Relation Client.** A CRM-titled parcours; Toulon is also cheap (rent €498).
  Worth a look precisely because it is under-applied-to.
- **Université de Haute-Alsace / UHA Business School (Mulhouse–Colmar)** — the
  dataset's *Marketing et Relations Clients (MRC)* parcours **no longer appears**
  in the live catalogue; current masters are IASD, MIFER, METOMA, Marketing
  International, and M1 CADRE². Treat the old CRM listing as **defunct**.
- **Cnam Paris** — *E-business et marketing*; *Marketing dans un monde digitalisé*.
- **Université de Lorraine (Nancy)** — Marketing, vente parcours Marketing digital.
- **Université Paris-Est Créteil (IAE Paris-Est)** — Marketing digital.
- **IAE Dijon (Université Bourgogne Europe)** — M2 Marketing Digital.
  https://iae.ube.fr/nos-masters-2/marketing-digital/
- **Université de Tours** — Marketing des services et Digital (2A verified a
  different Tours parcours).
- **Université Clermont Auvergne** — Marketing opérationnel et digital.
- **Université de La Rochelle** — Marketing digital (2A verified; not recommended).

**IAEs I could not reach at all in this pass:** Metz, Amiens, Orléans, Limoges,
Perpignan, Pau, Savoie Mont Blanc, Gustave Eiffel, Brest, Valenciennes. **The
network catalogue at https://www.iae-france.fr/formations/ (facets: IAE, niveau,
domaine "Marketing – Communication – Vente", admission, format) is the right tool
to finish the job — 106 pages, and it exposes the *format* facet, which is the
one that separates the usable programmes from the alternance mirages.**

---

## 4. The *Mastère Spécialisé* question — ANSWERED, and the answer is NO

**Verdict: no Mastère Spécialisé in France is accessible to this student, and the
reason is structural rather than subject-related. This closes the question; it
does not need another pass.**

**The blocking fact — CGE's own wording:** an MS is
*"accessible après un diplôme validé Bac+5 (Titre ingénieur, diplômés M2, titre
RNCP niveau 7) ou un diplôme validé M1 mais associé à 3 ans minimum d'expérience
professionnelle."*

He holds a **Bac+3 licence with no professional experience**. He therefore fails
both admission routes. **Every MS in France is out of reach for him — the
marketing ones, the data ones, the music ones, all of them.** An MS is a
*post-master's* qualification; it was never the tier he was shopping in.
**Consequence: the APS question does not arise for MS programmes at all.** He
would need to complete a French master's first, at which point an MS becomes a
possible *later* step — worth saying to him as a career note, not an application option.

**What the MS actually is, for the file:**
- It is a **collective trademark of the Conférence des Grandes Écoles**,
  registered at INPI and EUIPO since 1983 — **not a diplôme national**.
- It **does not confer the *grade de master***. This is the distinction the brief
  asked about, and it is decisive: a *master* is a national diploma carrying the
  grade; a *mastère spécialisé* is a school-delivered label.
- **RNCP registration is not automatic.** CGE accreditation and RNCP-7
  registration are two separate things; a school must apply separately, and doing
  so obliges it to open the qualification to VAE. So "MS" alone tells you nothing
  about RNCP status — it must be checked programme by programme.
- Minimum structural requirement: **at least four months of in-company mission.**
- Sources: https://www.cge.asso.fr/labels-accreditations/mastere-specialise/ ·
  CGE MS Vademecum (PDF, https://www.cge.asso.fr/wp-content/uploads/2023/11/2023-2024-MS_Vademecum.pdf) · checked 2026-08-17

**The MS programmes that do exist in his subjects** — all Bac+5 entry, all
therefore inaccessible, listed so nobody searches for them again: ESSEC MS
Marketing Management et Digital; KEDGE MS Marketing Digital & Data; SKEMA MS
Manager Marketing Data et Commerce Électronique (RNCP-7); NEOMA MS/MSc Marketing
& Data Analytics (RNCP-7); IÉSEG Executive MS Direction Marketing et Digital.
Several are *Executive* programmes, which adds a work-experience requirement on
top. **No CGE MS in music business or the music industry was found.**

**A trademark warning that matters for the private-school options in 2A's file.**
Schools outside the CGE use the words *"Mastère Spécialisé"* without holding the
label. **ESART Paris** advertises a *"Mastère Spécialisé Management de la
Musique"*; ESART is not a CGE member, and its qualification rests on **RNCP fiche
n° 35800, whose validity is shown as expiring 31 August 2026.** An expiring RNCP
fiche is a genuine risk — if it lapses and is not renewed, the qualification's
legal recognition, and with it any residence-permit consequence, changes under
him mid-course. **`Do not shortlist ESART. If any private "mastère" is
considered, check its RNCP fiche number and expiry date on
francecompetences.fr before applying — the school's own page will not volunteer
an expiry.`** The same check should be applied to ICART, IESA and ESG Nantes in
2A's Directions 3–4. (Agent 3H owns the RNCP-7/APS rule itself.)

---

## 5. Cost of living — the project-wide gap, now closed

### 5.1 The government number that changed — READ THIS FIRST

**The financial-resources threshold for a French student visa rose from €615 to
€877.50 per month on 1 August 2026.** A **43 % increase.**

- **Instrument:** décret n° 2026-526 of 22 June 2026.
- **Applications filed up to 31 July 2026:** assessed at **€615/month**.
- **Applications filed from 1 August 2026:** assessed at **€877.50/month**
  = **€10,530/year**.
- **The threshold is now indexed to 47 % of gross monthly SMIC and revised every
  year.** So the figure he will actually face for an autumn 2027 application is
  **€877.50 as a floor and probably higher**, once the 2027 SMIC revision lands.
  `Re-check the amount in spring 2027 — do not plan on €877.50 exactly.`
- **It applies to residence-permit renewals too**, not just the initial visa:
  a student who entered under the old threshold must justify the threshold in
  force *at the time of renewal*. For a two-year master's, that means proving it
  twice.
- **Exempt:** holders of a French government scholarship funded by the Ministry
  of Europe and Foreign Affairs — the BGF pays ~€900/month, above the new
  threshold. **Co-financed scholarships may fall short and are not automatically
  exempt.** This materially raises the value of a BGF in his case: it clears
  tuition (per 2A) *and* the resource proof in one move.
- **Sources:** https://www.japon.campusfrance.org/fr/modification-du-montant-des-ressources-exigees-pour-les-demandes-de-visa-etudiant-a-compter-du-1er ·
  https://pa.diplomatie.gouv.fr/fr/etudes-en-france-evolution-du-seuil-des-ressources-pour-les-visas-etudiants · checked 2026-08-17

**Planning consequence.** Tuition €4,055 + resources €10,530 means he must
demonstrate roughly **€14,500 for year one**. The resource proof is now nearly
**two and a half times** the tuition. Every earlier discussion in this project
treating French tuition as the affordability question was looking at the smaller
half of the problem.

### 5.2 Per-city monthly cost of living

**Source and its status:** the UNEF *Classement des villes universitaires 2025*
(published Aug 2025, covering academic years 2024-25 and 2025-26, 47 cities).
UNEF is a student union, **not a government body** — but France publishes no
official per-city table, and this survey is the reference cited by AEF, franceinfo
and France Bleu. Rent data comes from LocService.fr (private-market student
rentals). **Method:** a fixed common base (inscription fees, CVEC, catering,
electricity, home insurance, phone, internet, bank charges, medical costs,
mutuelle, food, hygiene, clothing, books, leisure) + city rent + city transport.
https://unef.fr/wp-content/uploads/2025/08/Classement-des-villes-universitaires-2025.pdf · checked 2026-08-17

Rent and transport below are **quoted directly from the survey**. Monthly totals
marked **†** are **derived**, not published: UNEF's provincial fixed base solves
to **€680.15/month**, confirmed against three cities whose totals the survey does
publish (Lyon €1,324, Rennes €1,192, Nice €1,370.15) — all three reproduce to the
euro. The derivation is sound but it is a derivation; say so if it is quoted onward.

| City | Rent/month | Transport/yr | **Total/month** |
|---|---|---|---|
| **Rennes** | €493 (+5.79 %) | €227 | **€1,192** (published) |
| **Nantes** | €511 (stable) | €249 (+1.63 %) | **~€1,212** † |
| **Toulouse** | €521 (+1.36 %) | €162 (+4.85 %) | **~€1,215** † |
| **Lille** | €517 (−1.33 %) | €278.10 (−14.17 %) | **~€1,220** † |
| **Montpellier** | €541 (+1.50 %) | **€0 — transport is free** | **~€1,221** † |
| **Bordeaux** | €589 (+4.80 %) | €249.60 | **~€1,290** † |
| **Lyon** | €623 (+4.18 %) | €250 | **€1,324** (published) |
| **Paris** | €857.47 (+2.56 %) | €392.30 (+2.59 %) | **€1,626.76** (published) |

Reference points: **Nice €675 rent / €1,370 total — the most expensive city
outside Île-de-France**; **Limoges €385 rent / €1,073 total — the cheapest city in
France**; national context — rents rose 2.46–2.75 % in 2025, overall student costs
+4.12 %, **and no French university city now costs under €1,000/month.**

Other cities in 2A's shortlist: **Aix-en-Provence €603 rent**, **La Rochelle €572**,
**Toulon €498**, **Amiens €446**, **Strasbourg €558**, **Marseille €558**.

**Reading it for this student:**
- **Paris costs ~€400/month more than the cheapest regional option — about
  €4,800/year, more than a full year's tuition.** This is the hard number behind
  2A's warning about the Paris-based options (Paris 8, Sorbonne Nouvelle, IESA,
  ICART, EPITA). It is not a marginal preference; it is the largest single
  controllable cost in the plan.
- **Montpellier is the standout on cost structure**, and not because rent is low
  — rent is mid-table — but because **transport is free**, uniquely in France, and
  because 2A's best Direction-2 find (IAE Montpellier M1 e-Marketing, interview-
  based, no SIM) is there. **Programme fit and cost point the same way.**
- **Rennes is the cheapest city in the shortlist AND hosts IGR-IAE (N2), the only
  formation-initiale-only M1 found.** Caution: Rennes had the third-largest cost
  rise in France in 2025 (+7.50 %, rents +5.79 %), so the gap will narrow.
- **Lyon and Nice are the two cities where a good programme sits in an expensive
  city.** Worth it only if the programme fit is decisive.
- **Reconciling the two figures:** UNEF's €1,192–€1,324 is what a student
  *actually spends*; the visa's €877.50 is what he must *prove*. The visa
  threshold is **below** real cost in every city listed. **Clearing the visa
  threshold does not mean he can afford the year.** Both numbers belong in the
  final deliverable, labelled differently.

### 5.3 Official levers that reduce the real figure

Verified, and all available to a VLS-TS holder:
- **CROUS housing: €200–330/month for a room, €320–470 for a renovated studio**,
  inclusive of water, electricity, heating and internet. Roughly **€200–300/month
  below private-market rent** in every city in the table. CROUS Toulouse rents
  start at **€217.35/month**. Places are scarce and allocated on social criteria,
  so it is upside, not a plan. Official tariff pages:
  https://www.crous-toulouse.fr/se-loger/je-cherche-un-logement/loyers-tarifs/ ·
  https://www.crous-bordeaux.fr/se-loger/le-tarif-des-logements-crous/
- **CROUS meal: €3.30**, or **€1 for non-scholarship non-EU students in financial
  difficulty**, after review of a dossier. That second rate is under-advertised
  and he qualifies to apply for it.
- **APL/ALS housing allowance: ~€100–200/month** depending on income, usually paid
  directly to CROUS as a rent reduction.
- **VISALE** free state rent guarantee — solves the French-guarantor problem,
  which is otherwise a common blocker for a student with no family in France.
- **964 work hours/year** permitted on a student visa.
- Campus France official baseline figures: food ~€300/month; student transport
  pass €374.40/yr in Paris, €250–300/yr in the regions; SNCF youth card €50/yr;
  GP visit €30 with €19 reimbursed. Health cover is free on student status;
  only the optional mutuelle costs.
  https://www.campusfrance.org/fr/preparer-budget-etudiant-France · checked 2026-08-17

---

## 6. Tuition — corrections and the €2,633 answer

**The €2,633 rate is NOT a general reduced rate and he cannot access it.**
It is **Paris 1 Panthéon-Sorbonne's "Taux 2ème diplôme Master 1 ou 2"** for non-EU
students — the rate charged when a student enrols in a **second** master's degree
alongside or after a first. **It is triggered by holding/pursuing a prior
diploma, not by means, merit or nationality.** It is also institution-specific,
not a national tariff. **Close this question: it is irrelevant to him.**

Paris 1's published 2026-2027 scale, as the clearest institutional example:

| | EU rate | **Non-EU rate** |
|---|---|---|
| Licence | €178 | **€2,902** |
| Licence, 2nd diploma | €118 | €1,934 |
| Licence, double degree | €296 | €4,836 |
| **Master (professional or research)** | €255 | **€3,950** |
| **Master, 2nd diploma** | €167 | **€2,633** |
| Doctorate | €398 | €398 |

https://www.pantheonsorbonne.fr/inscription/frais-dinscription · checked 2026-08-17

**A discrepancy to flag rather than silently resolve.** service-public.gouv.fr
states **licence €2,895 / master €3,941** and explicitly says *"the amounts for
2026-2027 are not yet known"*; Paris 1 publishes **€2,902 / €3,950** for
2026-2027; Campus France Tunisie gave 2A **€3,950**. The spread is under €10 and
does not change any decision, but **the national 2027-2028 rate is genuinely
unpublished** — his actual entry year has no confirmed tariff yet.
**`Re-check in spring 2027.`** Plan on €3,950 + €105 CVEC ≈ **€4,055**.
https://www.service-public.gouv.fr/particuliers/actualites/A18927 · checked 2026-08-17

**Exoneration caps (confirming 2A):** décret n° 2026-385 of 19 May 2026 caps
exonerations at **30 % of non-EU students in 2026-2027, 25 % in 2027-2028 — his
year — and 20 % thereafter.** Historical context that shows how much has changed:
as recently as 2023, **42 universities exempted non-EU students entirely** and 16
granted partial exemptions on linguistic, geographic or academic criteria; only 13
applied the differentiated rights in full. **That era is over, and any advice
found online predating May 2026 will be wrong about this.**

---

## 7. Structural findings to add to 2A's list

6. **The alternance trap is as large as the M2-only trap, and less obvious.**
   Alternance programmes advertise M1 entry from a licence and zero tuition —
   they look like the perfect answer. They require a signed French apprenticeship
   contract *before* enrolment, unobtainable from Tunisia pre-visa. **Screen every
   candidate programme on two axes, not one: entry point (M1 vs M2) and format
   (formation initiale vs alternance). A programme must pass both.** Of the
   thirteen new programmes in §3, **nine pass the M1 test but only nine-minus-four
   pass both.**
7. **The CRM label sits mostly on the wrong side of both traps.** France has many
   *relation client* master's programmes. Nearly all are M2-only or
   alternance-only. His CRM project is best pitched as *evidence within* a
   marketing application (iaelyon, Rennes, Nice) rather than as a search term for
   a CRM-titled degree.
8. **The Score IAE-Message is now a solved gate, and its variants matter.**
   With a Tunis centre plus a remote option confirmed, SIM-requiring IAEs are back
   in scope — which is most of the network. Three tiers, and the differences are
   worth exploiting: **no test at all** (IAE Montpellier — dossier + oral);
   **test with no eliminating minimum** (IAE Nice); **test mandatory and heavily
   weighted** (IAE Nantes, IGR Rennes, IAE Poitiers). **A 12–13/20 student should
   prefer the first two.** GMAT/TAGE MAGE are accepted substitutes at iaelyon and
   IAE Aix, but there is no reason to prefer them over the €42 SIM.
9. **SIM timing governs the whole calendar.** IGR Rennes' last receivable sitting
   is ~mid-February for a mid-March deadline — and **Études en France closes
   around 15 January, earlier still.** Working backwards: **he should sit the SIM
   in autumn 2026, alongside the TCF, before the EEF platform opens on ~1 October
   2026.** Two tests, one autumn.
10. **No French-test dispense was found at any programme in this pass.** 2A
    established he is not exempt at Campus France level; nothing in this sweep
    creates an institutional exception. The one partial escape is **IAE Aix's
    English-taught MSc 2 track**, which trades the French certificate for an
    English one — not obviously a good trade for a native French speaker.

---

## 8. Sources, with check dates (all checked 2026-08-17)

**Discovery infrastructure**
- Ministry open data, TMM parcours dataset: https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-tmm-donnees-du-portail-dinformation-trouver-mon-master-parcours-de-format/records
- IAE France network catalogue: https://www.iae-france.fr/formations/
- Score IAE-Message: https://www.iae-message.fr/

**Programmes** — URLs given inline in §3.

**Mastère Spécialisé**
- CGE, label Mastère Spécialisé: https://www.cge.asso.fr/labels-accreditations/mastere-specialise/
- CGE MS Vademecum 2023-2024 (PDF): https://www.cge.asso.fr/wp-content/uploads/2023/11/2023-2024-MS_Vademecum.pdf
- ESART (trademark-misuse warning, RNCP 35800 expiring): https://esart-paris.fr/mastere-specialise-management-de-la-musique/

**Money**
- Décret n° 2026-526 (22 Jun 2026), resource threshold €615 → €877.50: https://www.japon.campusfrance.org/fr/modification-du-montant-des-ressources-exigees-pour-les-demandes-de-visa-etudiant-a-compter-du-1er and https://pa.diplomatie.gouv.fr/fr/etudes-en-france-evolution-du-seuil-des-ressources-pour-les-visas-etudiants
- Paris 1 Panthéon-Sorbonne fee scale 2026-2027 (source of the €2,633 answer): https://www.pantheonsorbonne.fr/inscription/frais-dinscription
- Service-Public, droits d'inscription étudiants étrangers: https://www.service-public.gouv.fr/particuliers/actualites/A18927
- UNEF, Classement des villes universitaires 2025 (PDF): https://unef.fr/wp-content/uploads/2025/08/Classement-des-villes-universitaires-2025.pdf
- Campus France, préparer son budget: https://www.campusfrance.org/fr/preparer-budget-etudiant-France
- CROUS Toulouse tariffs: https://www.crous-toulouse.fr/se-loger/je-cherche-un-logement/loyers-tarifs/
- CROUS Bordeaux tariffs: https://www.crous-bordeaux.fr/se-loger/le-tarif-des-logements-crous/

**Failed / blocked (for the next pass)**
- campusfrance.org/fr/droits-differencies — 403
- france-visas.gouv.fr — reachable via firecrawl but the student page 404s (moved)
- iae-bordeaux.fr — 503 on two attempts
- cge.asso.fr — no public searchable directory of accredited MS programmes
- iaelille.fr/nos-formations/... — 404; live pages are under /formations/
