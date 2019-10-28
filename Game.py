import pygame
import sys
import random
import copy

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
YELLOW_BRIGHT = (255, 255, 224)
GREY = (169, 169, 169)

Dark = {
    RED: (200, 0, 0),
    GREEN: (0, 200, 0),
    BLUE: (0, 0, 200),
    YELLOW: (200, 200, 0),
}

size = (800, 600)
screen = pygame.display.set_mode(size)

game_name = pygame.display.set_caption("2019 Learning Fair")

clock = pygame.time.Clock()

def writeText(text, x, y, size, font='D2', color=BLACK, rect=None):
    if font == 'D2':
        textfont = pygame.font.Font('D2CodingBold-Ver1.3.2-20180524.ttf', size)
    elif font == '도현':
        textfont = pygame.font.Font('배달의민족_도현.ttf', size)

    text = textfont.render("{}".format(text), True, color)

    if rect == 'center':
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    else:
        screen.blit(text, (x, y))

while True:
    clock.tick(60)
    screen.fill(WHITE)
    done = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

