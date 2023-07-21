import pygame
from random import randint

WIDTH, HEIGHT, ROCKS = 640, 480, 50


class Robot:
    def __init__(self, image: str) -> None:
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        x = (WIDTH + self.image.get_width()) // 2
        y = HEIGHT - self.image.get_height()
        self.moving_right = False
        self.moving_left = False
        self.rect.topleft = (x, y)


class Asteroid:
    def __init__(self, image: str) -> None:
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        x = randint(0, WIDTH - self.rect.width)
        y = randint(-20 * HEIGHT, 0)
        self.rect.topleft = (x, y)

    def has_colided(self, robot: Robot):
        return self.rect.colliderect(robot.rect)


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
points = 0
game_over = False
robot = Robot("robot.png")
asteroids = [Asteroid("rock.png") for _ in range(ROCKS)]  # creates asteroids
game_font = pygame.font.SysFont("Arial", 24)
while True:
    if game_over:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                robot.moving_right = True
            if event.key == pygame.K_LEFT:
                robot.moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                robot.moving_right = False
            if event.key == pygame.K_LEFT:
                robot.moving_left = False
    if (
        robot.moving_right and
        robot.rect.centerx <= WIDTH - robot.image.get_width() // 2
    ):
        robot.rect.centerx += 4
    if robot.moving_left and robot.rect.centerx >= robot.image.get_width() // 2:
        robot.rect.centerx -= 4

    pygame.display.set_caption("Asteroidit")
    window.fill((0, 0, 0))  # black background
    score = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(score, (WIDTH - score.get_width() - 5, 5))  # updates score
    window.blit(robot.image, robot.rect)  # updates robot
    for asteroid in asteroids:  # updates all asteroids
        window.blit(asteroid.image, asteroid.rect)
        asteroid.rect.bottom += 1  # asteroid falling speed
        if asteroid.has_colided(robot):
            points += 1
            asteroids.remove(asteroid)
        if asteroid.rect.y == HEIGHT - asteroid.image.get_height():
            game_over = True
    pygame.display.flip()
    clock.tick(60)
while True:
    window.fill((0, 0, 0))  # black background
    score = game_font.render(f"Points: {points}", True, (255, 0, 0))
    over = game_font.render(f"GAME OVER", True, (0, 0, 255))
    window.blit(score, (WIDTH - score.get_width() - 5, 5))
    window.blit(over, ((WIDTH - over.get_width()) // 2, HEIGHT // 2))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
