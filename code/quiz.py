import tkinter as tk
from tkinter import messagebox
import pygame
import math
import copy
from borders import *
import pygame as pg
import sys
import numpy as np
import math
import pygame
from pygame.time import Clock
from puzzle import Puzzle
from game import Game
import time
import random
class GameSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Selector")
        self.geometry("1032x622")
        # Load background image
        self.background_image = tk.PhotoImage(file="boy.png")  # Replace "boy.png" with your image file
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_image_resized = self.background_image.subsample(3, 3)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_form()
    def create_form(self):
        self.form_label = tk.Label(self, text="Welcome to the Hero_Children Game Selector!", font=("Arial", 24, "bold"))
        self.form_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.name_label = tk.Label(self, text="Name:", font=("Arial", 16))
        self.name_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.name_entry = tk.Entry(self, font=("Arial", 16))
        self.name_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        self.age_label = tk.Label(self, text="Age:", font=("Arial", 16))
        self.age_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.age_entry = tk.Entry(self, font=("Arial", 16))
        self.age_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.submit_button = tk.Button(self, text="Submit", font=("Arial", 16), command=self.redirect_to_game_page)
        self.submit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    def redirect_to_game_page(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        # Validate inputs
        if not name or not age:
            messagebox.showerror("Error", "Please fill out all fields.")
            return
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return
        # Destroy current window
        self.destroy()
        # Redirect to game selection page
        game_selection_page = GameSelectionPage(name, age)
        game_selection_page.mainloop()
class GameSelectionPage(tk.Tk):
    def __init__(self, name, age):
        super().__init__()
        self.title("Game Selection")
        self.geometry("1032x622")
        # Load background image
        self.background_image = tk.PhotoImage(file="boy.png")  # Replace "background_image.png" with your image file
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.name = name
        self.age = age
        self.create_game_buttons()
    def create_game_buttons(self):
        self.welcome_label = tk.Label(self, text=f"Hello, {self.name}!", font=("Arial", 14, "bold"))
        self.welcome_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.game_label = tk.Label(self, text="Choose a game to play:")
        self.game_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.memory_card_button = tk.Button(self, text="PacMan", font=("Arial", 16), command=self.play_PacMan)
        self.memory_card_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.flag_matching_button = tk.Button(self, text="soduku", font=("Arial", 16), command=self.soduku)
        self.flag_matching_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.capital_guessing_button = tk.Button(self, text="puzzle", font=("Arial", 16), command=self.puzzle)
        self.capital_guessing_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.balloon_catching_button = tk.Button(self, text="Memory Card", font=("Arial", 16), command=self.MemoryCard)
        self.balloon_catching_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
#**************************************             start PacMan                    ******************************************************************
    def play_PacMan(self):
        SCREEN_WIDTH = 800  # Définition de la largeur de l'écran
        SCREEN_HEIGHT = 576  # Définition de la hauteur de l'écran
        def main():
            # Initialisation de tous les modules pygame importés
            pygame.init()
            # Définir la largeur et la hauteur de l'écran [largeur, hauteur]
            screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
            # Définir la légende de la fenêtre actuelle
            pygame.display.set_caption("PACMAN")
            # Boucle jusqu'à ce que l'utilisateur clique sur le bouton de fermeture.
            done = False
            # Utilisé pour gérer la vitesse de mise à jour de l'écran
            clock = pygame.time.Clock()
            # Créer un objet de jeu
            game = Game()
            # -------- Boucle principale du programme -----------
            while not done:
                # --- Traiter les événements (appuis sur les touches, clics de souris, etc.)
                done = game.process_events()
                # --- La logique du jeu devrait aller ici
                game.run_logic()
                # --- Dessiner la trame actuelle
                game.display_frame(screen)
                # --- Limiter à 30 images par seconde
                clock.tick(30)
                #tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))
            # Fermer la fenêtre et quitter.
            # Si vous oubliez cette ligne, le programme restera "bloqué"
            # à la sortie s'il est exécuté depuis IDLE.
            pygame.quit()

        if __name__ == '__main__':
            main()
# **************************************   end PacMan       *********************************************   

# **************************************  start Soduku       *********************************************  
    def soduku(self):
        # Dimensions de la fenêtre et des cases
        SCREEN_WIDTH = 600
        SCREEN_HEIGHT = 700  # Ajuster la hauteur pour inclure la zone de message
        GRID_SIZE = 9
        CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
        # Dimensions de la zone de message
        MESSAGE_AREA_HEIGHT = 100
        MESSAGE_AREA_COLOR = (200, 200, 200)
        # Couleurs
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GRAY = (200, 200, 200)
        BLUE = (0, 0, 255)
        # Exemple de grille Sudoku (0 représente une case vide)
        EXAMPLE_BOARD = np.array([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])
        # Chemin vers le fichier audio
        AUDIO_FILE = "song.mp3"
        class SudokuGame:
            def __init__(self, age):
                self.grid = EXAMPLE_BOARD.copy()
                self.selected = None
                self.error_message = ""  # Initialiser le message d'erreur comme une chaîne vide
                self.game_over = False  # Initialiser le statut de game over à False
                self.age = age
                # Initialiser la durée du jeu en fonction de l'âge
                if age < 5:
                    self.clock_time = 1200  # Temps réduit pour le test
                elif 5 <= age <= 13:
                    self.clock_time = 600  
                else:
                    self.clock_time = 240  
                self.start_time = pg.time.get_ticks()  # Temps de départ du jeu
            def draw(self, screen):
                screen.fill(WHITE)
                # Dessiner la zone de jeu
                self.draw_board(screen)
                # Dessiner la zone de message
                self.draw_message_area(screen)
                # Dessiner l'horloge à gauche de la zone de message
                self.draw_clock(screen)
            def draw_board(self, screen):
                for i in range(GRID_SIZE + 1):
                    thickness = 4 if i % 3 == 0 else 1
                    pg.draw.line(screen, BLACK, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE), thickness)
                    pg.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_HEIGHT - CELL_SIZE), thickness)
                for i in range(GRID_SIZE):
                    for j in range(GRID_SIZE):
                        value = self.grid[i][j]
                        if value != 0:
                            self.draw_number(screen, value, (j, i))
                if self.selected:
                    pg.draw.rect(screen, BLUE, (self.selected[0] * CELL_SIZE, self.selected[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
            def draw_message_area(self, screen):
                pg.draw.rect(screen, MESSAGE_AREA_COLOR, (0, SCREEN_HEIGHT - MESSAGE_AREA_HEIGHT, SCREEN_WIDTH, MESSAGE_AREA_HEIGHT))
                font = pg.font.Font(None, 25)
                # Afficher le message de game over si le jeu est terminé
                if self.game_over:
                    text = font.render("Game Over!", True, BLUE)
                else:
                    text = font.render(self.error_message, True, BLUE)
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - MESSAGE_AREA_HEIGHT // 2))
                screen.blit(text, text_rect)
            def draw_number(self, screen, value, pos):
                font = pg.font.Font(None, 40)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(pos[0] * CELL_SIZE + CELL_SIZE // 2, pos[1] * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)
            def draw_clock(self, screen):
                elapsed_time = (pg.time.get_ticks() - self.start_time) // 1000
                remaining_time = max(0, self.clock_time - elapsed_time)  # Calculer le temps restant
                font = pg.font.Font(None, 25)
                text = font.render("Time: " + str(remaining_time) + "s", True, BLACK)
                text_rect = text.get_rect(left=10, centery=SCREEN_HEIGHT - MESSAGE_AREA_HEIGHT // 2)
                screen.blit(text, text_rect)
                # Définir game_over sur True si le temps est écoulé
                if remaining_time == 0:
                    self.game_over = True
            def is_valid_move(self, value, pos):
                row, col = pos
                if value == 0:
                    return True
                # Check row
                if value in self.grid[row, :]:
                    return False
                # Check column
                if value in self.grid[:, col]:
                    return False
                # Check 3x3 grid
                start_row, start_col = (row // 3) * 3, (col // 3) * 3
                if value in self.grid[start_row:start_row + 3, start_col:start_col + 3]:
                    return False
                return True
            def input_number(self, number):
                if self.selected:
                    col, row = self.selected
                    if self.is_valid_move(number, (row, col)):
                        self.grid[row][col] = number
                        self.error_message = ""
                    else:
                        self.error_message = "Mouvement invalide"
            def click(self, pos):
                if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT - MESSAGE_AREA_HEIGHT:
                    col = pos[0] // CELL_SIZE
                    row = pos[1] // CELL_SIZE
                    self.selected = (col, row)
                else:
                    self.selected = None
        def main():
            pg.init()
            screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pg.display.set_caption("Sodoku")
            # Charger et jouer le fichier audio au début du jeu
            pg.mixer.init()
            pg.mixer.music.load(AUDIO_FILE)
            pg.mixer.music.play(-1)  # -1 pour jouer en boucle
            sudoku_game = SudokuGame(self.age)
            running = True
            clock = pg.time.Clock()  # Créer une horloge
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        pos = pg.mouse.get_pos()
                        sudoku_game.click(pos)
                    elif event.type == pg.KEYDOWN:
                        if event.key == pg.K_1:
                            sudoku_game.input_number(1)
                        elif event.key == pg.K_2:
                            sudoku_game.input_number(2)
                        elif event.key == pg.K_3:
                            sudoku_game.input_number(3)
                        elif event.key == pg.K_4:
                            sudoku_game.input_number(4)
                        elif event.key == pg.K_5:
                            sudoku_game.input_number(5)
                        elif event.key == pg.K_6:
                            sudoku_game.input_number(6)
                        elif event.key == pg.K_7:
                            sudoku_game.input_number(7)
                        elif event.key == pg.K_8:
                            sudoku_game.input_number(8)
                        elif event.key == pg.K_9:
                            sudoku_game.input_number(9)
                        elif event.key == pg.K_DELETE or event.key == pg.K_BACKSPACE:
                            sudoku_game.input_number(0)
                        elif event.key == pg.K_r:  # Appuyez sur 'r' pour réinitialiser le plateau
                            sudoku_game.grid = np.transpose(sudoku_game.grid)
                screen.fill(WHITE)
                sudoku_game.draw(screen)
                pg.display.flip()
                clock.tick(sudoku_game.clock_time)  # Régler la vitesse du jeu en fonction du clock time
            pg.quit()
            sys.exit()
        if __name__ == "__main__":
            main()

        messagebox.showinfo("Flag Matching Game", "You are playing Flag Matching Game. Click OK to finish the game.")

        # After playing the game, display score
        self.display_score()
# **************************************   end Soduku       *********************************************  

# **************************************   start puzzle      *********************************************  
    def puzzle(self):
        # Fonction principale du programme
        def main():
            # Créez une instance de Clock pour contrôler le taux de rafraîchissement
            clock = Clock()
            # Initialisation de Pygame
            pygame.init()
            pygame.font.init()
            # Définition de la taille de la fenêtre
            SIZE = WIDTH, HEIGHT = (1000, 1000)
            # Couleur de fond de la fenêtre
            BGCOLOR = (50, 50, 50)
            # Police de caractères pour le texte
            GFONT = pygame.font.SysFont("Comic Sans MS", 30)
            # Création de la fenêtre
            window = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
            pygame.display.set_caption('test')
            # Définition des coordonnées x et y pour la position initiale du puzzle dans la fenêtre
            x = 100
            y = 100
            # Taille initiale de l'image
            initial_image_size = (653, 750)
            # Taille de la fenêtre
            window_size = (1000, 1000)
            # Nombre de pièces dans le puzzle pour le premier niveau
            pieces_count = 2
            # Calculer la taille d'une pièce en fonction du nombre de pièces dans une rangée ou une colonne
            piece_width = initial_image_size[0] // pieces_count
            piece_height = initial_image_size[1] // pieces_count
            # Création de l'objet Puzzle initial avec les paramètres spécifiés
            p= Puzzle(f'C:\\Users\\White Devil\\Desktop\\PacMan\\code\\image.jpg', initial_image_size, (pieces_count, pieces_count), (x, y))
            p.scramble()  # Mélange initial du puzzle
            # Définit le niveau de puzzle actuel en fonction du nombre de pièces
            current_level = int(math.sqrt(pieces_count))
            # Variables pour le suivi des touches pressées et du clic de souris
            up = left = down = right = False
            mouse_clicked = False  # Nouvelle variable pour suivre l'état du clic de souris
            # Boucle principale du jeu
            running = True
            while running:
                # Limite le taux de rafraîchissement à 60 images par seconde
                clock.tick(60)
                # Gestion des événements Pygame
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre
                        running = False
                    # Gestion des événements de clic de souris
                    if event.type == pygame.MOUSEBUTTONDOWN:  # Si un bouton de la souris est enfoncé
                        if event.button == 1:  # Bouton gauche de la souris
                            mouse_clicked = True
                    elif event.type == pygame.MOUSEBUTTONUP:  # Si un bouton de la souris est relâché
                        if event.button == 1:  # Bouton gauche de la souris
                            mouse_clicked = False
                            # Vérifie si les coordonnées du clic sont à l'intérieur de la zone du bouton "Next Level"
                            if 800 < event.pos[0] < 950 and 50 < event.pos[1] < 100:
                                # Charge le niveau suivant du puzzle
                                current_level += 1
                                if current_level > 4:  # Supposons que le niveau maximal soit 4 (puzzle 4x4)
                                    current_level = 2  # Reviens au niveau initial si le niveau maximal est atteint
                                # Calculer le nombre de pièces pour le nouveau niveau
                                pieces_count = current_level ** 2
                                # Calculer la taille d'une pièce en fonction du nombre de pièces dans une rangée ou une colonne
                                piece_width = initial_image_size[0] // current_level
                                piece_height = initial_image_size[1] // current_level
                                # Redimensionner l'image du puzzle avec la nouvelle taille des pièces
                                p= Puzzle(f'C:\\Users\\White Devil\\Desktop\\PacMan\\code\\image.jpg', initial_image_size, (current_level, current_level), (x, y))
                                p.scramble()
                    # Vérifie si les mouvements sont autorisés avant de traiter les touches pressées
                    if p.moves_allowed():
                        if event.type == pygame.KEYDOWN:  # Si une touche est pressée
                            # Gestion des mouvements du puzzle
                            if event.key == pygame.K_UP:
                                if not up:
                                    p.move_up()
                                    up = True
                            elif event.key == pygame.K_LEFT:
                                if not left:
                                    p.move_left()
                                    left = True
                            elif event.key == pygame.K_DOWN:
                                if not down:
                                    p.move_down()
                                    down = True
                            elif event.key == pygame.K_RIGHT:
                                if not right:
                                    p.move_right()
                                    right = True
                    # Si une touche est relâchée, réinitialise le suivi des touches
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            up = False
                        elif event.key == pygame.K_LEFT:
                            left = False
                        elif event.key == pygame.K_DOWN:
                            down = False
                        elif event.key == pygame.K_RIGHT:
                            right = False
                # Efface la fenêtre avec la couleur de fond
                window.fill(BGCOLOR)
                # Met à jour et rend le puzzle sur la fenêtre
                p.update()
                p.render(window)
                # Si le puzzle est résolu, révèle-le à l'écran et affiche le bouton "Next Level"
                if p.is_solved():
                    p.reveal(window)
                    pygame.draw.rect(window, (0, 255, 0), pygame.Rect(800, 50, 150, 50), border_radius=5)
                    font = pygame.font.SysFont(None, 30)
                    text_surface = font.render("Next Level", True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=(875, 75))
                    window.blit(text_surface, text_rect)
                # Met à jour l'affichage de la fenêtre
                pygame.display.update()
        # Exécute la fonction principale si le script est lancé en tant que programme principal
        if __name__ == '__main__':
            main()
# **************************************   end puzzle      *********************************************

# **************************************   start MemoryCard     *********************************************
    def MemoryCard(self):
        # Placeholder function for playing Balloon Catching Game
        class MemoryCardGame:
            def __init__(self):
                self.root = tk.Toplevel()  # Utilise Toplevel pour la fenêtre enfant
                self.root.title("Memory Game")  # Définit le titre de la fenêtre
                self.current_level = tk.StringVar(value="hard")  # Niveau par défaut est "Difficile"
                self.game_end = 0  # Initialisation du compteur de fin de jeu
                level_frame = tk.Frame(self.root)  # Crée un cadre pour le choix du niveau
                level_frame.pack(pady=10)  # Ajoute un espacement en y de 10 pixels
                easy_button = tk.Radiobutton(level_frame, text="Facile", variable=self.current_level, value="easy", font=("Helvetica", 14), command=self.update_game)
                easy_button.pack(side=tk.LEFT, padx=10)  # Ajoute un bouton pour le niveau facile
                hard_button = tk.Radiobutton(level_frame, text="Difficile", variable=self.current_level, value="hard", font=("Helvetica", 14), command=self.update_game)
                hard_button.pack(side=tk.LEFT, padx=10)  # Ajoute un bouton pour le niveau difficile
                self.game_window = tk.Frame(self.root)  # Crée un cadre pour le jeu
                self.game_window.pack(pady=20)  # Ajoute un espacement en y de 20 pixels
                self.cards = []  # Liste pour stocker les boutons de carte
                self.clicked_cards = []  # Liste pour stocker les cartes cliquées
                self.start_time = None  # Initialise le temps de début du jeu
                self.create_widgets()  # Appelle la fonction pour créer les widgets
            def create_widgets(self):
                fonts = ('Helvetica', 20, 'bold')  # Définit la police pour les boutons de carte
                # Détermine le nombre de cartes en fonction du niveau actuel
                data_length = 8 if self.current_level.get() == 'easy' else 16
                # Génère des paires de données de carte mélangées
                data = random.sample(list("ABCDEFGH"), data_length // 2) * 2
                random.shuffle(data)
                # Crée les boutons de carte
                for i in range(data_length):
                    btn = tk.Button(self.game_window, font=fonts, width=5, height=3, text="", command=lambda idx=i: self.flip_card(idx, data[idx]))
                    btn.grid(row=i // 4, column=i % 4, padx=20, pady=40)  # Positionne les boutons dans une grille
                    self.cards.append(btn)  # Ajoute le bouton à la liste
            def flip_card(self, idx, text):
                if len(self.clicked_cards) < 2:
                    btn = self.cards[idx]
                    btn.configure(text=text, state=tk.DISABLED)  # Désactive le bouton après le clic
                    self.clicked_cards.append((idx, text))  # Ajoute la carte cliquée à la liste
                    if len(self.clicked_cards) == 2:
                        self.root.after(500, self.check_match)  # Vérifie les correspondances après un délai
                        # Démarre le chronomètre lors du premier clic sur une carte
                        if not self.start_time:
                            self.start_time = time.time()
            def check_match(self):
                if len(self.clicked_cards) == 2:
                    idx1, text1 = self.clicked_cards[0]
                    idx2, text2 = self.clicked_cards[1]
                    if text1 != text2:
                        # Retourne les cartes non correspondantes après un délai
                        self.cards[idx1].configure(text="", state=tk.NORMAL)
                        self.cards[idx2].configure(text="", state=tk.NORMAL)
                    else:
                        self.game_end += 1  # Incrémente le compteur de fin de jeu
                    self.clicked_cards.clear()  # Efface la liste des cartes cliquées
                    # Vérifie si le jeu est terminé
                    data_length = 8 if self.current_level.get() == 'easy' else 16
                    if self.game_end == data_length // 2:
                        elapsed_time = int(time.time() - self.start_time)
                        messagebox.showinfo("Félicitations !", f"Vous avez terminé le jeu en {elapsed_time} secondes.")
                        self.root.destroy()  # Ferme la fenêtre du jeu après la fin du jeu
            def update_game(self):
                # Détruit les cartes existantes
                for card in self.cards:
                    card.destroy()
                # Réinitialise l'état du jeu
                self.cards.clear()
                self.clicked_cards.clear()
                self.start_time = None
                self.game_end = 0
                # Crée de nouvelles cartes en fonction du niveau mis à jour
                self.create_widgets()
            def play(self):
                self.root.mainloop()
        # Exécute le jeu
        if __name__ == "__main__":
            game = MemoryCardGame()
            game.play()
# **************************************   end MemoryCard     *********************************************
    def display_score(self):
        # Placeholder function to display score
        score = 50  # Placeholder score, you can replace it with actual score
        messagebox.showinfo("Score", f"Your score is: {score}")
if __name__ == "__main__":
    app = GameSelector()
    app.mainloop()