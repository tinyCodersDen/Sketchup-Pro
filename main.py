from pygame.locals import *
import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Sketchup Pro")
activate = False
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==MOUSEBUTTONDOWN:
            activate = True
        elif event.type==MOUSEBUTTONUP:
            activate = False
    if activate == True:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,(255,255,255),pos,10)
    pygame.display.update()
