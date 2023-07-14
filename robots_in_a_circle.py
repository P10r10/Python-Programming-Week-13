import pygame
from math import cos, sin, pi

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
clock = pygame.time.Clock()
angle = 0

while True:  # frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    for _ in range(10):  # draws 10 robots in a circle
        x = 295 + 100 * cos(angle)
        y = 198 + 100 * sin(angle)
        window.blit(robot, (x, y))
        angle += pi / 5
    angle += .01

    pygame.display.flip()

    clock.tick(60)
