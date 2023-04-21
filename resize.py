from PIL import Image
import os

# Script permettant de redimensionner toutes les images d'un dossier

# Chemin du dossier contenant les images
folder_path = "path/to/folder"

# Définition de la taille maximale souhaitée
max_size = (940, 1648)

# Parcours de tous les fichiers du dossier
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):

        # Ouverture de l'image avec Pillow
        img = Image.open(os.path.join(folder_path, filename))

        # Redimensionnement de l'image tout en conservant le ratio
        img.thumbnail(max_size)

        # Définition du taux de qualité souhaité (entre 0 et 100)
        quality = 100
        
        # Enregistrement de l'image redimensionnée dans le même dossier
        img.save(os.path.join(folder_path, filename), optimize=True, quality=quality)
