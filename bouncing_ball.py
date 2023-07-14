import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")
clock = pygame.time.Clock()
x, y, h_speed, v_speed = 320, 240, 1, 1
while True:  # frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(ball, (x, y))

    if y >= 480 - ball.get_height() or y <= 0:
        v_speed = -v_speed
    if x >= 640 - ball.get_width() or x <= 0:
        h_speed = -h_speed

    x += h_speed
    y += v_speed

    pygame.display.flip()

    clock.tick(160)
