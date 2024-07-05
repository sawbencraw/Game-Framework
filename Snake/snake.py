import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors using RGB values
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set the dimensions of the game window
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Set the clock speed (frames per second)
clock = pygame.time.Clock()
snake_block = 10  # Size of each snake segment

# Define the font style for text
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Function to display the score on the screen
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Function to draw the snake on the screen
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Function to display a message on the screen
def message(msg, color, position):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, position)

# Function to display the game intro screen and select difficulty
def game_intro():
    intro = True
    while intro:
        dis.fill(blue)
        title_text = "Welcome to Snake"
        instruction_text = "Select Difficulty: S - Slow, R - Regular, F - Fast"

        # Render the title text and center it on the screen
        title_surface = font_style.render(title_text, True, green)
        title_rect = title_surface.get_rect(center=(dis_width / 2, dis_height / 3))
        dis.blit(title_surface, title_rect)

        # Render the instruction text and center it on the screen
        instruction_surface = font_style.render(instruction_text, True, black)
        instruction_rect = instruction_surface.get_rect(center=(dis_width / 2, dis_height / 2))
        dis.blit(instruction_surface, instruction_rect)

        pygame.display.update()

        # Event handling for user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the window
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # If the user presses a key
                if event.key == pygame.K_s:
                    return 10  # Slow speed
                if event.key == pygame.K_r:
                    return 20  # Regular speed
                if event.key == pygame.K_f:
                    return 30  # Fast speed

# Main game loop function
def gameLoop():
    snake_speed = game_intro()  # Get the selected game speed from the intro screen

    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0  # Change in x position (initially stationary)
    y1_change = 0  # Change in y position (initially stationary)

    snake_List = []
    Length_of_snake = 1  # Initial length of the snake

    # Random initial position for the food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red, [dis_width / 6, dis_height / 3])
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # Event handling for game over screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  # Restart the game

        # Event handling for the main game loop
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
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if the snake collides with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
