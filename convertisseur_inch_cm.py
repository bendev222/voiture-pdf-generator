def cm_vers_pouce(cm):
    return round(cm / 2.54, 2)


def pouce_vers_cm(pouce):
    return round(pouce * 2.54, 2)


def demander_nombre(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def convertisseur():

    print("******** CONVERTISSEUR CM <-> POUCES ********")

    while True:

        choix = input(
            "\n1 : cm vers pouces"
            "\n2 : pouces vers cm"
            "\nEntrée : quitter\n"
        )

        if choix == "1":

            cm = demander_nombre(
                "Entrez une valeur en cm : "
            )

            resultat = cm_vers_pouce(cm)

            print(f"{cm} cm = {resultat} pouces")

        elif choix == "2":

            pouce = demander_nombre(
                "Entrez une valeur en pouces : "
            )

            resultat = pouce_vers_cm(pouce)

            print(f"{pouce} pouces = {resultat} cm")

        elif choix == "":
            break

        else:
            print("Choix invalide.")


convertisseur()

print("Convertisseur benDev v1.0")