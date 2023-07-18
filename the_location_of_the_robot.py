import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = 320
robot_y = 240

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (
                event.pos[0] >= robot_x and
                event.pos[0] <= robot_x + robot.get_width() and
                event.pos[1] >= robot_y and
                event.pos[1] <= robot_y + robot.get_height()
            ):
                robot_x = randint(0, 640 - robot.get_width())
                robot_y = randint(0, 480 - robot.get_height())

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)
