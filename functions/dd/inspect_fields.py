from pdfrw import PdfReader

def extract_field_names(pdf_path):
    pdf = PdfReader(pdf_path)
    field_names = set()

    for page in pdf.pages:
        if '/Annots' in page:
            for annot in page['/Annots']:
                field_name = annot.get('/T')

                if field_name:
                    field_name = field_name.strip('()')
                    field_names.add(field_name)

    return list(field_names)

pdf_path = '/Users/angela.romanovska/my-scripts/trading-calculator/functions/dd/pdf.pdf'
field_names = extract_field_names(pdf_path)
print("Extracted Field Names:", field_names)
