import tkinter as tk
from tkinter import *

# Dictionnaire de coulaeur
couleur = {"nero":"#252726",
           "purple":"#800080","white":"#FFFFFF"}

# paramètrage de la fenêtre 
application = tk.Tk()
application.title("Aimé Tic tac toe Game")
application.config(bg="gray30")
application.geometry("400x650")
application.resizable(0,0)
#application.iconbitmap(bitmap= "logo.ico" ,default="logo.ico")
img=PhotoImage(file="C:\\Users\\hp\\Desktop\\PRE-CONSTRUIT\\ATG\\logo-icon.png") # chemin d'accès au fichier contenant l'image nomé:logo-icon.png
application.iconphoto(False,img)
# Paramètrage menu contextuel menuCont
btnEtat = False

# Chargement image application
closeIcon= PhotoImage(file="fermer.png")
imgfond= PhotoImage(file="imgbd.png")
menuimg= PhotoImage(file="menu.png")


# Définition des fontions
def menuCont():
    global btnEtat
    if btnEtat is True:
       # créer une fermeture
        for X in range(300):
           navLataral.place(x=-X, y=0 )
           topFrame.update()
        # Reset couleur widget
        #bannerText.config()
        acceuiltext.config(bg= couleur["purple"])
        topFrame.config(bg= couleur["purple"])
        application.config(bg="gray30")
        btnEtat = False
    else:
        for X in range(-300, 0):
            navLataral.place(x=X, y=0)
            topFrame.update()
            btnEtat = True
            
# Créer une fermeture animée


# Top bar 
topFrame = tk.Frame(application,bg= couleur["purple"])
topFrame.pack(side="top", fill=tk.X)

# Texte de top bar
acceuiltext = tk.Label(topFrame, text="ATG", font="ExtraCondensed 15", bg=couleur["purple"], fg= "white", height= 2, padx =20)
acceuiltext.pack(side="right")


# banner text & image de fond
can = Canvas(application, width = 6000, height = 1000)
can.create_image(0,0, anchor=NW, image=imgfond)
#bannerText=tk.Label(application, text="Aimé\n Tic tac toe\n Game",font="ExtraCondensed 15", fg=couleur["purple"])
#bannerText.place(x=100, y=400)
can.pack()

# Nav bar icon
navBarBtn= tk.Button(topFrame, image= menuimg, bg=couleur["purple"],bd=0 , padx = 20, activebackground=couleur["purple"],command=menuCont )
navBarBtn.place(x=10, y=10)

# Paramètre nav laterale
navLataral = tk.Frame(application, bg="gray30", width=300, height=600 )
navLataral.place(x=-300,y=0)
tk.Label(navLataral, font="ExtraCondensed 15", bg=couleur["purple"], fg="black", width= 300, height= 2 , padx=20).place(x=0, y=0)
Y= 80

# command
import pygame
import time

print("Lancement du test audio...")

# Initialisation de pygame
pygame.mixer.init()

# Chargement du son
pygame.mixer.music.load("intro_video_sound.mp3")


# Lecture
def play():
    pygame.mixer.music.play()

# Attente pendant la lecture
while pygame.mixer.music.get_busy():
    time.sleep(0.1)

print("Son terminé.")


#Les options dans la barre laterale
#option=["ACCEUIL","PAGE", "PROFIL","PARAMETRES","AIDE"]

# POsitionnement
#for i in range (5):
tk.Button(navLataral, text= "PLAY", font="ExtraCondensed 15", bg="gray30",fg=couleur["white"] ,activebackground="gray30",command=play, bd=0).place(x=0,y=55)
tk.Button(navLataral, text= "PAUSE", font="ExtraCondensed 15", bg="gray30",fg=couleur["white"] ,activebackground="gray30",command=play, bd=0).place(x=0,y=85)
#Y += 40

        
    #option[0]=Button(navLataral, text= option[0], font="ExtraCondensed 15", bg="gray30",fg=couleur["white"] ,activebackground="gray30",command=play, bd=0).place(x=26,y=75)


#option[i]= Button(application,text= option[i], command = play)
#option[i].pack()

# Paramètre bouton de fermeture menu
fermeBtn= tk.Button(navLataral, image=closeIcon, bg=couleur["purple"], activebackground=couleur["purple"],bd=0,command=menuCont )
fermeBtn.place(x=250, y=10)

application.mainloop()

