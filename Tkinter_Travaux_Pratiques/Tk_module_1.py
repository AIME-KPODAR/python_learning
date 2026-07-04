#----------------------------------------------------------------
# Création de fenêtre graphique avec tkinter , fond en coleur
# Greate graphical windows whith tkinter and back ground in color 
#----------------------------------------------------------------
#Enable resisable windows  you make (1,1) or (0,0) to desible it \ Activer le redimensinnement de la fenêtre par (1,1) ou le desactiver par (0,0)
#-------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import*
windows = Tk()
windows.title("~~ TKINTER WINDOWS BY AIME ~~")
windows.geometry("400x250")
windows.resizable(1,1) 
windows["bg"] = "green"
windows.mainloop()
