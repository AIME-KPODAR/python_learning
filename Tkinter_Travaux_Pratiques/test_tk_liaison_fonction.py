import pygame
import time

print("Lancement du test audio...")

# Initialisation de pygame
pygame.mixer.init()

# Chargement du son
pygame.mixer.music.load("intro_video_sound.mp3")


# Lecture
def play():
    pygame.mixer.music.play()

# Attente pendant la lecture
while pygame.mixer.music.get_busy():
    time.sleep(0.1)

print("Son terminé.")