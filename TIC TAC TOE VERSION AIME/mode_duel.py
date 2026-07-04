from tkinter import Tk, Toplevel, Canvas, Label, Button, messagebox, PhotoImage
import os
import pygame
import numpy as np

# Configuration du plateau
size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 10) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
highlight_color = "yellow"
background_color = "white"

def lancer_mode_deux_joueurs(parent=None):
    class Tic_Tac_Toe:
            
        def __init__(self):
            self.window = Toplevel(parent) if parent else Tk()
            try:
                img = PhotoImage(file="C:\\Users\\user\\Desktop\\TIC TAC TOE VERSION AIME\\assets\\images\\logo-icon.png")
                self.window.iconphoto(False, img)
            except Exception as e:
                print(f"Impossible de charger l'icône : {e}")
            self.window.title('Tic-Tac-Toe Version Assiongbon Aimé KPODAR')
            self.window.resizable(0, 0)
            self.window.protocol("WM_DELETE_WINDOW", self.close_window)

            # Canvas
            self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board, bg=background_color)
            self.canvas.pack()

            # Initialisation des sons
            try:
                pygame.mixer.init()
            except Exception as e:
                print(f"Erreur init pygame: {e}")

            self.place_sound = self.load_sound("C:\\Users\\user\\Desktop\\TIC TAC TOE VERSION AIME\\assets\\son\\click_sound.mp3")
            self.win_sound = self.load_sound("C:\\Users\\user\\Desktop\\TIC TAC TOE VERSION AIME\\assets\\son\\win_sound.mp3")
            self.error_sound = self.load_sound("C:\\Users\\user\\Desktop\\TIC TAC TOE VERSION AIME\\assets\\son\\error_sound.mp3")

            # Musique de fond
            bg_music_path = "C:\\Users\\user\\Desktop\\TIC TAC TOE VERSION AIME\\assets\\son\\background_music.mp3"
            if os.path.exists(bg_music_path):
                try:
                    pygame.mixer.music.load(bg_music_path)
                    pygame.mixer.music.play(-1)
                except Exception as e:
                    print(f"Erreur musique fond: {e}")

            # Scores
            self.score_X = 0
            self.score_O = 0
            self.score_X_label = Label(self.window, text=f"Score X: {self.score_X}", font=("Arial", 14), fg=symbol_X_color)
            self.score_X_label.pack(side='left', padx=20)
            self.score_O_label = Label(self.window, text=f"Score O: {self.score_O}", font=("Arial", 14), fg=symbol_O_color)
            self.score_O_label.pack(side='right', padx=20)

            # Timer
            self.timer_label = Label(self.window, text="Time: 00:00:00", font=("Arial", 14), fg="black")
            self.timer_label.pack(pady=10)

            # Play Again
            self.play_again_button = Button(self.window, text="Play Again", command=self.play_again, font=("Arial", 14))
            self.play_again_button.pack(pady=10)

            # Jeu
            self.board_status = np.zeros((3,3))
            self.player_X_turns = True
            self.X_pieces = 0
            self.O_pieces = 0
            self.selected_piece = None
            self.reset_board = False
            self.gameover = False
            self.time_elapsed = 0

            self.window.bind('<Button-1>', self.click)
            self.initialize_board()
            self.update_timer()

        # ----- Méthodes originales -----
        def load_sound(self, file_name):
            if os.path.exists(file_name):
                try:
                    return pygame.mixer.Sound(file_name)
                except:
                    return None
            return None

        def initialize_board(self):
            self.canvas.delete("all")
            for i in range(1,3):
                self.canvas.create_line(0, size_of_board/3*i, size_of_board, size_of_board/3*i, width=2)
                self.canvas.create_line(size_of_board/3*i, 0, size_of_board/3*i, size_of_board, width=2)
            self.redraw_pieces()
            if self.selected_piece:
                self.highlight_selected_piece(self.selected_piece)

        def redraw_pieces(self):
            for r in range(3):
                for c in range(3):
                    if self.board_status[r][c] == -1: self.draw_X([r,c])
                    elif self.board_status[r][c] == 1: self.draw_O([r,c])

        def draw_X(self,pos):
            x,y = self.convert_logical_to_grid_position(pos)
            self.canvas.create_line(x - symbol_size, y - symbol_size, x + symbol_size, y + symbol_size,
                                    width=symbol_thickness, fill=symbol_X_color)
            self.canvas.create_line(x + symbol_size, y - symbol_size, x - symbol_size, y + symbol_size,
                                    width=symbol_thickness, fill=symbol_X_color)

        def draw_O(self,pos):
            x,y = self.convert_logical_to_grid_position(pos)
            self.canvas.create_oval(x - symbol_size, y - symbol_size, x + symbol_size, y + symbol_size,
                                    width=symbol_thickness, outline=symbol_O_color)

        def convert_logical_to_grid_position(self,pos):
            return (size_of_board/3)*pos[1]+size_of_board/6, (size_of_board/3)*pos[0]+size_of_board/6

        def convert_grid_to_logical_position(self,pos):
            return int(pos[1]//(size_of_board/3)), int(pos[0]//(size_of_board/3))

        def play_again(self):
            self.initialize_board()
            self.board_status = np.zeros((3,3))
            self.X_pieces = 0
            self.O_pieces = 0
            self.player_X_turns = True
            self.selected_piece = None
            self.reset_board = False
            self.gameover = False
            self.time_elapsed = 0
            self.update_timer()
            self.canvas.delete("highlight")
            if os.path.exists("C:\\Users\\user\\Desktop\\TIC TAC TOE VERSION AIME\\assets\\son\\background_music.mp3"):
                pygame.mixer.music.play(-1)

        def update_timer(self):
            if not self.gameover:
                self.time_elapsed +=1
                h = self.time_elapsed//3600
                m = (self.time_elapsed%3600)//60
                s = self.time_elapsed%60
                self.timer_label.config(text=f"Time: {h:02d}:{m:02d}:{s:02d}")
                self.window.after(1000, self.update_timer)

        def is_valid_position(self,pos): return 0<=pos[0]<3 and 0<=pos[1]<3
        def is_grid_occupied(self,pos): return self.board_status[pos[0]][pos[1]] !=0
        def is_adjacent(self,p1,p2): return abs(p1[0]-p2[0])<=1 and abs(p1[1]-p2[1])<=1
        def move_piece(self,f,t,player):
            val = -1 if player=='X' else 1
            self.board_status[f[0]][f[1]] = 0
            self.board_status[t[0]][t[1]] = val

        def highlight_selected_piece(self,pos):
            x,y = self.convert_logical_to_grid_position(pos)
            self.canvas.create_rectangle(x - symbol_size, y - symbol_size, x + symbol_size, y + symbol_size,
                                         outline=highlight_color, width=4, tags="highlight")

        def is_gameover(self):
            for i in range(3):
                if abs(sum(self.board_status[i,:]))==3: return True
                if abs(sum(self.board_status[:,i]))==3: return True
            diag1 = self.board_status[0,0]+self.board_status[1,1]+self.board_status[2,2]
            diag2 = self.board_status[0,2]+self.board_status[1,1]+self.board_status[2,0]
            return abs(diag1)==3 or abs(diag2)==3

        def click(self,event):
            grid=[event.x,event.y]
            logical=self.convert_grid_to_logical_position(grid)
            if not self.is_valid_position(logical):
                if self.error_sound: self.error_sound.play()
                messagebox.showwarning("Position invalide","Vous avez cliqué en dehors du plateau.")
                return
            if not self.reset_board:
                self.handle_turn(logical,'X' if self.player_X_turns else 'O', -1 if self.player_X_turns else 1)
                if self.is_gameover(): self.display_gameover()
            else: self.play_again()

        def handle_turn(self,pos,player,val):
            pieces=self.X_pieces if player=='X' else self.O_pieces
            if pieces<3:
                if not self.is_grid_occupied(pos):
                    if self.place_sound: self.place_sound.play()
                    self.draw_X(pos) if player=='X' else self.draw_O(pos)
                    self.board_status[pos[0]][pos[1]] = val
                    self.X_pieces+=1 if player=='X' else 0
                    self.O_pieces+=1 if player=='O' else 0
                    self.player_X_turns = not self.player_X_turns
                    self.selected_piece=None
                    self.canvas.delete("highlight")
                else:
                    if self.error_sound: self.error_sound.play()
                    messagebox.showwarning("Case occupée","La case est déjà occupée.")
            else:
                if self.selected_piece is None:
                    if self.board_status[pos[0]][pos[1]]==val:
                        self.selected_piece=pos
                        self.canvas.delete("highlight")
                        self.highlight_selected_piece(pos)
                    else:
                        if self.error_sound: self.error_sound.play()
                        messagebox.showwarning("Sélection invalide","Vous devez sélectionner l'un de vos propres pions.")
                else:
                    if pos==self.selected_piece:
                        self.selected_piece=None
                        self.canvas.delete("highlight")
                    elif self.board_status[pos[0]][pos[1]]==val:
                        self.selected_piece=pos
                        self.canvas.delete("highlight")
                        self.highlight_selected_piece(pos)
                    else:
                        if not self.is_grid_occupied(pos) and self.is_adjacent(self.selected_piece,pos):
                            if self.place_sound: self.place_sound.play()
                            self.move_piece(self.selected_piece,pos,player)
                            self.selected_piece=None
                            self.player_X_turns = not self.player_X_turns
                            self.initialize_board()
                        else:
                            if self.error_sound: self.error_sound.play()
                            messagebox.showwarning("Déplacement invalide","La case doit être adjacente et vide.")

        def display_gameover(self):
            pygame.mixer.music.stop()
            if self.win_sound:
                self.win_sound.play()
                duration=int(self.win_sound.get_length()*1000)
                self.window.after(duration,self.show_winner_message)
            else: self.show_winner_message()
            self.gameover=True

        def show_winner_message(self):
            winner='O' if self.player_X_turns else 'X'
            if winner=='X': self.score_X+=1
            else: self.score_O+=1
            messagebox.showinfo("Fin de partie", f"Le joueur {winner} a gagné!")
            self.score_X_label.config(text=f"Score X: {self.score_X}")
            self.score_O_label.config(text=f"Score O: {self.score_O}")
            self.reset_board=True
                    
        def close_window(self):
            global duel_fenetre
            pygame.mixer.music.stop()
            self.window.destroy()
            duel_fenetre = None


    

    game_instance=Tic_Tac_Toe()
    return game_instance.window
