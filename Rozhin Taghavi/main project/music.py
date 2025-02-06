import pygame
import os
# راه‌اندازی میکسر
pygame.mixer.init()

def music():
    
    """پخش موسیقی به صورت مداوم"""
    base_path = os.path.dirname(__file__)
    file_name =   os.path.join(base_path,"ambient-piano-and-strings-10711.mp3")
    if not pygame.mixer.music.get_busy():  # بررسی اینکه آیا موسیقی در حال پخش است یا نه
        pygame.mixer.music.load(file_name)  # نام فایل موسیقی
        pygame.mixer.music.play(-1)  # پخش مداوم موسیقی
