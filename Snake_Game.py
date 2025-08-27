import pygame  # Importing the pygame library
import time
import random  # Importing random for food placement

pygame.init()  # Initializing pygame

# Defining colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (41, 240, 26)
red = (201, 18, 18)
yellow = (239, 250, 32)

# Display dimensions
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))  # Setting display size
pygame.display.set_caption("Snake game")  # Setting window title

clock = pygame.time.Clock()  # Creating game clock

snake_block = 10  # Snake block size
snake_speed = 15  # Speed of the snake

# Setting font styles
font_style = pygame.font.SysFont("calibri", 25)
score_font = pygame.font.SysFont("comicsans", 34)

def my_score(score):
    """Displays the current score on the screen."""
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def message(msg, color):
    """Displays a message at the center of the screen."""
    mssg = font_style.render(msg, True, color)
    dis.blit(mssg, [0, dis_height / 2])

def my_snake(snake_block, snake_list):
    """Draws the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def main_game():
    """Main game loop."""
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Movement variables
    x1_change = 0
    y1_change = 0

    snake_list = []  # List to keep track of snake body parts
    length_snake = 1  # Initial snake length

    # Generating initial food location
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(white)
            message("You lost! Press P to play again or Q to quit", red)
            my_score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:  # Restart game
                        main_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        # Checking if snake hits the boundary
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Drawing food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        
        # Updating snake position
        snake_size = [x1, y1]
        snake_list.append(snake_size)
        if len(snake_list) > length_snake:
            del snake_list[0]

        my_snake(snake_block, snake_list)
        my_score(length_snake - 1)
        pygame.display.update()

        # Checking if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_snake += 1

        clock.tick(snake_speed)  # Control game speed

    pygame.quit()
    quit()

main_game()  # Running the game
