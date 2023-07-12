import pygame
import random

WIDTH, HEIGHT = 700, 500

resolution = (WIDTH, HEIGHT)

pygame.init()

window = pygame.display.set_mode(resolution)
window.fill((0, 0, 0))
robot = pygame.image.load("robot.png")

for i in range(1000):
    rd_width = random.randint(0, WIDTH - robot.get_width())
    rd_height = random.randint(0, HEIGHT - robot.get_height())
    window.blit(robot, (rd_width, rd_height))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
