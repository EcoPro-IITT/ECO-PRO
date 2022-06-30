# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
from settings import *
from game import Game
from menu import Menu


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 32)
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

mainClock = pygame.time.Clock()


fps_font = pygame.font.SysFont("coopbl", 22)


state = "menu"


game = Game(SCREEN)
menu = Menu(SCREEN)


def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    global state
    if state == "menu":
        if menu.update() == "game":
            game.reset()
            state = "game"
    elif state == "game":
        if game.update() == "menu":
            state = "menu"
    pygame.display.update()
    mainClock.tick(FPS)


while True:

    user_events()

    update()

    if DRAW_FPS:
        fps_label = fps_font.render(
            f"FPS: {int(mainClock.get_fps())}", 1, (255, 200, 20))
        SCREEN.blit(fps_label, (5, 5))
