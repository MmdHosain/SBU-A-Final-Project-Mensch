import pygame
import FirstMenu as fir
import titles
# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BIEGE = (200, 174, 126)


# font = pygame.font.Font(None, 32)

# def how_to_play(WIDTH):
    
#     WIDTH, HEIGHT = 700, 400
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Mensch")
    
#     running = True
#     while running:
#         screen.fill(BIEGE)
        
#         # How to Play Information
#         instructions = [
#             "How to Play Mensch Game:",
#             "",
#             "1. Each player rolls a dice to move their pieces.",
#             "2. The goal is to move all your pieces to the end.",
#             "3. You can capture opponent's pieces by landing on them.",
#             "4. Captured pieces go back to the start.",
#             "5. The first player to move all pieces to the end wins.",
#             "",
#             "Creator: Parsa Kharaghani"
#         ]
        
#         # Render instructions
#         y_offset = 50
#         for line in instructions:
#             text_surface = font.render(line, True, BLACK)
#             text_rect = text_surface.get_rect(center=(WIDTH // 2, y_offset))
#             screen.blit(text_surface, text_rect)
#             y_offset += 40
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     running = False
#                     WIDTH, HEIGHT = 300, 400
#                     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#                     return fir.Lobby(screen, WIDTH, HEIGHT)
        
#         pygame.display.flip()

#     pygame.quit()



import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
BIEGE = (200, 174, 126)
font = pygame.font.Font(None, 32)

def how_to_play(WIDTH ):
    
    
    WIDTH, HEIGHT = 700, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mensch")
    
    running = True
    while running:
        screen.fill(BIEGE)
        
        #calling ESC title def
        titles.ESC(screen)
        
        
        # How to Play Information
        instructions = [
            "How to Play Mensch Game:",
            "",
            "1. Each player rolls a dice to move their pieces.",
            "2. The goal is to move all your pieces to the end.",
            "3. You can capture opponent's pieces by landing on them.",
            "4. Captured pieces go back to the start.",
            "5. The first player to move all pieces to the end wins.",
            "6. If you want to roll a dice click on D on your keyboard",
            "Creator: Parsa Kharaghani"
        ]
        
        # Render instructions
        y_offset = 100
        for line in instructions:
            text_surface = font.render(line, True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 40
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
       
                    WIDTH, HEIGHT = 300, 400
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    return fir.Lobby(screen, WIDTH, HEIGHT)
                
        pygame.display.flip()

    pygame.quit()



