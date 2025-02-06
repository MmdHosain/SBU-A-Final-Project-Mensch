import pygame

def how_play():
    pygame.init()       
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("How to Play")

    # Colors
    bg_color = (223, 198, 153)
    BLACK = (0, 0, 0)

    # Font
    font = pygame.font.Font(None, 20)

    # Instructions (as a list)
    instructions = [
        "=== How to Play ===",
        "- Goal: Move all your pieces to the destination.",
        "- Rules:",
        "  1. You must roll a 6 to enter the path.",
        "  2. Move the pieces to the destination squares.",
        "  3. If a piece lands on an opponent's square, the opponent's piece goes back to start.",
        "  4. The game ends when a player fills all 4 destination squares.",
        "",
        "Press ESC to return to the menu."
    ]

    running = True
    while running:
        screen.fill(bg_color)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC key to exit
                    import menu
                    menu.menu()
                    running = False

        # Display instructions on the screen
        y_position = 100
        for line in instructions:
            text = font.render(line, True, BLACK)
            screen.blit(text, (50, y_position))
            y_position += 40  # Spacing between lines

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    how_play()
