import pygame
import math
import copy
import os
import patterns


pygame.init()
os.system(" start readme.txt")
WINDOW = pygame.display.set_mode((1000, 1000))
START = False
FPS = 60
RFPS = 60


cells = [[0 for j in range(100)] for i in range(100)]


def getStart():
    return START


def setStart(x):
    global START
    START = x


def getFPS():
    return FPS


def setFPS(x):
    global FPS
    FPS = x


def getRFPS():
    return RFPS


def setRFPS(x):
    global RFPS
    RFPS = x


def next_generation():
    last_generation = copy.deepcopy(cells)
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            #
            if last_generation[i][j] == 1:
                if ([last_generation[k[0]][k[1]]for k in get_neighbour(i, j)].count(1)) == 2 or ([last_generation[k[0]][k[1]]for k in get_neighbour(i, j)].count(1)) == 3:
                    cells[i][j] = 1
                else:
                    cells[i][j] = 0
            else:
                if ([last_generation[k[0]][k[1]]for k in get_neighbour(i, j)].count(1)) == 3:
                    cells[i][j] = 1
                else:
                    cells[i][j] = 0
            #count = [last_generation[k[0]][k[1]]for k in get_neighbour(i, j)].count(1)
            # if last_generation[i][j] == 1:
            #    cells[i][j] = 1 if count in range(2, 4) else 0
            # elif last_generation[i][j] == 0:
            #    cells[i][j] = 1 if count == 3 else 0


def gridclear():
    global cells
    cells = [[0 for j in range(100)] for i in range(100)]


def get_neighbour(i, j):
    neighbour = [[i+1, j], [i-1, j], [i, j+1], [i, j-1],
                 [i+1, j+1], [i-1, j+1], [i+1, j-1], [i-1, j-1]]
    neighbour = [i for i in neighbour if 0 <= i[0] < 100 and 0 <= i[1] < 100]
    return neighbour


def update():
    WINDOW.fill((0, 0, 0))
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if cells[i][j] == 1:
                pygame.draw.rect(WINDOW, (255, 255, 255), (j*10, i*10, 10, 10))
                pygame.display.set_caption(
                    "Automat komórkowy {} FPS START-{}".format(getFPS(), getStart()))

    pygame.display.update()


def mouse_accion(mouse_pressed):
    if getStart() != True:
        setFPS(60)
        if mouse_pressed[0]:
            x, y = pygame.mouse.get_pos()
            cells[math.floor(y/10)][math.floor(x/10)] = 1
        if mouse_pressed[2]:
            x, y = pygame.mouse.get_pos()
            cells[math.floor(y/10)][math.floor(x/10)] = 0


def key_accion(keys_pressed):
    if keys_pressed[pygame.K_SPACE]:
        pygame.time.Clock().tick(5)
        if getStart():
            setStart(False)
            setRFPS(getFPS())
            setFPS(60)

        else:
            setStart(True)
            setFPS(getRFPS())

    if keys_pressed[pygame.K_1]:
        pygame.time.Clock().tick(10)
        setFPS(10)
        setRFPS(10)
    if keys_pressed[pygame.K_2]:
        pygame.time.Clock().tick(10)
        setFPS(20)
        setRFPS(20)
    if keys_pressed[pygame.K_3]:
        pygame.time.Clock().tick(10)
        setFPS(30)
        setRFPS(30)
    if keys_pressed[pygame.K_4]:
        pygame.time.Clock().tick(10)
        setFPS(60)
        setRFPS(60)
    if keys_pressed[pygame.K_5]:
        pygame.time.Clock().tick(10)
        setFPS(144)
        setRFPS(144)
    if keys_pressed[pygame.K_EQUALS]:
        pygame.time.Clock().tick(10)
        setFPS(getFPS()+5)
        setRFPS(getFPS())
    if keys_pressed[pygame.K_MINUS]:
        pygame.time.Clock().tick(10)
        if getFPS() > 5:
            setFPS(getFPS()-5)
            setRFPS(getFPS())
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
    if keys_pressed[pygame.K_BACKSPACE]:
        gridclear()
        setStart(False)
    if keys_pressed[pygame.K_g]:
        specialdraw(patterns.glider)
    if keys_pressed[pygame.K_p]:
        specialdraw(patterns.Penta_decathlon)

    if keys_pressed[pygame.K_a]:
        specialdraw(patterns.glider_gun)
    if keys_pressed[pygame.K_s]:
        specialdraw(patterns.pulsar)
    if keys_pressed[pygame.K_l]:
        specialdraw(patterns.lwss)


def specialdraw(pattern):
    y, x = pygame.mouse.get_pos()
    x = math.floor(x/10)
    y = math.floor(y/10)
    for i in pattern:
        try:
            cells[i[0]+x][i[1]+y] = 1
        except:
            print("Komórka poza range nie została utworzona")


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        mouse_pressed = pygame.mouse.get_pressed()
        keys_pressed = pygame.key.get_pressed()
        key_accion(keys_pressed)
        mouse_accion(mouse_pressed)
        if getStart():
            next_generation()
        clock.tick(getFPS())
        update()

    pygame.quit()


if __name__ == "__main__":
    main()
