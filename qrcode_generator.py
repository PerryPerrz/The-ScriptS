import qrcode

# Définir une fonction pour générer le QR code
def generate_qrcode(link, filename):
    # Générer le QR code en utilisant la bibliothèque qrcode
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    # Créer une image du QR code et l'enregistrer dans un fichier
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename + ".png")

# Entrer le lien que vous souhaitez encoder dans le QR code
link = input("Entrez le lien à encoder dans le QR code : ")
filename = input("Entrez le nom du fichier à créer : ")

# Appeler la fonction pour générer le QR code
generate_qrcode(link, filename)