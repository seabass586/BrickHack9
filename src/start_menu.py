import pygame 
import sys
  
pygame.init() 
pygame.display.set_caption("Shape It!")
bg = pygame.image.load("assets/main_screen.png")

WHITE = (255,255,255) 
GREY = (170,170,170)
DARK_GREY = (100,100,100)
difficulty = 0 

res = 1280, 720
screen = pygame.display.set_mode(res) 
smallfont = pygame.font.SysFont('Comics Sans MS',40) 

def start_screen():  
    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 610 <= mouse[0] <= 610+140 and 425 <= mouse[1] <= 490: 
                    if difficulty == 1:
                        print("Education Mode")
                    if difficulty == 2:
                        print("Challenge Mode")
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 610 <= mouse[0] <= 610+140 and 535 <= mouse[1] <= 590: 
                    difficulty_screen()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 610 <= mouse[0] <= 610+140 and 575 <= mouse[1] <= 650: 
                    pygame.quit()
                    sys.exit()

        mouse = pygame.mouse.get_pos() 
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))

        if 610 <= mouse[0] <= 610+140 and 450 <= mouse[1] <= 450+40: 
            img = pygame.image.load('assets/start_selected.png')
            screen.blit(img,(575,440))
        else: 
            img = pygame.image.load('assets/start_button.png')
            screen.blit(img,(575,440))

        if 610 <= mouse[0] <= 610+140 and 550 <= mouse[1] <= 550+40: 
            img = pygame.image.load('assets/mode_selected.png')
            screen.blit(img,(575,535))
        else: 
            img = pygame.image.load('assets/mode_button.png')
            screen.blit(img,(575,535))
        if 610 <= mouse[0] <= 610+140 and 625 <= mouse[1] <= 650+40: 
            img = pygame.image.load('assets/exit_selected.png')
            screen.blit(img,(575,615))
        else: 
            img = pygame.image.load('assets/exit_button.png')
            screen.blit(img,(575,615)) 

        pygame.display.update() 

def difficulty_screen():
    text1 = smallfont.render("Educational", True, WHITE)
    text2 = smallfont.render("Challenge", True, WHITE)
    text3 = smallfont.render('Go Back' , True , WHITE) 

    global difficulty

    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 610 <= mouse[0] <= 610+140 and 425 <= mouse[1] <= 490: 
                    global difficulty
                    difficulty = 1
                    start_screen()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 610 <= mouse[0] <= 610+140 and 535 <= mouse[1] <= 590: 
                    difficulty = 2
                    start_screen()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 610 <= mouse[0] <= 610+140 and 575 <= mouse[1] <= 650: 
                    start_screen()

        mouse = pygame.mouse.get_pos() 
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))

        if 610 <= mouse[0] <= 610+140 and 450 <= mouse[1] <= 450+40: 
            pygame.draw.rect(screen, GREY,[565,440,175,40]) 
        else: 
            pygame.draw.rect(screen, DARK_GREY, [565,440,175,40]) 

        if 610 <= mouse[0] <= 610+140 and 550 <= mouse[1] <= 550+40: 
            pygame.draw.rect(screen, GREY,[565,535,175,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[565,535,175,40]) 

        if 610 <= mouse[0] <= 610+140 and 625 <= mouse[1] <= 650+40: 
            pygame.draw.rect(screen, GREY,[565,615,175,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[565,615,175,40]) 

        screen.blit(text1, (575, 445)) 
        screen.blit(text2, (580, 545)) 
        screen.blit(text3, (585, 625)) 

        pygame.display.update() 

def main():
    start_screen()

main()