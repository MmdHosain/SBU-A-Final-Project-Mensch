import pygame
import dice
import os

base_path = os.path.dirname(__file__)

def dice_sound_effect():
        
        
    sound_file = os.path.join(base_path, "soundeffects","dice_sound.mp3")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.set_volume(0.2)
    sound.play()

def menu_click_sound_effect(click_volume) :
    sound_file = os.path.join(base_path, "soundeffects","click-sound.wav")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.set_volume(click_volume)
    sound.play()
    
    
def bg_music(status, volume):
    
    base_path = os.path.dirname(__file__)
    sound_file = os.path.join(base_path, "soundeffects", "bg-sound.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.set_volume(volume)
    if status:
        pygame.mixer.music.play(-1) # making music loop