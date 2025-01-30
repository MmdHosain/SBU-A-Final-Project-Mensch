# import pygame
# import FirstMenu as fir


# #colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (230, 0, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 230, 0)
# GREEN = (0, 150, 0)


# def confirm (screen_board,confirm_exit, selected_option) :
#     running = True
#     while running :
#         if confirm_exit:
#             # Draw confirmation box
#             pygame.draw.rect(screen_board, BLACK, (150, 200, 300, 200))
#             pygame.draw.rect(screen_board, WHITE, (160, 210, 280, 180))

#             font = pygame.font.Font(None, 36)
#             text_surface = font.render("Are you sure you want to exit?", True, BLACK)
#             screen_board.blit(text_surface, (180, 230))

#             yes_color = RED if selected_option == 0 else BLACK
#             no_color = GREEN if selected_option == 1 else BLACK

#             yes_surface = font.render("Yes", True, yes_color)
#             no_surface = font.render("No", True, no_color)

#             screen_board.blit(yes_surface, (200, 300))
#             screen_board.blit(no_surface, (350, 300))

import pygame
import FirstMenu as fir

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (230, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 230, 0)

def confirm(screen_board, selected_option, WIDTH, HEIGHT):
    
   
      
        # Draw confirmation box
        pygame.draw.rect(screen_board, BLACK, (150, 200, 300, 200))
        pygame.draw.rect(screen_board, WHITE, (160, 210, 280, 180))

        font = pygame.font.Font(None, 36)
        text_surface = font.render("""Are you sure   
                                    you want to exit?""", True, BLACK)
        screen_board.blit(text_surface, (180, 230))

        yes_color = RED if selected_option == 0 else BLACK
        no_color = GREEN if selected_option == 1 else BLACK

        yes_surface = font.render("Yes", True, yes_color)
        no_surface = font.render("No", True, no_color)

        screen_board.blit(yes_surface, (200, 300))
        screen_board.blit(no_surface, (350, 300))

        pygame.display.flip()

pygame.quit()