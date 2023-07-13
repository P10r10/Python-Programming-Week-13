import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

x, y, h_speed, v_speed = 0, 0, 1, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if x == 0 and y == 0:
        h_speed = 1
        v_speed = 0
    if x == 640 - robot.get_width():
        h_speed = 0
        v_speed = 1
    if y == 480 - robot.get_height():
        h_speed = -1
        v_speed = 0
    if x == 0 and y == 480 - robot.get_height():
        h_speed = 0
        v_speed = -1

    x += h_speed
    y += v_speed

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(260)
