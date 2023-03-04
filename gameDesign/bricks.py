import pygame
from pygame.locals import *

pygame.init()

'''info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h'''
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

background_image = pygame.image.load("427159.jpg")
background_rect = background_image.get_rect()
background_x = screen_width // 2 - background_rect.width // 2
background_y = screen_height // 2 - background_rect.height // 2

#background_color = (0, 0, 0) # black background color

title_font = pygame.font.SysFont("Arial", 72)
title = title_font.render("Hello, World!", True, (255, 255, 255)) # white text

title_x = screen_width // 2 - title.get_width() // 2
title_y = screen_height // 2 - title.get_height() // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.blit(background_image, (background_x, background_y))
    
    #screen.fill(background_color) # fill the screen with the background color
    
    screen.blit(title, (title_x, title_y)) # draw the title
    
    pygame.display.update() # update the screen

pygame.quit()
