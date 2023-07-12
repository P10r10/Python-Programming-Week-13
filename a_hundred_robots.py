import pygame

WIDTH, HEIGHT = 700, 500

resolution = (WIDTH, HEIGHT)

pygame.init()

window = pygame.display.set_mode(resolution)
window.fill((0, 0, 0))
robot = pygame.image.load("robot.png")
for i in range(10):
    for j in range(10):
        window.blit(robot, (j * 25 + i * 15, i * 20))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
