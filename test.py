import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen and clock
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()

# Create the game objects
ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
ball_speed_x = 5
ball_speed_y = 5

paddle = pygame.Rect(screen_width // 2 - 70, screen_height - 50, 140, 20)
paddle_speed = 0

brick_width = 80
brick_height = 30
brick_spacing = 10
bricks = []
for i in range(7):
    brick_x = brick_spacing + i * (brick_width + brick_spacing)
    for j in range(5):
        brick_y = brick_spacing + j * (brick_height + brick_spacing)
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick_rect)

# Define the game loop
while True:
    # Handle events
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
    
    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Check for collision with walls
    if ball.left < 0 or ball.right > screen_width:
        ball_speed_x = -ball_speed_x
    if ball.top < 0:
        ball_speed_y = -ball_speed_y
    if ball.bottom > screen_height:
        pygame.quit()
        sys.exit()
    
    # Check for collision with paddle
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y
    
    # Check for collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y
            break
    
    # Move the paddle
    paddle.x += paddle_speed
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