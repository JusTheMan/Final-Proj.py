#File Created by Justin Edusada - Final Intro to Computer Programming Project
#Project Goal - To create an object that is movable in any direction (Up, Down, Left, Right) 
#Project Goal Cont. - Complete a maze using the object where walls kill you and once you complete a "WIN" pops up.  
#works cited: https://iq.opengenus.org/maze-in-python/

import random
import pygame
import time
import Settings

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# making the maze / non visual representation of the maze 
maze = [
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 2],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 3, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
]

# Find the starting position

start_x = None
start_y = None
#itirate over rows and columns of the maze 0)
for y, row in enumerate(maze):
    for x, block in enumerate(row):
        if block == 3:
            start_x = x
            start_y = y
            break
    if start_x is not None:
        break

# renders the non visual representation of the maze
def renderMaze(maze):
    x = 0
    y = 0
    for row in maze:
        for block in row:
            # dimensions = 60x60 
            # 0 = movable area 
            if block ==     0:
                pygame.draw.rect(screen, (90, 90, 90), (x, y, 60, 60))
        # 1 = blocked area 
            elif block == 1:
                pygame.draw.rect(screen, (255, 0, 0) ,(x, y, 50, 60))
        # 2 = destination block 
            elif block == 2:
                pygame.draw.rect(screen, (255, 255, 255), (x, y, 60, 60))
        # 3 start block 
            elif block == 3:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, 60, 60))
            
        #since dimension of rectangle is 60*60, we move the starting coordinate after each block is drawn
            x = x + 60
        y = y + 60
        x = 0

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#IF a key is pressed on keyboard
        if event.type == pygame.KEYDOWN:
        
            #if left key is pressed
            if event.key == pygame.K_LEFT:
                #Block moves one value to the left
                block = maze[y][x-1]
                #0 = movable space
                if block == 0:
                    #new current position to the left
                    maze[y][x-1]= 2
                    maze[y][x] = 0
                    x = x - 1 

                elif block == 2:
                    maze[y][x-1] = 0
                    maze[y][x] = 0
                    x = x - 1                     
                    dest = 1
            
            #if right key is pressed
            if event.key == pygame.K_RIGHT:
                #Block moves one value to the right
                block = maze[y][x +1]
                
                if block == 0:
                    maze[y][x + 1] =2
                    maze[y][x]=0
                    x = x + 1
                elif block == 2:
                    maze[y][x + 1] = 0
                    maze[y][x] = 0
                    x = x + 1
                    dest = 1
        
            #if up key is pressed
            if event.key == pygame.K_UP:
                #Block moves one value up
                block = maze[y- 1][x]
                if block == 0:
                    maze[y - 1][x]= 2
                    maze[y][x]= 0
                    y = y-1
                elif block == 2:
                    maze[y -1][x] = 0
                    maze[y][x] = 0
                    y = y- 1
                    dest=1
            
            #if down key is pressed
            if event.key == pygame.K_DOWN:
                #Block moves one value down
                block=maze[y +1][x]
                if block == 0:
                    maze[y+ 1][x]=2
                    maze[y][x]=0
                    y = y + 1
                elif block == 2:
                    maze[y +1][x] = 1
                    maze[y][x] = 0
                    y = y+ 1
                    dest = 1

# fills the rest of screen with color 
    screen.fill("RED")
    #renders the maze
    renderMaze(maze)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # lLimits the frames 60 per second 
    #display text when winning the game 
def displayText(text):
    renderFont = pygame.font.Font('IMPACT.ttf', 45)
    
    textsc = renderFont.render(text, True, Settings.dark)

    surface, rect = textsc, textsc.get_rect()


    rect.center = ((Settings.width/2),(Settings.height/2))


    screen.blit(surface, rect)

    pygame.display.update()

    #delay of 1 second
    time.sleep(1)

# maze = [[1 for x in range(Settings.width)] for y in range(Settings.height)]
# start_x = random.randint(0, Settings.height-1)
# start_y = random.randint(0, Settings.width-1)
# maze[start_x][start_y] = 0


directions = [1, 2, 3, 4]

for dir in directions:
        if dir == 1:
            ...
        elif dir == 2:
            ...
if dir == 1:
            if (start_x-2) > 0 and maze[start_x - 2][start_y] != 0:
                maze[start_x-1][start_y] = 0
                maze[start_x-2][start_y] = 0
elif dir == 2:
    if start_x + 2 < Settings.height - 1 and maze[start_x + 2][start_y] != 0:
        maze[start_x+1][start_y] = 0
        maze[start_x+2][start_y] = 0
elif dir == 3:
    if start_y - 2 > 0 and maze[start_x][start_y - 2] != 0:
        maze[start_x][start_y - 1] = 0
        maze[start_x][start_y - 2] = 0
elif dir == 4:
    if (start_y+2) < Settings.width -1 and maze[start_x][start_y + 2] != 0:
        maze[start_x][start_y + 1] = 0
        maze[start_x][start_y + 2] = 0

pygame.quit()




