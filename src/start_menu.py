from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
pygame.display.set_caption("Shape It!")
surface = pygame.display.set_mode((1920, 1080))

def difficulty(value, difficulty):
    print(value)
    print(difficulty)

def start():
    pass

def level_menu():
    mainmenu._open(level)

#adds basic menu layout
mainmenu = pygame_menu.Menu('WELCOME TO SHAPE IT!', 1920, 1080, theme=themes.THEME_GREEN)
mainmenu.add.text_input('Name: ', default='insert name here', maxchar=20)
mainmenu.add.button('Play', start)
mainmenu.add.button('Select Difficulty', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
 
#lets you change the difficuty
level = pygame_menu.Menu('Select a Difficulty', 1920, 1080, theme=themes.THEME_BLUE)
level.add.selector('Difficulty :', [('Learning', 1), ('Challenge', 2)], onchange=difficulty)

#loading bar
loading = pygame_menu.Menu('Loading...', 1920, 1080, theme=themes.THEME_DARK)
loading.add.progress_bar("Progress", progressbar_id = "1", default=0, width = 200, )
 
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))
 
update_loading = pygame.USEREVENT + 0
 
#loading loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == update_loading:
            progress = loading.get_widget("1")
            progress.set_value(progress.get_value() + 1)
            if progress.get_value() == 100:
                pygame.time.set_timer(update_loading, 0)
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        if (mainmenu.get_current().get_selected_widget()):
            arrow.draw(surface, mainmenu.get_current().get_selected_widget())
 
    pygame.display.update()