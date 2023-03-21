import pdfplumber


def read_pdf_by_name(name):
    pdf_str = ''
    with pdfplumber.open(name) as pdf:
        for page in pdf.pages:
            pdf_str = pdf_str + page.extract_text()

    return pdf_str
