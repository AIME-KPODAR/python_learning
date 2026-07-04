"""Ici nous allons faire la gestion des erreurs en entrée utilisateur 
Suite du jeu de devinette des chiffres """
import random
nombre_secret = random.randint(0,100)
print("Benvenue dans le jeu de devinette des chiffres\nDébut du jeu\nC'est partie")
def userInput():
    while True:
        try :
            nombre_saisi = int(input("Veuillez sasir un entier: "))
            if (nombre_saisi < 0) :
                print("Vous devez entrer un entier positif")
                continue
            else:
                break
        except ValueError:
            print("Vous deviez saisir un entier. Exemple: 14")
    return nombre_saisi
      
nombre_saisi = userInput()
while (nombre_saisi != nombre_secret ): 
    if (nombre_saisi < nombre_secret):
        print("Nombre est trop petit")
    elif( nombre_saisi > nombre_secret):
        print("Nombre trop grand")
    nombre_saisi = userInput()
print(f"Bravo nombre trouvé. Il s'agit bien de l'entier: << {nombre_saisi} >>")
print("Fin du jeu")