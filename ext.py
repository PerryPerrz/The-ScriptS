import os

# Script permettant de renommer des fichiers d'un dossier en changeant leur extension

# Chemin vers le dossier contenant les fichiers à renommer
folder_path = "path/to/folder"

# Extension d'origine
ext_orig = ".vid"

# Extension finale
ext_finale = ".mp4"

for filename in os.listdir(folder_path):
    if filename.endswith(ext_orig):
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, filename[:-4] + ext_finale))
