'''
Created on Jan 11, 2011

@author: pntsgbljr
'''
# coding: utf-8

import pygame
from pygame.locals import *
from Camera import *
from objects import *
from LevelReader import *

camera = Camera()
lr = LevelReader()
pygame.init()
screen = pygame.display.set_mode(camera.get_tuple())
pygame.display.set_caption('Prototype')

nodes = []
clouds = []
isGameRunning = True


def load_image(image):
    if type(image) == list:
        return map(load_image, image)
    elif type(image) == str:  
        return pygame.image.load(image).convert_alpha()

def prepare():
    images = load_image(['data/image/ball/yellow_ball.png',
                         'data/image/ball/red_ball.png',
                         'data/image/ball/orange_ball.png',
                         'data/image/ball/green_ball.png',
                         'data/image/ball/black_ball.png',
                         'data/image/ball/blue_ball.png',
                         'data/image/cloud/cloud.png'])
    for iter in range(0,100):
        nodes.append(Node(images))
        pass
    for iter in range(0,10):
        clouds.append(Cloud(images))
        pass
    pass

def input():
    global isGameRunning
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            isGameRunning = False        
        elif event.type is pygame.KEYDOWN:
            pass
        elif event.type is pygame.KEYUP:
            pass
        elif event.type is pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type is pygame.MOUSEBUTTONUP:
            pass
        elif event.type is pygame.MOUSEMOTION:
            pass
        else:
            pass
        camera.handle_key(event)
    pass

def update(deltaTime):
    for obj in nodes:
        obj.update(deltaTime)
    for cloud in clouds:
        cloud.update(deltaTime)
    camera.update()
    pass

def render(surface):
    surface.fill((0,0,250))
    for obj in nodes:
        obj.draw(surface, camera)
    for cloud in clouds:
        cloud.draw(surface, camera)
    pass

def main():    
    prepare()
    updateClock = pygame.time.Clock()   
    lr.read_map_info()
    while(isGameRunning):        
        input()      
        update(updateClock.tick())        
        render(screen)
        pygame.display.update()
    pass

main()

