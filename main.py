import pygame
import os 
import subprocess
from pygame.locals import *

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
BLEU =(0,0,255)

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
'''screen_width = 800
screen_height = 600'''
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("P-BOYZ")
clock = pygame.time.Clock()


font_path = os.path.join("fonts", "Robus-BWqOd.otf")

background_image = pygame.image.load("427159.jpg")
background_rect = background_image.get_rect()
background_x = screen_width // 2 - background_rect.width // 2
background_y = screen_height // 2 - background_rect.height // 2

title_font = pygame.font.Font(font_path, int(((screen_width // 5) *1.5)/4*3))
title = title_font.render("P-BOYZ", True, WHITE)

text_font = pygame.font.Font(font_path, 69)
text = text_font.render("Lancer le jeu sur votre telephone", True, WHITE)

title_x = screen_width // 2 - title.get_width() // 2
title_y = 150

text_x = screen_width // 2 - text.get_width() // 2
text_y = screen_height // 1.5 - text.get_height() // 2

# Define the clickable area of the text as a Rect object
text_rect = text.get_rect(center=(text_x + text.get_width() // 2, text_y + text.get_height() // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            # Check if the mouse cursor is within the clickable area
            if text_rect.collidepoint(event.pos):
                subprocess.Popen(["python", "game.py"])
                pygame.quit()
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     running=False  

    screen.blit(background_image, (background_x, background_y))

    screen.blit(title, (title_x, title_y))
    screen.blit(text, (text_x, text_y))

    pygame.display.update()

pygame.quit()