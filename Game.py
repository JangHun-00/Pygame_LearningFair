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

person = pygame.image.load('졸라맨 축소.bmp')
person_width = person.get_width()
person_x = 400
move_x = 0
person_rect = person.get_rect(center=(person_x, 520))

bomb = pygame.image.load('폭탄.png')
bomb_width = bomb.get_width()
bomb_height = bomb.get_height()


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

done = False

while not done:
    clock.tick(60)
    screen.fill(WHITE)
    done = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT:
                move_x -= 10
            elif event.key == pygame.K_RIGHT:
                move_x += 10

        if event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                move_x = 0

    person_x += move_x

    if person_x - (person_width / 2) <= 0:
        person_x = person_width / 2
    elif person_x + (person_width / 2) > size[0]:
        person_x = size[0] - (person_width / 2)

    person_rect = person.get_rect(center=(person_x, 520))
    screen.blit(person, person_rect)


    pygame.display.update()

pygame.quit()
sys.exit()