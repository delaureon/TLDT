import pygame
import os
from map import *

pygame.init()
clock = pygame.time.Clock()
fps = 30
font = pygame.font.Font('fonts/VictorMono-Regular.ttf', 16)
screen = pygame.display.set_mode([320,240])

pygame.display.set_caption('TLDT')

def render_string(str, x, y, screen):
    enter = 0
    for line in str:
        screen.blit(font.render(line, True, 'white'), (x, y+enter))
        enter = enter + 16

run = True
while run:
    clock.tick(fps)
    screen.fill('black')
    render_string(map.get(0).get_description(), 3, 3, screen)
    my_othertext = font.render('look', True, 'white')
    screen.blit(my_othertext, (30, 200))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()