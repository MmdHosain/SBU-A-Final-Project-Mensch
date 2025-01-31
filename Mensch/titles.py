import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 230, 0)
GREEN = (0, 150, 0)



def ESC(screen) :
    esc_font = pygame.font.Font(None, 36)
    esc_text = "ESC"
    esc_surface_red1 = esc_font.render(esc_text[0], True, RED)
    esc_surface_black = esc_font.render(esc_text[1], True, BLACK)
    esc_surface_red2 = esc_font.render(esc_text[2], True, RED)
    
    screen.blit(esc_surface_red1, (10, 10))
    screen.blit(esc_surface_black, (22, 10))
    screen.blit(esc_surface_red2, (32, 10))
    
    
    
def Main_title(screen, WIDTH ,lobby):
    # Title
    colors = [BLACK,RED, GREEN, BLUE, YELLOW, BLACK]
    title_text = "Mensch"
    
    if lobby == 1 or lobby == 2 :
        title_font = pygame.font.Font(None, 120)
        y_loc = 100
    elif lobby == 0 :
        title_font = pygame.font.Font(None, 120)
        y_loc = 50
    else :
        title_font = pygame.font.Font(None, 80)
        y_loc =350
        

    
   
    for i, color in enumerate(colors):
        title_surface = title_font.render(title_text[i], True, color)
        title_rect = title_surface.get_rect(center=(WIDTH // 2 - 75 + i * 30, y_loc))
        screen.blit(title_surface, title_rect)