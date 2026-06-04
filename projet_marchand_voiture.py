from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class Voiture:
    def __init__(self, marque="", model="", annee=0, km=0, remarque="", norme_euros=""):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.km = km
        self.remarque = remarque
        self.norme_euros = norme_euros

    def saisir_infos(self):
        self.marque = input("Marque : ")
        self.model = input("Modèle : ")
        self.annee = int(input("Année : "))
        self.km = int(input("Kilométrage : "))
        self.norme_euros = input("Quelle est la norme euros ? ")
        self.remarque = input("Quelles sont les remarques sur la voiture ? ")

    def generer_pdf(self, nom_fichier="voiture.pdf"):
        doc = SimpleDocTemplate(nom_fichier, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        # Titre
        story.append(Paragraph("Fiche Voiture", styles['Title']))
        story.append(Spacer(1, 20))

        # Les données de la voiture
        infos = [
            f"Marque : {self.marque}",
            f"Modèle : {self.model}",
            f"Année : {self.annee}",
            f"Kilométrage : {self.km} km",
            f"Norme euros : {self.norme_euros}",
            f"Remarques : {self.remarque}",
        ]

        for ligne in infos:
            story.append(Paragraph(ligne, styles['Normal']))
            story.append(Spacer(1, 10))

        doc.build(story)
        print(f"PDF généré : {nom_fichier}")


# Utilisation
ma_voiture = Voiture()
ma_voiture.saisir_infos()
ma_voiture.generer_pdf(r"C:\Users\benja\Desktop\Projet pour Odoo\ma_voiture.pdf")