import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (180, 180, 180)

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value
        self.sketched_value = 0

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self, width, height):
        cell_width = width // 9
        cell_height = height // 9
        x = self.col * cell_width
        y = self.row * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)

        if self.selected:
            pygame.draw.rect(self.screen, RED, rect, 3)
        else:
            pygame.draw.rect(self.screen, BLACK, rect, 1)

        font_big = pygame.font.SysFont(None, 40)
        font_small = pygame.font.SysFont(None, 25)

        if self.value != 0:
            txt = font_big.render(str(self.value), True, BLACK)
            txt_rect = txt.get_rect(center=(x + cell_width // 2,
                                            y + cell_height // 2))
            self.screen.blit(txt, txt_rect)
        elif self.sketched_value != 0:
            txt = font_small.render(str(self.sketched_value), True, GRAY)
            txt_rect = txt.get_rect(
                center=(x + cell_width // 4, y + cell_height // 4)
            )
            self.screen.blit(txt, txt_rect)