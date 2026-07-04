#------------------------------------------------------------------------------------------------
# Création de boutton et commande
# Greating button and command
# ce petit programme affiche le texte saisi au clavier sur un label tout en le vérifiant comme...
# ...mot de passe , en cas de mot de passe incorrect il affiche un message d'erreur
# That small programme print text wich is writing on clavier like pass word 
#-------------------------------------------------------------------------------------------------

from tkinter import*
import  tkinter as tk
windows = Tk()
windows.title("~~ TKINTER WINDOWS BY AIME ~~")
windows.geometry("400x250")
windows.resizable(0,0) 
windows["bg"] = "red"

def verifie():
    if ma_variable.get () == "kpodar":
        label= Label(windows, text="c'est bien moi")
        label.pack()
    else:
        label= Label(windows, text="Mot de pass incorrect")
        label.pack()
ma_variable=StringVar()
label=Label(windows, text="PASS   WORD")
label.pack()
entree = Entry(windows,text=ma_variable)
entree.pack()
boutton = Button(windows,text="VALIDER", command=verifie)
boutton.pack()
##############################
#### FENETRE DANS FENETRE ####
##############################
# Nouvelle fenetre 
def new_windows():
    top=tk.Toplevel()
    top.title("new_windows")
    top.geometry("400x250")

# Ajout de widget
label= tk.Label(label, text="PASS   WORD")
label.pack()

# Bouton de commande de new_windows
btn= tk.Button(windows,text ="click me", command= new_windows)
btn.pack()


windows.mainloop()