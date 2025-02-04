import pygame

# راه‌اندازی میکسر
pygame.mixer.init()

def music():
    """پخش موسیقی به صورت مداوم"""
    if not pygame.mixer.music.get_busy():  # بررسی اینکه آیا موسیقی در حال پخش است یا نه
        pygame.mixer.music.load("ambient-piano-and-strings-10711.mp3")  # نام فایل موسیقی
        pygame.mixer.music.play(-1)  # پخش مداوم موسیقی
