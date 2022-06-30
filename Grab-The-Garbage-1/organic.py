import pygame
import random
import pictures
from variables import *
from garbage import Garbage

imgArray1 = []
# if images from 0 to 11, then run from 0 to 12.
for i in range(9):
    imgArray1.append("Assets/organic/" + str(i) + ".png")
    
class Organic(Garbage):

    def __init__(self):
        #size
        random_size_value = GARBAGE_SIZE_RANDOMIZE[0]
       
        size = (int(GARBAGES_SIZES[0] * random_size_value * 4), int(GARBAGES_SIZES[1] * random_size_value * 4))
        random_img = random.randint(0, 8)
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [pictures.load(imgArray1[random_img], size=size, flip=moving_direction == "down")]
        
        self.current_frame = 0
        self.animation_timer = 0
      
        

    def kill(self, garbages): # remove the GARBAGE from the list
        garbages.remove(self)
        return -ORGANIC_PENALITY