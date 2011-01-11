from random import randint
from World import world_width, world_height
import pygame


class Node():
    image = None            
    x , y = 0, 0
#    height, width = 10, 10
    def __init__(self, images):
        self.x = randint(0, world_width)
        self.y = randint(0, world_height)
        self.image = images[randint(0,5)]
        pass
    def update(self, deltaTime):        
        pass
    
    def draw(self, surface, camera):
        points = []
        h, w = self.image.get_rect().height,self.image.get_rect().width 
        points.append((self.x, self.y))
        points.append((self.x+w, self.y))
        points.append((self.x, self.y+h))
        points.append((self.x+w, self.y+h))
        shouldDraw = False
        for p in points:
            if p[0]>camera.camera_offset_x and p[0]<camera.camera_offset_x+camera.camera_width and p[1]>camera.camera_offset_y and p[1]<camera.camera_offset_y+camera.camera_height:
                shouldDraw = True        
        if shouldDraw:
            surface.blit(self.image,(int(self.x-camera.camera_offset_x), int(self.y-camera.camera_offset_y)))
        #pygame.draw.circle(surface, (0,255,255), (int(self.x), int(self.y)), 5, 0)
        pass
    pass