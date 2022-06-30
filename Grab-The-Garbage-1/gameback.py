import pygame
import pictures
from variables import *

class gameback:
    def __init__(self):
        self.pictures = pictures.load("Assets/background.png", size=(SWIDTH, SHEIGHT),
                                convert="default")


    def draw(self, surface):
        pictures.draw(surface, self.pictures, (SWIDTH//2, SHEIGHT//2), pos_mode="center")