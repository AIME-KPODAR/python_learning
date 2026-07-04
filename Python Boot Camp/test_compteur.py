#def userInput():
compteur = 0
while True:

    try:
        nombre_saisi = int(input("Saisissez un entier positive: "))
        if (nombre_saisi < 0):
            print("Verifiez votre saisi. Vous avez saisi un entier negative et non un entier positive")
            compteur = compteur + 1 
            if (compteur == 5):
                print("Vous avez perdu \nFin du jeu")
                print(compteur)
                quit() 
            continue
        else:
            break
    except ValueError:
        print("Verifiez votre saisi. Vous devez entrez un entier positive comme 12 par exemple.")
        compteur = compteur + 1
    if (compteur == 5):
        print("Vous avez perdu \nFin du jeu")
        print(compteur)
        quit()
    #return nombre_saisi 