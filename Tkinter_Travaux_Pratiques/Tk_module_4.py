#-----------------------------------------------------------------
# Création de boutton et commande
# Greating button and command
# ce petit programme affiche le texte saisi au clavier sur un label
# That small programme print text wich is writing on clavier 
#------------------------------------------------------------------

from tkinter import*
windows = Tk()
windows.title("~~ TKINTER WINDOWS BY AIME ~~")
windows.geometry("400x250")
windows.resizable(1,1) 
windows["bg"] = "orange"

# def verifie():
    #label['text']= ma_variable.get ()
   
#ma_variable=StringVar()
#label=Label(windows, text="Texte Modifiable")
#label.pack()
#entree = Entry(windows,text=ma_variable)
#entree.pack()

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

boutton = Button(windows,text="VALIDER")
boutton.pack()

windows.mainloop()