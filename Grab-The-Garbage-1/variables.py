import pygame
WINDOW_NAME = "GRAB THE GARBAGE"
GAME_TITLE = WINDOW_NAME

SWIDTH, SHEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
GARBAGES_SIZES = (50, 38)
GARBAGE_SIZE_RANDOMIZE = (1,2) # for each new garbage, it will multiply the size with an random value beteewn X and Y
ORGANIC_SIZES = (50, 50)
ORGANIC_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.08 #speed of the animation

GAME_DURATION = 60 # the game will last X sec
GARBAGES_SPAWN_TIME = 1
GARBAGES_MOVE_SPEED = {"min": 1, "max": 1}
ORGANIC_PENALITY = 1
TOXIC_PENALITY = 0


COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} 


MUSIC_VOLUME = 0.16 
SOUNDS_VOLUME = 1


pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
