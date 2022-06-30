import pygame
import random
import time
import image
from settings import *

imgArray = []
# if images from 0 to 7, then run from 0 to 8.
for i in range(8):
    imgArray.append("Assets/pollutant/" + str(i) + ".png")


class Pollutant:
    def __init__(self):
        #size
        random_size_value = random.uniform(POLLUTANT_SIZE_RANDOMIZE[0], POLLUTANT_SIZE_RANDOMIZE[1])
        # if images from 0 to 7, then use 0 to 7.
        random_img = random.randint(0, 7)
        # size = (int(POLLUTANTS_SIZES[0] * random_size_value), int(POLLUTANTS_SIZES[1] * random_size_value))
        size = (int(POLLUTANTS_SIZES[0])*3, int(POLLUTANTS_SIZES[1])*3)
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        # self.images = [image.load("Assets/POLLUTANT/POLLUTANT.png", size=size, flip=moving_direction=="up")]
        self.images = [image.load(imgArray[random_img], size=size, flip=moving_direction=="up")]
        self.current_frame = 0
        self.animation_timer = 0


    def define_spawn_pos(self, size): # define the start pos and moving vel of the pollutant
        vel = random.uniform(POLLUTANTS_MOVE_SPEED["min"], POLLUTANTS_MOVE_SPEED["max"])
        moving_direction = "up"
        start_pos = (random.randint(size[0]//1.4, SCREEN_WIDTH-size[0]//1.4), SCREEN_HEIGHT+size[1]//1.4)
        self.vel = [0, -vel]
        return moving_direction, start_pos


    def move(self):
        self.rect.move_ip(self.vel)


    def animate(self): # change the frame of the object when needed
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images)-1:
                self.current_frame = 0


    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)



    def draw(self, surface):
        self.animate()
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def drmove(self, poll): # remove the pollutant from the list
        poll.remove(self)
        return 1
