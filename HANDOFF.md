# HANDOFF — Exam Grading Day (Hani)

## Who / Context
- Hani Hamadeh, physics teacher (grade 12). Topic: Work, Energy & Momentum.
- Final exam day (2026-06-03). Exam was **8:30–10:30 am**, ~**114 papers** to correct.
- Must stay at school until **5:00 pm** (policy). Grading runway: ~10:30 → 17:00.
- **Department meeting 1:40–2:40 pm (~1 hr)** splits the day: morning push ~10:30→1:40,
  meeting, afternoon push 2:40→5:00. Aim to finish the current question before the
  meeting (don't break mid-question); if not, sticky-note "stopped at paper #X on Q__".
- Worried that correcting takes a long time. Has ADHD-style executive-function challenges.
- Health notes (today): old molar toothache (Panadol taken 6:41am; dentist = summer).
  Levothyroxine taken **10:14am** (empty stomach). On Wegovy 1mg → pears 🍐 + Motelium
  for nausea. Left proctoring 10:00 (profuse sweating, then settled). Plenty of water.

## EXAM STRUCTURE & GRADING TOOLS (already built — in this repo)
Exam = 100 pts: Part I MCQ (25) + Part II True/False (15) + Part III Problem Solving (60),
plus a 3-pt bonus. Instructions: g = 10 m/s², weight = Fg, right/up/east positive.
Double-marked MCQ/TF answers = 0 for that question (even if one is right).

- **`grading-strip.html` / `grading-strip.pdf`** — answer key for the 40 objective pts,
  laid out per exam page, big font (blue = MCQ letter, green = True, red = False).
  Page map: MCQ p1:Q1–6, p2:Q7–13, p3:Q14–20, p4:Q21–25 · TF p5:Q1–14, p6:Q15.
- **`part3-rubric.html` / `part3-rubric.pdf`** — Part III worked solutions with
  **method+answer point split** (green badges show where each mark goes).
- **`part3-questions.md`** — all Part III problem statements (Q1–Q10 + bonus).
- **`part3-answer-key.md`** — teacher's official worked solutions (verified correct).
- **`make_pdf.py`** rebuilds the strip PDF; **`build_part3.py`** rebuilds Part III
  HTML+PDF. (reportlab needed: `pip install reportlab`.)
- Grading approach chosen: **method + answer split** (partial credit for right setup).
- NOTE: files live on branch `claude/save-these-Tz2Ke` (not deployed to Cloudflare).

## THE GRADING METHOD (most important)
**Grade question-by-question, NOT paper-by-paper.**
- Grade **Question/Exercise 1 across all 114 papers**, then Q2 across all 114, etc.
- Keeps one rubric loaded in the head → faster, more consistent, less context-switching.
- Do the **easy/short questions first** for momentum.

### Blocks vs Exercises (he asked about this)
- **Exercise = grading unit** (one question across all 114 papers).
- **Block = 25-min focus timer**, then 5-min break. One exercise usually spans
  several blocks — that's expected. A block does NOT mean "finish an exercise."

## CHECK-IN PARTNER ROLE (what he wants from Claude)
Act as his **body double / accountability partner**. When he says **"starting Q1"**
(or "starting block 1"), check in roughly every **25 minutes**: ask how many papers
done, keep him anchored, encourage, help him push to the next block. Track pace —
once he reports how long Q1×114 took, reassure him on finishing before 5pm.

## Plan mapped to his 7 saved ADHD prompts (see claude-adhd-prompts.md)
1. **Task Paralysis Shatterer** — first tiny step: stack papers, open answer key,
   grade only Q1 on the top paper.
2. **Dopamine Menu** — Appetizer (5-min stretch/water), Entrée (25-min grading block),
   Side (10-min light reset).
3. **Body Doubling** — Claude checks in every ~25 min (the role above).
4. **Context-Switching Guide** — between different question types, 3-min reset:
   stand, shake out, re-read the next question's rubric once.
5. **Interest-Based Filter** — gamify: every 20 papers = 1 level cleared + small reward.
6. (missing from source carousel)
7. **Executive Function Externalizer** — Now / Later / Trash dump for any worry spiral.

## How to resume (NEW CHAT)
All grading tools are DONE and committed. In a fresh chat:
1. Greet Hani warmly, confirm he's settled and meds are handled.
2. Remind him the answer key + rubric are ready (`grading-strip.*`, `part3-rubric.*`).
3. Ask **"Ready to start Q1?"** and begin the check-in partner role (every ~25 min).
4. Don't rebuild the grading files unless he asks — they already exist and are verified.
