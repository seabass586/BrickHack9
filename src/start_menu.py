import pygame 
import sys
  
pygame.init() 
pygame.display.set_caption("Shape It!")
bg = pygame.image.load("assets/placeholder.jpg")

WHITE = (255,255,255) 
GREY = (170,170,170)
DARK_GREY = (100,100,100)

res = 1280, 720
screen = pygame.display.set_mode(res) 
smallfont = pygame.font.SysFont('Comics Sans MS',40) 
text1 = smallfont.render("Start", True, WHITE)
text2 = smallfont.render("Mode", True, WHITE)
text3 = smallfont.render('Quit' , True , WHITE) 

def start_screen():  
    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 610 <= mouse[0] <= 610+140 and 425 <= mouse[1] <= 490: 
                    print("Start game")
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 610 <= mouse[0] <= 610+140 and 535 <= mouse[1] <= 590: 
                    print("Options game")
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 610 <= mouse[0] <= 610+140 and 575 <= mouse[1] <= 650: 
                    pygame.quit()
                    sys.exit()

        mouse = pygame.mouse.get_pos() 
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))

        if 610 <= mouse[0] <= 610+140 and 450 <= mouse[1] <= 450+40: 
            pygame.draw.rect(screen, GREY,[575,440,140,40]) 
        else: 
            pygame.draw.rect(screen, DARK_GREY, [575,440,140,40]) 

        if 610 <= mouse[0] <= 610+140 and 550 <= mouse[1] <= 550+40: 
            pygame.draw.rect(screen, GREY,[575,535,140,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[575,535,140,40]) 

        if 610 <= mouse[0] <= 610+140 and 625 <= mouse[1] <= 650+40: 
            pygame.draw.rect(screen, GREY,[575,615,140,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[575,615,140,40]) 

        screen.blit(text1, (610, 445)) 
        screen.blit(text2, (610, 545)) 
        screen.blit(text3, (610, 625)) 

        pygame.display.update() 

def main():
    start_screen()

main()