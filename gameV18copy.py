import math
import random
import sys
import time
import pygame
import os 
import subprocess
import cv2
from threading import Thread
from multiprocessing import Process
from matrixe import *
from pygame.locals import *
from flask import Flask, render_template, request, jsonify

global_var = 0
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
class bonus1():
    def __init__(self):
        self.bonus1 = 0
    def get(self):
        return self.bonus1
    def set(self,value):
        self.bonus1 = value
bonus1 = bonus1()

class bonus2():
    def __init__(self):
        self.bonus2 = 0
    def get(self):
        return self.bonus2
    def set(self,value):
        self.bonus2 = value
bonus2 = bonus2()

class bonus3():
    def __init__(self):
        self.bonus3 = 0
    def get(self):
        return self.bonus3
    def set(self,value):
        self.bonus3 = value
bonus3 = bonus3()

class bonus4():
    def __init__(self):
        self.bonus4 = 0
    def get(self):
        return self.bonus4
    def set(self,value):
        self.bonus4 = value
bonus4 = bonus4()

class bonus5():
    def __init__(self):
        self.bonus5 = 0
    def get(self):
        return self.bonus5
    def set(self,value):
        self.bonus5 = value
bonus5 = bonus5()

class bonus6():
    def __init__(self):
        self.bonus6 = 0
    def get(self):
        return self.bonus6
    def set(self,value):
        self.bonus6 = value
bonus6 = bonus6()

class bonus7():
    def __init__(self):
        self.bonus7 = 0
    def get(self):
        return self.bonus7
    def set(self,value):
        self.bonus7 = value
bonus7 = bonus7()

class bonus8():
    def __init__(self):
        self.bonus8 = 0
    def get(self):
        return self.bonus8
    def set(self,value):
        self.bonus8 = value
bonus8 = bonus8()

class pointsPlayer1 ():
    def __init__(self):
        self.pointsPlayer1  = 0
    def get(self):
        return self.pointsPlayer1 
    def set(self,value):
        self.pointsPlayer1  = value
pointsPlayer1 = pointsPlayer1()

class pointsPlayer2 ():
    def __init__(self):
        self.pointsPlayer2  = 0
    def get(self):
        return self.pointsPlayer2 
    def set(self,value):
        self.pointsPlayer2  = value
pointsPlayer2 = pointsPlayer2()


class start ():
    def __init__(self):
        self.start  = False
    def get(self):
        return self.start
    def set(self,value):
        self.start  = value
start = start()

class pause ():
    def __init__(self):
        self.pause  = False
    def get(self):
        return self.pause 
    def set(self,value):
        self.pause  = value
pause = pause()
    


ballVelocity = 5
ballRadius = 5
sprites = []
end = False

WHITE = (255,255,255)
BLACK = (0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
BLUE =(0,0,255)
def phoneConnection():
    app = Flask(__name__)
    @app.route('/update_bonus', methods=['POST'])
    def update_bonus():
        bonus = str(request.form['bonus'])
        bonusValue = request.form.get('bonusValue')
        if bonus == 'bonus1' : bonus1.set(bonusValue)
        elif bonus == 'bonus2' : bonus2.set(bonusValue)
        elif bonus == 'bonus3' : bonus3.set(bonusValue)
        elif bonus == 'bonus5' : bonus5.set(bonusValue)
        elif bonus == 'bonus6' : bonus6.set(bonusValue)
        elif bonus == 'bonus7' : bonus7.set(bonusValue)
        elif bonus == 'bonus8' : bonus8.set(bonusValue)
        
        return f"{bonus} : {bonusValue}"

    @app.route('/update_pause', methods=['POST'])
    def update_pause():
        #print(str(request.form['pause']) == "true")
        pause.set(str(request.form['pause']) == "true")
        
        
        return f"py pause : {pause.get()}"


    @app.route('/recupValeurInPy')
    def get_bonus1():
        return jsonify(bonus1.get(),bonus2.get(),bonus3.get(),bonus4.get(),pointsPlayer1.get(),pointsPlayer2.get(),pause.get(),bonus5.get(),bonus6.get(),bonus7.get(),bonus8.get())



    @app.route("/")
    def index():
        # Pass global variable value to template
        return render_template("index.html", global_var=global_var)

    @app.route("/player1")
    def player1():
        # Pass global variable value to template
        return render_template("player1.html", global_var=global_var)

    @app.route("/player2")
    def player2():
        # Pass global variable value to template
        return render_template("player2.html", global_var=global_var)
    app.run(host="0.0.0.0", port=5000, debug=True)

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
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
xPos = Thread(target = getxPos)
xPos.start()
phoneCo = Process(target = phoneConnection)
phoneCo.start()

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
                #rect_vies[brick] -=1
                #if rect_vies[brick]<= 0:
                bricks.remove(brick)
                if (ball.bottom > brick.top and ball.top < brick.top) or (ball.top < brick.bottom and ball.bottom > brick.bottom):   
                    self.velocityY = -self.velocityY
                if (ball.right > brick.left and ball.left < brick.left) or (ball.left < brick.right and ball.right > brick.right):
                    self.velocityX = -self.velocityX
            
                if self.color == RED:
                    pointsPlayer1.set(pointsPlayer1.get()+1)
                else:
                    pointsPlayer2.set(pointsPlayer2.get()+1)  
                break  
        
                game.nbrBlocks -= 1        
       
            
        
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
redBasePlace = screen_width // 1.5 - 70, screen_height - 50
blueBasePlace = []
blueBasePlace = screen_width // 2.5 - 70, screen_height - 50

#gestion de la barre
paddleRed = pygame.Rect(redBasePlace[0], redBasePlace[1], 140, 20)
paddleBlue = pygame.Rect(blueBasePlace[0], blueBasePlace[1], 140, 20)

paddle_speedRed = 0
paddle_speedBlue = 0

#gestion des balles
redBalls = []
x = redBasePlace[0] + 70 # screen_width /2 - 10 #
y = redBasePlace[1]-20 # screen_height / 1.3 # 
color = RED
redBall = Ball(x, y, ballRadius, color)
redBalls.append(redBall)
sprites.append(redBall.draw())


blueBalls = []
x =   blueBasePlace[0] + 70 # screen_width /2 + 10 #
y =  blueBasePlace[1]-20 # screen_height / 1.3  #
color = BLUE
blueBall = Ball(x, y, ballRadius, color)
blueBalls.append(blueBall)
sprites.append(blueBall.draw())


#creation en fonction de la map
actualMatrixe = getMatrixes(5)
mapWidth = actualMatrixe[0] +5
print(mapWidth)
mapHeight = actualMatrixe[1] +4
print(mapHeight)
matrix_data = actualMatrixe[2] 


#creation des briques
brick_spacing = screen_width // 350
brick_width = screen_width // (mapHeight)
brick_height = screen_height // (mapWidth)
bricks = []

print(brick_spacing)
print(brick_width)
print(brick_height)

for i in range(mapHeight-4):
    brick_x = brick_spacing + i * (brick_width + brick_spacing)
    for j in range(mapWidth-10):
        if matrix_data[j][i] == 2:
            brick_y = brick_spacing + j * (brick_height + brick_spacing)
            brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
            bricks.append(brick_rect)
            #game.nbrBlocks +=1
            #rect_vies[brick_rect] = 1
        



while end != True:
    
    while pause.get():
        time.sleep(0.1)

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

    #move the balls
    for ball in redBalls:
        ball.update()
      #  print("update Red Balls")
    for ball in blueBalls:
        ball.update()
    #  print("BlueBalls update")
    print("x1: ",x1.get(),"pause: ",pause.get()," user1 point: ",pointsPlayer1.get())
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