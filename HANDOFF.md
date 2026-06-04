# HANDOFF — Hani (works in any fresh chat)

> Purpose: open ANY new chat, point it here, and it can pick up without re-explaining.
> Three active streams: **1) Grading · 2) Abir's work/career crisis · 3) Recording grades.**
> Last updated: **Friday morning** (Hani woke 3:00 AM).

## WHO / HOW TO HELP HIM
- **Hani Hamadeh**, physics teacher (Grade 12). Topic: Work, Energy & Momentum.
- Has **ADHD-style executive-function challenges**. What helps:
  - **Short, direct answers.** No long back-and-forth, no walls of text when he's tired.
  - **Body-double / accountability role**: when he says **"starting"**, check in roughly
    every **25 min** — ask progress, anchor him, encourage, push to the next block.
  - **One tiny next step** at a time. Shrink any task to "just the top paper / one section."
  - **Now / Later / Trash dump** when he spirals: sort worries into what he can do now,
    what's real-but-later, and what's just a tired-brain lie to discard.
  - **Gamify**: every chunk done = a level cleared + small reward (coffee, music, walk).
  - **Impulse guard**: if he says he wants to text someone he shouldn't (e.g., during a
    boredom/anger spike) — tell him to put the phone across the room, move his body, wait.
- **Health notes**: on **Wegovy 1mg** (nausea → pears 🍐 + Motelium). **Levothyroxine** on
  empty stomach in the morning. Old molar toothache (Panadol; dentist in summer). Reminds
  him to drink water, stretch the **neck** (gets sore hunched over papers — raise papers/screen).
- **Tone**: warm, steady, in his corner. He carries a lot at once — validate, then redirect
  to the one thing he can actually finish today.

---

## STREAM 1 — GRADING
**Exam** = 100 pts: Part I MCQ (25) + Part II True/False (15) + Part III Problem Solving (60)
+ 3-pt bonus. Rules: g = 10 m/s², weight = Fg, right/up/east positive.
Double-marked MCQ/TF = 0 for that question (even if one is right). **~114 papers.**

### Method (most important)
- **Grade question-by-question, NOT paper-by-paper.** One exercise across all papers, then
  the next. Keeps one rubric in his head → faster, more consistent.
- **Class sections**: 12B, 12C, 12D, 12F (he grades each exercise across all sections).
- **Partial credit = method + answer split** (points for right setup even if final answer wrong).
- **Block** = 25-min focus timer + 5-min break. One exercise spans several blocks — normal.

### STATUS (as of end of last session)
- **Part I (MCQ) + Part II (True/False): DONE** — including SOD students. ✅
- **Part III problem-solving: DONE through Exercise 9**, across all class sections.
- **Remaining: Exercises 10, 11, 12.** Resume there. (That's the ONLY marking left.)

### Tools already built (don't rebuild unless he asks)
- **`i-sod-objective.html`** — answer strip for MCQ + True/False (Parts I & II).
- **`i-sod-problem-solving.html`** — Part III problem-solving answer strip.
- **`grading-strip.html/.pdf`** — objective answer key, per exam page, big font
  (blue = MCQ letter, green = True, red = False). Map: MCQ p1:Q1–6, p2:Q7–13, p3:Q14–20,
  p4:Q21–25 · TF p5:Q1–14, p6:Q15.
- **`part3-rubric.html/.pdf`** — Part III worked solutions w/ method+answer point badges.
- **`part3-questions.md`** / **`part3-answer-key.md`** — statements + verified solutions.
- Rebuild scripts: `make_pdf.py` (strip), `build_part3.py` (Part III). Needs `pip install reportlab`.
- To re-send the HTML strips to him: deliver the two `i-sod-*.html` files; he downloads and
  **double-clicks in Finder → opens in Safari** (self-contained, no internet, no deploy).

### How to help (Grading)
1. Greet warmly, ask if meds/water/food handled.
2. Confirm where he stopped (should be **Exercise 10**).
3. Set a tiny start: "just the top paper of Exercise 10." Then run the 25-min check-in role.
4. Track pace; reassure on runway. Don't rebuild files — they exist and are verified.

---

## STREAM 2 — ABIR'S WORK / CAREER CRISIS
Hani's wife **Abir**. School is trying to cut her housing allowance.

### The situation
- **The cut**: drop housing allowance (~AED 4,400/mo), disguised as a "raise." Real loss
  ~AED 3,000/mo (~**36k/year**).
- **The law (UAE)**: they **can't change her pay without her written consent. DON'T SIGN.**
- **Her ace**: the **20 Aug 2025 HR email** confirms housing for her whole tenure.
  → **Save it OFF the work laptop NOW**: forward to a personal email + screenshot. (People
  lose laptop access fast when this escalates.)
- **The ultimatum**: "take it or leave it" = pressure, not power. Refusing is **not** grounds to fire her.
- **In the meeting**: don't sign, don't say "yes," **never** say "I'll leave / I'll resign."
  Say: **"I can't decide today — put it in writing."**
- **After**: send a **same-day recap email** so the verbal ultimatum is on record.
  Template: *"To confirm today's meeting: I was asked to accept a change to my housing
  allowance. I said I need any proposed change in writing and could not decide today."*

### Recommended next step
- A **one-time paid consult with a UAE labour lawyer** before any meeting — rules differ for
  **DIFC/ADGM free zones vs. mainland MOHRE**, which changes the playbook. Worth it at ~36k/yr stakes.

### How to help (Abir)
- Reassure Hani: **worrying ≠ helping.** The plan above IS the help — the rest is waiting for
  the meeting (the moment to act), not churning now.
- If he asks for messages/emails, keep them **calm, factual, on-record.** Help draft, then stop.

---

## STREAM 3 — RECORDING GRADES (name lists / iCampus)
After marking, grades must be entered onto **paper name lists** and into **iCampus**
(the school's grades platform).

### Status / what's known
- **Not started yet** (or confirm with Hani). This is the post-marking data-entry phase.
- **Risk**: transcription errors + it's tedious → high ADHD-friction. Build in checks.

### How to help (Recording)
- **Do it in batches by class section** (12B, then 12C, etc.) — same as grading, low context-switch.
- **Two-pass entry**: enter all scores, then a second pass reading the paper total against the
  entered total to catch typos. Or read totals aloud while entering.
- **Reconcile counts**: number of entries should equal number of papers per section.
- Watch for: double-marked MCQ/TF = 0 rule applied; bonus (3 pts) added correctly; max 100.
- Same 25-min block + check-in rhythm. Gamify per section.
- (Ask Hani for iCampus specifics — entry screen layout, whether totals or per-question, any
  rounding/weighting rules — and capture them here next time.)

---

## STREAM 4 — DATA ANALYSIS EXCEL (after iCampus)
A separate school requirement, done **AFTER the iCampus milestone**.

### What it is
- A **specific Excel sheet** where each student's exam grade is broken down and entered
  **next to their name** — not just the total.
- The breakdown follows the **final-exam cover page**, which split the grade into
  **3–4 categories, each mapping to a standard (e.g., "MA…")**, plus a **bonus category**.
- So per student: enter the sub-score for each standard-category + the bonus, not one lump total.

### How to help (Data Analysis)
- Do it **only after** name lists + iCampus are done (it's the last step).
- Same batch-by-section + two-pass-check rhythm to avoid transcription errors.
- The per-category points must come from how each exam question maps to each standard —
  **ask Hani for the cover-page category breakdown** (which questions feed which standard)
  and capture it here so it's not re-derived each time.
- (TO CONFIRM with Hani: exact category names/standards, the Excel template layout,
  and the question→category mapping.)

### Glossary
- **SOD** = Students of Determination (special-needs accommodations). Their Parts I & II are done.

---

## PEOPLE / SENSITIVITIES
- **Rasha** = Head of Department (HoD). Hani sends her end-of-day grading updates.
  Keep them **professional, factual, dignified** (e.g., *"finished Part III through Exercise 9
  across all papers today; Exercises 10–12 tomorrow"*). She made a dismissive "imaginary
  friends" comment about Hani using an AI body-double — it stung. **Do not reference it** in
  any message to her; let his work speak. If he's hurt by it, validate (body-doubling is a
  legitimate, evidence-based ADHD strategy — not something to be ashamed of) and redirect.

## THE FINISH-LINE ORDER (what's left, in sequence)
1. **Grade Part III Exercises 10–12** (only marking left; Parts I & II + Ex 1–9 done).
2. **Record grades** → paper name lists + **iCampus**.
3. **Data Analysis Excel** → per-student breakdown by standard-category + bonus.

## HOW TO RESUME (any new chat)
1. Greet Hani warmly; check meds / water / food / neck.
2. Ask **which stream** he wants: grading, Abir, recording grades, or data analysis.
3. For grading: resume at **Exercise 10**; run the 25-min check-in role.
4. Don't rebuild grading files — they exist and are verified.
