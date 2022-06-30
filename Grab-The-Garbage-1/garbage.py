import pygame
import random
import time
import pictures
from variables import *

imgArray = []

for i in range(8):
    imgArray.append("Assets/garbage/" + str(i) + ".png")


class Garbage:
    def __init__(self):
        #size
        random_size_value = GARBAGE_SIZE_RANDOMIZE[0]
        # if images from 0 to 11, then run from 0 to 11.
        random_img = random.randint(0, 7)
        size = (int(GARBAGES_SIZES[0] * random_size_value * 4), int(GARBAGES_SIZES[1] * random_size_value * 4))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [pictures.load(imgArray[random_img], size=size, flip=moving_direction=="down")]
        self.current_frame = 0
        self.animation_timer = 0


    def define_spawn_pos(self, size): # define the start pos and moving vel of the GARBAGE
        vel = random.uniform(GARBAGES_MOVE_SPEED["min"], GARBAGES_MOVE_SPEED["max"])
        moving_direction = "down"
        start_pos = (random.randint(size[0]//1.4,SWIDTH-size[0]//1.4), -size[1]//1.4)
        self.vel = [0, vel]
        return moving_direction, start_pos


    def move(self):
        self.rect.move_ip(self.vel)
    def move_2(self):
        self.rect.move_ip(self.vel)

        

    def animate(self): # change the frame of the insect when needed
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
        pictures.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def kill(self, GARBAGEs): # remove the GARBAGE from the list
        GARBAGEs.remove(self)
        return 1
