import os
import random 
import time 
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def interface_debut():
    print ("******************************************")
    print ("**Bienvenue dans le test de memorisation**")
    print ("******************************************")
    time.sleep(5)
    clear_screen()
interface_debut()

point =0
point_totale = 10
NBR_BASE = str(random.randint (1000,9999))
for i in range (10):
    nbr_supp = str(random.randint (0,9))
    NBR_BASE = NBR_BASE + nbr_supp
    print ("Retener la sequence")
    time.sleep(3)
    clear_screen()
    print (NBR_BASE)
    time.sleep(6)
    clear_screen()
    reponse_utilisateur= input ("Quelle est le nombre : ")
    if reponse_utilisateur != NBR_BASE :
        print(f"Mauvaise reponse , la reponse etait {NBR_BASE}")
        break
    else :
        point+=1
        print ("Bonne reponse !!!!" )
        time.sleep(1)
        clear_screen()
        print (f"Vous avez {point} point")
        continue


def interface_de_fin():
    print ("**************************************************")
    print ("******************Vous avez perdu .***************")
    print ("***********Votre score final est de :*************")
    print (f"******************* {point} | {point_totale}***********************")
    print ("**************************************************")



interface_de_fin()
