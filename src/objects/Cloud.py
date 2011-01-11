from Node import *
class Cloud(Node):    
    def __init__(self, images):
        Node.__init__(self, images)
        self.image=images[6]
        self.speed = randint(50,150)
        pass
    
    def update(self, deltaTime):
        self.x -= self.speed*deltaTime/1000.
        if self.x+self.image.get_rect().width<0:
            self.x = world_width
            self.y = randint(0,world_height-self.image.get_rect().height)
        pass
        
    pass