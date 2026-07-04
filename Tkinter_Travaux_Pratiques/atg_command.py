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
import test_tk_liaison_fonction
play=test_tk_liaison_fonction.play

boutton = Button(windows,text="VALIDER", command = play)
boutton.pack()

windows.mainloop()