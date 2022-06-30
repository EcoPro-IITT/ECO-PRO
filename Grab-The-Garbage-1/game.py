import pygame
import time
from variables import *
from gameback import gameback
from virtualhand import virtHand
from FindingHand import FindHands
from garbage import Garbage
from toxic import Toxic
from organic import Organic
import cv2
import userinterface

class Game:
    
    def __init__(self, surface):
        self.surface = surface
        self.background = gameback()
        self.targettime = 58
        # Load camera
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["slap"] = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
        self.sounds["slap"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"Assets/Sounds/screaming.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)


    def reset(self): # reset all the needed variables
        self.hand_tracking = FindHands()
        self.hand = virtHand()
        self.wastes = []
        self.wastes_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()


    def spawn_wastes(self):
        t = time.time()
        if t > self.wastes_spawn_timer:
            self.wastes_spawn_timer = t + GARBAGES_SPAWN_TIME
            self.wastes.append(Organic())
            self.wastes.append(Garbage())
            self.wastes.append(Toxic())

    def load_camera(self):
        _, self.frame = self.cap.read()


    def set_hand_position(self):
        self.frame = self.hand_tracking.cv2Hands(self.frame)
        (x, y) = self.hand_tracking.get_Fist_center()
        self.hand.rect.center = (x, y)

    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        # draw the wastes
        for waste in self.wastes:
            waste.draw(self.surface)
        # draw the hand
        self.hand.draw(self.surface)
        # draw the score
        userinterface.draw_text(self.surface, f"Score : {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))
        # draw the time left
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] # change the text color if less than 5 s left
        userinterface.draw_text(self.surface, f"Time left : {self.time_left}", (SWIDTH//2, 5),  timer_text_color, font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)



    def update(self):

        self.load_camera()
        self.set_hand_position()
        self.game_time_update()
        
        self.draw()
        if self.time_left > 0:
            if self.time_left < self.targettime:
                self.spawn_wastes()
                self.targettime = self.time_left-10
            (x, y) = self.hand_tracking.get_Fist_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.Fistclosed
            print("Hand closed", self.hand.left_click)
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
                temp = self.hand.on_waste(self.wastes)
               
                if len(temp)!=0:
                    k=temp[0];
                    k.rect.move_ip(x-k.rect.center[0],y-k.rect.center[1])
                    if(k.rect.center[0]<230  and k.rect.center[1]>400):
                        self.score = self.hand.garbage_waste(self.wastes, self.score, self.sounds)
                    if(k.rect.center[0]>1050  and k.rect.center[1]>400):
                        self.score = self.hand.organic_waste(self.wastes, self.score, self.sounds)
                    if(k.rect.center[0]>500 and k.rect.center[0]<700 and k.rect.center[1]>400):
                        self.score = self.hand.toxic_waste(self.wastes, self.score, self.sounds)
               
            else:
                self.hand.image = self.hand.orig_image.copy()
            
                
            
            for waste in self.wastes:
                waste.move()

        else: # when the game is over
            self.targettime = 58
            if userinterface.button(self.surface, 540, "Continue", click_sound=self.sounds["slap"]):
                return "menu"


        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
