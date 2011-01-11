import pygame   #loads the pygame module
 
w = 640   #sets pygame screen width
h = 480   #sets pygame screen height
screen = pygame.display.set_mode((w, h))  #make and display screen
 
#Next line loads graphic.  Replace ball.bmp with the name of your image
graphic = pygame.image.load("data/image/ball/black_ball.png").convert()
 
screen.blit(graphic, (0, 0)) #Display image at 0, 0
 
pygame.display.flip()   #Update screen

running = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0                 #make running 0 to break out of loop
 
    screen.blit(graphic, (0, 0)) #Display image at 0, 0
    pygame.display.flip()   #Update screen