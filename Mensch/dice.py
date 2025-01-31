


import random
import pygame
import os
import sounds
pygame.init()

def dice_roll(screen):
    base_path = os.path.dirname(__file__)
    dice_number = random.randint(1, 6)
    sounds.dice_sound_effect()

    def dice_image(screen, dice_number):
        
        image_path = os.path.join(base_path, f"dice-images/dice-six-faces-{dice_number}.png")
        img = pygame.image.load(image_path).convert()
        new_size = (50, 50)  # New size (width, height)
        img = pygame.transform.scale(img, new_size)
        screen.blit(img, (275, 275))
        
        pygame.display.update()

    dice_image(screen, dice_number)

    pygame.time.wait(2000)
