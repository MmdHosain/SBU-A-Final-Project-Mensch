import pygame
import SecondMenu as sec
import visuals

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 230, 0)
GREEN = (0, 150, 0)
BIEGE = (200, 174, 126)
HIGHLIGHT_COLOR = (255, 0, 0)

font = pygame.font.Font(None, 48)

def color_selecting(players_count, bot_count, total, screen, WIDTH, HEIGHT):
    selected_colors = []
    colors = [RED, GREEN, BLUE, YELLOW]
    color_positions = [(100, 50), (200, 50), (100, 150), (200, 150)]
    circle_radius = 35
    selected_option = 0
    selecting_colors = True

    running = True
    while running:
        screen.fill(BIEGE)
        
        # Draw color circles
        for i, color in enumerate(colors):
            color_pos = color_positions[i]
            pygame.draw.circle(screen, color, color_pos, circle_radius)
            if i in selected_colors:
                pygame.draw.line(screen, BLACK, (color_pos[0] - 25, color_pos[1]), (color_pos[0] + 25, color_pos[1]), 4)
                pygame.draw.line(screen, BLACK, (color_pos[0], color_pos[1] - 25), (color_pos[0], color_pos[1] + 25), 4)
            if selecting_colors and i == selected_option:
                pygame.draw.circle(screen, BLACK, color_pos, circle_radius, 2)  # Highlight current selection

        # Draw confirm and back buttons
        confirm_color = HIGHLIGHT_COLOR if not selecting_colors and selected_option == len(colors) else BLACK
        back_color = HIGHLIGHT_COLOR if not selecting_colors and selected_option == len(colors) + 1 else BLACK
        
        confirm_text = font.render("Start Game", True, confirm_color)
        back_text = font.render("Back", True, back_color)
        screen.blit(confirm_text, (75, 250))
        screen.blit(back_text, (75, 320))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if selecting_colors:
                    if event.key == pygame.K_LEFT:
                        selected_option = (selected_option - 1) % len(colors)
                    elif event.key == pygame.K_RIGHT:
                        selected_option = (selected_option + 1) % len(colors)
                    elif event.key == pygame.K_RETURN:
                        if selected_option in selected_colors:
                            selected_colors.remove(selected_option)
                        elif len(selected_colors) < total:
                            selected_colors.append(selected_option)
                        if len(selected_colors) == total:
                            selecting_colors = False
                            selected_option = len(colors)  # Automatically move to the confirm button
                    elif event.key == pygame.K_ESCAPE:
                        return sec.second_menu(screen, WIDTH, HEIGHT)  # Go back to second lobby
                else:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        selected_option = len(colors) + (selected_option - len(colors) + 1) % 2
                    elif event.key == pygame.K_RETURN:
                        if selected_option == len(colors):
                            visuals.board()
                            return selected_colors
                        elif selected_option == len(colors) + 1:
                            selecting_colors = True
                    elif event.key == pygame.K_ESCAPE:
                        selecting_colors = True

        pygame.display.flip()

    pygame.quit()


