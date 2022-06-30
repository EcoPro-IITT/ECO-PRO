import pygame
import random
import image
from settings import *
from pollutant import Pollutant

imgArray = []
for i in range(1):
    imgArray.append("Assets/oxygen/" + str(i) + ".png")


class Oxygen(Pollutant):
    def __init__(self):
        # size
        random_size_value = random.uniform(
            OXYGEN_SIZE_RANDOMIZE[0], OXYGEN_SIZE_RANDOMIZE[1])
        size = (int(OXYGEN_SIZES[0] * random_size_value),
                int(OXYGEN_SIZES[1] * random_size_value))
        # moving
        random_img = random.randint(0, 0)
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(
            start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load(
            imgArray[random_img], size=size, flip=moving_direction == "up")]  # load the images
        self.current_frame = 0
        self.animation_timer = 0

    def drmove(self, Pollutants):  # remove the Pollutant from the list
        Pollutants.remove(self)
        return -OXYGEN_PENALITY
