import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprites with Controls")
clock = pygame.time.Clock()

sprite1 = pygame.Rect(100, 100, 60, 60)
sprite2 = pygame.Rect(300, 300, 60, 60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.x -= 5
    if keys[pygame.K_RIGHT]:
        sprite1.x += 5
    if keys[pygame.K_UP]:
        sprite1.y -= 5
    if keys[pygame.K_DOWN]:
        sprite1.y += 5

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), sprite1)
    pygame.draw.rect(screen, (0, 255, 0), sprite2)
    pygame.display.flip()
    clock.tick(60)
