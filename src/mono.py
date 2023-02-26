import pygame 
import sys
import moviepy.editor
import game 
import cv2

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


def lose(points):
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
    video = moviepy.editor.VideoFileClip("assets/intro.mov")
    video2 = video.resize((1280, 720))
    video2.preview()

def loading_screen():
    video = moviepy.editor.VideoFileClip("assets/loading.mov")
    video2 = video.resize((1280, 720))
    video2.preview()  

IMAGE_TIME = 10

def empty(a):
    pass


def getContours(img, imgContour, shapeDict):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, 
                                           cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 5000:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            x, y, w, h = cv2.boundingRect(approx)

            match len(approx):
                case 3:
                    cv2.putText(imgContour, "Triangle", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['triangle'] += 1
                    break 
                case 4:
                    cv2.putText(imgContour, "Square", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['square'] += 1
                    break 
                case 5:
                    cv2.putText(imgContour, "Pentagon", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['pentagon'] += 1
                    break 
                case 6:
                    cv2.putText(imgContour, "Hexagon", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['hexagon'] += 1
                    break 
                case 8:
                    cv2.putText(imgContour, "Octagon", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['octagon'] += 1
                    break 
                case _:
                    cv2.putText(imgContour, "Unknown", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    break 


def check(shapeDict, target):

    for shape in shapeDict:
        if shapeDict[shape] >= 50:
            if shape == target:
                return True
            elif shapeDict[shape] >= 80 and shape != target:
                return False


def get_shape():
    val = random.randint(0,4)
    if val == 0:
        return 'triangle'
    elif val == 1:
        return 'square'
    elif val == 2:
        return 'pentagon'
    elif val == 3:
        return 'hexagon'
    elif val == 4:
        return 'octagon'
    

def clear_dict(shapeDict):
    for shape in shapeDict:
        shapeDict[shape] = 0
    return shapeDict


def game_loop(webcam, mode):
    pygame.init()
    width, height = 1280, 720

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("ShapeIt!")

    fps = 30
    clock = pygame.time.Clock()
    counter = 25
    img_check = 0

    offset = 0
    font = pygame.font.SysFont('Consolas', 30)
    text = font.render(str(counter), True, (0, 128, 0))

    time_delay = 1000
    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, time_delay)

    pygame.time.set_timer(pygame.USEREVENT, time_delay)

    shapeDict = {'triangle': 0, 'square': 0, 'pentagon': 0, 
                 'hexagon': 0, 'octagon': 0}
    
    if mode == 1:
        bg = pygame.image.load("assets/BORDER_GRAD.png").convert()
    else:
         bg = pygame.image.load("assets/BORDER_GRAD_REDDD.png").convert()
    
    tessy_n = pygame.image.load("assets/tessy1.png")
    tessy_s = pygame.image.load("assets/thumbsup.png")
    tessy_f = pygame.image.load("assets/thumbsdown.png")
    circle_g = pygame.image.load("assets/circle.png")
    ecks = pygame.image.load("assets/x.png")

    bg_border = pygame.draw.rect(window, [  0,  0, 223], (1000,1000,25,25), 0)

    start = True

    goodbad = True

    points = 0

    drawing = True
    task = get_shape()
    request = font.render("Draw me a... " + task, True, (255, 255, 255))

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
            if event.type == pygame.USEREVENT:
                counter -= 1
                if mode == 1:
                    counter = 1000
                if img_check != 0:
                    img_check -= 1
                text = font.render(str(counter), True, (0, 128, 0))

        # OpenCV
        success, img = webcam.read()
        imgContour = img.copy()

        imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
        imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

        # thresholds for the canny detection algorithm
        threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
        threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

        # canny algorithm detects edges and shows the contours
        imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

        # dilates the image so the edges are bigger and easier to see
        kernel = np.ones((5, 5))
        imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

        getContours(imgDil, imgContour, shapeDict)

        if check(shapeDict, task) == True:
            goodbad = True
            points+=1
            img_check = 2
            shapeDict = clear_dict(shapeDict)
            task = get_shape()
            request = font.render("Draw me a... " + task, True, (0, 0, 0))
            counter += 2
            print(task)
        elif check(shapeDict, task) == False:
            goodbad = False
            img_check = 2
            shapeDict = clear_dict(shapeDict)
            task = get_shape()
            request = font.render("Draw me a... " + task, True, (0, 0, 0))
            counter -= 5
            print(task)

        if counter <= 0 and mode == 2:
            img_check = 2
            print("no time, you lose!")
            shapeDict = clear_dict(shapeDict)
            task = get_shape()
            print(task)
            lose(points)
        

        imgContour = cv2.cvtColor(imgContour.copy(), cv2.COLOR_BGR2RGB)
        imgContour = np.rot90(imgContour) 

        frame = pygame.surfarray.make_surface(imgContour).convert()
        frame = pygame.transform.flip(frame, True, False)

        window.blit(bg, (0,0))
        window.blit(frame, (155, 90))

        if mode != 1:
            window.blit(text, (640,25))
        window.blit(request, (440, 670))

        if img_check != 0:
            if goodbad == False:
                window.blit(tessy_f, (0,0))
                window.blit(ecks, (0,0))
            if goodbad == True:
                window.blit(tessy_s, (0,0))
                window.blit(circle_g, (0,0))
        else:
            window.blit(tessy_n, (0,0))

        pygame.display.flip()

        clock.tick(fps)


def run(mode):
    frameWidth = 1180
    frameHeight = 620
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)

    cv2.namedWindow("Parameters")
    cv2.resizeWindow("Parameters", 640, 240)
    cv2.createTrackbar("Threshold1", "Parameters", 255, 255, empty)
    cv2.createTrackbar("Threshold2", "Parameters", 116, 255, empty)

    game_loop(cap, mode)

run(2)


def main():
    start_screen()

main()