import cv2
import numpy as np

# Fonction pour supprimer le fond d'une image

def remove_bg(img_name) :
    # Chemin de l'image
    path = "path/to/image"

    # Charger l'image
    img = cv2.imread(path + img_name + ".jpg")

    # Convertir l'image en échelle de gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou gaussien pour réduire le bruit de l'image
    blur = cv2.GaussianBlur(gray, (255, 255), 0)

    # Définir un seuil pour créer un masque binaire
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # Trouver les contours de l'image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Créer un masque blanc pour remplacer le fond
    mask = np.zeros(img.shape[:2], np.uint8)
    cv2.drawContours(mask, contours, -1, 255, -1)

    # Appliquer le masque à l'image d'origine
    result = cv2.bitwise_and(img, img, mask=mask)

    # Enregistrer l'image résultante en tant que fichier PNG transparent
    cv2.imwrite(path + img_name + "_sans_fond.png", result)

# Appeler la fonction pour supprimer le fond d'une image
remove_bg("image_name")