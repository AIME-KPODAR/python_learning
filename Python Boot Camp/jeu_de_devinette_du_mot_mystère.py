""" Nous allons écrir un petit programme 
Notre programme demandera à l'utillisteur de deviner un mot mystère que le programme génère atomatiquement
La possibilité d'essai sera limité à l'utilisteur si le nombre de possibilité est atteint et que le joueur 
ou l'utilisateur n'a puis trouvé le mot mystère alors il a perdu au cas contraire il gagne """
import random
import string

LIMITE_ESSAI = 15


#if__name__ == "__main__" :
nombreEssai = 1  # Nombre d'essai en cours du joueur
a1 = random.choice(string.ascii_uppercase)
a2 = random.choice(string.ascii_lowercase)
a3 = random.choice(string.ascii_lowercase)
a4 = random.choice(string.ascii_lowercase)
liste_autonome = [a1,a2,a3,a4]
voyelle = ["a", "i","e","o","y","u"]
compteur_voyelle = 0
for Voyelle in voyelle :
    #print(Voyelle)
    for i in liste_autonome:
        if i == Voyelle :
            print(i)
            compteur_voyelle = compteur_voyelle +1
            print (compteur_voyelle)
        controleur = i  
  
mot_mystere = a1 + a2 + a3 + a4 
length_mot_mystere = len(mot_mystere)
nombre_consonne_mot_mystere = length_mot_mystere - compteur_voyelle
print(length_mot_mystere)
print(nombre_consonne_mot_mystere)
print (f"Vous devez deviner un mot mystère comportant: {compteur_voyelle} voyelle (s) et {nombre_consonne_mot_mystere} consonne (s)")
print(mot_mystere)
mot_saisi = input("Saisissez un alphabet du mot mystère: ")
while True :
    if mot_saisi == controleur   :
        print(f"Vous avez deviner un alphabet du mot mystère. L'alphabet trouvé est: {mot_saisi}")
        break
    else :
        print("Vous avez rater un essai\nRéessayez à nouveau")
        #mot_saisi = input("Saisissez un alphabet du mot mystère: ")
        break
print (controleur)








