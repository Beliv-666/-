#Создай собственный Шутер!

import pygame


W = 1280
H = 720

qwer = pygame.display.set_mode((W, H) )

bg = pygame.image.load('galaxy.jpg')
bg = pygame.transform.scale(bg, (W, H))

timer = pygame.time.Clock()

while True:
    qwer.blit(bg, (0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    timer.tick(25)