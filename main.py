# # from docx import Document
from pathlib import Path
from docxtpl import DocxTemplate
from docx2pdf import convert
import weasyprint
# # import subprocess
# file_path = Path("C:/Users/savas/OneDrive/Desktop/doc_to_pdf/devis.docx")


# doc = DocxTemplate(file_path)


# data = {
#     "entreprise": "Savas poultry advising",
#     "adresse": "Av mohammed 5 no 166",
#     "ville": "Kenitra",
#     "client_name": "Ahmed savas",
#     "client_adresse": "Rue 5 no 77",
#     "client_city": 'sidi yahia gharb'
# }

# doc.render(data)
# doc.save("devisTest.docx")


# file_path_2 = Path("C:/Users/savas/OneDrive/Desktop/doc_to_pdf/devisTest.docx")

# convert(file_path_2)


html_content = """
<html>
    <head>
        <title>Sample PDF</title>
    </head>
    <body>
        <h1>Hello, WeasyPrint!</h1>
        <p>This is a sample PDF generated from HTML.</p>
    </body>
</html>
"""

# Convert the HTML string to PDF
pdf = weasyprint.HTML(string=html_content).write_pdf()

# Save the PDF to a file
with open("output.pdf", "wb") as f:
    f.write(pdf)
