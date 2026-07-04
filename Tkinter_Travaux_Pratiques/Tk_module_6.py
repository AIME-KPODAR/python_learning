#----------------------------------------------------------------
# Création de menu : les onglets et les sous onglets
# Greating menu whith tkinter 
#----------------------------------------------------------------
#Enable resisable windows  you make (1,1) or (0,0) to desible it \ Activer le redimensinnement de la fenêtre par (1,1) ou le desactiver par (0,0)
#-------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import*
windows = Tk()
windows.title("~~ TKINTER WINDOWS BY AIME ~~")
windows.geometry("400x250")
windows.resizable(1,1) 
windows["bg"] = "gray"

mon_menu = Menu(windows)

# Les onglets: Fichier, Acceuil, Partage, Affichage
mon_menu.add_cascade(label = "Fichier", menu = fichier)
mon_menu.add_cascade(label = "Acceuil" , menu = acceuil)
mon_menu.add_cascade(label = "Partage" , menu = partage)
mon_menu.add_cascade(label = "Affichage" , menu =affichage)

# Les sous onglets: Fichier -> ouvrir une nouvelle fenetre, ouvrir power shell
#                   Acceuil -> déplacer vers , nouveau dossier 
#                   Partage -> partager avec, courrier electronique
#                   Affichage -> Grande icône, Très grande icône, Petite icône

fichier = Menu(mon_menu, teaorff = 0)
fichier.add_command(label="ouvrir une nouvelle fenêtre", command = command1)

fichier = Menu (mon_menu, tearoff = 0)
fichier.add_command(label="ouvrir power shell", command= command2)

acceuil = Menu(mon_menu, tearoff = 0)
acceuil.add_command(label=" Déplacer vers", command3)

acceuil = Menu(mon_menu, tearoff = 0)
acceuil.add_command(label="Nouveau dossier", command= command4)

partage = Menu(mon_menu, tearoff = 0)
partage.add_command(label = "Partager avec", command = command5)

partage = Menu(mon_menu, tearoff = 0)
partage.add_command(label =" Courrier electronique", command = command6)

affichage = Menu(mon_menu, tearoff = 0)
affichage.add_command(label = "Grande icône", command =command7)



   


windows.config(menu= mon_menu)
windows.mainloop()  

                                                                                                                           