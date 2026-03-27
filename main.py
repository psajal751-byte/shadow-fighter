import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shadow Fighter")

clock = pygame.time.Clock()

player = pygame.Rect(100, 300, 50, 50)
enemy = pygame.Rect(600, 300, 50, 50)

speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # TOUCH CONTROL (for mobile)
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        if x < WIDTH // 2:
            player.x -= speed
        else:
            player.x += speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.update()
    clock.tick(60)
