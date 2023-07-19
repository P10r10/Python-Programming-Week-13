import pygame
from datetime import datetime

WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    pygame.display.set_caption(datetime.now().strftime("%H:%M:%S"))
    pygame.draw.circle(window, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), 200, 4)
    pygame.draw.circle(window, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), 5)
    pygame.display.flip()

    clock.tick(60)
