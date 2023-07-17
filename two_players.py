import pygame


class Robot:
    def __init__(self, image: str, x: int, y: int) -> None:
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False


pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = Robot("robot.png", 0, 0)
robot2 = Robot("robot.png", 320, 240)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                robot1.to_left = True
            if event.key == pygame.K_RIGHT:
                robot1.to_right = True
            if event.key == pygame.K_UP:
                robot1.to_up = True
            if event.key == pygame.K_DOWN:
                robot1.to_down = True
            if event.key == pygame.K_a:
                robot2.to_left = True
            if event.key == pygame.K_d:
                robot2.to_right = True
            if event.key == pygame.K_w:
                robot2.to_up = True
            if event.key == pygame.K_s:
                robot2.to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                robot1.to_left = False
            if event.key == pygame.K_RIGHT:
                robot1.to_right = False
            if event.key == pygame.K_UP:
                robot1.to_up = False
            if event.key == pygame.K_DOWN:
                robot1.to_down = False
            if event.key == pygame.K_a:
                robot2.to_left = False
            if event.key == pygame.K_d:
                robot2.to_right = False
            if event.key == pygame.K_w:
                robot2.to_up = False
            if event.key == pygame.K_s:
                robot2.to_down = False

        if event.type == pygame.QUIT:
            exit()

    if robot1.to_right and robot1.x <= 640 - robot1.image.get_width():
        robot1.x += 2
    if robot1.to_left and robot1.x >= 0:
        robot1.x -= 2
    if robot1.to_up and robot1.y >= 0:
        robot1.y -= 2
    if robot1.to_down and robot1.y <= 480 - robot1.image.get_height():
        robot1.y += 2
    if robot2.to_right and robot2.x <= 640 - robot2.image.get_width():
        robot2.x += 2
    if robot2.to_left and robot2.x >= 0:
        robot2.x -= 2
    if robot2.to_up and robot2.y >= 0:
        robot2.y -= 2
    if robot2.to_down and robot2.y <= 480 - robot2.image.get_height():
        robot2.y += 2

    window.fill((0, 0, 0))
    window.blit(robot1.image, (robot1.x, robot1.y))
    window.blit(robot2.image, (robot2.x, robot2.y))
    pygame.display.flip()

    clock.tick(60)
