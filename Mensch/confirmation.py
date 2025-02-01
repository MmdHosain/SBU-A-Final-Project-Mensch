
# import pygame
# import FirstMenu as fir

# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (230, 0, 0)
# GREEN = (0, 150, 0)
# TRANSPARENT_BLACK = (0, 0, 0, 128)

# def confirm(screen_board, selected_option):
#     # Create a semi-transparent surface
#     overlay = pygame.Surface((screen_board.get_width(), screen_board.get_height()), pygame.SRCALPHA)
    
#     # Draw confirmation box
#     pygame.draw.rect(overlay, BLACK, (150, 200, 300, 200))
#     pygame.draw.rect(overlay, WHITE, (160, 210, 280, 180))

#     font = pygame.font.Font(None, 36)
#     text_surface = font.render("Are you sure you want to exit?", True, BLACK)
#     overlay.blit(text_surface, (180, 230))

#     yes_color = RED if selected_option == 0 else BLACK
#     no_color = GREEN if selected_option == 1 else BLACK

#     yes_surface = font.render("Yes", True, yes_color)
#     no_surface = font.render("No", True, no_color)

#     overlay.blit(yes_surface, (200, 300))
#     overlay.blit(no_surface, (350, 300))

#     # Blit the overlay onto the screen_board
#     screen_board.blit(overlay, (0, 0))
#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     selected_option = (selected_option + 1) % 2
#                 elif event.key == pygame.K_RETURN:
#                     if selected_option == 0:  # Yes
#                         WIDTH, HEIGHT = 300, 400
#                         screen = pygame.display.set_mode((WIDTH, HEIGHT))
#                         pygame.display.set_caption("Mensch")
#                         fir.Lobby(screen, WIDTH, HEIGHT)
#                         return True
#                     elif selected_option == 1:  # No
#                         running = False
#                         return False

#         # Redraw the confirmation box with updated selection
#         pygame.draw.rect(overlay, BLACK, (150, 200, 300, 200))
#         pygame.draw.rect(overlay, WHITE, (160, 210, 280, 180))
#         overlay.blit(text_surface, (180, 230))

#         yes_color = RED if selected_option == 0 else BLACK
#         no_color = GREEN if selected_option == 1 else BLACK

#         yes_surface = font.render("Yes", True, yes_color)
#         no_surface = font.render("No", True, no_color)

#         overlay.blit(yes_surface, (200, 300))
#         overlay.blit(no_surface, (350, 300))

#         screen_board.blit(overlay, (0, 0))
#         pygame.display.flip()

#     pygame.quit()



import pygame
import FirstMenu as fir

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (230, 0, 0)
GREEN = (0, 150, 0)
TRANSPARENT_BLACK = (0, 0, 0, 128)

def confirm(screen_board, selected_option, click_volume,music_volume):
    # Create a semi-transparent surface
    overlay = pygame.Surface((screen_board.get_width(), screen_board.get_height()), pygame.SRCALPHA)
    
    
    # Draw confirmation box
    pygame.draw.rect(overlay, BLACK, (150, 200, 300, 200))
    pygame.draw.rect(overlay, WHITE, (160, 210, 280, 180))

    font = pygame.font.Font(None, 36)
    text_surface = font.render("""Are you sure 
                               you want to exit?""", True, BLACK)
    overlay.blit(text_surface, (180, 230))

    yes_color = RED if selected_option == 0 else BLACK
    no_color = GREEN if selected_option == 1 else BLACK

    yes_surface = font.render("Yes", True, yes_color)
    no_surface = font.render("No", True, no_color)

    overlay.blit(yes_surface, (200, 300))
    overlay.blit(no_surface, (350, 300))

    # Blit the overlay onto the screen_board
    screen_board.blit(overlay, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    selected_option = (selected_option + 1) % 2
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Yes
                        WIDTH, HEIGHT = 300, 400
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        pygame.display.set_caption("Mensch")
                        fir.Lobby(screen, WIDTH, HEIGHT, click_volume, music_volume)
                        return True
                    elif selected_option == 1:  # No
                        return False

        # Redraw the confirmation box with updated selection
        
        pygame.draw.rect(overlay, BLACK, (150, 200, 300, 200))
        pygame.draw.rect(overlay, WHITE, (160, 210, 280, 180))
        overlay.blit(text_surface, (180, 230))

        yes_color = RED if selected_option == 0 else BLACK
        no_color = GREEN if selected_option == 1 else BLACK

        yes_surface = font.render("Yes", True, yes_color)
        no_surface = font.render("No", True, no_color)

        overlay.blit(yes_surface, (200, 300))
        overlay.blit(no_surface, (350, 300))

        screen_board.blit(overlay, (0, 0))
        pygame.display.flip()

    pygame.quit()