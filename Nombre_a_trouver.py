nbre_a_trouver = 7
vies = 4
nbr_de_joueurs = 3
age_personne_majeur = 18


def demander_nom():

    joueurs = []

    for _ in range(nbr_de_joueurs):

        nom = input("\nQuel est votre nom ? ")
        joueurs.append(nom)

    return joueurs


def demander_age(nom):

    while True:

        try:
            age = int(input(f"\nBonjour {nom}, quel est votre âge ? "))
            return age

        except ValueError:
            print("Veuillez entrer un âge valide.")


def demander_nombre():

    while True:

        try:
            nombre = int(input("Devinez un nombre entre 1 et 10 : "))
            return nombre

        except ValueError:
            print("Veuillez entrer un nombre valide.")


def verifier_nombre(nombre):

    return nombre == nbre_a_trouver


def jouer_jeu(nom):

    for vie in range(vies, 0, -1):

        nombre = demander_nombre()

        if verifier_nombre(nombre):

            print(f"Félicitations {nom}, vous avez gagné !")
            return

        else:
            print(f" Mauvaise réponse. Il vous reste {vie - 1} vies.")

    print(f"Perdu {nom}, le nombre était {nbre_a_trouver}")


# Programme principal

nom_des_joueurs = demander_nom()

joueurs_autorises = []

for nom in nom_des_joueurs:

    age = demander_age(nom)

    if age >= age_personne_majeur:

        joueurs_autorises.append(nom)

    else:
        print(f"Désolé {nom}, vous êtes mineur.")


for joueur in joueurs_autorises:

    jouer_jeu(joueur)