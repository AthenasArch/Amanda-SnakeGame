# Import required libraries
import pygame, random
from pygame.locals import *
from tkinter import *
from PIL import ImageTk, Image

SCREEN_HEIGHT = 600
SCREEN_LENGTH = 600

GAME_NAME = 'Snake Amanda'

SIZE_PIXEL = 10 

SCORE_ADDER = 3 # Essa constante adiciona diretamente na pontuacao e velocidade da snake
SCORE_TO_SCARY = 30 # pontos necessarios para assustar o usuario

START_CLOCK_MIN_PEED = 10

# Sem a grade externa
# def on_grid_random():
#     x = random.randint(0, 590)
#     y = random.randint(0, 590)
#     return (x//SIZE_PIXEL * SIZE_PIXEL, y//SIZE_PIXEL * SIZE_PIXEL)

# Com a grade externa
def on_grid_random_withFrame():
    x = random.randint(0 + SIZE_PIXEL, 590 - SIZE_PIXEL)
    y = random.randint(0 + SIZE_PIXEL, 590 - SIZE_PIXEL)
    return (x//SIZE_PIXEL * SIZE_PIXEL, y//SIZE_PIXEL * SIZE_PIXEL)

def colission(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1]) 


pontuacao = 0

UP = 0
RIGHT = 1 
DOWN = 2
LEFT = 3

# color       (R, G, B)
COLOR_WITE  = (255, 255, 255)
COLOR_RED   = (255, 0, 0)
COLOR_BLUE   = (0, 0, 255)

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_LENGTH))
pygame.display.set_caption(GAME_NAME)


# definimos a imagem de susto
def scary():    
    # Create an instance of tkinter window
    win = Tk()

    # Define the geometry of the window
    win.geometry("700x500")

    frame = Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    #Create a fullscreen window
    win.attributes('-fullscreen', True)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("imagem.png"))
    pygame.mixer.Sound('horror.wav').play()
    # img = ImageTk.PhotoImage(Image.open("imagem.png"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()

    win.mainloop()
    


myFrame = pygame.Surface((SIZE_PIXEL, SIZE_PIXEL))
myFrame.fill(COLOR_BLUE) 
# def makeLargeFrame():
#     sup = [(0, 0)]
#     for i in range(0, SCREEN_HEIGHT, SIZE_PIXEL):   
#         sup.append([i + SIZE_PIXEL, 0])# [(200, 200), (210, 200), (220, 200)]    


# A Snake e uma lista (cada elemento da lista e uma tupla)
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((SIZE_PIXEL, SIZE_PIXEL))
snake_skin.fill(COLOR_WITE)

# apple_pos = on_grid_random()
apple_pos = on_grid_random_withFrame()
apple = pygame.Surface((SIZE_PIXEL, SIZE_PIXEL))
apple.fill(COLOR_RED)

my_direction = RIGHT

# makeLargeFrame()

while True:
    clock.tick(pontuacao + START_CLOCK_MIN_PEED)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
        
        # if event.type == KEYLE
        # if event.type == KEYDOWN
    if colission(snake[0], apple_pos):
        # apple_pos = on_grid_random()
        apple_pos = on_grid_random_withFrame()
        snake.append((0,0))
        pontuacao = pontuacao + SCORE_ADDER
        print("ponto = ", pontuacao)

    # se chegou em uma determinada qtde de pontos, assusta o caboclo
    if pontuacao > SCORE_TO_SCARY:
        print("Da um susto")
        scary()
        pygame.quit()

    # # Faz a cobra aumentar o tamanho
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - SIZE_PIXEL)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + SIZE_PIXEL)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + SIZE_PIXEL, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - SIZE_PIXEL, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    
    # janela em x sup
    for frame_pos in range(0, SCREEN_LENGTH, 10):
        frame_x_y_pos = (frame_pos, 0)
        screen.blit(myFrame, frame_x_y_pos)
        if colission(snake[0], frame_x_y_pos):
            pygame.quit()
            print("SE FODEU")

    # janela em x inf
    for frame_pos in range(0, SCREEN_LENGTH, 10):
        frame_x_y_pos = (frame_pos, SCREEN_LENGTH-10)
        screen.blit(myFrame, frame_x_y_pos)
        if colission(snake[0], frame_x_y_pos):
            pygame.quit()
            print("SE FODEU")
    # janela em y esq
    for frame_pos in range(0, SCREEN_HEIGHT, 10):
        frame_x_y_pos = (0, frame_pos)
        screen.blit(myFrame, frame_x_y_pos)
        if colission(snake[0], frame_x_y_pos):
            pygame.quit()
            print("SE FODEU")
    # janela em y dir
    for frame_pos in range(0, SCREEN_HEIGHT, 10):
        frame_x_y_pos = (SCREEN_HEIGHT - 10, frame_pos)
        screen.blit(myFrame, frame_x_y_pos)
        if colission(snake[0], frame_x_y_pos):
            pygame.quit()
            print("SE FODEU")

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()