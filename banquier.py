class Client:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    def se_presenter(self):
        print(self.nom)
        print(self.prenom)
        print(self.age)

class Compte :
    def __init__(self,client):
        self.client=client
        self.solde=0
    def deposer(self,montant):
        self.solde+=montant
        print(f"Vous avez depose {montant} euros")
    def retirer(self,montant):
        self.solde-=montant
        print(f"Vous avez retire {montant} euros") 
    def consulter_solde(self):
        print(f"Solde actuel : {self.solde} $") 

class CompteEpargne(Compte):
    def __init__(self,client,taux_interet):
        super().__init__(client)
        self.taux_interet=taux_interet
    def appliquer_interet(self):
        self.solde= self.solde*(1+self.taux_interet)
        print(f"Interet appliquer :( + {self.taux_interet * 100} % ) ! ")

print ("=== Bienvenue chez PythonBank ===")
jean = Client("Dupont", "Jean", 35)
jean.se_presenter()
mon_epargne = CompteEpargne(jean, 0.05)
mon_epargne.deposer(1000)
mon_epargne.retirer(500)
mon_epargne.consulter_solde()
mon_epargne.appliquer_interet()
mon_epargne.consulter_solde()