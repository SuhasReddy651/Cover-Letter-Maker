import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
import os

# Predefined fonts (standard + custom)
FONT_OPTIONS = {
    "Arial": "Helvetica",
    "Times New Roman": "Times-Roman",
    "Oxygen": "fonts/Oxygen.ttf",
    "NotoSans": "fonts/NotoSans.ttf",
    "Inter": "fonts/Inter.ttf"
}

# Register custom TTF fonts
for label, path in FONT_OPTIONS.items():
    if path.endswith(".ttf") and os.path.exists(path):
        pdfmetrics.registerFont(TTFont(label, path))

# Function to generate PDF


def create_cover_letter_pdf(content, company_name, font_name):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=LETTER,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Heading',
                              alignment=TA_CENTER,
                              fontName=font_name,
                              fontSize=16,
                              leading=20))
    styles.add(ParagraphStyle(name='Justified',
                              alignment=TA_JUSTIFY,
                              fontName=font_name,
                              fontSize=12,
                              leading=15))

    flowables = []
    flowables.append(Paragraph("COVER LETTER", styles['Heading']))
    flowables.append(Spacer(1, 20))

    for para in content.strip().split('\n\n'):
        flowables.append(Paragraph(para.strip(), styles['Justified']))
        flowables.append(Spacer(1, 12))

    doc.build(flowables)
    buffer.seek(0)
    return buffer

# UI Part


st.set_page_config(page_title="📄 Cover Letter Generator", page_icon="🖋️")
st.title("📄 Cover Letter PDF Generator with Font Choice")

company_name = st.text_input("Enter Company Name")
cover_letter_text = st.text_area(
    "Paste Your Cover Letter Text Here", height=300)

selected_font = st.selectbox(
    "Choose a Font", options=list(FONT_OPTIONS.keys()))

if st.button("Generate Cover Letter PDF"):
    if not company_name or not cover_letter_text.strip():
        st.warning("Please provide both company name and cover letter text.")
    else:
        font_name = selected_font if selected_font in pdfmetrics.getRegisteredFontNames(
        ) else FONT_OPTIONS[selected_font]
        pdf_file = create_cover_letter_pdf(
            cover_letter_text, company_name, font_name)
        st.success(f"Cover letter generated using font: {selected_font}!")

        st.download_button(
            label="📥 Download PDF",
            data=pdf_file,
            file_name=f"Cover_Letter_{company_name}.pdf",
            mime="application/pdf"
        )
