from tkinter import *
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

#from video_intro import lancer_video_intro
from mode_duel import lancer_mode_deux_joueurs

couleur = {"nero": "#252726", "purple": "#800080", "white": "#FFFFFF"}
fenetres_ouvertes = {}
video_fenetre = None
duel_fenetre = None
btnEtat = False

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets" / "images"

application = tk.Tk()
application.title("Aimé Tic Tac Toe Game")
application.config(bg="gray30")
application.geometry("900x750")
application.resizable(0, 0)

# Chargement des images APRÈS la création de Tk()
img = PhotoImage(file=str(ASSETS_DIR / "logo-icon.png"))
closeIcon = PhotoImage(file=str(ASSETS_DIR / "fermer.png"))
imgfond = PhotoImage(file=str(ASSETS_DIR / "imgbd2.png"))
menuimg = PhotoImage(file=str(ASSETS_DIR / "menu.png"))

application.iconphoto(False, img)

def menuCont():
    global btnEtat
    if btnEtat:
        for x in range(0, 301, 10):
            navLataral.place(x=-x, y=0)
            application.update()
        btnEtat = False
    else:
        for x in range(-300, 1, 10):
            navLataral.place(x=x, y=0)
            application.update()
        btnEtat = True

topFrame = tk.Frame(application, bg=couleur["purple"])
topFrame.pack(side="top", fill=tk.X)

tk.Label(
    topFrame,
    text="ATG",
    font="ExtraCondensed 15",
    bg=couleur["purple"],
    fg="white",
    height=2,
    padx=20
).pack(side="right")

can = Canvas(application, width=6000, height=1000)
can.create_image(0, 0, anchor=NW, image=imgfond)
can.pack()

navBarBtn = tk.Button(
    topFrame,
    image=menuimg,
    bg=couleur["purple"],
    bd=0,
    padx=20,
    activebackground=couleur["purple"],
    command=menuCont
)
navBarBtn.place(x=10, y=10)

navLataral = tk.Frame(application, bg="gray30", width=300, height=750)
navLataral.place(x=-300, y=0)

tk.Label(
    navLataral,
    font="ExtraCondensed 15",
    bg=couleur["purple"],
    fg="black",
    width=300,
    height=2,
    padx=20
).place(x=0, y=0)

def ouvrir_fenetre(nom, creation_fonction):
    if nom in fenetres_ouvertes:
        fen = fenetres_ouvertes[nom]
        if fen.winfo_exists():
            fen.lift()
            return
        else:
            del fenetres_ouvertes[nom]

    fen = creation_fonction()
    if fen:
        fenetres_ouvertes[nom] = fen
        fen.protocol("WM_DELETE_WINDOW", lambda: fermer_fenetre(nom))

def fermer_fenetre(nom):
    global video_fenetre, duel_fenetre

    if nom in fenetres_ouvertes:
        if nom == "VIDEO D'INTRODUCTION" and video_fenetre:
            video_fenetre.stop_video()
            video_fenetre = None
        elif nom == "MODE DEUX JOUEURS" and duel_fenetre:
            duel_fenetre.destroy()
            duel_fenetre = None
        else:
            fenetres_ouvertes[nom].destroy()

        del fenetres_ouvertes[nom]

def creer_video_intro():
    global video_fenetre
    if video_fenetre and video_fenetre.winfo_exists():
        video_fenetre.lift()
        return video_fenetre
    #video_fenetre = lancer_video_intro()
    return video_fenetre

def creer_mode_deux_joueurs():
    global duel_fenetre
    if duel_fenetre and duel_fenetre.winfo_exists():
        duel_fenetre.lift()
        return duel_fenetre
    duel_fenetre = lancer_mode_deux_joueurs(application)
    return duel_fenetre

def creer_mode_solo():
    fen = tk.Toplevel(application)
    fen.title("Mode Solo")
    tk.Label(fen, text="Bienvenue dans le mode solo !").pack(padx=20, pady=20)
    return fen

def creer_parametres():
    fen = tk.Toplevel(application)
    fen.title("Paramètres")
    tk.Label(fen, text="Paramètres du jeu").pack(padx=20, pady=20)
    return fen

def creer_aide():
    fen = tk.Toplevel(application)
    fen.title("Aide")
    tk.Label(fen, text="Aide du jeu").pack(padx=20, pady=20)
    return fen

options = [
    ("VIDEO D'INTRODUCTION", lambda: ouvrir_fenetre("VIDEO D'INTRODUCTION", creer_video_intro)),
    ("MODE DEUX JOUEURS", lambda: ouvrir_fenetre("MODE DEUX JOUEURS", creer_mode_deux_joueurs)),
    ("MODE SOLO", lambda: ouvrir_fenetre("MODE SOLO", creer_mode_solo)),
    ("PARAMETRES", lambda: ouvrir_fenetre("PARAMETRES", creer_parametres)),
    ("AIDE", lambda: ouvrir_fenetre("AIDE", creer_aide))
]

y_position = 80
for texte, action in options:
    tk.Button(
        navLataral,
        text=texte,
        font="ExtraCondensed 15",
        bg="gray30",
        fg=couleur["white"],
        activebackground="gray30",
        bd=0,
        command=action
    ).place(x=25, y=y_position)
    y_position += 40

fermeBtn = tk.Button(
    navLataral,
    image=closeIcon,
    bg=couleur["purple"],
    activebackground=couleur["purple"],
    bd=0,
    command=menuCont
)
fermeBtn.place(x=250, y=10)

application.mainloop()