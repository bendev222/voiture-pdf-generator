import time
import winsound

def interface_utilisateur():
    print ("***********************************")
    print ("**  Preparation ouef a la coque  **")
    print ("***********************************")
    print ("**------Mode d'utilisation-------**")
    print ("**************Mode 1***************")
    print ("** Oeufs à la coque : 3 minutes  **")
    print ("**************Mode 2***************")
    print ("**   Oeufs mollets : 6 minutes   **") 
    print ("**************Mode 3**************")
    print ("**   oeufs durs : 9 minutes      **")
    print ("***********************************")
interface_utilisateur()


mode = {
   "mode1": 180,
   "mode2": 360,
   "mode3": 540
} 
#1er point demander a l'utilisateur de choisir sont mode de prépararion 
mode_de_cuisson = input (" Veuillez choisir votre mode de cuissont: \n" 
                         "Mode 1\n" "Mode 2 \n" "Mode 3 : \n").strip().lower().replace(" " , "" )
#Cas d'erreur :
while mode_de_cuisson not in mode :
    mode_de_cuisson = input ("Erreur veuillez introduire un mode valide !!!!").strip().lower().replace(" " , "" )
#Assignation du mode 
if mode_de_cuisson == "mode1":
    mode_de_cuisson=10
if mode_de_cuisson == "mode2":
    mode_de_cuisson=360
if mode_de_cuisson == "mode3":
    mode_de_cuisson=540

temps_cuisson = mode_de_cuisson
print(f"Temps de cuisson sélectionné : {temps_cuisson} secondes")

while temps_cuisson >-1 :
    MINUTE = temps_cuisson // 60 
    SEC = temps_cuisson % 60
    for i in range (10):
        print (f"\r temp restant : {MINUTE : 02d} : {SEC: 02d}",end="")
        time.sleep(1)
        temps_cuisson-= 1
    winsound.Beep(770,1000)
