import random
import time
import pygame
from matrixe import *
import cv2
from threading import Thread
from flask import Flask, render_template, request, jsonify
import requests
import subprocess
import playsound
global_var = 0
class sizeBluePadle():
    def __init__(self):
        self.sizeBluePadle  = 140
    def get(self):
        return self.sizeBluePadle 
    def set(self,value):
        self.sizeBluePadle  = value
sizeBluePadle = sizeBluePadle()

class sizeRedPadle():
    def __init__(self):
        self.sizeRedPadle  = 140
    def get(self):
        return self.sizeRedPadle 
    def set(self,value):
        self.sizeRedPadle  = value
sizeRedPadle = sizeRedPadle()
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
        self.bonus1 = False
    def get(self):
        return self.bonus1
    def set(self,value):
        if(value):
            requests.post("http://localhost:5000/update_bonus",data={"bonus":"bonus1","bonusValue":"true"})
        self.bonus1 = value
bonus1 = bonus1()

class bonus2():
    def __init__(self):
        self.bonus2 = False
    def get(self):
        return self.bonus2
    def set(self,value):
        if value:
            requests.post("http://localhost:5000/update_bonus",data={"bonus":"bonus2","bonusValue":"true"})
        self.bonus2 = value
bonus2 = bonus2()

class bonus3():
    def __init__(self):
        self.bonus3 = False
    def get(self):
        return self.bonus3
    def set(self,value):
        if value:
            requests.post("http://localhost:5000/update_bonus",data={"bonus":"bonus3","bonusValue":"true"})
        self.bonus3 = value
bonus3 = bonus3()

class bonus4():
    def __init__(self):
        self.bonus4 = False
    def get(self):
        return self.bonus4
    def set(self,value):
        if value:
            requests.post("http://localhost:5000/update_bonus",data={"bonus":"bonus4","bonusValue":"true"})
        self.bonus4 = value
bonus4 = bonus4()

class bonus5():
    def __init__(self):
        self.bonus5 = False
    def get(self):
        return self.bonus5
    def set(self,value):
        if value:
            requests.post("http://localhost:5000/update_bonus",data={"bonus":"bonus5","bonusValue":"true"})
        self.bonus5 = value
bonus5 = bonus5()

class bonus6():
    def __init__(self):
        self.bonus6 = False
    def get(self):
        return self.bonus6
    def set(self,value):
        if value:
            requests.post("http://localhost:5000/update_bonus",data={"bonus":"bonus6","bonusValue":"true"})
        self.bonus6 = value
bonus6 = bonus6()

class bonus7():
    def __init__(self):
        self.bonus7 = False
    def get(self):
        return self.bonus7
    def set(self,value):
        if value:
            requests.post("http://localhost:5000/update_bonus",data={"bonus":"bonus7","bonusValue":"true"})
        self.bonus7 = value
bonus7 = bonus7()

class bonus8():
    def __init__(self):
        self.bonus8 = False
    def get(self):
        return self.bonus8
    def set(self,value):
        if value:
            requests.post("http://localhost:5000/update_bonus",data={"bonus":"bonus8","bonusValue":"true"})
        self.bonus8 = value
bonus8 = bonus8()

class pointsPlayer1 ():
    def __init__(self):
        self.pointsPlayer1  = 0
    def get(self):
        return self.pointsPlayer1 
    def set(self,value):
        self.pointsPlayer1  = value
        requests.post("http://localhost:5000/updatePoints",data={"pointsPlayer1":value,"pointsPlayer2":pointsPlayer2.get()})
        
pointsPlayer1 = pointsPlayer1()

class pointsPlayer2 ():
    def __init__(self):
        self.pointsPlayer2  = 0
    def get(self):
        return self.pointsPlayer2 
    def set(self,value):
        self.pointsPlayer2  = value
        requests.post("http://localhost:5000/updatePoints",data={"pointsPlayer1":pointsPlayer1.get(),"pointsPlayer2":value})
pointsPlayer2 = pointsPlayer2()



class start ():
    def __init__(self):
        self.start  = -1
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

class nbrBlocks():
    def __init__(self):
        self.nbrBlocks  = 0
    def get(self):
        return self.nbrBlocks 
    def set(self,value):
        self.nbrBlocks  = value
nbrBlocks = nbrBlocks()

class nbrRedBalls():
    def __init__(self):
        self.nbrRedBalls  = 1
    def get(self):
        return self.nbrRedBalls 
    def set(self,value):
        self.nbrRedBalls  = value
nbrRedBalls = nbrRedBalls()

class nbrBlueBalls():
    def __init__(self):
        self.nbrBlueBalls  = 1
    def get(self):
        return self.nbrBlueBalls 
    def set(self,value):
        self.nbrBlueBalls  = value
nbrBlueBalls = nbrBlueBalls()
class end():
    def __init__(self):
        self.end  = False
    def get(self):
        return self.end 
    def set(self,value):
        self.end  = value
end = end()
def setAllData():
    response = requests.get("http://localhost:5000/recupValeurInPy").json()
    bonus1.set(response[0])
    bonus2.set(response[1])
    bonus3.set(response[2])
    bonus4.set(response[3])
    pause.set(response[6])
    bonus5.set(response[7])
    bonus6.set(response[8])
    bonus7.set(response[9])
    bonus8.set(response[10])
    start.set(response[11])
    print("GEEEEETTTT:: ",start.get())


WHITE = (255,255,255)
BLACK = (0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
BLUE =(0,0,255)
GRAY =(128,128,128)
BORDAUX =(109,7,50)
AMBRE =(240, 195, 0)
BRUN =(91, 60, 17)
CITROUILLE=(223, 109, 20)
TERRE=(146, 109, 39)

ballVelocity = 5
ballRadius = 5
sprites = []
atouts = []
#part telephon
# part face recognition
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
        #cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    

def UI():
    class Atout():
        def __init__(self,x,y,radius,nbrAtout):
            self.x = x
            self.y = y
            self.radius = radius
            self.velocityX = 0
            self.velocityY = ballVelocity
            self.nbrAtout = nbrAtout
            self.color = WHITE

        def update(self):

            self.y += self.velocityY /2

            atout = self.draw()
            
            if self.y + self.radius > screen_height:
                if self.color == RED:    
                    print("INNNN")
                    self.x = 2 * screen_width
                    self.y = screen_height//2
                    self.velocityX = 1
                    self.velocityY = 0
                    if self.nbrAtout == 1:
                        bonus1.set(True)
                    if self.nbrAtout == 2:
                        bonus2.set(True)
                    if self.nbrAtout == 3:
                        bonus3.set(True)
                    if self.nbrAtout == 4:
                        bonus4.set(True)
                        
                else:
                    self.x = 2 * screen_width
                    self.y = screen_height//2   
                    self.velocityX = 0
                    self.velocityY = 0
                    if self.nbrAtout == 1:
                        bonus5.set(True)
                    if self.nbrAtout == 2:
                        bonus6.set(True)
                    if self.nbrAtout == 3:
                        bonus7.set(True)
                    if self.nbrAtout == 4:
                        bonus8.set(True)
        
        def draw(self):
            if self.nbrAtout == 1:
                color = CITROUILLE
                # image = pygame.image.load("x3.png").convert()
            elif self.nbrAtout == 2:
                color = AMBRE
                #image = pygame.image.load("+3.png").convert()
            elif self.nbrAtout == 3:
                color = TERRE
                #image = pygame.image.load("ext.png").convert()
            else:
                color = BRUN
                #image = pygame.image.load("int.png").convert()

            ##image_rect = pygame.Rect(self.x, self.y, self.radius/2, self.radius/2)
            #image_resized = pygame.transform.scale(image, (self.radius/2, self.radius/2))            
            #screen.blit(image_resized, image_rect)
            
        
            #return pygame.draw(image_rect)
            return pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius) 
    class Ball:
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            
            if random.randint(0,1) == 1:
                self.velocityX = -ballVelocity 
            else:
                self.velocityX = -ballVelocity
            
            if random.randint(0,1) == 1:
                self.velocityY = -ballVelocity
            else:
                self.velocityY = -ballVelocity

        def update(self):
            self.x += self.velocityX /2
            self.y += self.velocityY /2

            ball = self.draw()

            # Check for collision with bricks
            for i in bricks:
                brick = i[1]
                numAtout = 0
                if ball.colliderect(brick):
                    i[0] -=1
                    
                    if i[0] <= 0 and i[0] > -999:
                        numAtout = i[2]
                        bricks.remove(i)
                        if numAtout >  0: 
                            atout = Atout(self.x,self.y,self.radius,numAtout)
                            atouts.append(atout)
                            atout.draw()
                    if (ball.bottom > brick.top and ball.top < brick.top) or (ball.top < brick.bottom and ball.bottom > brick.bottom):   
                        self.velocityY = -self.velocityY
                    if (ball.right > brick.left and ball.left < brick.left) or (ball.left < brick.right and ball.right > brick.right):
                        self.velocityX = -self.velocityX
                        nbrBlocks.set(nbrBlocks.get() - 1)
                        if self.color == RED:
                            pointsPlayer1.set(pointsPlayer1.get()+1)
                        else:
                            pointsPlayer2.set(pointsPlayer2.get()+1)     
            
                
            
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
                        nbrRedBalls.set(nbrRedBalls.get()-1)
                        print("nbrRedBalls",nbrRedBalls.get())
            else:
                if ball.colliderect(paddleBlue):
                    self.velocityY *= -1
                elif self.y + self.radius > screen_height:
                    self.x = 2 * screen_width
                    self.y = screen_height//2   
                    self.velocityX = 0
                    self.velocityY = 0
                    nbrBlueBalls.set(nbrBlueBalls.get()-1)
                    print("nbrBlueBalls",nbrBlueBalls.get())

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


    #font_path = os.path.join("fonts", "Robus-BWqOd.otf")
    def updateBackgroundImage():
        background_image = pygame.image.load("img/427159.jpg")
        background_rect = background_image.get_rect()
        background_x = screen_width // 2 - background_rect.width // 2
        background_y = screen_height // 2 - background_rect.height // 2
        screen.blit(background_image, (background_x, background_y))

    updateBackgroundImage()

    redBasePlace = []
    redBasePlace = screen_width // 1.5 - (sizeRedPadle.get()//2), screen_height - 100
    blueBasePlace = []
    blueBasePlace = screen_width // 2.5 - (sizeBluePadle.get()//2), screen_height - 100

    #gestion de la barre
    paddleRed = pygame.Rect(redBasePlace[0], redBasePlace[1], sizeRedPadle.get(), 20)
    paddleBlue = pygame.Rect(blueBasePlace[0], blueBasePlace[1], sizeBluePadle.get(), 20)
    paddle_speedRed = 0
    paddle_speedBlue = 0

    #gestion des balles
    redBalls = []
    blueBalls = []
    def createRedBall():
        x = redBasePlace[0] + (sizeRedPadle.get()//2) # screen_width /2 - 10 #
        y = redBasePlace[1]-20 # screen_height / 1.3 # 
        color = RED
        redBall = Ball(x, y, ballRadius, color)
        redBalls.append(redBall)
        sprites.append(redBall.draw())

    def createBlueBall():
        x =   blueBasePlace[0] + (sizeBluePadle.get()//2) # screen_width /2 + 10 #
        y =  blueBasePlace[1]-20 # screen_height / 1.3  #
        color = WHITE
        blueBall = Ball(x, y, ballRadius, color)
        blueBalls.append(blueBall)
        sprites.append(blueBall.draw())
    createBlueBall()
    createRedBall()

    #creation en fonction de la map
    actualMatrixe = getMatrixes(start.get())
    tauxAtout = 1
    mapWidth = actualMatrixe[0] +5
    #print(mapWidth)
    mapHeight = actualMatrixe[1] +4
    #print(mapHeight)
    matrix_data = actualMatrixe[2] 


    #creation des briques
    brick_spacing = screen_width // 350
    brick_width = screen_width // (mapHeight)
    brick_height = screen_height // (mapWidth)
    bricks = []


    for i in range(mapHeight-4):
        brick_x = brick_spacing + i * (brick_width + brick_spacing)
        for j in range(mapWidth-10):
            randomNum = random.randint(0,tauxAtout)
            if matrix_data[j][i] >= 2:
                brick_y = brick_spacing + j * (brick_height + brick_spacing)
                brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
                brickX = []
                brickX.append((matrix_data[j][i])-1) #vie
                brickX.append(brick_rect)
                randomAtout = 0
                if randomNum == 1:
                    randomAtout = random.randint(1,4)
                brickX.append(randomAtout)
                bricks.append(brickX)
                nbrBlocks.set(nbrBlocks.get()+1)

            if matrix_data[j][i] == 0:

                brick_y = brick_spacing + j * (brick_height + brick_spacing)
                brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
                brickX = []
                brickX.append(-9999)#vie &
                brickX.append(brick_rect)
                randomAtout = 0
                if randomNum == 1:
                    randomAtout = random.randint(1,4)
                brickX.append(randomAtout)
                bricks.append(brickX)
                nbrBlocks.set(nbrBlocks.get()+1)

    while(start.get()==-1):
        setAllData()
        time.sleep(0.5)
    while end.get() != True:
        while pause.get():
            setAllData()
            time.sleep(0.1)
    
        # Handle events
        #X3 RED
        if bonus5.get() == "Active":
            bonus5.set(False)
            newRedBalls = []
            for i in redBalls:
                for y in range(3):
                    x = i.x
                    y = i.y
                    ball = Ball(x, y, ballRadius, RED)
                    newRedBalls.append(ball)
                    sprites.append(ball.draw())
                    nbrRedBalls.set(nbrRedBalls.get()+1)

            for ball in newRedBalls:
                redBalls.append(ball)

        #X3 Blue
        if bonus1.get() == "Active":
            bonus1.set(False)
            newBlueBalls = []
            for i in blueBalls:
                for y in range(3):
                    x = i.x
                    y = i.y
                    ball = Ball(x, y, ballRadius, BLUE)
                    newBlueBalls.append(ball)
                    sprites.append(ball.draw())
                    nbrBlueBalls.set(nbrBlueBalls.get() + 1)
            for ball in newBlueBalls:
                blueBalls.append(ball)

        #+3 BLUE
        if bonus2.get() == "Active":
            bonus2.set(False)
            for i in range(3):
                createBlueBall()
        #+3 RED
        if bonus6.get() == "Active":
            bonus6.set(False)
            for i in range(3):
                createRedBall()
        
        #++ padleBlue
        if bonus3.get() == "Active":
            bonus3.set(False)
            sizeBluePadle.set(sizeBluePadle.get()*1.5)
        
        #++ padleRed
        if bonus7.get() == "Active":
            bonus7.set(False)
            sizeRedPadle.set(sizeRedPadle.get()*1.5)

        #-- padleBlue
        if bonus8.get() == "Active":
            bonus8.set(False)
            sizeBluePadle.set(sizeBluePadle.get()*0.5)
        
        #-- padleRed
        if bonus4.get() == "Active":
            bonus4.set(False)
            sizeRedPadle.set(sizeRedPadle.get()*0.5)


        #move the balls
        for ball in redBalls:
            ball.update()
        #  print("update Red Balls")
        for ball in blueBalls:
            ball.update()
        #  print("BlueBalls update")
        for atout in atouts:
            atout.update()
        paddleRed.x = 1900 - 2*((1900/500)*x1.get())
        if paddleRed.left < 0:
            paddleRed.left = 0
        elif paddleRed.right > screen_width:
            paddleRed.right = screen_width

        # Move the paddleBlue
        paddleBlue.x = 1900 - 2*(1900/500*(x2.get()-250))
        if paddleBlue.left < 0:
            paddleBlue.left = 0
        elif paddleBlue.right > screen_width:
            paddleBlue.right = screen_width
        
        pygame.draw.rect(screen, RED, paddleRed)
        pygame.draw.rect(screen, WHITE, paddleBlue)

        for i in bricks:
            brick = i[1]
            color = i[0]

            if color < -9990:
                pygame.draw.rect(screen, GRAY, brick)
            if color == 3:
                pygame.draw.rect(screen, BORDAUX, brick)
            if color == 2:
                pygame.draw.rect(screen, GREEN, brick)
            if color == 1:
                pygame.draw.rect(screen, WHITE, brick)
                
        setAllData()
        pygame.display.flip()
        clock.tick(60)
        updateBackgroundImage()    
        if nbrBlueBalls.get() <= 0:
            print(nbrBlocks.get())
            end.set(True)
            playsound.playsound("./sounds/Redwins.mp3")
            break
        if nbrRedBalls.get() <= 0:
            end.set(True)
            playsound.playsound("./sounds/Bluewins.mp3")
            break
        
    pygame.quit()
    cv2.destroyAllWindows()
    return 0
if __name__ == '__main__':
    xPos = Thread(target = getxPos)
    xPos.start()
    UI()
