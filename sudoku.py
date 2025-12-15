import pygame
import sys
from board import Board

pygame.init()

WINDOW_WIDTH = 540
WINDOW_HEIGHT = 600
BOARD_HEIGHT = 540

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sudoku")

FONT_MED = pygame.font.SysFont(None, 32)

def main():
    removed_cells = 40  # difficulty

    board = Board(WINDOW_WIDTH, BOARD_HEIGHT, screen, removed_cells)

    running = True
    while running:
        screen.fill(WHITE)

        board.draw()

        msg = FONT_MED.render("Click a cell, press 1-9. ESC to quit.", True, BLACK)
        screen.blit(msg, (20, 550))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y < BOARD_HEIGHT:
                    pos = board.click(x, y)
                    if pos:
                        board.select(*pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if pygame.K_1 <= event.key <= pygame.K_9:
                    number = event.key - pygame.K_0
                    board.place_number(number)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()