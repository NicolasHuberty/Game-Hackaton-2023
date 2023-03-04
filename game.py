import math
import random
import sys
import pygame
import os 
import subprocess
from pygame.locals import *

WHITE = (255,255,255)
BLACK = (0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
BLEU =(0,0,255)

class Game:
    def __init__(self, x, y, nbrBlocks):
        self.posBarreRed = x/2
        self.posBarreBlue = x/2
        self.x = x
        self.y = y
        self.nbrBlocks = nbrBlocks
        self.GameFinish = False
        self.matrix = [[0 for j in range(y)] for i in range(x)]

        global pointBlue
        pointBlue = 0
        global pointRed
        pointRed = 0
        global bonusBlue
        bonusBlue = []
        global bonusRed
        bonusRed = []
        global start
        start = False
        global pause
        pause = False  
        
    def choose(self,choose):
        if choose == 1:
            for i in range(0,(self.x),1):
                for j in range(0,(self.y),1):
                    if i == 0 or j == 0:
                        self.matrix[i][j] = Block([i,j],False)

            for i in range(1,(self.x-10),1):
                for j in range(1,(self.y-1),1):
                        self.matrix[i][j] = Block([i,j],True)
            

    def removeBlock(self, pos):
        self.matrix[pos[0],pos[1]] = None
        self.nbrBlocks -=1

        if self.nbrBlocks <= 0:
            self.GameFinish == True
    
    def GetFroPosition(self, pos):
        return self.matrix[pos[0]][pos[1]]
                


class Block:
    def __init__(self, pos, outLigne):
        self.position = pos
        if outLigne == True:
            self.durte = 1
        else:
            self.durte = sys.maxsize
    
    def hit(self):
        self.durte = self.durte -1

        if self.durte <= 0:
            Game.removeBlock(self.position)



class Ball:
    def __init__(self, pos , direction , speed, size, color):
        self.position = pos
        self.direction = []
        self.direction[0] = direction[0] 
        self.direction[1] = direction[1] 
        self.speed = speed
        self.size = size
        self.color = color
        self.alive = True

    def bouger(self):
        while self.alive:
            positionSuivante = []
            positionSuivante[0] = 1 if self.direction[0] > self.position[0] else -1 if self.direction[0] < self.position[0] else 0
            positionSuivante[1] = 1 if self.direction[1] > self.position[1] else -1 if self.direction[1] < self.position[1] else 0   

            if positionSuivante[0] > game.x:
                self.alive = False
                return

            next = Game.GetFroPosition(game,positionSuivante)

            if next == None:
                self.position = positionSuivante
            else:
                self.changerDirrection()
                Block.hit(next)



    
    def changerDirrection(self, direction_x , direction_y):
        self.direction_x = direction_x
        self.direction_y = direction_y


pygame.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
'''screen_width = 800
screen_height = 600'''
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("P-BOYZ")
clock = pygame.time.Clock()


#font_path = os.path.join("fonts", "Robus-BWqOd.otf")
def updateBackgroundImage():
    background_image = pygame.image.load("427159.jpg")
    background_rect = background_image.get_rect()
    background_x = screen_width // 2 - background_rect.width // 2
    background_y = screen_height // 2 - background_rect.height // 2
    screen.blit(background_image, (background_x, background_y))

updateBackgroundImage()
game = Game(100,100,20)

#gestion de la barre
paddleRed = pygame.Rect(screen_width // 1.5 - 70, screen_height - 50, 140, 20)
paddleBlue = pygame.Rect(screen_width // 2.5 - 70, screen_height - 50, 140, 20)

paddle_speedRed = 0
paddle_speedBlue = 0


print("screen_width ")
print(screen_width)

#creation des briques
brick_width = 40
brick_height = 20
brick_spacing = 10
bricks = []
for i in range(screen_width// (brick_spacing + brick_width)):
    brick_x = brick_spacing + i * (brick_width + brick_spacing)
    for j in range(int((screen_height // (brick_spacing + brick_height)//1.5))):
        brick_y = brick_spacing + j * (brick_height + brick_spacing)
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick_rect)



while game.GameFinish != True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speedRed = -10
            elif event.key == pygame.K_RIGHT:
                paddle_speedRed = 10
            if event.key == pygame.K_q:
                paddle_speedBlue = -10
            elif event.key == pygame.K_d:
                paddle_speedBlue = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_speedRed = 0
            if event.key == pygame.K_q or event.key == pygame.K_d:
                paddle_speedBlue = 0
   
    # Move the paddleRed
    paddleRed.x += paddle_speedRed
    if paddleRed.left < 0:
        paddleRed.left = 0
    elif paddleRed.right > screen_width:
        paddleRed.right = screen_width

      # Move the paddleBlue
    paddleBlue.x += paddle_speedBlue
    if paddleBlue.left < 0:
        paddleBlue.left = 0
    elif paddleBlue.right > screen_width:
        paddleBlue.right = screen_width


    pygame.draw.rect(screen, RED, paddleRed)
    pygame.draw.rect(screen, BLEU, paddleBlue)
    pygame.draw.circle(screen, BLEU, (480, 540), 10)
    pygame.draw.circle(screen, RED, (1440, 540), 10)

    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)
    
    # Update the screen and clock
    pygame.display.flip()
    clock.tick(60)
    updateBackgroundImage()
    

pygame.quit()