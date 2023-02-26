import pygame
import sys

def lose(points):
    res = 1280, 720
    screen = pygame.display.set_mode(res) 
    bigfont = pygame.font.SysFont('Roboto', 80)

    WHITE = (255,255,255) 
    GREY = (170,170,170)
    DARK_GREY = (100,100,100)
    BLACK = (0,0,0)

    new_bg = pygame.image.load("assets/timesup.png")

    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= mouse[0] <= 610+140 and 415 <= mouse[1] <= 415+80: 
                   print("hi")
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 550 <= mouse[0] <= 610+140 and 535 <= mouse[1] <= 535+80: 
                    pygame.quit()
                    sys.exit()

        text = bigfont.render("Points: " + str(points), True, WHITE)

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

def main():
    lose(0)
