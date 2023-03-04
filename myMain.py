import pygame
import sys
from threading import Thread
import cv2

class Game():
    def __init__(self):
        self.x1 = 0
        thread = Thread(target = self.ui)
        thread2 = Thread(target = self.get_result)
        thread.start()
        thread2.start()

    def get_result(self):
        face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if(len(faces) > 0):
                x = (faces[0][0])
                self.x1 = x
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


    def ui(self):
        pygame.init()
        info = pygame.display.Info()
        screen_width, screen_height = info.current_w, info.current_h
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("P-Boyz breaker")
        clock = pygame.time.Clock()

        #Set ball settings
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_color = (100, 100, 100)
        ball_radius = 25
        #ball = pygame.Rect(screen_width // 2 - 35, screen_height // 2 - 35, 30, 30)
        ball_speed_x = 5
        ball_speed_y = 5
        ball = pygame.draw.circle(screen, ( 0 ,1,255 ), (ball_x, ball_y), ball_radius)

        #Set paddle settings
        paddle_speed = 0
        paddle = pygame.Rect(screen_width/2, screen_height-100, 140, 20)


        #Set bricks settings
        brick_width = 80
        brick_height = 30
        brick_spacing = 10
        bricks = []
        for i in range(15):
            brick_x = brick_spacing + i * (brick_width + brick_spacing)
            for j in range(10):
                brick_y = brick_spacing + j * (brick_height + brick_spacing)
                brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
                bricks.append(brick_rect)


        #Main loop
        while True:
            #Necessary functions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        paddle_speed = -10
                    elif event.key == pygame.K_RIGHT:
                        paddle_speed = 10
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        paddle_speed = 0
            
            #Update ball position
            ball.x += ball_speed_x
            ball.y += ball_speed_y
            print(self.x1)
            #Check for collision with walls
            if ball.left < 0 or ball.right > screen_width:
                ball_speed_x = -ball_speed_x
            if ball.top < 0:
                ball_speed_y = -ball_speed_y
            #if ball.bottom > screen_height:
                #pygame.quit()
                #sys.exit()
            
            #Check for collision with paddle
            if ball.colliderect(paddle):
                ball_speed_y = -ball_speed_y
            
            #Check for collision with bricks
            for brick in bricks:
                if ball.colliderect(brick):
                    bricks.remove(brick)
                    if (ball.bottom > brick.top and ball.top < brick.top) or (ball.top < brick.bottom and ball.bottom > brick.bottom):   
                        ball_speed_y = -ball_speed_y
                    if (ball.right > brick.left and ball.left < brick.left) or (ball.left < brick.right and ball.right > brick.right):
                        ball_speed_x = -ball_speed_x
                    break
            
            #Move the paddle
            paddle.x =  1900 - (1900/500 * self.x1)
            if paddle.left < 0:
                paddle.left = 0
            elif paddle.right > screen_width:
                paddle.right = screen_width
            
            # Fill the screen
            screen.fill((0, 0, 0))
            
            # Draw the ball, paddle, and bricks
            pygame.draw.rect(screen, (255, 255, 255), ball)
            pygame.draw.rect(screen, (255, 255, 255), paddle)
            for brick in bricks:
                pygame.draw.rect(screen, (255, 255, 255), brick)
            
            # Update the screen and clock
            pygame.display.flip()
            clock.tick(60)

        # Quit Pygame
        pygame.quit()
Game()