#------------------------------------------------------------------------------------------------
# Création de boutton et commande
# Greating button and command
# ce petit programme affiche le texte saisi au clavier sur un label tout en le vérifiant comme...
# ...mot de passe , en cas de mot de passe incorrect il affiche un message d'erreur
# That small programme print text wich is writing on clavier like pass word 
#-------------------------------------------------------------------------------------------------

from tkinter import*
import  tkinter as tk

class Windows:
    def __int__(self,windows):
        self.windows=windows
        self.windows.title("~~ TKINTER WINDOWS BY AIME ~~")
        self.windows.geometry("400x250")
        self.windows.resizable(0,0)
        self.windowswindows["bg"] = "red"


        self.number_of_windows = 0
        self.bouton_ouvrir = tk.Button(self.windows, text ="open", command = None)
        self.bouton_ouvrir.pack
        

    def open_windows(self):
        if self.number_of_windows < 2 :
            self.number_of_windows += 1
            fenetre_top_level = tk.Toplevel(self.windows)
            fenetre_top_level.title("TOP windows")


            bouton_fermer = tk.Button(fenetre_top_level,text = "Fermer", command = self.fermer_fenetre)
            bouton_fermer.pack()
        else:
            tk.messagebox.showinfo("INFO","nbre atteint")


    def fermer_fenetre(self,evenement= None):
        self.number_of_windows -= 1
        evenement.widget.destroy()

gate = tk.Tk()
aplli = Windows(gate)


"""windows = Tk()
windows.title("~~ TKINTER WINDOWS BY AIME ~~")
windows.geometry("400x250")
windows.resizable(0,0) 
windows["bg"] = "red"
"""

"""def verifie():
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
boutton.pack()"""
##############################
#### FENETRE DANS FENETRE ####
##############################
# Nouvelle fenetre 
"""def new_windows():
    top=tk.Toplevel()
    top.title("new_windows")
    top.geometry("400x250")

# Ajout de widget
label= tk.Label(label, text="PASS   WORD")
label.pack()
"""
"""# Bouton de commande de new_windows
btn= tk.Button(windows,text ="click me", command= new_windows)
btn.pack()
"""

gate.mainloop()