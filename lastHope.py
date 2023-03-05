import math
import random
import sys
import pygame
import os 
import subprocess
import cv2
from threading import Thread
from pygame.locals import *
bonus1 = False
bonus2 = False
bonus3 = False
bonus4 = False
bonus5 = False
bonus6 = False
bonus7 = False
bonus8 = False
class x1():
    def __init__(self):
        self.x1 = 0
    def get(self):
        return self.x1
    def set(self,value):
        self.x1 = value
x1 = x1()
class x2():
    def __init__(self):
        self.x2 = 0
    def get(self):
        return self.x2
    def set(self,value):
        self.x2 = value
x2 = x2()
start = False
pause = False
pointsPlayer1 = 0
pointsPlayer2 = 0
def modifyBonus1(value):
    bonus1 = value
def modifyBonus2(value):
    bonus2 = value
def modifyBonus3(value):
    bonus3 = value
def modifyBonus4(value):
    bonus4 = value
def modifyBonus5(value):
    bonus5 = value
def modifyBonus6(value):
    bonus6 = value
def modifyBonus7(value):
    bonus7 = value
def modifyBonus8(value):
    bonus8 = value
def modifyPointPlayer1(value):
    pointsPlayer1 =value
def modifyPointPlayer2(value):
    pointsPlayer2 =value
def modifyStart(value):
    start =value
def modifyPause(value):
    pause =value
    

ballVelocity = 5
ballRadius = 5
sprites = []
end = False

WHITE = (255,255,255)
BLACK = (0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
BLUE =(0,0,255)


def getxPos():
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        faces = sorted(faces, key=lambda x: x[0])
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if(len(faces) == 2):
            face2 = faces[1][0]
            face1 = faces[0][0]
            x1.set(face1)
            x2.set(face2)
            print("x1 has been modified: ",face1)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
xPos = Thread(target = getxPos)
xPos.start()
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.nbrBlueBalls = 0
        self.nbrRedBalls = 0
        
        if random.randint(0,1) == 1:
            self.velocityX = ballVelocity 
        else:
            self.velocityX = -ballVelocity
         
        if random.randint(0,1) == 1:
            self.velocityY = ballVelocity
        else:
            self.velocityY = -ballVelocity

    def update(self):
        self.x += self.velocityX /2
        self.y += self.velocityY /2

        ball = self.draw()

         # Check for collision with bricks
        for brick in bricks:
            if ball.colliderect(brick):
                bricks.remove(brick)
                if (ball.bottom > brick.top and ball.top < brick.top) or (ball.top < brick.bottom and ball.bottom > brick.bottom):   
                    self.velocityY = -self.velocityY
                if (ball.right > brick.left and ball.left < brick.left) or (ball.left < brick.right and ball.right > brick.right):
                    self.velocityX = -self.velocityX
                break
        
       
            
        
        if self.x - self.radius < 0  or self.x + self.radius > screen_width:
            self.velocityX *= -1        
        if self.color == RED:
            if ball.colliderect(paddleRed):
                self.velocityY *= -1
            elif self.y + self.radius > screen_height:
                    self.x = 2 * screen_width
                    self.y = screen_height//2
                    self.velocityX = 1
                    self.velocityY = 0
                    self.nbrRedBalls -=1
        else:
            if ball.colliderect(paddleBlue):
                self.velocityY *= -1
            elif self.y + self.radius > screen_height:
                self.x = 2 * screen_width
                self.y = screen_height//2   
                self.velocityX = 0
                self.velocityY = 0
                self.nbrBlueBalls -=1

        if  self.y - self.radius < 0 : 
            self.velocityY *= -1
           
    def draw(self):
        return pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

pygame.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("P-BOYZ")
clock = pygame.time.Clock()

def updateBackgroundImage():
    background_image = pygame.image.load("427159.jpg")
    background_rect = background_image.get_rect()
    background_x = screen_width // 2 - background_rect.width // 2
    background_y = screen_height // 2 - background_rect.height // 2
    screen.blit(background_image, (background_x, background_y))

updateBackgroundImage()
redBasePlace = []
redBasePlace = screen_width // 2.5 -70, screen_height - 100
blueBasePlace = []
blueBasePlace = screen_width // 2.5 - 200, screen_height - 100

#gestion de la barre
paddleRed = pygame.Rect(redBasePlace[0], redBasePlace[1], 140, 20)
paddleBlue = pygame.Rect(blueBasePlace[0], blueBasePlace[1], 140, 20)

paddle_speedRed = 0
paddle_speedBlue = 0

#gestion des balles
redBalls = []
x = screen_width /2 - 10 # redBasePlace[0]+ 10
y = screen_height / 1.3 # redBasePlace[1]+200
color = RED
redBall = Ball(x, y, ballRadius, color)
redBalls.append(redBall)
sprites.append(redBall.draw())


blueBalls = []
x =  screen_width /2 + 10 # blueBasePlace[0]+10
y =  screen_height / 1.3  # blueBasePlace[1]+200
color = BLUE
blueBall = Ball(x, y, ballRadius, color)
blueBalls.append(blueBall)
sprites.append(blueBall.draw())


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



while end != True:

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
            if event.key == pygame.K_r:
                print(event.key)
                newRedBalls = []
                for i in redBalls:
                     for y in range(3):
                        x = i.x
                        y = i.y
                        ball = Ball(x, y, ballRadius, RED)
                        newRedBalls.append(ball)
                        sprites.append(ball.draw())
                        self.nbrRedBalls +=1

                for ball in newRedBalls:
                    redBalls.append(ball)

            if event.key == pygame.K_b:
                print(event.key)
                newBlueBalls = []
                for i in blueBalls:
                    for y in range(3):
                        x = i.x
                        y = i.y
                        ball = Ball(x, y, ballRadius, BLUE)
                        newBlueBalls.append(ball)
                        sprites.append(ball.draw())
                        self.nbrBlueBalls +=1
                for ball in newBlueBalls:
                    blueBalls.append(ball)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_speedRed = 0
            if event.key == pygame.K_q or event.key == pygame.K_d:
                paddle_speedBlue = 0
    print(x1.get())
    #move the balls
    for ball in redBalls:
        ball.update()
      #  print("update Red Balls")
    for ball in blueBalls:
        ball.update()
    #  print("BlueBalls update")
      
    # Move the paddleRed
    paddleRed.x = 1900 - 2.5*((1900/500)*x1.get())
    if paddleRed.left < 0:
        paddleRed.left = 0
    elif paddleRed.right > screen_width:
        paddleRed.right = screen_width

    # Move the paddleBlue
    paddleBlue.x = 1900 - 2.5*(1900/500*(x2.get()-250))
    if paddleBlue.left < 0:
        paddleBlue.left = 0
    elif paddleBlue.right > screen_width:
        paddleBlue.right = screen_width

    pygame.draw.rect(screen, RED, paddleRed)
    pygame.draw.rect(screen, BLUE, paddleBlue)

    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)
    
    pygame.display.flip()
    clock.tick(60)
    updateBackgroundImage()    

    #if self.nbrBlueBalls <= 0:
        #end = True
    #if self.nbrRedBalls <= 0:
        #end = True
    

pygame.quit()