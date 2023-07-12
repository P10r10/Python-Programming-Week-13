import pygame

WIDTH, HEIGHT = 700, 500

resolution = (WIDTH, HEIGHT)

pygame.init()

window = pygame.display.set_mode(resolution)
window.fill((0, 0, 0))

robot = pygame.image.load("robot.png")
window.blit(robot, (0, 0))
window.blit(robot, (WIDTH - robot.get_width(), 0))
window.blit(robot, (0, HEIGHT - robot.get_height()))
window.blit(robot, (WIDTH - robot.get_width(), HEIGHT - robot.get_height()))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
