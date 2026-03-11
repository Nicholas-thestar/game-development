import pygame,random
pygame.init() 
w,h = 400, 400
screen = pygame.display.set_mode((w,h))
bg = pygame.image.load(r"C:\Users\Prince\OneDrive\Desktop\nicholas game dev\pygame class\Image20260222174758.png")
bg = pygame.transform.scale(bg,(w,h))
clock = pygame.time.Clock()
running = True
class Bat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Prince\OneDrive\Desktop\nicholas game dev\batIm.png")
        self.image = pygame.transform.scale(self.image,(100,50))
        self.rect = self.image.get_rect(center=(w//2,h-2))
        self.speed = 10
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -=self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < w:
            self.rect.x +=self.speed
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Prince\OneDrive\Desktop\nicholas game dev\pygame class\ball.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect(center=(w//2,10))
        self.velX = 5
        self.velY = 5
    def update(self):
        if self.rect.x > w or self.rect.x <0:
            self.velX = -self.velX
        if self.rect.y < -20:
            self.velY = -self.velY
        self.rect.x +=self.velX
        self.rect.y += self.velY


    
bat = Bat()
batGr = pygame.sprite.Group()
batGr.add(bat)

ball = Ball()
ballGr = pygame.sprite.Group()
ballGr.add(ball)
while running:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.sprite.groupcollide(batGr,ballGr,False,False):
            ball.velY = -ball.velY
    screen.blit(bg,(0,0))
    batGr.draw(screen)
    batGr.update()
    ballGr.draw(screen)
    ballGr.update()
    pygame.display.update()
