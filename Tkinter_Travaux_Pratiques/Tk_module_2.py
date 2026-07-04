#----------------------------------------------------------------
# Affichage d'image , fond en coleur
# Import image in tkinter
#----------------------------------------------------------------

from tkinter import*
windows = Tk()
windows.title("~~ TKINTER WINDOWS BY AIME ~~")
windows.geometry("400x250")
windows.resizable(1,1) 
windows["bg"] = "gray"
photo = PhotoImage(file='lan.png')
label = Label (windows, image=photo)
label.pack()
windows.mainloop()