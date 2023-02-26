import pygame 
import sys
from moviepy.editor import *
import game 

pygame.init() 
pygame.display.set_caption("Shape It!")
bg = pygame.image.load("assets/main_screen.png")

WHITE = (255,255,255) 
GREY = (170,170,170)
DARK_GREY = (100,100,100)
BLACK = (0,0,0)
difficulty = 2

res = 1280, 720
screen = pygame.display.set_mode(res) 
smallfont = pygame.font.SysFont('Comics Sans MS',40) 
bigfont = pygame.font.SysFont('Roboto', 80)

def lose_screen(points):
    new_bg = pygame.image.load("assets/timesup.png")

    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= mouse[0] <= 610+140 and 415 <= mouse[1] <= 415+80: 
                   start_screen()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 550 <= mouse[0] <= 610+140 and 535 <= mouse[1] <= 535+80: 
                    pygame.quit()
                    sys.exit()

        text = bigfont.render("Points: " + points, True, WHITE)

        mouse = pygame.mouse.get_pos() 
        new = pygame.transform.scale(new_bg, (1280, 720))
        screen.blit(new, (0, 0))

        if 550 <= mouse[0] <= 600+140 and 415 <= mouse[1] <= 415+80: 
            img = pygame.image.load('assets/home_selected.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,415))
        else: 
            img = pygame.image.load('assets/home_button.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,415))
        if 550 <= mouse[0] <= 600+140 and 535 <= mouse[1] <= 535+80: 
            img = pygame.image.load('assets/exit_selected.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,535))
        else: 
            img = pygame.image.load('assets/exit_button.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,535)) 

        screen.blit(text,(500, 315))
        
        pygame.display.update() 


def start_screen():  
    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit() 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= mouse[0] <= 610+140 and 335 <= mouse[1] <= 335+80: 
                    if difficulty == 1:
                        intro_scene()
                        loading_screen()
                        pygame.quit()
                        game.run(difficulty)
                        break
                    if difficulty == 2:
                        intro_scene()
                        loading_screen()
                        pygame.quit()
                        game.run(difficulty)
                        break
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= mouse[0] <= 610+140 and 435 <= mouse[1] <= 435+80: 
                    difficulty_screen()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 550 <= mouse[0] <= 610+140 and 535 <= mouse[1] <= 535+80: 
                    pygame.quit()
                    sys.exit()

        text = smallfont.render("Mode: ", True, BLACK)

        mouse = pygame.mouse.get_pos() 
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))

        if difficulty == 1:
            text = smallfont.render("Mode: Education", True, BLACK)
        if difficulty == 2:
            text = smallfont.render("Mode: Challenge", True, BLACK)

        if 550 <= mouse[0] <= 600+140 and 335 <= mouse[1] <= 335+80: 
            img = pygame.image.load('assets/start_selected.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,320))
        else: 
            img = pygame.image.load('assets/start_button.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,320))
        if 550 <= mouse[0] <= 600+140 and 435 <= mouse[1] <= 435+80: 
            img = pygame.image.load('assets/mode_selected.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,435))
        else: 
            img = pygame.image.load('assets/mode_button.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,435))
        if 550 <= mouse[0] <= 600+140 and 535 <= mouse[1] <= 535+80: 
            img = pygame.image.load('assets/exit_selected.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,545))
        else: 
            img = pygame.image.load('assets/exit_button.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,545)) 

        screen.blit(text,(950,680))

        pygame.display.update() 

def difficulty_screen():
    global difficulty

    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= mouse[0] <= 610+140 and 335 <= mouse[1] <= 335+80: 
                    global difficulty
                    difficulty = 1
                    start_screen()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= mouse[0] <= 610+140 and 435 <= mouse[1] <= 435+80: 
                    difficulty = 2
                    start_screen()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 550 <= mouse[0] <= 610+140 and 535 <= mouse[1] <= 535+80: 
                    start_screen()    

        text = smallfont.render(" ", True, BLACK)

        mouse = pygame.mouse.get_pos() 
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))

        if 550 <= mouse[0] <= 600+140 and 335 <= mouse[1] <= 335+80: 
            img = pygame.image.load('assets/education_selected.png')
            img = pygame.transform.scale(img, (200, 90))
            text = smallfont.render("No time limit!", True, BLACK)
            screen.blit(img,(545,320))
        else: 
            img = pygame.image.load('assets/education_button.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,320))
        if 550 <= mouse[0] <= 600+140 and 435 <= mouse[1] <= 435+80: 
            img = pygame.image.load('assets/challenge_selected.png')
            img = pygame.transform.scale(img, (200, 90))
            text = smallfont.render("A timed challenge!", True, BLACK)
            screen.blit(img,(545,435))
        else: 
            img = pygame.image.load('assets/challenge_button.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,435))
        if 550 <= mouse[0] <= 600+140 and 535 <= mouse[1] <= 535+80: 
            img = pygame.image.load('assets/back_selected.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,545))
        else: 
            img = pygame.image.load('assets/back_button.png')
            img = pygame.transform.scale(img, (200, 90))
            screen.blit(img,(545,545))

        screen.blit(text,(750, 680))

        pygame.display.update() 

def intro_scene():
    video = VideoFileClip("assets/intro.mov")
    video2 = video.resize((1280, 720))
    video2.preview()

def loading_screen():
    video = VideoFileClip("assets/loading.mov")
    video2 = video.resize((1280, 720))
    video2.preview()  

def main():
    intro_scene()

main()