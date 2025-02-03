
import pygame
import SecondMenu as sec
import how_to_play as howt
import titles
import sounds
import options


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 230, 0)
GREEN = (0, 150, 0)
BIEGE = (200, 174, 126)
LIGHT_GREEN = (144, 238, 144)
LIGHT_RED = (255, 104, 101)
LIGHT_BLUE = (173, 216, 230)
LIGHT_YELLOW = (255, 255, 102)


menu_font = pygame.font.Font(None, 48)

def Lobby(screen, WIDTH, HEIGHT,click_volume , music_volume ):
    screen.fill(BIEGE)
    
    
    First_menu_options = ["Start", "Option","How To Play", "Exit"]
    
    selected_option = 0
    running = True
    while running:
        
        # calling title printer      
        lobby = 1
        titles.Main_title(screen,WIDTH,lobby)
        
    
        # Render menu options
        for i, option in enumerate(First_menu_options):
            
            if i == selected_option:
                color = BLACK 
            else  :
                color = WHITE
                
            
            text_surface = menu_font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))
            screen.blit(text_surface, text_rect)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(First_menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(First_menu_options)
                elif event.key == pygame.K_RETURN:
                    
                    if selected_option == 0:
                        sounds.menu_click_sound_effect(click_volume)
                        sec.second_menu(screen, WIDTH, HEIGHT, click_volume , music_volume )  # going to next menu
                    elif selected_option == 1:
                        
                        WIDTH, HEIGHT = 400, 300
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        pygame.display.set_caption("Mensch")
                        
                        sounds.menu_click_sound_effect(click_volume)
                        
                        options.option(screen, WIDTH, HEIGHT,click_volume , music_volume) # going to option
                    elif selected_option == 2:
                        sounds.menu_click_sound_effect(click_volume)
                        howt.how_to_play(WIDTH, click_volume, music_volume)  # How To Play
                    elif selected_option == 3:
                        sounds.menu_click_sound_effect(click_volume)
                        running = False
        
        pygame.display.flip()

    pygame.quit()


