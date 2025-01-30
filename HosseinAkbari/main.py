# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
WIN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Mensch by Hossein Akbari")
clock = pygame.time.Clock()

BG = pygame.transform.scale(pygame.image.load("bg.png"), (720, 720))
running = True


def draw():
    WIN.blit(BG, (320, 0))
    pygame.display.update()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    WIN.fill("purple")
    # RENDER YOUR GAME HERE
    draw()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
