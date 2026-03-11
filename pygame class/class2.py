import pygame
pygame.init()

pygame.mixer.music.load(r"C:\Users\Prince\OneDrive\Desktop\nicholas game dev\din_music.mp3")
pygame.mixer.music.play(-1)
w=600
height =500
screen = pygame.display.set_mode((w,height))
bg = pygame.image.load(r"C:\Users\Prince\OneDrive\Desktop\nicholas game dev\class 5\Image20260301171330.png") 
bg = pygame.transform.scale(bg,(w,height))  
count = 1
# earth = pygame.image.load(r"C:\Users\Prince\OneDrive\Desktop\nicholas game dev\pygame class\Image20260222173431.png")
# earth = pygame.transform.scale(earth,(200,200))
class Earth(pygame.sprite.Sprite):
     def __init__(self, *groups):
          super().__init__()
          self.image = pygame.image.load(r"C:\Users\Prince\OneDrive\Desktop\nicholas game dev\pygame class\Image20260222173431.png")
          self.image = pygame.transform.scale(self.image,(100,100))
          self.rect = self.image.get_rect(center=(w//2,height//2))
          self.velx = 4
          self.vely = 4
     def update(self):
          global count
          if self.rect.right > w or self.rect.left<0:
               self.velx = - self.velx
               if count < 5:
                    earth = Earth()
                    earthGr.add(earth)
                    count +=1
          if self.rect.bottom > height or self.rect.top<0:
               self.vely = -self.vely
          print("hello")
          self.rect.x += self.velx
          self.rect.y += self.vely

earth = Earth()
earthGr = pygame.sprite.Group()
earthGr.add(earth)


earthX = 100
earthY = 100
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                     earthY -=10
                if event.key == pygame.K_DOWN:
                     earthY +=10
                if event.key == pygame.K_LEFT:
                     earthX -=10
                if event.key == pygame.K_RIGHT:
                     earthX +=10

    screen.fill("red")
    screen.blit(bg,(0,0))
    earthGr.draw(screen)
    earthGr.update()
#     screen.blit(earth,(earthX,earthY))
    pygame.display.update()
    