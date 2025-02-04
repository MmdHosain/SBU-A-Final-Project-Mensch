import pygame  
import sys  
import os  


# Initialize Pygame  
pygame.init()  

# Screen settings  
WIDTH, HEIGHT = 600, 600  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption('Mensch Game Menu')  
font = pygame.font.SysFont("bold", 30)  

# Colors  
WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)  
GREEN = (0, 255, 0)  
GREY = (200, 200, 200)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 102)  

# Button class to create buttons  
class Button:  
    def __init__(self, text, x, y, width, height):  
        self.text = text  
        self.rect = pygame.Rect(x, y, width, height)  

    def draw(self, surface):  
        pygame.draw.rect(surface, LIGHT_YELLOW, self.rect)  
        draw_text(self.text, font, BLACK, surface, self.rect.x + 20, self.rect.y + 10)  

# Function to display text  
def draw_text(text, font, color, surface, x, y):  
    textobj = font.render(text, True, color)  
    textrect = textobj.get_rect()  
    textrect.topleft = (x, y)  
    surface.blit(textobj, textrect)  

# Function to start the game  
def start_game():  
    os.system('python menschfinal.py')  
    pygame.quit()  
    sys.exit()  

# Function to show rules  
def show_rules():  
    rules_screen = True  
    while rules_screen:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                rules_screen = False  

        screen.fill(LIGHT_GREEN)  
        draw_text("Rules of the mensch game:", font, BLACK, screen, 120, 35)  
        rules = [  
        "mensch is a board game where",
"players must use dice",  
"to move their pieces"
"to the finishing area.", 
"The goal is to get your",
"pieces home before the other players.", 
"On each turn, players roll dice", 
"and move based on the dice number.",  
"If a player lands on another",
"player's piece, the opponent's piece", 
"returns to its starting position.", 
"note:the game starts with yellow then red",
"then blue then green.", 
"Press Enter to return to the menu...",
        ]  
        for i, rule in enumerate(rules):  
            draw_text(rule, font, BLACK, screen, 120, 70 + i * 40)  

        pygame.display.flip()  
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_RETURN]:  
            rules_screen = False  

# Main menu function  
def main_menu():  
    start_button = Button("Start Game", 170, 200, 250, 50)  
    rules_button = Button("How to Play", 170, 270, 250, 50)  
    exit_button = Button("Exit", 170, 340, 250, 50)  

    while True:  
        screen.fill(LIGHT_GREEN)  
        draw_text("Mench Game Menu:", font, BLACK, screen, 30, 20)  

        # Draw buttons  
        start_button.draw(screen)  
        rules_button.draw(screen)  
        exit_button.draw(screen)  

        pygame.display.flip()  

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()  
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if start_button.rect.collidepoint(event.pos):  
                    start_game()  
                elif rules_button.rect.collidepoint(event.pos):  
                    show_rules()  
                elif exit_button.rect.collidepoint(event.pos):  
                    pygame.quit()  
                    sys.exit()  
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_1:  
                    start_game()  
                elif event.key == pygame.K_2:  
                    show_rules()  
                elif event.key == pygame.K_3:  
                    pygame.quit()  
                    sys.exit()  

 
main_menu()