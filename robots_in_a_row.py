import pygame

WIDTH, HEIGHT = 700, 500

resolution = (WIDTH, HEIGHT)

pygame.init()

window = pygame.display.set_mode(resolution)
window.fill((0, 0, 0))
robot = pygame.image.load("robot.png")
for i in range(10):
    window.blit(robot, (i * robot.get_width(),
                (HEIGHT - robot.get_height()) / 2))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
