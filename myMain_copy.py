import pygame
import sys
from threading import Thread
from multiprocessing import Process
import cv2
from flask import Flask, render_template, request, jsonify
 
class Game():
    def __init__(self):
        self.start = False
        self.x1 = 0
        self.x2 = 0
        self.globalVar = False
        self.global_var = True
        self.bonus1 = True
        self.bonus2 = True
        self.bonus3 = True
        self.bonus4 = True
        self.pointsPlayer1 = 0
        self.pointsPlayer2 = 0
        self.activeBonus = []
        self.pause = False
        self.bonus5 = True
        self.bonus6 = True
        self.bonus7 = True
        self.bonus8 = True
        #ui = Thread(target = self.ui)
        #xPos = Thread(target = self.xPos)
        thread3 = Process(target = self.phone_connection)
        #ui.start()
        #xPos.start()
        thread3.start()
        
    def phone_connection(self):
        app = Flask(__name__)
        
        @app.route('/start', methods=['POST'])
        def update_start():
            self.start = True
            return f"Nico ce gros fdp à lancé le jeu"
        
        
        @app.route('/update_bonus', methods=['POST'])
        def update_bonus():
            bonus = str(request.form['bonus'])
            bonusValue = request.form.get('bonusValue')
            if bonus == 'bonus1' :   self.bonus1 = bonusValue
            elif bonus == 'bonus2' : self.bonus2 = bonusValue
            elif bonus == 'bonus3' : self.bonus3 = bonusValue
            elif bonus == 'bonus4' : self.bonus4 = bonusValue
            elif bonus == 'bonus5' : self.bonus5 = bonusValue
            elif bonus == 'bonus6' : self.bonus6 = bonusValue
            elif bonus == 'bonus7' : self.bonus7 = bonusValue
            elif bonus == 'bonus8' : self.bonus8 = bonusValue
            print(self.bonus2)
            return f"{self.bonus2} : {bonusValue}"

        @app.route('/update_pause', methods=['POST'])
        def update_pause():
            print(request.form["pause"])
            self.pause = bool((request.form['pause'] == "true"))
            print(self.pause)
            return f"py pause : {self.pause}"

        @app.route('/recupValeurInPy')
        def get_bonus1():
            return jsonify(self.bonus1,self.bonus2,self.bonus3,self.bonus4,self.pointsPlayer1,self.pointsPlayer2,self.pause,self.bonus5,self.bonus6,self.bonus7,self.bonus8)

        @app.route("/")
        def index():
            # Pass global variable value to template
            return render_template("index.html", global_var=self.global_var)

        @app.route("/player1")
        def player1():
            # Pass global variable value to template
            return render_template("player1.html", global_var=self.global_var)

        @app.route("/player2")
        def player2():
            # Pass global variable value to template
            return render_template("player2.html", global_var=self.global_var)
        app.run(host="0.0.0.0", debug=True)





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
        
            paddleRed.x = 1900 - 2.5*(1900/500*x1)
            if paddleRed.left < 0:
                paddleRed.left = 0
            elif paddleRed.right > screen_width:
                paddleRed.right = screen_width

            # Move the paddleBlue
            paddleBlue.x = 1900 - 2.5*(1900/500*(x2-250))
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