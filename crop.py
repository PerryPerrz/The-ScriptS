from PIL import Image, ImageDraw

# Script permettant de découper une image et de sauvegarder le résultat

# Charger l'image originale
original_image = Image.open("path/to/image/original.jpg")

# Récupérer les coordonnées du rectangle
x1, y1, x2, y2 = 0, 200, 200, 400  # Mettre vos propres valeurs ici

# Créer une nouvelle image avec la même taille que la région découpée
cropped_region = original_image.crop((x1, y1, x2, y2))
cropped_size = cropped_region.size
cropped_image = Image.new('RGB', cropped_size)

# Dessiner le rectangle sur la nouvelle image
draw = ImageDraw.Draw(cropped_image)
draw.rectangle((0, 0, cropped_size[0], cropped_size[1]), fill=None, outline=(255, 0, 0))

# Coller la région découpée sur la nouvelle image
cropped_image.paste(cropped_region, (0, 0))

# Enregistrer l'image générée
cropped_image.save("path/to/image/cropped.jpg")