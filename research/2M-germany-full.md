# 2M — GERMANY, FULL SWEEP (the pass the project never did)

**All checks made 2026-08-17. Target intake: winter semester 2027/28.**

---

## 1. BOTTOM LINE

**Germany is not closed. The previous verdict was wrong, and it was wrong for a
specific, correctable reason: it generalised from one programme (THM) that
happens to sit at the strict end of the distribution.** Converted properly, his
grade is **German 3.0–3.4** — below every numeric bar in Germany, which cluster
at 2.2/2.3/2.5/2.9. But **roughly half of the German master's in his directions
publish no numeric bar at all.** Of 42 programmes whose admission wording I read
in full, **19 impose a grade minimum (or a de-facto one) that he misses, and 23
publish none.** The best of the no-bar group is genuinely strong: **KU
Eichstätt-Ingolstadt's MSc Business Administration / Digital Customer Experience
& Service Design — €88 a semester, taught in English, German A2 only *after*
arrival, French A2 which he has natively, a dual German + French (Toulouse)
degree, and an aptitude procedure with no published grade floor.** Behind it,
**HWR Berlin's MA International Marketing Management** is tuition-free, 100%
English, asks only IELTS 6.0 — the lowest English bar found anywhere in this
project — explicitly accommodates a 180-ECTS bachelor, and lists **no grade
requirement whatsoever**; its catch is a grade-weighted ranking for 35 places,
which is a competition he can lose but not a wall he cannot approach. The real
German obstacles are not the ones previously named: they are (a) **the NRW
non-EU quota**, which reduces admission-restricted North Rhine-Westphalia
programmes to a handful of places and an effective 1.0–1.3 requirement; (b) the
**€11,904 blocked account**, now verified from the German Embassy in Tunis; and
(c) the embassy's demand for an ***unconditional*** admission letter, which sits
awkwardly with the 180→210 ECTS "make up 30 credits" routes that several of the
best programmes rely on. Directions 3 and 4 return **near-zero in English and
very little in German**; the only genuine music-business master's is
Popakademie, which is German-taught, charges Baden-Württemberg's non-EU fee, and
requires six months of creative-sector experience he does not have.

---

## 2. COVERAGE STATEMENT — what I searched and what came back empty

**Databases queried systematically (not via Google):**

| Source | How | Result |
|---|---|---|
| **DAAD International Programmes** database | via its public JSON search API (`www2.daad.de/…/api/solr/en/search.json`), 21 query terms, master's filter, English-language filter on and off | primary programme source; **detail pages are server-rendered and carry the verbatim "Academic admission requirements" block** — I pulled 42 of them |
| **anabin (KMK)** | public REST API (`anabin.kmk.org/api/public/…`) | confirmed working; Tunisia country record retrieved; **no re-derivation done — Agent 2H's H+ / "Entspricht" result stands** |
| **Hochschulkompass (HRK)** | attempted; its advanced-search URL 404s to automated fetchers | **failed** — German-taught coverage is therefore from targeted searches, not an exhaustive sweep. **This is my known coverage gap.** |
| German Embassy Tunis (`tunis.diplo.de`) | Firecrawl (French-language pages) | **Tunisia-specific visa checklist recovered — the single most valuable source in this file** |
| make-it-in-germany | Firecrawl (WebFetch gets Radware-blocked) | Blue Card + post-study permit verified |
| Individual university admission pages | WebFetch / Firecrawl | ~15 verified directly against the DAAD summary |

**Search terms used (English):** marketing; digital marketing; marketing
analytics; business analytics; data-driven business; music; music business;
music management; cultural management; creative industries; media management;
entertainment; digital business; e-business; brand management; consumer;
communication management; innovation management; digital transformation; sales
management; international business.
**Search terms used (German):** Musikwirtschaft; Musikmanagement; Musik; audio;
Notenumrechnung Tunesien; Studiengebühren Nicht-EU; Zulassungsordnung;
Auswahlverfahren; Notendurchschnitt.

### FOUND NOTHING ON — stated explicitly

- **Direction 3 (music marketing / artist promotion): ZERO.** Not one German
  master's, in English or German. DAAD `q=entertainment` returns **0** results
  across all degree levels. `q=Musikwirtschaft` returns **0**.
- **English-taught music business: effectively zero.** DAAD `q=music` with the
  master's + English filters returns **3 hits, none relevant** (FAU
  Communications & Multimedia Engineering; Hildesheim *Future Analytics: AI &
  Audio Worlds*; SRH *Music Therapy*). Dropping the language filter adds only
  Detmold *Music Acoustics (MSc)* and Paderborn *PopMediaCulture*
  (German/Spanish).
- **No German programme anywhere combining music with digital marketing or
  data.** The hybrid the brief flags as a priority find does not exist here.
- **No German master's found that is simultaneously free, English-taught,
  no-GPA-cutoff AND admission-*unrestricted*.** The two free English no-GPA
  finds (KU Eichstätt, HWR Berlin) both run competitive selection. The
  unrestricted ones (HNU Neu-Ulm, four programmes) all print 2.5.
- **Hochschulkompass could not be swept.** German-taught marketing master's at
  smaller FHs are therefore **under-covered**. Given German is Tier C for him
  (2028+ at the earliest), I judged this an acceptable gap, but it is a gap.
- **Zwickau MBA "Business in a Digital World" (€1,800/yr)**: admission wording
  not published on DAAD, not verified. `NOT VERIFIED — check directly`:
  https://www.whz.de/english/study/incomings/courses-of-study/business-in-a-digital-world-mba/

---

## 3. HIS GERMAN GRADE — CONVERTED, AND THE CONVERSION IS VERIFIED

### 3.1 The formula, and the assumption that matters

The **modified Bavarian formula** (KMK, used by uni-assist and German
universities since 2004):

> **German grade = 1 + 3 × (N_max − N_actual) / (N_max − N_min)**

`N_max` = best obtainable grade; **`N_min` = the lowest *passing* grade, not the
bottom of the scale**. The brief flagged the choice of `N_min` as an
unverified assumption. It is now verified two ways.

### 3.2 VERIFIED — Tunisia is converted with N_max = 20, N_min = 10

**Primary source: Otto-von-Guericke-Universität Magdeburg, Faculty of Economics
and Management, examination board resolution — official conversion table
"System der Notenumrechnung: *University of Tunis* (Tunesien)".**

| Tunisian mark /20 | German grade | German label |
|---|---|---|
| 20–19 | 1,0 | sehr gut |
| 18 | 1,3 | |
| 17 | 1,7 | |
| 16 | 2,0 | gut |
| 15 | 2,3 | |
| 14 | 2,7 | |
| **13** | **3,0** | **befriedigend** |
| **12** | **3,3** | |
| 11 | 3,7 | ausreichend |
| 10 | 4,0 | |
| **< 10** | **5,0** | **nicht ausreichend (Fail)** |

Source: `https://www.fww.ovgu.de/fww_media/Pruefungsamt/Dokumente/Anerkennung+Ausland/Gesamtliste_Notenumrechnung.pdf`, p. 27.
The table's own fail line (`< 10 = Fail`) confirms **N_min = 10**, and its
values reproduce the modified Bavarian formula with N_max = 20, N_min = 10 to
within one band.

**Corroboration that this formula is what is actually applied to foreign
degrees:** Hochschule Osnabrück states on its own master's application page that
"the university applies the **Modified Bavarian Formula** for converting foreign
degrees". H-BRS points applicants at TUM's Bavarian-formula converter.

### 3.3 THE ANSWER

> **12/20 → German 3,3–3,4. 13/20 → German 3,0–3,1.**
> **His band is German 3.0–3.4 — "befriedigend" (satisfactory), on a scale
> where 1.0 is best and 4.0 is the bare pass.**
> **Status: VERIFIED against a German university's official examination-board
> conversion table for Tunisia.**

One caveat carried honestly: a stray secondary source claims some institutions
use **N_min = 9** for Tunisia. That would give 12/20 → 3.18 and 13/20 → 2.91 —
which would put a 13/20 *just inside* Magdeburg's 2.9 bar. This is a **single
unverified secondary claim against a primary source that says `<10 = Fail`.**
Treat 3.0–3.4 as the working number; if his transcript average is genuinely 13.0
or above it is worth asking uni-assist to state the figure before writing
Germany off at the margin.

**Implication:** he clears **no** German numeric bar found in this sweep. Every
one of them is 2.9 or better. **Therefore the entire German question reduces to:
which programmes do not publish a bar.**

---

## 4. THE CENTRAL QUESTION — HOW MANY IMPOSE A GRADE MINIMUM?

**42 programmes' admission wording read in full. 19 impose a bar he misses. 23 publish none.**

### 4.1 GROUP A — imposes a numeric grade minimum (19). He fails all of them.

| # | University / programme | Tuition (non-EU) | **Exact wording** |
|---|---|---|---|
| 1 | **TH Nürnberg** — MA International Marketing | free (€82/sem) | *"ein Durchschnitt von **1,5 oder besser** (nach dem deutschen Notensystem)"*; grades 1.5–2.5 must add **GMAT ≥ 550**. Also 20-week marketing internship, IELTS 7.0, German A1. **Hardest bar found.** |
| 2 | **Hochschule Bonn-Rhein-Sieg** — MSc Marketing | free (~€300/sem) | *"places are allocated to applicants with the very best final grades (CGPA)"* + *"**Only 2 places are available for non-EU/non-EEA nationals** for this admission-restricted programme by NRW Allocation Regulation (Vergabeverordnung NRW). This means that only non-EU/non-EEA nationals with a **CGPA of 1.0 to usually about 1.2/1.3** according to the German grading system can be admitted"*. No published minimum, but a de-facto 1.2. |
| 3 | **Uni Pforzheim** — MSc Corporate Communication Management | **€1,500/sem (BW)** | *"with an overall grade of **2.2 or better** (German grading system)"* |
| 4 | **THM Gießen** — MSc Digital and International Marketing | free (~€350/sem) | *"First university degree… with **at least 2.3 overall grade** and **210 ECTS** credits in business administration"* + 5 ECTS maths/stats + **German B1** |
| 5 | **FH Münster** — MA International Marketing and Sales | free (~€300/sem) | *"Bachelor's degree in Business Administration or Economics with **ECTS grade B or a minimum mark of 2.3** (according to ECTS). Marks from foreign education systems should be converted using the ANABIN transformation guidelines."* |
| 6 | **Uni Bremen** — MA Digital Media and Society | free (~€425/sem) | *"A **minimum grade of 2.3** (German university grading system) as the overall grade of the previous degree"* |
| 7 | **HNU Neu-Ulm** — MSc AI and Data Analytics | free (~€100/sem) | *"**grade 2.5 or better**"* + 210 ECTS + 25 ECTS programming/DB/stats + GRE for non-Lisbon applicants |
| 8 | **HNU Neu-Ulm** — MSc Int'l Corporate Communication & Media Mgmt (ICCMM) | free | *"**grade 2.5 or better**"* + 210 ECTS + 60 ECTS comms/media + **GRE General Test** |
| 9 | **HNU Neu-Ulm** — MSc Digital Transformation & Global Entrepreneurship | free | *"**average grade of 2.5 or better**"* + 210 ECTS + GRE |
| 10 | **HNU Neu-Ulm** — MSc Digital Leadership in Information Management | free | *"**minimum grade: 2.5 or better**"* + GRE |
| 11 | **Hof University** — MA Global Management | free (~€150/sem) | *"**a minimum grade 2.5** according to the German grading system"* + *"at least **210 ECTS**"* + 110 ECTS business |
| 12 | **Uni Pforzheim** — MSc Digital Business Management | **€1,500/sem (BW)** | *"with an overall grade of **2.5 or better** (German grading system)"* |
| 13 | **Uni Köln** — MSc Business Analytics & Econometrics | free | *"Bachelor's **GPA of at least 2.5** (German grade)"* |
| 14 | **Mainz UAS** — MA International Business (MA.IB) | free (~€350/sem) | *"Above-average results (**minimum requirement: ECTS grade C or 2.5 or better** (calculated into the German grading system). Grades from non-EU applicants will be transferred into German grades by uni-assist."* |
| 15 | **Mainz UAS** — MSc International Business Management | €7,400/yr | *"average **at least 2.5** calculated into the German system"* — also **part-time, 50/50 online** |
| 16 | **Rhine-Waal** — MSc Economics and Finance | free (~€300/sem) | *"A final undergraduate mark equivalent to an A or a B on the ECTS grading scale (**2.5 or better** in the German grading system)"* |
| 17 | **TH Köln** — MSc Digital Sciences | free | *"A final grade of **'good' or better** has been achieved"* (= ≤2.5) |
| 18 | **OVGU Magdeburg** — MSc Int'l Management, Marketing, Entrepreneurship (IMME) | free (€311/sem) | *"a **GPA from 1.0 up to 2.9** (according to the German grading system)"* + C1 English + *"limited places… selection procedure"* |
| 19 | **htw saar** — MA International Management | free (€414/sem) | *"Bachelor's degree (180 ECTS) in business or economics… with an **average mark of 2.9 or better**"* + 10 ECTS maths/stats + C1 English + **German B1** |

**Note on #19:** htw saar's 2.9 is the *most generous numeric bar in Germany* —
and he still misses it, by 0.1–0.5. That is the clearest single illustration of
how the German scale works against him.

### 4.2 GROUP B — publishes NO numeric grade minimum (23)

Ranked by how usable they actually are.

#### ★★★ Tier 1 — free or near-free, English-taught, no published bar

| # | Programme | Wording on grade | Why it works / what to watch |
|---|---|---|---|
| **B1** | **KU Eichstätt-Ingolstadt (WFI Ingolstadt School of Management) — MSc Business Administration, spec. *Digital Customer Experience & Service Design* (DICE)** | *"Open to all students who pass the aptitude procedure"*; DAAD's requirement block lists **no grade**. KU's page: *"**Bonus points may be awarded** based on relevant prior knowledge for your chosen specialization"* and *"professional experience and/or internships related to that specialization."* | **THE FIND.** €88/semester, no tuition. English B2. **German A2 only by end of 3rd term** (i.e. after arrival). **French A2 — he is a native speaker.** **Dual degree: German MSc Business Administration + French *Master International Marketing of Innovation*, Toulouse School of Management.** 120 ECTS / 4 semesters. His CRM build and Renault internship are exactly the "relevant prior knowledge + internship" the bonus points reward. **Catch: only 10 places**, selection interviews. Non-EU deadline **1 April – 15 May**. |
| **B2** | **HWR Berlin (Berlin School of Economics and Law) — MA International Marketing Management** | Verbatim, complete list from HWR's own page: *"Bachelor's or equivalent degree in Business Studies from an accredited university / At least 210 credit points. **Applicants with 180 credits will be required to obtain the additional 30 credits, for example by completing a placement in the third semester** / Evidence specifically of having completed undergraduate modules in Marketing, totalling **at least 15 ECTS** / English language skills on a **high B2 level**…"* — **no grade anywhere.** | Tuition-free, ~€350/sem. **100% English.** **IELTS 6.0 / TOEFL 83** — the lowest English bar in this whole project. 90 ECTS, 3 semesters (4 with the placement). Akkreditierungsrat-sealed. Direction-2 bullseye. **Catch:** HWR's own FAQ: *"a ranking is established, composed by the **bachelor's overall grade**, the bachelor grades of the relevant courses and the work experience in the field of studies"*, **35 places**. Grade is the first ranking criterion — so this is a competition, not a wall. His marketing-module grades and Renault internship are the levers. **No non-EU quota at HWR.** Non-EU window **15 March – 15 May** via uni-assist. |
| **B3** | **HM München (Munich UAS) — MA Entrepreneurship and Digital Transformation** | *"Proof of a first university degree worth **180-210 ECTS**. If your degree comprises 180 ECTS, you must provide evidence of an additional 30 ECTS-equivalent (e.g. via relevant courses, work experience, or an internship)… Proof of English proficiency at **B2** level… Demonstrated experience or knowledge in entrepreneurship/intrapreneurship, digital transformation, and project implementation… **A convincing project description (one page) and pitch reel (two minutes)**… A successful application interview"* — **no grade.** | Free, **€97/semester** — cheapest in the file. English B2. 3 semesters. **Selection is by project + pitch + interview, not by grade** — the single most favourable selection architecture found in Germany for this student. **His CRM platform is precisely the "project implementation" evidence asked for.** Requires a VPD from uni-assist (allow 8 weeks). |
| **B4** | **KU Eichstätt-Ingolstadt — MSc Business Administration, spec. *Business Analytics & Operations Research*** | *"**Open to all students who pass the aptitude procedure.** This is based on the Bachelor's degree grade, specific previous knowledge of the chosen specialisation and relevant professional experience."* | Free, English B2, German A2. Grade is *a* factor, not a floor. Direction 1. Quantitatively demanding — weaker fit than DICE. |
| **B5** | **Hochschule Osnabrück — MA International Business and Management** | *"Bachelor's degree (or equivalent) in business management, economics, or related programmes (**at least 80% of the subjects… need to be related to business and/or economics**)"* — no grade. Allocation: *"Selection uses a **points system** based on bachelor's grade, international experience, vocational training, professional experience, internships, scholarships, and voluntary work."* | Free, ~€380/sem. **"50% of the available study places are reserved for international applicants from non-EU countries"** — the opposite of the NRW quota, and rare. **Catch: English C1 / IELTS 7.0** and **German A1 certificate**. The IELTS 7.0 is a real obstacle given he has no test yet. Non-EU window **1 February – 1 April**. |
| **B6** | **European University Viadrina — MA Digital Entrepreneurship (MoDE)** — double degree with Adam Mickiewicz University Poznań | *"You may apply… if you have a Bachelor's degree (or a comparable undergraduate degree) and have obtained **10 ECTS in two of the major subjects** of the MoDE (economics, law, sociology, political science, informatics or interdisciplinary digital studies)"* — no grade. | Free, ~€350/sem, Frankfurt (Oder) — commuting distance to Berlin. Dual German+Polish degree. **Catch: English C1.** A marketing licence covers the economics ECTS. |
| **B7** | **European University Viadrina — MA Digital Studies: Technology, Media, Society** | *"requires a first professionally qualifying university degree of **at least 180 ECTS credits (six semesters)**"* + 60 ECTS in social sciences/humanities or digitalisation research — no grade. | Free. **Explicitly 180 ECTS — one of very few German programmes that does not want 210.** **Catch: English C1**, and *"a maximum of 10 ECTS can also be from… Economics"* — a pure business/marketing licence probably **fails the 60-ECTS subject test.** `BORDERLINE — email admissions`. |
| **B8** | **TU Chemnitz — MSc Business & Economics** | §3 study regulations; requirements framed as equivalence to TU Chemnitz's own BSc Business Administration, with *"The Examinations Committee shall take the final decision in respect of the admission of applicants with a professional qualification in a course of study equivalent in content"* — **no numeric grade.** | Free, €340/sem. **Catch:** courses run in German *and* English — "sufficient proficiency in both is required"; DAAD lists German A1 only, which contradicts. `NOT VERIFIED — check directly` with the faculty. |

#### ★★ Tier 2 — no grade bar, but paid, or the direction/format is off

| # | Programme | Wording on grade | Cost & catch |
|---|---|---|---|
| B9 | **Internationale Hochschule SDI München — MA Digital Media Manager** | *"**NC-freier Studiengang**"*; *"Bachelorabschluss **unabhängig von der Fachrichtung**"* (any subject); *"Englischkenntnisse auf B2-Niveau"* — DAAD: **B2 proven by placement test / interview, no external certificate.** | **€640/month (€620 if paid half-yearly, €600 in full) ≈ €7,200–7,680/yr; ~€11,520 total.** Private but **staatlich anerkannt und akkreditiert**. Taught in **English**, 90 ECTS, 3 semesters full-time (3 days/week), Munich. **This is the only German programme found that needs neither a grade nor an external English test.** Band-2 cost. |
| B10 | **Nürtingen-Geislingen University — MSc Digital Business Management** | *"First university degree… with at least 210 ECTS. **If you only have 180 ECTS, you can also get admitted, but would need to have a work experience of at least six months**"* — no grade; DAAD lists **no minimum English level**. | €3,200/yr. BW, but the fee is stated as "all countries" (continuing-education programme, so the €1,500/sem non-EU rule may not stack — `NOT VERIFIED`). |
| B11 | **Hochschule Ludwigshafen — MBA International Business Management** | *"…with a good average grade (at least 2.5…)"* **BUT** *"**If your average grade is lower than required, admission can be possible after a personal interview showing your motivation for the programme.**"* | €2,250/yr. **The only German programme found with an explicit, published escape hatch below its own stated grade bar.** Also wants ≥1 year commercial work experience. English B2. Worth one email. |
| B12 | **TH Ingolstadt — MA Retail and Consumer Management** | *"an economics or retail-oriented Bachelor's degree… with **at least 210 ECTS**… A successfully completed **selection procedure**"* — no numeric grade. | **€1,200/yr non-EU** (Bavaria does charge here — see §5). English B2 / IELTS 5.5. 210 ECTS is the block. |
| B13 | **accadis Hochschule Bad Homburg — MA Global Marketing Management** | *"A Bachelor's degree in a business or management-related subject with **min. 180 credit points (ECTS)**"* — no grade. | €5,880/yr + €800 admission fee + €435/6mo admin. Private, state-recognised. English B2 / IELTS 6.5. **180 ECTS explicitly.** Direction-2 match. Band 2–3. |
| B14 | **Hochschule Fresenius — MSc Marketing & Brand Management** | *"a Bachelor's programme consisting of **at least 180 credit points**… **at least 60 credit points in management or business administration**… If you have earned less than 60 credit points… you must pass an admissions test."* — no grade. | ~€5,280/yr EU rate (non-EU rate truncated in DAAD — `NOT VERIFIED`). Private. English B2 / TOEFL 70. Direction-2 match, 180 ECTS fine. |
| B15 | **Furtwangen University — MSc Business Consulting (BCM)** | *"Undergraduate degree/BSc in Business Economics, Information Technology, Engineering, Social Sciences or similar"* — no grade. | €4,676 total for 3 semesters. **Blocker: "Minimum of one year of relevant professional experience AFTER graduation (full-time)."** He does not have it. |
| B16 | **WH Zwickau — MBA Business in a Digital World** | not published on DAAD | €1,800/yr. `NOT VERIFIED — check directly` |

#### ★ Tier 3 — no grade bar, but blocked on subject fit or format

| # | Programme | Why it fails |
|---|---|---|
| B17 | **Leuphana Lüneburg — MA Arts and Cultural Management** | *"an undergraduate degree (Bachelor or at least equivalent)… **generally one year's relevant work experience**… advanced English skills"* — no grade. **But: distance-learning format with an on-campus week — part-time/blended → no student visa, no post-study work rights.** Fee €7,710 (60 CP / 3 sem) or €9,760 (90 CP / 4 sem). **EXCLUDED per brief §4.** Closest thing Germany offers to direction 4 in English, and it does not qualify. |
| B18 | **Uni Hildesheim — MA Future Analytics: AI & Audio Worlds** | Free, no grade, English B2 with **no proof required**. **But eligibility is *"a Bachelor's degree in Computer Science, Data Science, or AI, or in Music, Musicology or Anthropology (with a focus on sound), Cultural and Sound Studies, Sociology of Music"* — a marketing licence is not on the list.** The tantalising AI + audio hybrid, and he is not eligible. |
| B19 | **Uni Bremen — MA/MSc Digital Media** | Free, no grade, but *"substantial experience both in **computer science (i.e. programming and algorithms, beyond using existing tools)** and design"* + portfolio. IELTS 7.0. |
| B20 | **TU Ilmenau — MA Media and Communication Science** | Free, no numeric grade, but requires a **communication-science** first degree and *"profound knowledge… of core theories"* + C1 English. |
| B21 | **Uni Hildesheim — MSc Data Analytics** | Free, no cutoff, but ranked: *"overall mark of your Bachelor's (**53%**)"* — grade-dominant ranking, and a CS/maths background is expected. |
| B22 | **HWR Berlin — MSc Business Intelligence and Process Management** | Free, **no grade in the requirements list**, English B2. **But requires 10 ECTS quantitative methods/databases AND 10 ECTS (applied) informatics** — a marketing licence will not have them. 20 places. |
| B23 | **Popakademie Baden-Württemberg — MA Music and Creative Industries** | See §7. No numeric grade, 180 ECTS accepted — but German-taught, BW non-EU fee, and six months' creative-sector experience. |

### 4.3 The structural finding that matters more than any single bar

**The North Rhine-Westphalia non-EU quota.** H-BRS states it plainly:

> *"Only **2 places** are available for non-EU/non-EEA nationals for this
> admission-restricted programme by **NRW Allocation Regulation
> (Vergabeverordnung NRW)**. This means that only non-EU/non-EEA nationals with
> a **CGPA of 1.0 to usually about 1.2/1.3** according to the German grading
> system can be admitted."*

This is not a programme policy; it is **state law applying to every
admission-restricted (*zulassungsbeschränkt*) programme in NRW** — a state that
contains Köln, Bonn, Münster, Aachen, Dortmund, Bochum, Düsseldorf, Kleve.
**Practical rule: do not apply to any NC-restricted NRW programme.** Only
*zulassungsfrei* NRW programmes are worth the fee.

Conversely, **Hochschule Osnabrück (Lower Saxony) reserves 50% of places for
non-EU applicants** — the exact inverse. **The state, and the restricted/
unrestricted status, matter as much as the published requirement.** This is the
question to ask every German admissions office, and nobody in this project has
asked it before.

---

## 5. TUITION — WHICH STATES CHARGE NON-EU STUDENTS (verified)

| State | Non-EU fee | Source |
|---|---|---|
| **Baden-Württemberg** | **€1,500 per semester** for all non-EU/EEA students entering for study, at **all state higher-education institutions**, since WS 2017/18, under the **Landeshochschulgebührengesetz (LHGebG)**. Confirmed live for SS 2026. Individual universities decide exemptions. | Ministerium für Wissenschaft, Forschung und Kunst BW — mwk.baden-wuerttemberg.de. Corroborated by DAAD programme records showing exactly "non-EU countries: 1,500 EUR" for **Uni Pforzheim** (two programmes). Affects: Pforzheim, Reutlingen, Furtwangen, Heilbronn, Konstanz, Mannheim, Nürtingen, Karlsruhe, Freiburg, Heidelberg, Stuttgart, Tübingen, **Popakademie**. |
| **Bavaria** | **Enabled but not universal.** The **Bayerisches Hochschulinnovationsgesetz (BayHIG)** lets institutions charge third-country students. **Observed live**: **TH Ingolstadt — €1,200/yr non-EU** (DAAD record). **Not charged** at: HM München (€97/sem), HNU Neu-Ulm (~€100/sem), TH Nürnberg (€82/sem), **KU Eichstätt (€88/sem)**, Hof (~€150/sem). **So Bavaria is mostly still free — check per institution, never assume.** |
| **All other 14 states** | **No tuition.** Semester contribution only, €82–440. Berlin ~€350, Saxony ~€340, Lower Saxony ~€380, Bremen ~€425, Thuringia ~€320, Saarland €414, Hildesheim ~€440. | DAAD programme records, cross-checked against university fee pages |

**The previous file's claim that "Baden-Württemberg charges non-EU students
€1,500/semester; most other states charge only a semester contribution"
is CORRECT and remains current — but it missed Bavaria's per-institution fees.**

---

## 6. THE 210-ECTS PROBLEM — which programmes want 210, and how hard is it

The brief asked whether 210 is a harder block than 180. **Answer: it is
frequently *softer*, because German programmes routinely publish a make-up
route.** Of the programmes requiring 210, almost all offer one.

| Programme | 210 required? | Make-up route published? |
|---|---|---|
| **HWR Berlin — Int'l Marketing Management** | Yes | **YES** — *"Students who acquired less than 210 ECTS… must obtain the missing credit points… by way of an integrated period of practical training, for which 30 ECTS points are awarded. This internship semester is scheduled in the third semester… The master programme will thus last four semesters."* Alternatively via study abroad. |
| **HM München — Entrepreneurship & Digital Transformation** | 180–210 | **YES, and 180 is explicitly listed** — *"Proof of a first university degree worth 180-210 ECTS."* Make-up "via relevant courses, work experience, or an internship". |
| **THM Gießen** | Yes | YES — *"Applicants with 180 ECTS must make up 30 ECTS through a practical phase, study abroad, or additional coursework"* (but 2.3 kills it anyway) |
| **Hof — Global Management** | Yes | YES — internship ≥900 h / 6 months, or modules at Hof, + a 4th semester (but 2.5 kills it) |
| **HNU Neu-Ulm (all four)** | Yes | **YES** — 180-ECTS holders take a **four-semester (120 ECTS) version with a preparatory first semester** (German for Academic Studies, Academic English, Intercultural Skills, Research Skills + 2 subject modules). *Or*, for Lisbon-Convention institutions, **six months' relevant professional experience** counts. **Tunisia is not a Lisbon Convention party — so he would need the GRE and the four-semester version.** (2.5 kills it anyway.) |
| **Rhine-Waal — Economics & Finance** | 210 for unconditional | YES — *"With at least 180 ECTS credits → **conditional admission**, i.e. upon admission, a 'Learning Agreement' will be established, covering an additional 30 ECTS"* |
| **H-BRS — Marketing** | Yes | YES — *"the additional module 'Practical Term' must be completed with a duration of at least 20 and a maximum of 27 weeks"* |
| **TH Ingolstadt — Retail & Consumer Mgmt** | Yes | **NO route published** — hardest 210 found |
| **Nürtingen — Digital Business Mgmt** | Yes | YES — 180 + 6 months' work experience |
| **KU Eichstätt (both), Viadrina (both), Osnabrück, Chemnitz, Leuphana, SDI, accadis, Fresenius, Bremen, Ilmenau, Hildesheim** | **NO — 180 is fine** | n/a |

**Verdict on 210: it is NOT the harder block.** The grade is. **But there is a
real visa consequence — see §8.2.**

**146-ECTS verdict for Germany specifically: `LIKELY OK`.** anabin's Tunisian
*Licence* entry describes the qualification **in years, not credits** — *"der
grundständige Abschluss nach einem **dreijährigen** Studium"* — and rates it
**"Entspricht"** to a German 3-year bachelor. Where a German programme says "180
ECTS", uni-assist's evaluation of the anabin entry should carry it. Where it
says "210 ECTS", he is in the make-up route regardless.

---

## 7. DIRECTIONS 3 & 4 — MUSIC. The honest, near-empty answer.

**English-taught: ZERO. Not one programme.** (DAAD `entertainment` = 0;
`Musikwirtschaft` = 0; `music` + master's + English = 3 irrelevant hits.)

**German-taught, the only real options:**

| Programme | Status | Entry rules | Cost | Verdict |
|---|---|---|---|---|
| **Popakademie Baden-Württemberg — MA Music and Creative Industries** | **State institution of BW; Master of Arts, 120 ECTS, 4 semesters, full-time in-person, consecutive** | *"ein Hochschulabschluss oder ein gleichwertiger Abschluss"* in Musikbusiness, Popmusikdesign, **Wirtschaftswissenschaften**, Kulturwissenschaften, Sozialwissenschaften, Musik/Musikwissenschaft or Medien- und Kommunikationswissenschaften — **"6 Semestern bzw. 180 ECTS-Punkten"**, so **180 is fine** and **a business/marketing licence is an eligible field**. **No numeric grade bar** — *"Abschlussnote im Erststudium"* is one selection factor. Selection = document pre-screen + personal interview; English assessed in the interview. **20 places.** Deadline **15 June**. | *"keine"* tuition for a consecutive master — **BUT** the FAQ states BW *"erhebt seit dem Wintersemester 2017/18 bei allen staatlichen Hochschulen Studiengebühren für gewisse Internationale Studierende"* → **€1,500/semester = €3,000/yr applies.** Plus ~€100/sem Studierendenwerk. | **BLOCKED, but not for the reasons previously recorded.** The real blocker is **mandatory practical experience**: *"einschlägige Praxiserfahrung im Bereich Musik-, Kultur- oder Kreativwirtschaft"* evidenced by completed vocational training, **an internship of at least six months**, or **at least six months' volunteer work**. He has none. **Correction to Agent 3G/2H: I found NO published C1-German requirement and NO entrance exam for this MA** — the FAQ lists DSH/TestDaF-family certificates without stating a level, and selection is by interview. `NOT VERIFIED — confirm the German level directly` at popakademie.de. **Actionable note: six months' volunteer work in the music/creative sector in Tunisia would satisfy the one hard prerequisite.** |
| **HMTM München — Kultur- und Musikmanagement (MA)** | State music university | German or foreign degree + **aptitude test (Eignungsprüfung)** | Bavaria — likely free | German-taught, aptitude exam. Tier C. |
| **HfM Detmold — Musikvermittlung/Musikmanagement (MA)** | State music university | Music-performance oriented | free | Not a fit — he is not a qualified musician. |
| **Uni Hildesheim — MA Future Analytics: AI & Audio Worlds** | State uni, free, English, **no grade bar** | **Eligible backgrounds do not include business/marketing** | free | The one AI+audio hybrid in Germany, and he is ineligible. Worth one speculative email given his self-taught production hobby, but do not plan on it. |

**Bottom line on music in Germany: one viable programme (Popakademie), gated on
German (Tier C, 2028+), €3,000/yr of BW fees, and six months of creative-sector
experience. It is not a 2027 option. It could be a 2029 option if he starts
German now and does music-sector volunteering.**

---

## 8. VISA, MONEY, POST-STUDY — verified, with a Tunisia-specific finding

### 8.1 Blocked account — VERIFIED, from the German Embassy in Tunis

> **"Le montant prévu pour le financement d'une année d'études s'élève à
> **11.904 EUR** (992 EUR par mois)"**
> — Ambassade d'Allemagne à Tunis, checklist "Études",
> https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172 (checked 2026-08-17)

**This upgrades Agent 2H's `VERIFIED ONLY FROM SECONDARY SOURCES` to fully
verified, from the exact mission that will process his application.** The
Federal Foreign Office confirms the mechanism (payout capped at 1/12 per month,
amount pegged to the maximum German student support rate) at
auswaertiges-amt.de/en/sperrkonto/388600. A *Verpflichtungserklärung* (formal
sponsorship under §§66–68 AufenthG) by a person resident in Germany is the
published alternative.

### 8.2 THREE Tunisia-specific visa findings nobody has recorded

1. **The embassy requires an *unconditional* admission letter** — *"**Certificat
   d'admission inconditionnel** à un établissement universitaire en Allemagne"*.
   **This is a live risk for exactly the programmes that solve his 180-ECTS
   problem**: Rhine-Waal, for instance, calls the 180-ECTS route
   *"**conditional** admission"*. **Before relying on any 180→210 make-up route,
   confirm in writing that the resulting Zulassungsbescheid is unconditional.**
   This may be the sharpest practical constraint in the whole German file, and
   it is invisible from the university side.
2. **Appointments are rationed by a waiting list.** *"Votre inscription sur la
   liste d'attente sera transmise par l'Ambassade à TLS lorsque ce sera votre
   tour."* Applications go through **TLScontact**, in person. **Build months of
   slack into the 2027 timeline.**
3. **Every document must be translated into German**, and the university diploma
   must be **legalised by the Ministry of Higher Education and the Ministry of
   Foreign Affairs** — a Tunisian bureaucratic chain that takes weeks. The
   baccalauréat must be legalised by the Ministry of Education and MFA.
   Documents must be submitted **unstapled and unbound**.

### 8.3 Post-study work — verified

> *"you have the possibility of obtaining a residence permit valid for up to **18
> months** to look for qualified employment. During these 18 months, **you are
> allowed to take up any type of job**. Please note that this type of residence
> permit is **not renewable**."*
> — make-it-in-germany.com/en/study-vocational-training/studies-in-germany/prospects-after

### 8.4 EU Blue Card 2026 — verified, and the previously reported figures are correct

> *"Your job in Germany must enable you to earn a gross annual salary of at least
> **€50,700** (as of 2026)."*
> *"If you are employed in a **shortage occupation**… at least **€45,934.20**
> (as of 2026) if the Federal Employment Agency has approved your employment."*
> *"The following applies to **new entrants to the labour market**: If you
> obtained your last degree… **less than three years ago**, you can also obtain
> an EU Blue Card if your job offer includes a gross annual salary of at least
> **€45,934.20**… **This applies to entry-level jobs in all professions.**"*
> — make-it-in-germany.com/en/visa-residence/types/eu-blue-card (checked 2026-08-17)

**Both figures in the brief are CONFIRMED for 2026.** Legal basis §18g AufenthG;
the threshold is half the pension-insurance contribution ceiling and rises ~5%
a year — **expect roughly €53,000 / €48,000 by his 2029 graduation.** The
crucial nuance for him: **as a graduate within 3 years, he qualifies for the
€45,934.20 reduced threshold in *any* profession, including marketing** — he
does not need a shortage occupation. A German marketing/CRM entry salary of
~€45–50k is realistic in Munich/Berlin/Frankfurt, so the Blue Card is
attainable rather than aspirational.

### 8.5 Cost of living — official

**DAAD, citing the DZHW 22nd Social Survey (2023):**

| Item | Monthly |
|---|---|
| **Total average student expenditure** | **€876** |
| Rent incl. utilities | €410 |
| Food | €198 |
| Health insurance, doctor, medication | €100 |
| Transport | €89 |
| Semester contribution (amortised) | €36 |
| **Visa proof requirement** | **€992/month = €11,904/yr** |

Semester contribution range: **€70–430**. Source:
daad.de/en/studying-in-germany/living-in-germany/finances/

**City-level, from the universities' own pages (official):**

| City | Stated monthly cost | Source |
|---|---|---|
| **Berlin** (HWR) | **€800–1,000** — *"Student residence: 400 to 500 EUR; Health insurance: approx. 100 to 150 EUR"* | HWR Berlin / DAAD record |
| **Osnabrück** | **~€750** | hs-osnabrueck.de |
| Ingolstadt / Eichstätt | not published — small Bavarian towns, below the national average | — |
| Munich | Germany's most expensive city; budget at or above €992 | — |

**Practical total for a free programme, Berlin:** €0 tuition + ~€700/yr
semester contributions + ~€10,500–12,000/yr living = **≈ €11,000–13,000/yr all
in**, against **€11,904 that must be shown up front**. In Ingolstadt or Neu-Ulm
it is materially less. **This is the cheapest total cost of any country in the
project** — but the €11,904 must exist as cash before he can go.

---

## 9. RECOMMENDED GERMAN SHORTLIST

| # | Programme | City / state | Direction | Language | Cost/yr | Grade bar | Verdict |
|---|---|---|---|---|---|---|---|
| **1** | **KU Eichstätt-Ingolstadt — MSc BA / Digital Customer Experience & Service Design (DICE)** | Ingolstadt, Bavaria | **1 + 2** | **English** (Tier A) + French A2 (native) + German A2 post-arrival | **€176** | **None published** — aptitude procedure with bonus points for prior knowledge and internships | **APPLY.** Best cost-to-fit ratio in the project. Dual German+French degree with Toulouse. 10 places — a real risk. **Non-EU deadline 1 April – 15 May.** |
| **2** | **HWR Berlin — MA International Marketing Management** | Berlin | **2** | **English 100%** (Tier A) | **~€700** | **None published**; grade-ranked selection, 35 places | **APPLY.** IELTS **6.0** — the most achievable English bar found. 180 ECTS explicitly accommodated. **Non-EU window 15 March – 15 May via uni-assist.** |
| **3** | **HM München — MA Entrepreneurship and Digital Transformation** | Munich, Bavaria | **2** | **English** (Tier A) | **€194** | **None** — project description + 2-min pitch reel + interview | **APPLY.** The selection method rewards his CRM build over his transcript. Needs a VPD (8 weeks) — start early. |
| 4 | **SDI München — MA Digital Media Manager** | Munich | 2 (+3 adjacent) | English (Tier A) | ~€7,200–7,680 | **"NC-frei"**, any bachelor subject, **English B2 by internal placement test** | **Backup with the highest admission certainty in Germany.** No grade, no external English test. Band-2 cost. |
| 5 | **Hochschule Osnabrück — MA International Business and Management** | Osnabrück, Lower Saxony | 2 | English (Tier A) | **~€760** | **None**; points system, **50% of places reserved for non-EU** | Apply **only if he can reach IELTS 7.0**. Non-EU window 1 Feb – 1 Apr. |
| 6 | **Hochschule Ludwigshafen — MBA International Business Management** | Ludwigshafen, RLP | 2 | English (Tier A) | €2,250 | 2.5 **with a published interview escape hatch** | One email. Wants 1 yr commercial experience. |
| 7 | **accadis Bad Homburg — MA Global Marketing Management** | Bad Homburg, Hesse | 2 | English (Tier A) | €5,880 + fees | **None**, 180 ECTS explicit | Stretch on cost; clean on entry. |
| — | **Popakademie BW — MA Music and Creative Industries** | Mannheim, BW | **4** | **German (Tier C)** | €3,000 + fees | **None** — grade is one factor; **180 ECTS accepted** | **2029, not 2027.** Blocker is six months' creative-sector experience, which he could start building now. |
| ✗ | Anything **admission-restricted in NRW** | Köln, Bonn, Münster, Aachen, Kleve… | — | — | free | **de-facto 1.0–1.3** via Vergabeverordnung NRW | **Do not apply.** |
| ✗ | THM, FH Münster, TH Nürnberg, Hof, HNU (×4), OVGU IMME, htw saar, Pforzheim (×2), Rhine-Waal, Mainz (×2), Köln, TH Köln, Bremen DMS | — | — | — | mostly free | **2.2–2.9** | **Excluded on grade. Do not spend application fees.** |

### The three actions that change the German answer

1. **Get the English test.** Every Tier-1 recommendation above turns on it, and
   the spread is enormous: **HWR wants IELTS 6.0; Osnabrück wants 7.0.** IELTS
   6.0 is a realistic target; 7.0 is a different project. **Sit IELTS before
   deciding where to apply, not after.**
2. **Ask KU Eichstätt and HWR, in writing, one question each:**
   *"For a Tunisian applicant with a 3-year Licence and a German converted grade
   of approximately 3.2, is there any grade threshold below which the
   application is not considered?"* Both publish none; both run selection. The
   answer converts a maybe into a plan.
3. **Ask HWR whether a 180-ECTS applicant's Zulassungsbescheid is
   *unconditional*** — because the German Embassy in Tunis will not accept a
   conditional one. Same question to any programme whose 210-ECTS route he uses.

---

## 10. WHAT CHANGES IN THE PROJECT'S OVERALL PICTURE

- **Germany moves from CLOSED to OPEN-CONDITIONAL.** The condition is an
  English test, not the grade and not the credential.
- **The "GPA is the blocker" hypothesis is confirmed as a fact and simultaneously
  shown to be non-universal.** 19 programmes yes, 23 no.
- **"Applied sciences are more flexible" is disproved again** — the FH sector
  supplied *both* the strictest bars (TH Nürnberg 1.5, THM 2.3, FH Münster 2.3)
  and the most open doors (HWR, HM München). Institution type predicts nothing;
  **the individual Zulassungsordnung and the state's allocation regulation
  predict everything.**
- **New portable insight for other countries:** ask not only "what is the
  minimum grade" but **"is the programme admission-restricted, and is there a
  non-EU quota"**. NRW's 2-places rule and Osnabrück's 50%-reserved rule are
  opposite extremes hiding behind identical-looking admission requirements.
- **Cost:** at €176–760/year of fees, the German Tier-1 options are **the
  cheapest degrees identified anywhere in this project**, and cheaper than
  Austria's FH Kufstein (€726.72). The offsetting cost is the €11,904 blocked
  account, which Austria does not match in size.

---

## 11. SOURCES — all checked 2026-08-17

**Grade conversion**
- OVGU Magdeburg, FWW examination board, *Gesamtliste Notenumrechnung* (Tunisia table, p. 27) — https://www.fww.ovgu.de/fww_media/Pruefungsamt/Dokumente/Anerkennung+Ausland/Gesamtliste_Notenumrechnung.pdf
- Hochschule Osnabrück, "How to apply" (states use of the Modified Bavarian Formula) — https://www.hs-osnabrueck.de/en/study/study-offerings/master/international-business-and-management-ma/how-to-apply/
- TUM grade-conversion tool (referenced by H-BRS) — https://www.tum.de/en/studies/application/application-info-portal/grade-conversion-formula-for-grades-earned-outside-germany

**Programme database**
- DAAD International Programmes — https://www2.daad.de/deutschland/studienangebote/international-programmes/en/ (detail IDs cited inline: 10324, 10432, 10480, 10573, 10714, 11089, 11131, 3631, 3737, 3765, 3826, 3844, 3852, 3876, 3995, 4226, 4266, 4473, 4529, 4732, 4734, 4867, 5205, 5242, 5247, 5561, 5636, 6972, 7142, 7648, 8272, 8334, 8353, 8423, 9122, 9173, 9180, 9204, 9222, 9267, 3621)

**Universities (verified directly)**
- HWR Berlin — https://www.hwr-berlin.de/en/study/degree-programmes/detail/26-international-marketing-management/
- HWR Berlin, master's application FAQ (ranking, places) — https://www.hwr-berlin.de/en/hwr-berlin/departments-and-bps/department-1-business-and-economics/studying-at-the-department/faqs-applying-for-master-degree-programmes
- KU Eichstätt-Ingolstadt DICE — https://www.ku.de/en/study-offer/bwl-digital-customer-experience-service-design-master
- Hochschule Bonn-Rhein-Sieg, MSc Marketing application (NRW quota) — https://www.h-brs.de/en/masters-degree-programme-marketing-online-application
- Hochschule Osnabrück (50% non-EU reservation, points system) — as above
- TH Nürnberg, MA International Marketing, Bewerbungsablauf — https://www.th-nuernberg.de/fakultaeten/bw/studium/internationale-bachelor-und-masterstudiengaenge/master-international-marketing-ma/bewerbungsablauf/
- TU Chemnitz, MSc Business & Economics, professional requirements — https://www.tu-chemnitz.de/wirtschaft/studium/master/be/application_requirements_prof.html
- Popakademie BW, Zulassung — https://popakademie.de/de/studium/music-and-creative-industries-ma/zulassung/ ; Facts — https://www.popakademie.de/de/studium/music-and-creative-industries-ma/facts/ ; FAQ — https://www.popakademie.de/de/studium/music-and-creative-industries-ma/faq/
- Internationale Hochschule SDI München — https://www.sdi-muenchen.de/hochschule/studium/ma/digital-media-manager
- Leuphana, Arts & Cultural Management application — https://www.leuphana.de/en/professional-school/masters-studies/arts-and-cultural-management/application.html

**Government / official**
- **Ambassade d'Allemagne à Tunis, checklist "Études"** — https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172 *(the €11,904 figure, the unconditional-admission requirement, TLScontact waiting list)*
- Auswärtiges Amt, blocked account — https://www.auswaertiges-amt.de/en/sperrkonto/388600
- Make it in Germany, EU Blue Card — https://www.make-it-in-germany.com/en/visa-residence/types/eu-blue-card
- Make it in Germany, prospects after graduation (18-month permit) — https://www.make-it-in-germany.com/en/study-vocational-training/studies-in-germany/prospects-after
- MWK Baden-Württemberg, fees for international students — https://mwk.baden-wuerttemberg.de/de/hochschulen-studium/studieren-in-bw/studienfinanzierung/gebuehren-fuer-internationale-studierende-und-zweitstudium
- DAAD, costs of education and living (DZHW 22nd Social Survey 2023) — https://www.daad.de/en/studying-in-germany/living-in-germany/finances/
- anabin (KMK) public API — https://anabin.kmk.org/api/public/

**Access notes for future agents**
- DAAD IP database search API: `https://www2.daad.de/deutschland/studienangebote/international-programmes/api/solr/en/search.json?q=<term>&degree[]=2&lang[]=2&limit=60` — `degree[]=2` = master's, `lang[]=2` = English. **Do not send `display`/`sort` params — they zero out `courses` while leaving facets populated.** Detail pages at `/en/detail/<id>/` are **server-rendered** and carry the verbatim admission block.
- `www2.daad.de` rate-limits: sleep ≥1.5 s between requests or the connection is reset.
- **make-it-in-germany blocks WebFetch (Radware) but yields to Firecrawl `--proxy auto`.**
- **Hochschulkompass advanced search 404s to automated fetchers — unsolved.**
