
    
# import random
# import pygame

# pygame.init()
# def dice_roll(screen):
#     dice_number = random.randint(1, 6)
#     sound_file = "./dice_sound.mp3"


#     def sound_effect(sound_file):
#         pygame.mixer.init()
#         sound = pygame.mixer.Sound(sound_file)
#         sound.set_volume(0.2)
#         sound.play()

#     def dice_image(screen, dice_number):
#         print(dice_number)
#         image_path = f"./dice-images/dice-six-faces-{dice_number}.png"
#         img = pygame.image.load(image_path).convert()
#         new_size = (50, 50)  
#         img = pygame.transform.scale(img, new_size)
#         screen.blit(img, (275, 275))
#         pygame.display.update()
        
#     sound_effect(sound_file)
#     dice_image(screen, dice_number)

#     pygame.time.wait(5000)  
    
#     return dice_number




import random
import pygame
import os

pygame.init()

def dice_roll(screen):
    
    dice_number = random.randint(1, 6)
    base_path = os.path.dirname(__file__)
    sound_file = os.path.join(base_path, "dice_sound.mp3")

    def sound_effect(sound_file):
        
        pygame.mixer.init()
        sound = pygame.mixer.Sound(sound_file)
        sound.set_volume(0.2)
        sound.play()

    def dice_image(screen, dice_number):
        
        image_path = os.path.join(base_path, f"dice-images/dice-six-faces-{dice_number}.png")
        img = pygame.image.load(image_path).convert()
        new_size = (50, 50)  # New size (width, height)
        img = pygame.transform.scale(img, new_size)
        screen.blit(img, (275, 275))
        
        pygame.display.update()

    sound_effect(sound_file)
    dice_image(screen, dice_number)

    pygame.time.wait(2000)
