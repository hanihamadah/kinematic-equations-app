#!/usr/bin/env python3
"""Build the Part III grading rubric in two forms: large-font HTML + printable PDF.
Point scheme: METHOD + ANSWER split (partial credit for correct setup)."""

# ----------------------------------------------------------------------------
# RUBRIC DATA  — each part: (label, prompt+pts, [solution lines], [(split, pts)])
# ----------------------------------------------------------------------------
RUBRIC = [
 ("Q1", "Forces on a block (6 pts)",
  "Given: m = 4 kg, F₁ = +18 N (right), F₂ = −6 N (left), frictionless.",
  [("a) Net force (2 pts)",
    ["Fnet = F₁ + F₂ = (+18) + (−6) = +12 N (to the right)"],
    [("Setup Fnet = F₁ + F₂", 1), ("+12 N with direction", 1)]),
   ("b) Acceleration (2 pts)",
    ["a = Fnet / m = 12 / 4 = +3 m/s² (to the right)"],
    [("Setup a = Fnet/m", 1), ("+3 m/s² with direction", 1)]),
   ("c) Balanced or unbalanced? (2 pts)",
    ["Unbalanced — Fnet ≠ 0 (Fnet = +12 N), so the block accelerates right."],
    [("States 'unbalanced'", 1), ("Justifies: Fnet ≠ 0", 1)])]),

 ("Q2", "Suitcase in an elevator (6 pts)",
  "Given: m = 25 kg, g = 10 m/s², elevator at rest.",
  [("a) Weight Fg (3 pts)",
    ["Fg = m·g = 25 × 10 = 250 N (downward)"],
    [("Formula Fg = m·g", 1), ("Substitute 25 × 10", 1), ("250 N downward", 1)]),
   ("b) Normal force Fn (3 pts)",
    ["At rest a = 0 → Fnet = 0 → Fn − Fg = 0 → Fn = Fg",
     "Fn = 250 N (upward)"],
    [("Reasoning a = 0 → Fn = Fg", 1), ("Setup Fn − Fg = 0", 1), ("250 N upward", 1)])]),

 ("Q3", "Worker pulls a toolbox (5 pts)",
  "Given: F_pull = 50 N (horizontal), f = 15 N (opposes), d = 20 m.",
  [("a) Work by the pull (2 pts)",
    ["Pull ∥ displacement → θ = 0°, cos0 = 1",
     "W_pull = F·d·cos0 = 50 × 20 × 1 = +1000 J"],
    [("Uses cos0 = 1 (W = F·d·cosθ)", 1), ("+1000 J", 1)]),
   ("b) Work by friction (2 pts)",
    ["Friction opposes → θ = 180°, cos180 = −1",
     "W_f = f·d·cos180 = −(15)(20) = −300 J"],
    [("Uses cos180 = −1 (negative work)", 1), ("−300 J", 1)]),
   ("c) Net work (1 pt)",
    ["W_net = W_pull + W_f = (+1000) + (−300) = +700 J"],
    [("+700 J", 1)])]),

 ("Q4", "Work–energy theorem (6 pts)",
  "Given: m = 3 kg, vᵢ = 4 m/s, W_net = +30 J.",
  [("a) Initial KEᵢ (3 pts)",
    ["KEᵢ = ½·m·vᵢ² = ½ × 3 × 4² = ½ × 3 × 16 = 24 J"],
    [("Formula KE = ½mv²", 1), ("Substitute ½×3×16", 1), ("24 J", 1)]),
   ("b) Final KE_f via W_net = ΔKE (3 pts)",
    ["W_net = KE_f − KEᵢ → KE_f = W_net + KEᵢ = 30 + 24 = 54 J"],
    [("Uses W_net = ΔKE", 1), ("Substitute 30 + 24", 1), ("54 J", 1)])]),

 ("Q5", "Energy of a falling ball (6 pts)",
  "Given: m = 0.5 kg, h = 5 m, g = 10, released from rest (vᵢ = 0), ground h = 0.",
  [("a) PEg at release + state KE (3 pts)",
    ["PEg = m·g·h = 0.5 × 10 × 5 = 25 J",
     "At release vᵢ = 0 → KE = 0 J"],
    [("Formula PEg = mgh", 1), ("25 J", 1), ("KE = 0 J at release", 1)]),
   ("b) Total mechanical energy ME (3 pts)",
    ["ME = KE + PEg = 0 + 25 = 25 J"],
    [("Uses ME = KE + PEg", 1), ("Substitute 0 + 25", 1), ("25 J", 1)])]),

 ("Q6", "Momentum of a ball (5 pts)",
  "Given: m = 2 kg, v₁ = +8 m/s (right), v₂ = −8 m/s (left); right positive.",
  [("a) Momentum p₁ (2 pts)",
    ["p₁ = m·v₁ = 2 × (+8) = +16 kg·m/s (to the right)"],
    [("Setup p = m·v", 1), ("+16 kg·m/s right", 1)]),
   ("b) New momentum p₂ (2 pts)",
    ["p₂ = m·v₂ = 2 × (−8) = −16 kg·m/s (to the left)"],
    [("Setup p = m·v", 1), ("−16 kg·m/s left", 1)]),
   ("c) Change in momentum Δp (1 pt)",
    ["Δp = p₂ − p₁ = (−16) − (+16) = −32 kg·m/s (to the left)"],
    [("−32 kg·m/s", 1)])]),

 ("Q7", "Impulse on a cart (6 pts)",
  "Given: F = +40 N, m = 5 kg, vᵢ = 0 (at rest), Δt = 0.5 s, frictionless.",
  [("a) Impulse J (2 pts)",
    ["J = F·Δt = 40 × 0.5 = +20 N·s"],
    [("Setup J = F·Δt", 1), ("+20 N·s", 1)]),
   ("b) Initial momentum pᵢ (2 pts)",
    ["pᵢ = m·vᵢ = 5 × 0 = 0 kg·m/s (starts at rest)"],
    [("Setup pᵢ = m·vᵢ", 1), ("0 kg·m/s", 1)]),
   ("c) Final momentum p_f via J = Δp (2 pts)",
    ["p_f = pᵢ + J = 0 + 20 = +20 kg·m/s (direction of force)"],
    [("Uses J = Δp = p_f − pᵢ", 1), ("+20 kg·m/s", 1)])]),

 ("Q8", "Baseball struck by a bat (6 pts)",
  "Given: m = 0.15 kg, vᵢ = +30 m/s, v_f = −20 m/s, Δt = 0.02 s.",
  [("a) Initial & final momenta (2 pts)",
    ["pᵢ = m·vᵢ = 0.15 × (+30) = +4.5 kg·m/s",
     "p_f = m·v_f = 0.15 × (−20) = −3.0 kg·m/s"],
    [("Setup p = m·v", 1), ("+4.5 and −3.0 kg·m/s", 1)]),
   ("b) Change in momentum Δp (2 pts)",
    ["Δp = p_f − pᵢ = (−3.0) − (+4.5) = −7.5 kg·m/s"],
    [("Setup Δp = p_f − pᵢ", 1), ("−7.5 kg·m/s", 1)]),
   ("c) Force from the bat (2 pts)",
    ["F = Δp / Δt = (−7.5) / (0.02) = −375 N (opposite to initial motion)"],
    [("Uses F = Δp/Δt", 1), ("−375 N", 1)])]),

 ("Q9", "Two skaters push off (7 pts)",
  "Given: m₁ = 60 kg (rest), m₂ = 40 kg (rest); after push v₁f = −2 m/s. Left −, right +.",
  [("a) Total momentum before push (2 pts)",
    ["Both at rest → p_total,i = 0 kg·m/s (system initially at rest)"],
    [("p_total,i = 0", 1), ("Justifies: both at rest", 1)]),
   ("b) Velocity of 40 kg skater after push (5 pts)",
    ["0 = m₁·v₁f + m₂·v₂f",
     "0 = (60)(−2) + (40)·v₂f = −120 + 40·v₂f",
     "v₂f = +120 / 40 = +3 m/s (to the right — opposite the 60 kg skater)"],
    [("Conservation: 0 = m₁v₁f + m₂v₂f", 2),
     ("Substitute values", 1), ("Solve for v₂f", 1), ("+3 m/s with direction", 1)])]),

 ("Q10", "Car collision — perfectly inelastic (7 pts)",
  "Given: m_A = 1200 kg, v_Ai = +25 m/s (east); m_B = 1800 kg, v_Bi = 0; cars lock.",
  [("a) Total momentum before (2 pts)",
    ["p_total,i = m_A·v_Ai + m_B·v_Bi = (1200)(+25) + (1800)(0)",
     "p_total,i = +30,000 kg·m/s (east)"],
    [("Setup p = m_Av_A + m_Bv_B", 1), ("+30,000 kg·m/s east", 1)]),
   ("b) Common velocity after (5 pts)",
    ["p_before = (m_A + m_B)·v_f → +30,000 = 3000·v_f",
     "v_f = 30,000 / 3000 = +10 m/s (east)"],
    [("Inelastic: p_i = (m_A+m_B)v_f", 2),
     ("Substitute 30,000 = 3000·v_f", 1), ("Solve", 1), ("+10 m/s east", 1)])]),

 ("BONUS", "Braking with impulse (3 pts — Extra Credit)",
  "Given: m = 1500 kg, vᵢ = +20 m/s, v_f = 0, F = −300 N.",
  [("Time to stop (3 pts)",
    ["J = Δp = m·v_f − m·vᵢ = (1500)(0) − (1500)(+20) = −30,000 kg·m/s",
     "J = F·Δt → Δt = J / F = (−30,000) / (−300) = 100 s"],
    [("J = Δp = mv_f − mvᵢ", 1), ("J = −30,000 kg·m/s", 1), ("Δt = 100 s", 1)])]),
]

# ----------------------------------------------------------------------------
# 1) HTML
# ----------------------------------------------------------------------------
def build_html():
    css = """
    *{box-sizing:border-box;} body{font-family:-apple-system,BlinkMacSystemFont,
    "Segoe UI",Arial,sans-serif;margin:0;padding:22px;color:#111;background:#fff;}
    h1{font-size:32px;margin:0 0 4px;} .sub{font-size:17px;color:#444;margin:0 0 14px;}
    .policy{border:3px solid #c00;background:#fff4f4;color:#900;padding:11px 15px;
    border-radius:8px;font-weight:700;font-size:19px;margin:0 0 22px;}
    .q{border:2px solid #999;border-radius:12px;padding:0 0 14px;margin:0 0 22px;
    overflow:hidden;break-inside:avoid;}
    .qhead{background:#111;color:#fff;padding:10px 16px;font-size:23px;font-weight:800;}
    .given{font-size:16px;color:#333;font-style:italic;padding:10px 16px 4px;}
    .part{padding:6px 16px 4px;}
    .plabel{font-size:19px;font-weight:800;color:#0040c0;margin:8px 0 4px;}
    .sol{font-size:19px;line-height:1.45;margin:2px 0;}
    .ans{font-weight:800;color:#0040c0;}
    .split{margin:6px 0 2px;}
    .badge{display:inline-block;background:#e8f5e9;border:1px solid #0a7a00;color:#0a7a00;
    border-radius:6px;padding:3px 9px;font-size:15px;font-weight:700;margin:3px 6px 3px 0;}
    @media print{body{padding:8px;}.q{break-inside:avoid;}
    .policy,.qhead{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
    .badge{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
    """
    out = ['<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">',
           '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
           '<title>Part III Rubric — Physics Final</title><style>', css,
           '</style></head><body>',
           '<h1>Part III — Grading Rubric</h1>',
           '<p class="sub">Problem Solving (60 pts) + Bonus (3 pts). g = 10 m/s². '
           'Right / up / east positive. Scoring = <b>method + answer split</b>.</p>',
           '<p class="policy">⚖ PARTIAL CREDIT: award the method marks even if the '
           'final number is wrong. Green badges = where each point goes.</p>']
    def esc(s):
        return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    for num, title, given, parts in RUBRIC:
        out.append('<div class="q">')
        out.append(f'<div class="qhead">{esc(num)} · {esc(title)}</div>')
        out.append(f'<div class="given">{esc(given)}</div>')
        for plabel, lines, splits in parts:
            out.append('<div class="part">')
            out.append(f'<div class="plabel">{esc(plabel)}</div>')
            for ln in lines:
                out.append(f'<div class="sol">{esc(ln)}</div>')
            out.append('<div class="split">')
            for desc, pts in splits:
                out.append(f'<span class="badge">{esc(desc)} = {pts} pt</span>')
            out.append('</div></div>')
        out.append('</div>')
    out.append('</body></html>')
    with open("part3-rubric.html","w") as f:
        f.write("\n".join(out))
    print("part3-rubric.html written")

# ----------------------------------------------------------------------------
# 2) PDF (platypus, flowing multi-page)
# ----------------------------------------------------------------------------
def build_pdf():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                    TableStyle, KeepTogether)
    BLUE = HexColor("#0040c0"); DARK = HexColor("#111111")
    GREEN = HexColor("#0a7a00"); GREENBG = HexColor("#e8f5e9")
    RED = HexColor("#c00000"); REDBG = HexColor("#fff4f4")
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle("h1", parent=styles["Title"], fontSize=22, spaceAfter=4,
                        textColor=DARK, alignment=0)
    sub = ParagraphStyle("sub", parent=styles["Normal"], fontSize=11, textColor=HexColor("#444"))
    qhead = ParagraphStyle("qhead", parent=styles["Normal"], fontSize=15,
                           textColor=white, fontName="Helvetica-Bold", leading=20)
    given = ParagraphStyle("given", parent=styles["Normal"], fontSize=10.5,
                           textColor=HexColor("#333"), fontName="Helvetica-Oblique", spaceAfter=2)
    plab = ParagraphStyle("plab", parent=styles["Normal"], fontSize=12.5,
                          textColor=BLUE, fontName="Helvetica-Bold", spaceBefore=6, spaceAfter=2)
    sol = ParagraphStyle("sol", parent=styles["Normal"], fontSize=12, leading=16)
    badge = ParagraphStyle("badge", parent=styles["Normal"], fontSize=9.5,
                           textColor=GREEN, fontName="Helvetica-Bold")
    doc = SimpleDocTemplate("part3-rubric.pdf", pagesize=A4,
                            leftMargin=14*mm, rightMargin=14*mm,
                            topMargin=12*mm, bottomMargin=12*mm)
    story = [Paragraph("Part III — Grading Rubric", h1),
             Paragraph("Problem Solving (60 pts) + Bonus (3 pts). g = 10 m/s². "
                       "Right / up / east positive. Scoring = method + answer split.", sub),
             Spacer(1, 6)]
    pol = Table([[Paragraph("⚖ PARTIAL CREDIT: award method marks even if the final "
                  "number is wrong. Green badges show where each point goes.",
                  ParagraphStyle("p", parent=sub, textColor=RED, fontName="Helvetica-Bold",
                                 fontSize=11))]], colWidths=[doc.width])
    pol.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),REDBG),
                             ("BOX",(0,0),(-1,-1),1.5,RED),
                             ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
                             ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
    story += [pol, Spacer(1, 10)]

    for num, title, gtext, parts in RUBRIC:
        block = []
        head = Table([[Paragraph(f"{num} &middot; {title}", qhead)]], colWidths=[doc.width])
        head.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),DARK),
                                  ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
                                  ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
        block += [head, Spacer(1,3), Paragraph(gtext, given)]
        for plabel, lines, splits in parts:
            block.append(Paragraph(plabel, plab))
            for ln in lines:
                block.append(Paragraph(ln, sol))
            cells = [Paragraph(f"{d} = {p} pt", badge) for d, p in splits]
            bt = Table([cells], colWidths=[doc.width/len(cells)]*len(cells))
            bstyle = [("BACKGROUND",(0,0),(-1,-1),GREENBG),("BOX",(0,0),(-1,-1),0.5,GREEN),
                      ("INNERGRID",(0,0),(-1,-1),0.5,GREEN),
                      ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
                      ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
                      ("VALIGN",(0,0),(-1,-1),"MIDDLE")]
            bt.setStyle(TableStyle(bstyle))
            block += [Spacer(1,2), bt]
        story += [KeepTogether(block), Spacer(1, 12)]
    doc.build(story)
    print("part3-rubric.pdf written")

if __name__ == "__main__":
    build_html()
    build_pdf()
