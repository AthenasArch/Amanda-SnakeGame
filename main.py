# Import required libraries
import pygame, random
from pygame.locals import *
from tkinter import *
from PIL import ImageTk, Image

# dimensoes da tela
SCREEN_HEIGHT = 600
SCREEN_LENGTH = 600

# Nome do jogo, dicas: Ex, irma ou Sogra...
GAME_NAME = 'Snake Amanda'

# Tamanho dos pixels utilizados (Tambem e o tamanho da caomida da cobra)
SIZE_PIXEL = 10 

SCORE_ADDER = 3 # Essa constante adiciona diretamente na pontuacao e velocidade da snake
SCORE_TO_SCARY = 30 # pontos necessarios mostrar a imagem de susto

# velocidade inicial da cobra
START_CLOCK_MIN_PEED = 10 

# Sem a grade externa, caso nao queira utilizar a grade externa, utilize esta funcao
# def on_grid_random():
#     x = random.randint(0, 590)
#     y = random.randint(0, 590)
#     return (x//SIZE_PIXEL * SIZE_PIXEL, y//SIZE_PIXEL * SIZE_PIXEL)

# Faz os calculos de geracao da comida da Snke 
def on_grid_random_withFrame():
    # gera um valor randomico dentro das margens do tamanho da tela
    x = random.randint(0 + SIZE_PIXEL, 590 - SIZE_PIXEL)
    y = random.randint(0 + SIZE_PIXEL, 590 - SIZE_PIXEL)
    return (x//SIZE_PIXEL * SIZE_PIXEL, y//SIZE_PIXEL * SIZE_PIXEL)

# funcao que trata o colisor
def colission(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1]) 

# pontos iniciais
pontuacao = 0

# Teclas utilizadas
UP = 0
RIGHT = 1 
DOWN = 2
LEFT = 3

# pegue a tabela de cores RGB para gerenciar cores
# color       (R, G, B)
COLOR_WITE  = (255, 255, 255)
COLOR_RED   = (255, 0, 0)
COLOR_BLUE   = (0, 0, 255)

# relogio para atualizar a tela
clock = pygame.time.Clock()

pygame.init() # inicia o pygame
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_LENGTH)) # inicia a tela com os tamanhos setados
pygame.display.set_caption(GAME_NAME) # nome do jogo

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

# rat_pos = on_grid_random()
rat_pos = on_grid_random_withFrame()
rat = pygame.Surface((SIZE_PIXEL, SIZE_PIXEL))
rat.fill(COLOR_RED)

# direcao de inicio do jogo
my_direction = RIGHT

# makeLargeFrame()

while True:
    clock.tick(pontuacao + START_CLOCK_MIN_PEED)
    
    # habilita tratamento de eventos do telcado
    for event in pygame.event.get():
        # evento de saida do jogo
        if event.type == QUIT:
            pygame.quit()

        # trata os eventos das telcas direcionais
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
        
    # se a cobra colidir com o rato (Comer o rato)
    if colission(snake[0], rat_pos):
        # rat_pos = on_grid_random()
        rat_pos = on_grid_random_withFrame()
        snake.append((0,0))
        pontuacao = pontuacao + SCORE_ADDER
        print("ponto = ", pontuacao)

    # se chegou em uma determinada qtde de pontos, assusta o caboclo
    if pontuacao > SCORE_TO_SCARY:
        print("Da um susto")
        scary()
        pygame.quit()

    # Faz a cobra aumentar o tamanho
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # as condicionais abaixo fazem com que a matriz da cobra se movimente nas posicoes
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - SIZE_PIXEL)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + SIZE_PIXEL)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + SIZE_PIXEL, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - SIZE_PIXEL, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(rat, rat_pos)
    
    # se colidir na janela em x sup 
    for frame_pos in range(0, SCREEN_LENGTH, 10):
        frame_x_y_pos = (frame_pos, 0)
        screen.blit(myFrame, frame_x_y_pos)
        if colission(snake[0], frame_x_y_pos):
            pygame.quit()
            print("SE FODEU")

    # se colidir na janela em x inf
    for frame_pos in range(0, SCREEN_LENGTH, 10):
        frame_x_y_pos = (frame_pos, SCREEN_LENGTH-10)
        screen.blit(myFrame, frame_x_y_pos)
        if colission(snake[0], frame_x_y_pos):
            pygame.quit()
            print("SE FODEU")

    # se colidir na janela em y esq
    for frame_pos in range(0, SCREEN_HEIGHT, 10):
        frame_x_y_pos = (0, frame_pos)
        screen.blit(myFrame, frame_x_y_pos)
        if colission(snake[0], frame_x_y_pos):
            pygame.quit()
            print("SE FODEU")

    # se colidir na janela em y dir
    for frame_pos in range(0, SCREEN_HEIGHT, 10):
        frame_x_y_pos = (SCREEN_HEIGHT - 10, frame_pos)
        screen.blit(myFrame, frame_x_y_pos)
        if colission(snake[0], frame_x_y_pos):
            pygame.quit()
            print("SE FODEU")

    # isso aqui atualiza a posicao da cobra na tela
    for pos in snake:
        screen.blit(snake_skin, pos)

    # isso aqui atualiza a tela
    pygame.display.update()