import pygame
import pictures
from variables import *
from FindingHand import FindHands


class virtHand:
    def __init__(self):
        self.orig_image = pictures.load("Assets/h1.png", size=(HAND_SIZE, HAND_SIZE))
        self.image = self.orig_image.copy()
        self.image_smaller = pictures.load("Assets/h2.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.rect = pygame.Rect(SWIDTH//2, SHEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False
        #self.hand_tracking = HandTracking()


    def follow_mouse(self): # change the hand pos center at the mouse pos
        self.rect.center = pygame.mouse.get_pos()
        #self.hand_tracking.display_hand()

    def follow_mediapipe_hand(self, x, y):
        self.rect.center = (x, y)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)


    def draw(self, surface):
        pictures.draw(surface, self.image, self.rect.center, pos_mode="center")

        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def on_waste(self, wastes): # return a list with all wastes that collide with the hand hitbox
        return [waste for waste in wastes if self.rect.colliderect(waste.rect)]
    
    def garbage_waste(self, wastes, score, sounds):
        if self.left_click: # if left click
            for waste in self.on_waste(wastes):
                waste_score = waste.kill(wastes)
                score += waste_score
                sounds["slap"].play()
                if waste_score <= 0:
                    sounds["screaming"].play()
        else:
            self.left_click = False
        return score

        
    def organic_waste(self, wastes, score, sounds): 
        if self.left_click: # if left click
            for waste in self.on_waste(wastes):
                waste_score = waste.kill(wastes)
                score -= waste_score
                sounds["slap"].play()
                if waste_score >= 0:
                    sounds["screaming"].play()
        else:
            self.left_click = False
        return score

    def toxic_waste(self, wastes, score, sounds): 
        if self.left_click: # if left click
            for waste in self.on_waste(wastes):
                waste_score = waste.kill(wastes)
                if waste_score == 0 :
                    score += 1
                    sounds["slap"].play()
                if waste_score > 0 :
                    score -= waste_score
                    sounds["screaming"].play()
                if waste_score < 0 :
                    score += waste_score
                    sounds["screaming"].play()
        else:
            self.left_click = False
        return score
