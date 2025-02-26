# # from docx import Document
from pathlib import Path
from docxtpl import DocxTemplate
# import subprocess
file_path = Path("C:/Users/savas/OneDrive/Desktop/doc_to_pdf/devis.docx")


doc = DocxTemplate(file_path)


data = {
    "entreprise": "Savas poultry advising",
    "adresse": "Av mohammed 5 no 166",
    "ville": "Kenitra",
    "client_name": "Ahmed savas",
    "client_adresse": "Rue 5 no 77",
    "client_city": 'sidi yahia gharb'
}

doc.render(data)
doc.save("devisTest.docx")


from docx2pdf import convert
file_path_2 = Path("C:/Users/savas/OneDrive/Desktop/doc_to_pdf/devisTest.docx")

convert(file_path_2)