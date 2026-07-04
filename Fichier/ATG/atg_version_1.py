import tkinter as tk
from tkinter import *

# Dictionnaire de couleurs
couleur = {"nero": "#252726",
           "purple": "#800080", "white": "#FFFFFF"}

# Paramétrage de la fenêtre
application = tk.Tk()
application.title("Aimé Tic Tac Toe Game")
application.config(bg="gray30")
application.geometry("900x750") # Taille de la fenêtre = 900x750(pour :imagbd2) ou 400x650(pour :imagbd) (largeur x hauteur;= format de l'image de fond)
application.resizable(0, 0)

# Chargement des images
img = PhotoImage(file="C:\\Users\\hp\\Desktop\\PRE-CONSTRUIT\\ATG\\logo-icon.png")
application.iconphoto(False, img)
closeIcon = PhotoImage(file="fermer.png")
imgfond = PhotoImage(file="imgbd2.png")
menuimg = PhotoImage(file="menu.png")

# État du menu latéral
btnEtat = False

# Fonction pour animer le menu latéral
def menuCont():
    global btnEtat
    if btnEtat:  # Si le menu est ouvert, le fermer
        for x in range(0, 301, 10):  # Animation fluide
            navLataral.place(x=-x, y=0)
            application.update()
        btnEtat = False
    else:  # Si le menu est fermé, l'ouvrir
        for x in range(-300, 1, 10):  # Animation fluide
            navLataral.place(x=x, y=0)
            application.update()
        btnEtat = True

# Barre supérieure
topFrame = tk.Frame(application, bg=couleur["purple"])
topFrame.pack(side="top", fill=tk.X)

# Texte de la barre supérieure
acceuiltext = tk.Label(topFrame, text="ATG", font="ExtraCondensed 15", bg=couleur["purple"], fg="white", height=2, padx=20)
acceuiltext.pack(side="right")

# Image de fond
can = Canvas(application, width=6000, height=1000)
can.create_image(0, 0, anchor=NW, image=imgfond)
can.pack()

# Bouton pour ouvrir/fermer le menu latéral
navBarBtn = tk.Button(topFrame, image=menuimg, bg=couleur["purple"], bd=0, padx=20,
                      activebackground=couleur["purple"], command=menuCont)
navBarBtn.place(x=10, y=10)

# Paramètres du menu latéral
navLataral = tk.Frame(application, bg="gray30", width=300, height=750)
navLataral.place(x=-300, y=0)  # Initialement caché
tk.Label(navLataral, font="ExtraCondensed 15", bg=couleur["purple"], fg="black", width=300, height=2, padx=20).place(x=0, y=0)

# Options dans la barre latérale
options = ["INTRO_VIDEO", "MODE DEUX JOUEURS", "MODE SOLO", "PARAMETRES", "AIDE"]
y_position = 80
for option in options:
    tk.Button(navLataral, text=option, font="ExtraCondensed 15", bg="gray30", fg=couleur["white"],
              activebackground="gray30", bd=0).place(x=25, y=y_position)
    y_position += 40

# Bouton de fermeture du menu
fermeBtn = tk.Button(navLataral, image=closeIcon, bg=couleur["purple"], activebackground=couleur["purple"],
                     bd=0, command=menuCont)
fermeBtn.place(x=250, y=10)

# Lancement de l'application
application.mainloop()