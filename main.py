import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("you pressed the button number",
                  event.button, "at location", event.pos)

        if event.type == pygame.QUIT:
            exit()
