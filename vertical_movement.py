import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

x, y, speed = 0, 0, 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if y == 480 - robot.get_height():
        speed = -1
    if y == 0:
        speed = 1
    y += speed

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
