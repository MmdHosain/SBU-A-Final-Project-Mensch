import titles
import pygame
import FirstMenu as fir
import sounds
import os
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 230, 0)
BIEGE = (200, 174, 126)
HIGHLIGHT_COLOR = (255, 0, 0)

font = pygame.font.Font(None, 48)



def option(screen, WIDTH, HEIGHT,click_volume , music_volume):
    
    
    selected_option = 0

    options = [
        "Click Sound Volume: ",
        "Music Volume: ",
        "Back"
    ]

    running = True
    while running:
        screen.fill(BIEGE)

        #calling title
        lobby = 0
        titles.Main_title(screen,WIDTH,lobby)

        titles.ESC(screen)
        
        
        for i, option in enumerate(options):
            if i == 0:
                text = f"{option} {click_volume * 10:.0f}"
            elif i == 1:
                text = f"{option} {music_volume * 10:.0f}"
            else:
                text = option

            color = WHITE if i == selected_option else BLACK
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))
            screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.menu_click_sound_effect(click_volume)
                    
                    running = False
       
                    WIDTH, HEIGHT = 300, 400
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    return fir.Lobby(screen, WIDTH, HEIGHT, click_volume, music_volume)
                
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_LEFT:
                    if selected_option == 0 and click_volume > 0:
                        click_volume = max(0, click_volume - 0.1)
                        sounds.menu_click_sound_effect(click_volume)
                    elif selected_option == 1 and music_volume > 0:
                        music_volume = max(0, music_volume - 0.1)
                        pygame.mixer.music.set_volume(music_volume)
                elif event.key == pygame.K_RIGHT:
                    if selected_option == 0 and click_volume < 1:
                        click_volume = min(1, click_volume + 0.1)
                        sounds.menu_click_sound_effect(click_volume)
                    elif selected_option == 1 and music_volume < 1:
                        music_volume = min(1, music_volume + 0.1)
                        pygame.mixer.music.set_volume(music_volume)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 2:
                        
                        sounds.menu_click_sound_effect(click_volume)
                        
                        WIDTH, HEIGHT = 300, 400
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        pygame.display.set_caption("Mensch")
                        fir.Lobby(screen, WIDTH, HEIGHT,click_volume , music_volume)
                        return
                
                

        pygame.display.flip()

    pygame.quit()

