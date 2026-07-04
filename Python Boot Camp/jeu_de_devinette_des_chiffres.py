""" Nous allons écrire un petit programme qui demandera à l'utilisateur
de deviner des chiffres en les saisissant si les chiffres saisis 
correspondent à ceux du programme alors l'utilisateur à gagner """

import random
nombre_secret = random.randint(0,100)
print("Bienvenue dans noter jeu de devinette des fichres\nC'est partie!")
nombre_saisi = int(input("Vous devez saisir votre premier essai: "))
while (nombre_saisi != nombre_secret):
    if (nombre_saisi < nombre_secret):
        print("Nombre saisi est trop petit")
    elif (nombre_saisi > nombre_secret):
        print("Nombre saisi est trop grand")
    nombre_saisi=int(input("Essai a nouveau: "))
print("Bravo nombre trouver")
print("Fin du jeu")
