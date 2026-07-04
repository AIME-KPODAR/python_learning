""" Ici nous allons limiter la possibilité d'essai à 5 
Après une tentative simultanée de 5 le joueur a perdu et le jeu ce termine """
import random
nombre_secret = random.randint(0,100)
print("Début du jeu de devinette d'un entier secret\nBienvenue dans notre jeu de devinette d'un entier secret compris entre 0 et 100 (inclus 0 et 100)\nVous n'avez que cinq essais\nC'est partie")
def userInput():
    compteur = 0
    while True:
        try:
            nombre_saisi = int(input("Saisissez un entier positive: "))
            if (nombre_saisi < 0):
                print("Verifiez votre saisi. Vous avez saisi un entier negative et non un entier positive")
                compteur = compteur + 1
                if (compteur == 5) :
                    print(f"Vous avez perdu car vous avez faire 5 essais \nL'entier secret est << {nombre_secret} >>\nFin du jeu")
                    quit()
                continue
            else:
                break
        except ValueError:
            print("Verifiez votre saisi. Vous devez entrez un entier positive comme 12 par exemple.")
            compteur = compteur + 1
            if (compteur == 5):
                print(f"Vous avez perdu car votre essai dépasse 5 essais et l'entier secret est << {nombre_secret} >> \nFin du jeu")
                quit()
    return nombre_saisi 

nombre_saisi = userInput()
compteur = 0
while (nombre_saisi != nombre_secret):
    if (nombre_saisi < nombre_secret):
        print("Entier saisi inférieur à l'entier secret")
        compteur = compteur + 1
        if (compteur == 5):
            print(f"Vous avez perdu car votre essai dépasse 5 essais \nL'entier secret est << {nombre_secret} >>\nFin du jeu")
            quit()
    elif (nombre_saisi > nombre_secret):
        print("Entier saisi supérieur à l'entier secret")
        compteur = compteur + 1
        if (compteur == 5):
            print(f"Vous avez perdu car votre essai dépasse 5 essais et l'entier secret est << {nombre_secret} >>\nFin du jeu")
            quit()
    nombre_saisi = userInput ()
print(f"Bravo entier secret trouvé. L'entier secret est exactement: << {nombre_saisi} >>\nFin du jeu")

            
