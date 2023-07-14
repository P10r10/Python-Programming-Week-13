import pygame
from random import choice, randint


class Robot:
    def __init__(self, image: str, x: int, y: int, h_speed: int) -> None:
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.h_speed = h_speed  # h_speed when robot hits the ground (-1 or 1)


pygame.init()
window = pygame.display.set_mode((640, 480))
robots = [Robot("robot.png", randint(0, 590), randint(-1000, 0),
                choice([-1, 1])) for _ in range(50)]  # creates 50 robots
clock = pygame.time.Clock()

while True:  # each iteration is a frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))  # black background
    for robot in robots:  # updates position of all robots in collection
        window.blit(robot.image, (robot.x, robot.y))
        if robot.y >= 480 - robot.image.get_height():  # robot hits ground
            robot.x += robot.h_speed
        else:  # robot is falling
            robot.y += 1

    pygame.display.flip()

    clock.tick(60)
