import pygame
pygame.init

width = 500
height = 500
screen = pygame.display.set_mode((width,height))
image = pygame.image.load(r"C:\Users\Prince\OneDrive\Desktop\nicholas game dev\pygame class\Image20260222173431.png")
image = pygame.transform.scale(image,(100,100))

bgImg = pygame.image.load(r"C:\Users\Prince\OneDrive\Desktop\nicholas game dev\pygame class\Image20260222174758.png")
bgImg = pygame.transform.scale(bgImg,(width,height))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bgImg,(0,0))
    screen.blit(image,(100,100))
    pygame.display.update()