## Description

Ce script est utilisé pour convertir un fichier PDF en une séquence de fichiers texte, où chaque fichier texte représente une page du PDF. Le script utilise la bibliothèque PyPDF2 pour lire le fichier PDF et extraire le texte de chaque page.

## Installation

> pip install PyPDF2

## Utilisation

Il faut penser à mettre le script au même niveau que le fichier PDF à convertir. Le dossier contenant les fichiers texte sera créé au même niveau que le fichier PDF.

> python pdf2txt.py <inputfile.pdf> <outputdir>

Développé avec Python 3.10.0