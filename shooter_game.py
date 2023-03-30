#Создай собственный Шутер!

import pygame

sise = 20
W = 1280
H = 720

qwer = pygame.display.set_mode((W, H) )

bg = pygame.image.load('galaxy.jpg')
bg = pygame.transform.scale(bg, (W, H))

Beliv_img = pygame.image.load('01.png')
Beliv_img = pygame.transform.scale(Beliv_img, (sise*5, sise*5))

gun_img = pygame.image.load('qwerkutf 2.png')
gun_img = pygame.transform.scale(gun_img, (sise, sise*2))

class ASDF():
    def __init__(self, x, y, image, speed):
        self.hitbox = image.get_rect(center = (x, y))
        self.speed = speed

class Player(ASDF):
    def contoll(self):
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_LEFT]:
            self.hitbox.x -= self.speed

        if key_list[pygame.K_RIGHT]:
            self.hitbox.x += self.speed

        if key_list[pygame.K_SPACE]:
            gun = Gun(self.hitbox.centerx, self.hitbox.centery, gun_img, 20)
            gun_list.append(gun)

class Gun(ASDF):
    def move(self):
        self.hitbox.y -= self.speed

gun_list = []

Beliv = Player(W/2, H-100, Beliv_img, 20)



timer = pygame.time.Clock()

while True:
    qwer.blit(bg, (0, 0))
    for gun in gun_list:
        qwer.blit(gun_img, gun.hitbox)
        gun.move()
    qwer.blit(Beliv_img, Beliv.hitbox)
    Beliv.contoll()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    timer.tick(25)