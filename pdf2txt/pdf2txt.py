import os
import sys
from PyPDF2 import PdfReader

# Author : Hugo IOPETI
# Date : 05/06/2023
# Description : Script permettant de convertir un fichier PDF en fichier texte

def save_pdf_pages(pdf_path, output_dir):
    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    # Ouvrir le fichier PDF
    with open(pdf_path, "rb") as f:
        pdf = PdfReader(f)
        total_pages = len(pdf.pages)

        # Parcourir chaque page du PDF
        for page_num in range(total_pages):
            # Obtenir la page actuelle
            page = pdf.pages[page_num]

            # Enregistrer le texte de la page dans un fichier
            output_path = os.path.join(output_dir, f"page_{page_num + 1}.txt")
            with open(output_path, "w", encoding="utf-8") as output_file:
                output_file.write(page.extract_text())

            print(f"Page {page_num + 1} enregistrée : {output_path}")

# Vérifier si le bon nombre d'arguments est fourni
if len(sys.argv) != 3:
    print("Utilisation : python script.py <pdf_path> <output_dir>")
    print("Exemple : python pdf2txt.py pdf_a_recup.pdf res")
    sys.exit(1)

# Récupérer les arguments du programme
pdf_path = sys.argv[1]
output_dir = sys.argv[2]

# Appeler la fonction pour enregistrer les pages du PDF
save_pdf_pages(pdf_path, output_dir)