import pygame


class Robot:
    def __init__(self, image: str, x: int, y: int, speed: int) -> None:
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.speed = speed


pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = Robot("robot.png", 1, 50, 1)
robot2 = Robot("robot.png", 1, 150, 2)

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if robot1.x >= 640 - robot1.image.get_width() or robot1.x <= 0:
        robot1.speed = -robot1.speed
    if robot2.x >= 640 - robot2.image.get_width() or robot2.x <= 0:
        robot2.speed = -robot2.speed

    robot1.x += robot1.speed
    robot2.x += robot2.speed

    window.fill((0, 0, 0))
    window.blit(robot1.image, (robot1.x, robot1.y))
    window.blit(robot2.image, (robot2.x, robot2.y))
    pygame.display.flip()

    clock.tick(160)
