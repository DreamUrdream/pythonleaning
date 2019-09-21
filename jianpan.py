# encoding utf-8
import sys, random, time, pygame
from pygame.locals import *

screen_x = 640
sceen_y = 460*2

image_y = 400



pygame.init()
screen = pygame.display.set_mode((screen_x,sceen_y))
pygame.display.set_caption("奇趣练字")


font1 = pygame.font.Font(None, 32)
font2 = pygame.font.Font(None, 160)
font_ch = pygame.font.SysFont("timesnewromanttf",32)



white = 255,255,255
green = 0,255,0
background = 30,144,255
red = 255,0,0
yellow = 255, 255, 0
color = green

correct_answer = 97
seconds = 10
score = 0
start_time =0
game_over = True
count =0

lx= 0
ly = 240

correct_text = ""

image = pygame.image.load("./typing.jpeg")
image = pygame.transform.scale(image,(screen_x,image_y))

background_image = pygame.image.load("./beijing.jpeg")
background_image.set_alpha(80)
size = background_image.get_size()

background_image = pygame.transform.scale(background_image,(screen_x,size[1]//2))

def split_text(text, step=70):
    for i in range(0,len(text), step):
        yield text[i:i+step]

def display_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    
def display_split(font,lx,ly, text, color = (255,255,255)):
    for context in split_text(text):
        display_text(font, lx,ly,context, color)
        ly +=25


def display_screen(font, color):
    screen.fill(background)
    display_text(font1, 10, 40, "Time: " + str(int(current)))
    display_split(font1, lx, ly, correct_text, yellow )
    display_text(font, 260, 360, chr(correct_answer-32), color)
    #pygame.display.update()

def display_screen_gameover():
    screen.fill(background)
    display_text(font1,260, 320, "Speed: "+ str(score)+"/min" )
    display_text(font1,260, 360, "Faild: " + str(count -score))
    display_text(font1,260, 420, "Press Enter to start...")
    #display_picture()
    #pygame.display.update()


def display_picture():
    display_text(font1, 100,0,"Welcome using QiQu Keyboard Practice")
    #text = font_ch.render(u'奇趣练字',True,(255,255,255))
    #screen.blit(text,(100,100))
    screen.blit(background_image,(0,0))
    screen.blit(image, (0,sceen_y-image_y))




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is pygame.KEYDOWN:
            if event.key == K_RETURN:
                if game_over:
                    game_over = False
                    score = 0
                    count = 0
                    correct_text = ""
                    color = green
                    start_time = time.time()

            else:
                count +=1
                display_text(font2, lx,ly, chr(event.key))
                if event.key == correct_answer:
                    correct_text += " "+chr(correct_answer)
                    correct_answer = random.randint(97,122)
                    score +=1
                    color = green
                else:

                    color = red

    current = time.time()-start_time

    if current >60:
        game_over = True


    if game_over:
        display_screen_gameover()

    else:
        display_screen(font2, color)

    display_picture()
    pygame.display.update()

if __name__ == "__main__":
    main()






