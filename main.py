from pygame.locals import *
import pygame
clock = pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((600,600),RESIZABLE)
pygame.display.set_caption("Sketchup Pro")
line_logo=pygame.image.load('Line Logo.png')
line_logo=pygame.transform.rotozoom(line_logo,0,0.25)
rectangle=pygame.image.load('Rectangle.png')
rectangle=pygame.transform.rotozoom(rectangle,0,0.25)
activate = False
color = 'White'
coordinates = []
while True:
    clock.tick(200)
    pygame.draw.rect(screen,(255,0,0),(500,1,100,100))
    pygame.draw.rect(screen,(255,255,255),(400,1,100,100))
    screen.blit(line_logo,(0,0))
    screen.blit(rectangle,(136,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if activate=='Rect NOW':
                coordinates.append(pos)
                activate='Rect end'
            elif activate=='Rect end':
                coordinates.append(pos)
                pygame.draw.rect(screen,(255,255,255),(coordinates[0][0],coordinates[0][1],abs(coordinates[1][0]-coordinates[0][0]),abs(coordinates[1][1]-coordinates[0][1])))
                coordinates=[]
                activate=False
            elif activate=='LINE NOW':
                coordinates.append(pos)
                activate='LINE END'
            elif activate=='LINE END':
                coordinates.append(pos)
                pygame.draw.line(screen,(255,255,255),(coordinates[0]),(coordinates[1]),2)
                coordinates=[]
                activate=False
            elif 500<=pos[0]<=600 and 1<=pos[1]<=100:
                color='Red'
            elif 400<=pos[0]<=500 and 1<=pos[1]<=100:
                color='White'
            elif 0<=pos[1]<=134 and 0<=pos[0]<=134:
                activate='LINE NOW'
            elif 136<=pos[0]<=270 and 0<=pos[1]<=134:
                activate='Rect NOW'
            else:
                activate = True
        elif event.type==MOUSEBUTTONUP:
            if activate not in ['LINE END','LINE NOW','Rect NOW','Rect end']:
                activate = False
        pygame.display.update()
    if activate == True:
        if color=='White':
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(255,255,255),pos,10)
        elif color=='Red':
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(255,0,0),pos,10)
    pygame.display.update()
