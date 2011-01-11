import pygame
from World import world_height, world_width
class Camera():
    
    def __init__(self):
        self.camera_width = 450
        self.camera_height = 250
        self.camera_offset_x = 0
        self.camera_offset_y = 0
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        pass     
    def get_tuple(self):
        return (self.camera_width, self.camera_height)
    
    def update(self):
        if (self.down):
            if self.camera_offset_y+self.camera_height>world_height:
                self.camera_offset_y = world_height-self.camera_height
            else:
                self.camera_offset_y += 2
        if (self.up):
            if self.camera_offset_y<0:
                self.camera_offset_y = 0
            else:
                self.camera_offset_y -= 2
        if (self.right):
            if self.camera_offset_x+self.camera_width>world_width:
                self.camera_offset_x = world_width-self.camera_width
            else:
                self.camera_offset_x += 2
        if (self.left):
            if self.camera_offset_x<0:
                self.camera_offset_x=0
            else:
                self.camera_offset_x -= 2
        pass
    
    def handle_key(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.up = True
            if event.key == pygame.K_DOWN:
                self.down = True
            if event.key == pygame.K_LEFT:
                self.left = True
            if event.key == pygame.K_RIGHT:
                self.right = True
            pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.up = False
            if event.key == pygame.K_DOWN:
                self.down = False
            if event.key == pygame.K_LEFT:
                self.left = False
            if event.key == pygame.K_RIGHT:
                self.right = False
            pass                
        pass
        
    pass

