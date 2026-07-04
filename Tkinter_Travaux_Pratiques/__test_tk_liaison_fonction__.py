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