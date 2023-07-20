import pygame
from datetime import datetime
from math import sin, cos, pi

WIDTH = 640
HEIGHT = 480


def draw_hand(size, thickness, angle):
    pygame.draw.line(  # seconds
        window, (0, 0, 255),
        (WIDTH // 2, HEIGHT // 2),
        (WIDTH // 2 + size * cos(angle - pi / 2),
         HEIGHT // 2 + size * sin(angle - pi / 2)),
        thickness
    )


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    pygame.display.set_caption(datetime.now().strftime("%H:%M:%S"))
    seconds = int(datetime.now().strftime("%S")) * pi / 30
    minutes = int(datetime.now().strftime("%M")) * pi / 30
    hours = int(datetime.now().strftime("%H")) * pi / 6
    window.fill((0, 0, 0))  # black background
    pygame.draw.circle(window, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), 200, 4)
    pygame.draw.circle(window, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), 7)
    draw_hand(185, 1, seconds)  # seconds
    draw_hand(180, 2, minutes)  # minutes
    draw_hand(135, 5, hours)  # hours
    pygame.display.flip()
    clock.tick(60)
