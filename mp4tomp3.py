import os
from moviepy.editor import *

# Script permettant de convertir des fichiers MP4 en fichiers MP3 

# chemin du dossier contenant les fichiers MP4
input_folder = "path/to/folder/containing/mp4/files"

# boucle à travers tous les fichiers dans le dossier d'entrée
for filename in os.listdir(input_folder):

    # vérifier si le fichier est un fichier MP4
    if filename.endswith(".mp4"):

        # construire le chemin complet vers le fichier d'entrée
        input_file = os.path.join(input_folder, filename)

        # construire le chemin complet vers le fichier de sortie MP3
        output_file = os.path.join(input_folder, os.path.splitext(filename)[0] + ".mp3")

        # charger le clip vidéo avec MoviePy
        clip = VideoFileClip(input_file)

        # extraire la piste audio et enregistrer en tant que fichier MP3
        clip.audio.write_audiofile(output_file)

        # fermer le clip vidéo
        clip.close()
