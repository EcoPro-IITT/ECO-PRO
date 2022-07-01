import pygame
import csv
import os
import cv2
import time

DRAW_HITBOX  = False

pygame.font.init()
SIZE = WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("LEVEL-3 Quiz")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
PINK = (255,100,180)
GRAY = (127, 127, 127)

FPS = 60

class MCQ():
    def __init__(self, data):
        self.question = data[0]
        self.answer = int(data[1])
        self.userAns = 0

# Import csv file data
pathCSV = "ECO-PRO/Quiz-3/Mcqs.csv"
with open(pathCSV, newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]

# Create Object for each MCQ
mcqList = []
for q in dataAll:
    mcqList.append(MCQ(q))

print("Total MCQ Objects Created:", len(mcqList))
mcq = mcqList[0]
print(mcq.question)

myfont = pygame.font.SysFont('arial',32)

BG_IMAGE = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/FOREST.png'))

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(BG_IMAGE,(0,0))

def main():
    
    score = 0
    qNo = 0
    qTotal = len(dataAll)
    clock = pygame.time.Clock()
    run = True
    while run: 
        clock.tick(FPS)
        
        draw_window()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        if qNo < qTotal:
            mcq = mcqList[qNo]

            pygame.draw.rect(WIN, GRAY, pygame.Rect(WIDTH//2 - 290, HEIGHT//2 - 262, 610, 100))
            pygame.draw.rect(WIN,GRAY, pygame.Rect(WIDTH//2 - 290, HEIGHT//2 -150, 300, 200))
            pygame.draw.rect(WIN,GRAY, pygame.Rect(WIDTH//2 +20, HEIGHT//2 -150, 300, 200))
            pygame.draw.rect(WIN, GRAY, pygame.Rect(WIDTH//2 - 290, HEIGHT//2 + 60, 300, 200 ))
            pygame.draw.rect(WIN,GRAY, pygame.Rect(WIDTH//2 +20, HEIGHT//2 + 60, 300, 200))
            pygame.draw.rect(WIN,GRAY, pygame.Rect(WIDTH//2 -390 , HEIGHT//2 + 300, 800, 50))

            text = myfont.render(mcq.question, True, GREEN)
            textRect = text.get_rect()
            textRect.center = (WIDTH//2 + 10,HEIGHT//2 -210)
            WIN.blit(text, textRect)
            text10 = myfont.render('SCORE  : ', True, GREEN)
            textRect10 = text10.get_rect()
            textRect10.center = (WIDTH//2 - 50 ,HEIGHT//2 +323)

            if qNo ==0:
            
                
            # text1 = myfont.render(mcq.choice1, True, GREEN)
            # textRect1 = text.get_rect()
            # textRect1.center = (WIDTH//2 + 50, HEIGHT//2)
            # WIN.blit(text1, textRect1)
            # text2 = myfont.render(mcq.choice2, True, GREEN)
            # textRect2 = text.get_rect()
            # textRect2.center = (WIDTH//2 + 310, HEIGHT//2)
            # WIN.blit(text2, textRect2)
            # text3 = myfont.render(mcq.choice3, True, GREEN)
            # textRect3 = text.get_rect()
            # textRect3.center = (WIDTH//2 + 40, HEIGHT//2 + 106)
            # WIN.blit(text3, textRect3)
            # text4 = myfont.render(mcq.choice4, True, GREEN)
            # textRect4 = text.get_rect()
            # textRect4.center = (WIDTH//2 + 310, HEIGHT//2 + 106)
            # WIN.blit(text4, textRect4)
                Q1_OPTION1 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/Q1_IMG1.png')).convert_alpha()
                Q1_OPTION1 = pygame.transform.scale(Q1_OPTION1, (151, 154))
                WIN.blit(Q1_OPTION1, (420,220))
                Q1_OPTION2 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/Q1_IMG2.png')).convert_alpha()
                Q1_OPTION2 = pygame.transform.scale(Q1_OPTION2, (98, 161))
                WIN.blit(Q1_OPTION2, (755,220))
                Q1_OPTION3 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/Q1_IMG3.png')).convert_alpha()
                Q1_OPTION3 = pygame.transform.scale(Q1_OPTION3, (151, 154))
                WIN.blit(Q1_OPTION3, (420,430))
                Q1_OPTION4 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/Q1_IMG4.png')).convert_alpha()
                Q1_OPTION4 = pygame.transform.scale(Q1_OPTION4, (151, 154))
                WIN.blit(Q1_OPTION4, (730,430))
                WIN.blit(text10, textRect10)
                # print("SCORE: " )
                # print(score)
                text11 = myfont.render(f"{score}", True, GREEN)
                textRect11 = text11.get_rect()
                textRect11.center = (WIDTH//2 + 30  ,HEIGHT//2 + 323)
                WIN.blit(text11, textRect11)

            if qNo == 1:

                Q2_OPTION1 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/solar_panel.png')).convert_alpha()
                Q2_OPTION1 = pygame.transform.scale(Q2_OPTION1, (150, 150))
                WIN.blit(Q2_OPTION1, (420,220))
                Q2_OPTION2 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/oil_energy.png')).convert_alpha()
                Q2_OPTION2 = pygame.transform.scale(Q2_OPTION2, (150, 150))
                WIN.blit(Q2_OPTION2, (730,220))
                Q2_OPTION3 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/nuclear_energy.png')).convert_alpha()
                Q2_OPTION3 = pygame.transform.scale(Q2_OPTION3, (160, 131))
                WIN.blit(Q2_OPTION3, (420,440))
                Q2_OPTION4 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/coal.png')).convert_alpha()
                Q2_OPTION4 = pygame.transform.scale(Q2_OPTION4, (150, 161))
                WIN.blit(Q2_OPTION4, (730,430))
                WIN.blit(text10, textRect10)
                # print("SCORE: " )
                # print(score)
                text11 = myfont.render(f"{score}", True, GREEN)
                textRect11 = text11.get_rect()
                textRect11.center = (WIDTH//2 + 30,HEIGHT//2 + 323)
                WIN.blit(text11, textRect11)
                

            if qNo == 2:

                Q3_OPTION1 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/bike_vehicle.png')).convert_alpha()
                Q3_OPTION1 = pygame.transform.scale(Q3_OPTION1, (160, 117))
                WIN.blit(Q3_OPTION1, (420,240))
                Q3_OPTION2 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/car_vehicle.png')).convert_alpha()
                Q3_OPTION2 = pygame.transform.scale(Q3_OPTION2, (150, 150))
                WIN.blit(Q3_OPTION2, (735,230))
                Q3_OPTION3 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/scooty_vehicle.png')).convert_alpha()
                Q3_OPTION3 = pygame.transform.scale(Q3_OPTION3, (130, 140))
                WIN.blit(Q3_OPTION3, (430,440))
                Q3_OPTION4 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/cycle_vehicle.png')).convert_alpha()
                Q3_OPTION4 = pygame.transform.scale(Q3_OPTION4, (150, 142))
                WIN.blit(Q3_OPTION4, (735,435))
                WIN.blit(text10, textRect10)
                # print("SCORE: " )
                # print(score)
                text11 = myfont.render(f"{score}", True, GREEN)
                textRect11 = text11.get_rect()
                textRect11.center = (WIDTH//2 + 30 ,HEIGHT//2 + 323)
                WIN.blit(text11, textRect11)

            if qNo == 3:

                Q5_OPTION1 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/factory.jpg')).convert_alpha()
                Q5_OPTION1 = pygame.transform.scale(Q5_OPTION1, (170,160))
                WIN.blit(Q5_OPTION1, (420,230))
                Q5_OPTION2 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/deforestation.jpg')).convert_alpha()
                Q5_OPTION2 = pygame.transform.scale(Q5_OPTION2, (250, 130))
                WIN.blit(Q5_OPTION2, (690,240))
                Q5_OPTION3 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/smoke_emission.jpg')).convert_alpha()
                Q5_OPTION3 = pygame.transform.scale(Q5_OPTION3, (200,130))
                WIN.blit(Q5_OPTION3, (400,450))
                Q5_OPTION4 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/ALL.jpg')).convert_alpha()
                Q5_OPTION4 = pygame.transform.scale(Q5_OPTION4, (160, 100))
                WIN.blit(Q5_OPTION4, (730,460))
                WIN.blit(text10, textRect10)
                # print("SCORE: " )
                # print(score)
                text11 = myfont.render(f"{score}", True, GREEN)
                textRect11 = text11.get_rect()
                textRect11.center = (WIDTH//2 + 30,HEIGHT//2 + 323)
                WIN.blit(text11, textRect11)

            if qNo == 4:
                Q4_OPTION1 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/vaquita.png')).convert_alpha()
                Q4_OPTION1 = pygame.transform.scale(Q4_OPTION1, (170, 80))
                WIN.blit(Q4_OPTION1, (420,260))
                Q4_OPTION2 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/panda.png')).convert_alpha()
                Q4_OPTION2 = pygame.transform.scale(Q4_OPTION2, (150, 161))
                WIN.blit(Q4_OPTION2, (730,220))
                Q4_OPTION3 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/cat.png')).convert_alpha()
                Q4_OPTION3 = pygame.transform.scale(Q4_OPTION3, (150, 161))
                WIN.blit(Q4_OPTION3, (460,430))
                Q4_OPTION4 = pygame.image.load(os.path.join('ECO-PRO/Quiz-3/Assets/white_wolf.png')).convert_alpha()
                Q4_OPTION4 = pygame.transform.scale(Q4_OPTION4, (200, 180))
                WIN.blit(Q4_OPTION4, (710,430))
                WIN.blit(text10, textRect10)
                # print("SCORE: " )
                # print(score)
                text11 = myfont.render(f"{score}", True, GREEN)
                textRect11 = text11.get_rect()
                textRect11.center = (WIDTH//2 + 30,HEIGHT//2 + 323)
                WIN.blit(text11, textRect11)


            pygame.display.update()

        if qNo == qTotal:

            pygame.draw.rect(WIN, GRAY, pygame.Rect(WIDTH//2 - 200, HEIGHT//2 - 45 , 350, 80))
            text10 = myfont.render('YOUR TOTAL SCORE: ', True, GREEN)
            textRect10 = text10.get_rect()
            textRect10.center = (WIDTH//2 - 50,HEIGHT//2)
            WIN.blit(text10, textRect10)
            text11 = myfont.render(f"{score}", True, GREEN)
            textRect11 = text11.get_rect()
            textRect11.center = (WIDTH//2 + 120,HEIGHT//2)
            WIN.blit(text11, textRect11)
            # print(score)

            pygame.display.update()
        

        

        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            if qNo<qTotal:
                x,y = pygame.mouse.get_pos()
                print(x, ' ', y)
                if(350 < x and x < 650 and 210<y and y<410):
                    mcq.userAns = 1
                    print("1")
                if(660 < x and x < 960 and 210<y and y<410):
                    mcq.userAns = 2
                    print("2")
                if(350 < x and x < 650 and 420<y and y<620):
                    mcq.userAns = 3
                    print("3")
                if(660 < x and x < 960 and 420<y and y<620):
                    mcq.userAns = 4
                    print("4")

                if mcq.userAns == mcq.answer:
                    score = score + 50

            

            # text10 = myfont.render('SCORE: ', True, GREEN)
            # textRect10 = text10.get_rect()
            # textRect10.center = (WIDTH//2 ,HEIGHT//2 +200)
            # WIN.blit(text10, textRect10)
            # pygame.display.update()   

                if mcq.userAns != 0:
                    time.sleep(0.3)
                    qNo += 1

            # if mcq.userAns == mcq.answer:
            #     score = score + 50
            # text10 = myfont.render('SCORE: ', True, GREEN)
            # textRect10 = text10.get_rect()
            # textRect10.center = (WIDTH//2 ,HEIGHT//2 +410)
            # WIN.blit(text10, textRect10)
            # pygame.display.update()


    
    pygame.quit()

if __name__ == "__main__":
    main()
