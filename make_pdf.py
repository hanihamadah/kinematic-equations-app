#!/usr/bin/env python3
"""Generate a large-font, color-coded printable grading strip PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas

MCQ_BLUE = HexColor("#0040c0")
T_GREEN  = HexColor("#0a7a00")
F_RED    = HexColor("#c00000")
RED      = HexColor("#c00000")
GREY     = HexColor("#666666")

# Answer data
mcq = {
    "Page 1 · Q1-6":   [(1,"b"),(2,"b"),(3,"d"),(4,"b"),(5,"d"),(6,"c")],
    "Page 2 · Q7-13":  [(7,"d"),(8,"a"),(9,"b"),(10,"d"),(11,"c"),(12,"b"),(13,"c")],
    "Page 3 · Q14-20": [(14,"b"),(15,"c"),(16,"c"),(17,"b"),(18,"b"),(19,"a"),(20,"a")],
    "Page 4 · Q21-25": [(21,"b"),(22,"b"),(23,"c"),(24,"a"),(25,"d")],
}
tf = [(1,"T"),(2,"F"),(3,"T"),(4,"T"),(5,"F"),(6,"T"),(7,"F"),
      (8,"T"),(9,"F"),(10,"T"),(11,"T"),(12,"T"),(13,"T"),(14,"F"),(15,"F")]

PAGE_W, PAGE_H = A4
M = 15 * mm
c = canvas.Canvas("grading-strip.pdf", pagesize=A4)

def header(title):
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(M, PAGE_H - M - 18, title)

def ans_color(a):
    if a == "T": return T_GREEN
    if a == "F": return F_RED
    return MCQ_BLUE

# ---------- PAGE 1: MCQ ----------
header("Grading Strip — MCQ (Part I)")
c.setFont("Helvetica-Bold", 13)
c.setFillColor(RED)
c.drawString(M, PAGE_H - M - 38, "DOUBLE-MARK = 0  (more than one option marked = 0, even if one is right)")

cols = list(mcq.items())
col_w = (PAGE_W - 2*M) / 2
row_h = 30
top = PAGE_H - M - 70
for i, (title, items) in enumerate(cols):
    cx = M + (i % 2) * col_w
    cy = top - (i // 2) * (row_h * 8 + 30)
    # column header
    c.setFillColor(black)
    c.roundRect(cx, cy - 6, col_w - 12, 26, 5, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(cx + (col_w-12)/2, cy + 2, title)
    # rows
    for j, (q, a) in enumerate(items):
        ry = cy - 12 - (j+1) * row_h
        c.setFillColor(GREY)
        c.setFont("Helvetica-Bold", 26)
        c.drawRightString(cx + 55, ry, str(q))
        c.setFillColor(ans_color(a))
        c.setFont("Helvetica-Bold", 34)
        c.drawString(cx + 75, ry - 3, a)
c.showPage()

# ---------- PAGE 2: T/F ----------
header("Grading Strip — True / False (Part II)")
c.setFillColor(black)
c.roundRect(M, PAGE_H - M - 80, PAGE_W - 2*M, 30, 5, fill=1, stroke=0)
c.setFillColor(white)
c.setFont("Helvetica-Bold", 18)
c.drawCentredString(PAGE_W/2, PAGE_H - M - 72, "Page 5 (Q1-14)  +  Page 6 (Q15)")

# two columns of T/F
left = tf[:8]    # 1-8
right = tf[8:]   # 9-15
start_y = PAGE_H - M - 130
row_h = 44
for j, (q, a) in enumerate(left):
    ry = start_y - j * row_h
    c.setFillColor(GREY); c.setFont("Helvetica-Bold", 32)
    c.drawRightString(M + 70, ry, str(q))
    c.setFillColor(ans_color(a)); c.setFont("Helvetica-Bold", 44)
    c.drawString(M + 90, ry - 4, a)
for j, (q, a) in enumerate(right):
    ry = start_y - j * row_h
    cx = PAGE_W/2 + 10
    c.setFillColor(GREY); c.setFont("Helvetica-Bold", 32)
    c.drawRightString(cx + 70, ry, str(q))
    c.setFillColor(ans_color(a)); c.setFont("Helvetica-Bold", 44)
    c.drawString(cx + 90, ry - 4, a)

c.setFillColor(RED); c.setFont("Helvetica-Bold", 13)
c.drawString(M, M + 10, "DOUBLE-MARK = 0  ·  Each correct = 1 pt  ·  MCQ 25 + T/F 15 = 40 objective pts")
c.showPage()
c.save()
print("grading-strip.pdf written")
