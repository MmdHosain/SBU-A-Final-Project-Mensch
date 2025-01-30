


import pygame
import SecondMenu as sec
import how_to_play as howt
import titles
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

def Lobby(screen, WIDTH, HEIGHT ):
    screen.fill(BIEGE)
    
    
    First_menu_options = ["Start", "How To Play", "Exit"]
    
    selected_option = 0
    running = True
    while running:
        
        # calling title printer      
        titles.Main_title(screen, WIDTH )
        
    
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
                        sec.second_menu(screen, WIDTH, HEIGHT)  # Start Game
                    elif selected_option == 1:
                        howt.how_to_play(WIDTH)  # How To Play
                    elif selected_option == 2:
                        running = False
        
        pygame.display.flip()

    pygame.quit()


