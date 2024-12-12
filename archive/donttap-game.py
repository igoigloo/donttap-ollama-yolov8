import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Don't Tap the White Tile")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tile dimensions
TILE_WIDTH = SCREEN_WIDTH // 4
TILE_HEIGHT = SCREEN_HEIGHT // 4

# Font
FONT = pygame.font.SysFont("Arial", 30)

# Clock
clock = pygame.time.Clock()

# Game variables
tiles = []
score = 0
game_over = False

# Function to create tiles
def create_tiles():
    global tiles
    tiles = []
    for i in range(4):
        row = [WHITE] * 4
        black_tile = random.randint(0, 3)
        row[black_tile] = BLACK
        tiles.append(row)

# Function to draw tiles
def draw_tiles():
    for i, row in enumerate(tiles):
        for j, color in enumerate(row):
            pygame.draw.rect(SCREEN, color, (j * TILE_WIDTH, i * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))

# Function to check for click
def check_click(pos):
    global score, game_over
    x, y = pos
    row = y // TILE_HEIGHT
    col = x // TILE_WIDTH
    if tiles[row][col] == BLACK:
        score += 1
        tiles.pop(row)
        new_row = [WHITE] * 4
        black_tile = random.randint(0, 3)
        new_row[black_tile] = BLACK
        tiles.insert(0, new_row)
    else:
        game_over = True

# Function to display score
def display_score():
    score_text = FONT.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(score_text, (10, 10))

# Function to display game over
def display_game_over():
    game_over_text = FONT.render("Game Over!", True, BLACK)
    SCREEN.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))

# Main game loop
def main():
    global game_over
    create_tiles()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                check_click(pygame.mouse.get_pos())

        SCREEN.fill(WHITE)
        draw_tiles()
        display_score()
        if game_over:
            display_game_over()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
