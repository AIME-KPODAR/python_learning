#--------------------------------
# Création de label ,sub_label 
# Greating label, sub_label 
#-------------------------------

from tkinter import*
windows = Tk()
windows.title("~~ TKINTER WINDOWS BY AIME ~~")
windows.geometry("400x250")
windows.resizable(1,1) 
windows["bg"] = "blue"
label = Label(windows, text = "WELCOME TO CFTP-MA", font = ("verdana",20,"italic"), bg = "white", fg = "black")
label.config(width = 100 , height = 1)
label.pack(pady=4)
sub_label = Label(windows, text = "STUDENT  PLATFORME", font = ("time new roman",20,"italic", "underline"), bg = "blue", fg = "white")
sub_label.config(width = 40 , height = 1)
sub_label.pack()
windows.mainloop()