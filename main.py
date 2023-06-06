from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Page 1
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Master page
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=150, h=12, txt=row['Topic'], align="L")
    pdf.cell(w=30, h=12, txt=r'Notes', align="R", ln=1)

    for y in range(20, 298, 10):
        pdf.set_draw_color(100, 100, 100)
        pdf.line(10, y, 210, y)

    rows = list(range(15, 170, 10))
    for i,  x in enumerate(rows):
        if i != len(rows) - 1:
            pdf.set_draw_color(237, 237, 237)
            pdf.dashed_line(x, 20, x, 290, dash_length=1, space_length=1)
        else:
            pdf.set_draw_color(100, 100, 100)
            pdf.line(x, 20, x, 290)

    # fOOTER FOR MASTER PAGE
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

        for y in range(20, 298, 10):
            pdf.set_draw_color(100, 100, 100)
            pdf.line(10, y, 210, y)

        rows = list(range(15, 170, 10))
        for i, x in enumerate(rows):
            if i != len(rows) - 1:
                pdf.set_draw_color(237, 237, 237)
                pdf.dashed_line(x, 20, x, 290, dash_length=1, space_length=1)
            else:
                pdf.set_draw_color(100, 100, 100)
                pdf.line(x, 20, x, 290)


pdf.output("output.pdf")
