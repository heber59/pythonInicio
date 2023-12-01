import pygame

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define constants for the board width and height
BOARD_WIDTH = 16
BOARD_HEIGHT = 13

# Define constants for the tile size
TILE_SIZE = 50

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
BLACK = (10, 10, 10)
WHITE = (100, 0, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game board
board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

# Define a function to draw the board
def draw_board():
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the board
    draw_board()

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
