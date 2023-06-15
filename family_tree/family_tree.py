import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Génère et exporte l'arbre généalogique
def generer_arbre_genealogique():
    G = nx.DiGraph()

    # Ajoutez les nœuds de votre arbre généalogique avec leurs attributs
    G.add_node("Grand-père paternel", gender="Homme", nom="Nom1", prenom="Prenom1", date_naissance="01/01/1950", date_deces="01/01/2000", origine="France")
    G.add_node("Grand-mère paternelle", gender="Femme", nom="Nom2", prenom="Prenom2", date_naissance="01/01/1960", date_deces="01/01/2010", origine="Belgique")
    G.add_node("Grand-père maternel", gender="Homme", nom="Nom3", prenom="Prenom3", date_naissance="01/01/1970", date_deces="01/01/2020", origine="Luxembourg")
    G.add_node("Grand-mère maternelle", gender="Femme", nom="Nom4", prenom="Prenom4", date_naissance="01/01/1980", date_deces="01/01/2030", origine="Italie")
    G.add_node("Père", gender="Homme", nom="Nom5", prenom="Prenom5", date_naissance="01/01/1990", date_deces="undefined", origine="Allemagne")
    G.add_node("Mère", gender="Femme", nom="Nom6", prenom="Prenom6", date_naissance="01/01/2000", date_deces="undefined", origine="Espagne")
    G.add_node("Moi", gender="Homme", nom="Nom7", prenom="Prenom7", date_naissance="01/01/2010", date_deces="undefined", origine="Japon")

    # Ajoutez les liens entre les nœuds
    G.add_edge("Grand-père paternel", "Père")
    G.add_edge("Grand-mère paternelle", "Père")
    G.add_edge("Grand-père maternel", "Mère")
    G.add_edge("Grand-mère maternelle", "Mère")
    G.add_edge("Père", "Moi")
    G.add_edge("Mère", "Moi")

    # Positionne les nœuds selon la généalogie
    pos = {
        "Grand-père paternel": (0, 0),
        "Grand-mère paternelle": (1, 0),
        "Grand-père maternel": (2, 0),
        "Grand-mère maternelle": (3, 0),
        "Père": (1, -1),
        "Mère": (3, -1),
        "Moi": (2, -2)
    }

    # Définit les drapeaux correspondant aux pays d'origine
    flags = {
        "France": "flags/fr.png",
        "Belgique": "flags/be.png",
        "Luxembourg": "flags/lu.png",
        "Italie": "flags/it.png",
        "Allemagne": "flags/de.png",
        "Espagne": "flags/es.png",
        "Japon": "flags/jp.png"
    }

    # Crée une figure et un axe
    fig, ax = plt.subplots(figsize=(12, 8))

    # Dessine l'arbre généalogique avec les informations supplémentaires
    for node in G.nodes:
        x, y = pos[node]
        attrs = G.nodes[node]
        node_label = f"Nom: {attrs['nom']}\nPrénom: {attrs['prenom']}\nNaissance: {attrs['date_naissance']}\nDécès: {attrs['date_deces']}\nSexe: {attrs['gender']}"

        # Ajoute le drapeau dans le coin supérieur gauche du rectangle
        flag_path = flags.get(attrs['origine'], 'flags/undefined.png')
        flag_image = OffsetImage(plt.imread(flag_path), zoom=0.01, alpha=0.8)  # Réduction de la taille et ajout de transparence au drapeau
        if node == "Grand-père paternel":
            flag_box = AnnotationBbox(flag_image, (x - 0.33, y + 0.13), frameon=False)  # Ajustement de la position du drapeau
        else:
            flag_box = AnnotationBbox(flag_image, (x - 0.33, y+ 0.13), frameon=False)  # Ajustement de la position du drapeau
        ax.add_artist(flag_box)

        # Dessine le rectangle contenant les informations supplémentaires
        rect_width = 0.8
        rect_height = 0.4
        rect_x = x - rect_width / 2
        rect_y = y - rect_height / 2
        rect = plt.Rectangle((rect_x, rect_y), rect_width, rect_height, facecolor='white', edgecolor='black', linewidth=1, alpha=0.8)
        ax.add_patch(rect)

        # Affiche les informations supplémentaires dans le rectangle
        ax.text(x, y, node_label, ha='center', va='center', fontsize=8)

    # Dessine les arêtes avec des flèches partant du centre bas du rectangle et arrivant au centre haut des rectangles
    for edge in G.edges:
        x_start, y_start = pos[edge[0]]
        x_end, y_end = pos[edge[1]]
        arrow_start = (x_start, y_start - rect_height / 2)
        arrow_end = (x_end, y_end + rect_height / 2)
        arrow = plt.arrow(arrow_start[0], arrow_start[1], arrow_end[0] - arrow_start[0], arrow_end[1] - arrow_start[1],
                          color='gray', width=0.004, head_width=0.04, length_includes_head=True)  # Réduction de la taille des flèches
        ax.add_patch(arrow)

    # Supprime les axes
    ax.axis('off')

    # Exporte l'arbre généalogique en image
    print("Export de l'arbre généalogique effectué")
    plt.savefig("arbre_genealogique.png", bbox_inches='tight')

    # Affiche l'arbre généalogique à l'écran
    plt.show()

# Appel de la fonction pour générer et exporter l'arbre généalogique
generer_arbre_genealogique()