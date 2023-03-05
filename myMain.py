import pygame
import sys
from threading import Thread
from multiprocessing import Process
import cv2
from flask import Flask, render_template, request
 
class Game():
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.globalVar = False
        self.app = Flask(__name__)
        ui = Thread(target = self.ui)
        xPos = Thread(target = self.xPos)
        thread3 = Process(target = self.phone_connection)
        ui.start()
        xPos.start()
        thread3.start()
        
    def phone_connection(self):
        @self.app.route("/")
        def index():
            # Pass global variable value to template
            return render_template("index.html", globalVar=self.globalVar)

        @self.app.route("/toggle")
        def toggle():
            # Toggle global variable value on button click
            self.globalVar = True
            return render_template("index.html", globalVar=self.globalVar)

        if __name__ == "__main__":
            self.app.run(host="0.0.0.0", debug=True)

    def xPos(self):
        face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if(len(faces) == 2):
                face2 = faces[1][0]
                face1 = faces[0][0]
                self.x1 = face1
                self.x2 = face2
             #   if((faces[1][0] < (self.x2-self.x2/10)or (faces[1][0] > (self.x2 + self.x2/10))) or (self.x2 == 0)):
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


    def ui(self):
        class UIGame:
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
                    UIGame.removeBlock(self.position)



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

                    next = UIGame.GetFroPosition(game,positionSuivante)

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
        uigame = UIGame(100,100,20)

        #gestion de la barre
        paddleRed = pygame.Rect(1900 - (1900/500 * self.x1), screen_height - 100 , 140, 20)
        paddleBlue = pygame.Rect(1900 - (1900/500 * self.x2), screen_height - 100, 140, 20)

        paddle_speedRed = 0
        paddle_speedBlue = 0


        #creation des briques
        brick_width = 20
        brick_height = 10
        brick_spacing = 5
        bricks = []
        for i in range(screen_width// (brick_spacing + brick_width)):
            brick_x = brick_spacing + i * (brick_width + brick_spacing)
            for j in range((screen_height // (brick_spacing + brick_height))//2):
                brick_y = brick_spacing + j * (brick_height + brick_spacing)
                brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
                bricks.append(brick_rect)



        while uigame.GameFinish != True:

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
            paddleRed.x = 1900 - (1900/500 * self.x1)
            if paddleRed.left < 0:
                paddleRed.left = 0
            elif paddleRed.right > screen_width:
                paddleRed.right = screen_width

            # Move the paddleBlue
            paddleBlue.x = 1900 - (1900/500 * self.x2)
            if paddleBlue.left < 0:
                paddleBlue.left = 0
            elif paddleBlue.right > screen_width:
                paddleBlue.right = screen_width


            pygame.draw.rect(screen, (255, 0, 0), paddleRed)
            pygame.draw.rect(screen, (0, 0, 255), paddleBlue)

            for brick in bricks:
                pygame.draw.rect(screen, (255, 0, 0), brick)
            
            # Update the screen and clock
            pygame.display.flip()
            clock.tick(60)
            updateBackgroundImage()
            

        pygame.quit()
Game()