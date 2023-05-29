# Modélisation - 08/03/2022 - IOPETI Hugo

# 1) La bande passante de C est la plus petite valeur possible entre un rij et un rij + 1 sur le chemin.

# 2) Soit 2 chemins C1 et C2, la meilleure de ces 2 routes en fonction de la matrice b est celle qui possède la bande passante minimale la plus grande.
# On choisit le chemin ou le "goulot d'étranglement" est le plus grand. (qui possède le goulot pouvant faire passer le plus de choses / ayant le meilleur débit)(Sachant que le goulot d'étranglement correspond à la valeur minimale d'une arête d'un chemin de s vers t)

# 3)
# Fonction qui recherche tous les chemins dans un réseau, d'un routeur source à un routeur destination.
def recherche_chemin(
    reseau, r_sour, r_dest, sommets_visites, liste_sommets, liste_chemins
):
    # Je dit que je visite le routeur source. (Je met le routeur source dans le tableau contenant tous les sommets visités).
    sommets_visites[r_sour] = True
    # Création d'une copie du chemin pour la modifier et garder l'original.
    chem = liste_sommets.copy()
    # Ajout du routeur source au chemin. (avec l'appel récursif, cela permet de stocker tous les sommets d'un chemin)
    chem.append(r_sour)

    # Si le routeur source est le même que le routeur destination, on stock le chemin.
    if r_sour == r_dest:
        liste_chemins.append(chem)
    # Sinon, on parcourt tout le réseau, on ré-appel la fonction avec comme routeur source le routeur d'après/suivant dans le chemin.
    else:
        for i in range(0, len(reseau)):
            if (reseau[r_sour][i] != 0) and not (sommets_visites[i]):
                recherche_chemin(reseau, i, r_dest, sommets_visites, chem, liste_chemins)
    sommets_visites[r_sour] = False

# Foncion qui calcule le flot max dans un réseau à partir d'un chemin.
def calcul_flot_max(reseau, chemin):
    # On init à 999999 pour faire le minimum après. (n'importe quel valeur utilisée ici est meilleur que celle-ci)
    flot_max = 999999.0
    # On parcourt le chemin donné et on fait le minimum entre la précedante valeur de flot_max et celle parcouru actuellement.
    for i in range(0, len(chemin) - 1):
        flot_max = min(flot_max, reseau[chemin[i]][chemin[i + 1]])

    return flot_max

# Fonction qui parcourt tout les chemins et retourne celle qui a le flot max le plus intéressant/élevé.
def meilleur_chemin(reseau, r_sour, r_dest):
    sommets_visites = len(reseau) * [False]
    liste_chemins = []
    meilleur_chemin = []
    # La pire valeur, n'importe quelle valeur du graph trouvée sera meilleure.
    flot_max = -999999.0

    # On recherche tous les chemins qui vont du routeur source au routeur destination.
    recherche_chemin(reseau, r_sour, r_dest, sommets_visites, [], liste_chemins)

    # Pour tous les chemins trouvés, on fait le max de tous les flots, et on stock le meilleur chemin.
    for chem in liste_chemins:
        tmp = calcul_flot_max(reseau, chem)
        if tmp > flot_max:
            flot_max = tmp
            meilleur_chemin = chem

    # On affiche le meilleur_chemin.
    print_chemin(meilleur_chemin)

# Fonction qui gère l'affichage du résultat.
def print_chemin(meilleures_routes):
    temp = ""
    #J'ajoute les "->" entre chaque sommets.
    for i in range(0, len(meilleures_routes)-1):
        temp = temp + str(meilleures_routes[i]) + "->"

    temp = temp + str(meilleures_routes[len(meilleures_routes)-1])

    print("Le meilleur chemin entre", meilleures_routes[0], "et", meilleures_routes[len(
        meilleures_routes)-1], "est", temp)

# Graph correspondant à celui donné dans l'énoncé.
reseau = [
    # A  #B #C #D #E #F
    [0, 5, 8, 0, 0, 0],  # A
    [0, 0, 2, 4, 2, 4],  # B
    [0, 0, 0, 3, 1, 0],  # C
    [0, 0, 0, 0, 1, 6],  # D
    [0, 0, 0, 0, 0, 5],  # E
    [0, 0, 0, 0, 0, 0],  # F
]

# Test, on cherche le meilleur chemin de 0 -> 5 soit de A -> F.
meilleur_chemin(reseau, 0, 2)
meilleur_chemin(reseau, 0, 4)
meilleur_chemin(reseau, 1, 5)
meilleur_chemin(reseau, 2, 5)
meilleur_chemin(reseau, 0, 5)