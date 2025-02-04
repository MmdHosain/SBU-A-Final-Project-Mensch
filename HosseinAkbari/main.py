import pygame
import random
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60
BG_COLOR = (128, 128, 128)
BG_IMAGE_PATH = "bg.jpg"

# Menu options
MENU_OPTIONS = ["New Game", "How to Play", "Quit", "I'm Feeling Lucky"]
PLAYER_OPTIONS = ["2 Players", "3 Players", "4 Players", "Back to Menu"]
FONT_SIZE = 40


# Initialize Pygame
def init_game():
    pygame.init()
    pygame.font.init()  # Initialize the font module
    pygame.mixer.init()  # Initialize the mixer module
    WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mensch by Hossein Akbari")

    # Load and play background music
    pygame.mixer.music.load("Soghoot.mp3")  # Specify the path to your music file
    pygame.mixer.music.play(-1)  # Play the music in a loop (-1 means infinite loop)

    return WIN


# Load background image
def load_background_image():
    bg_image = pygame.image.load(BG_IMAGE_PATH)
    return pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Draw the game elements
def draw(WIN, bg_image):
    WIN.fill(BG_COLOR)
    WIN.blit(bg_image, (0, 0))
    pygame.display.update()


# Draw the menu
def draw_menu(WIN, selected_option):
    WIN.fill((0, 0, 0))
    font = pygame.font.Font(None, FONT_SIZE)
    for index, option in enumerate(MENU_OPTIONS):
        color = (255, 255, 255) if index == selected_option else (200, 200, 200)
        text = font.render(option, True, color)
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + index * 50)
        )
        WIN.blit(text, text_rect)
    pygame.display.update()


# Draw the player selection menu
def draw_player_selection(WIN, selected_option):
    WIN.fill((0, 0, 0))
    font = pygame.font.Font(None, FONT_SIZE)
    for index, option in enumerate(PLAYER_OPTIONS):
        color = (255, 255, 255) if index == selected_option else (200, 200, 200)
        text = font.render(option, True, color)
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + index * 50)
        )
        WIN.blit(text, text_rect)
    pygame.display.update()


# Define Colors
COLORS = {
    "red": (255, 0, 0),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
}

# Define Font for Text
pygame.font.init()
FONT = pygame.font.Font(None, 43)

# Define Player Home Positions
PLAYER_START_POSITIONS = {
    "red": [(67, 67), (134, 67), (67, 134), (134, 134)],
    "yellow": [(67, 667), (134, 667), (67, 735), (134, 735)],
    "green": [(669, 667), (735, 667), (670, 735), (735, 735)],
    "blue": [(669, 67), (735, 67), (669, 133), (735, 133)],
}


def select_piece_to_move(WIN, player, dice_value):
    selected_piece = 0
    running = True
    while running:
        WIN.fill((0, 0, 0))  # Black background
        font = pygame.font.Font(None, 36)
        text = font.render(f"Dice roll:{dice_value} ", True, (255, 255, 255))
        WIN.blit(text, (400, 400))
        # Draw player's pieces
        for i, pos in enumerate(player.pieces):
            color = (255, 255, 255) if selected_piece == i else (200, 200, 200)
            pygame.draw.circle(WIN, color, pos, 25)
            text = font.render(f"{i + 1}", True, (255, 255, 255))
            WIN.blit(text, (pos[0] - 10, pos[1] + 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_piece = (selected_piece - 1) % 4  # Assuming 4 pieces
                elif event.key == pygame.K_DOWN:
                    selected_piece = (selected_piece + 1) % 4
                elif event.key == pygame.K_SPACE:
                    return selected_piece  # Return the index of the selected piece


# Define Base Path
BASE_PATH = [
    (67, 334),
    (134, 334),
    (201, 334),
    (268, 334),
    (335, 334),
    (335, 267),
    (335, 200),
    (335, 133),
    (335, 66),
    (402, 66),
    (469, 66),
    (469, 133),
    (469, 200),
    (469, 267),
    (469, 334),
    (536, 334),
    (603, 334),
    (670, 334),
    (737, 334),
    (737, 401),
    (737, 468),
    (670, 468),
    (603, 468),
    (536, 468),
    (469, 468),
    (469, 535),
    (469, 602),
    (469, 669),
    (469, 736),
    (400, 736),
    (333, 736),
    (333, 669),
    (333, 602),
    (333, 535),
    (333, 468),
    (266, 468),
    (199, 468),
    (132, 468),
    (65, 468),
    (65, 401),
]

# Define Finishing Paths
PLAYER_FINISH_PATHS = {
    "red": [(134, 401), (201, 401), (268, 401), (335, 401)],
    "yellow": [(400, 669), (400, 602), (400, 535), (400, 468)],
    "green": [(670, 401), (603, 401), (536, 401), (469, 401)],
    "blue": [(402, 133), (402, 200), (402, 267), (402, 334)],
}

# Define Paths for Each Player
PLAYER_PATHS = {
    "red": BASE_PATH[:40] + PLAYER_FINISH_PATHS["red"],
    "yellow": BASE_PATH[30:] + BASE_PATH[:30] + PLAYER_FINISH_PATHS["yellow"],
    "green": BASE_PATH[20:] + BASE_PATH[:20] + PLAYER_FINISH_PATHS["green"],
    "blue": BASE_PATH[10:] + BASE_PATH[:10] + PLAYER_FINISH_PATHS["blue"],
}


# Function to load meme images
def load_meme_images():
    meme_folder = "meme"
    meme_images = []

    # Get a list of all files in the meme folder
    for filename in os.listdir(meme_folder):
        if filename.endswith(
            (".png", ".jpg", ".jpeg", ".webp")
        ):  # Check for image files
            image_path = os.path.join(meme_folder, filename)
            meme_images.append(pygame.image.load(image_path))

    return meme_images


# Function to show a meme image
def show_meme_image(WIN, meme_image):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to return to menu
                    running = False

        WIN.fill((0, 0, 0))  # Black background
        WIN.blit(
            meme_image,
            (
                SCREEN_WIDTH // 2 - meme_image.get_width() // 2,
                SCREEN_HEIGHT // 2 - meme_image.get_height() // 2,
            ),
        )
        pygame.display.update()

    pygame.quit()


# Player Class
class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = [pos for pos in PLAYER_START_POSITIONS[color]]
        self.path_index = [-1, -1, -1, -1]  # -1 means still in home

    def draw(self, WIN):
        for pos in self.pieces:
            pygame.draw.circle(WIN, (0, 0, 0), pos, 31)
            pygame.draw.circle(WIN, COLORS[self.color], pos, 25)

    def move(self, piece_index, steps, players):
        path = PLAYER_PATHS[self.color]
        if self.path_index[piece_index] == -1:  # If piece is in home
            if steps == 6:  # Can only move out on a 6
                self.path_index[piece_index] = 0
                self.pieces[piece_index] = path[0]
        else:
            new_index = self.path_index[piece_index] + steps
            if new_index >= len(path):
                return
            self.path_index[piece_index] = new_index
            self.pieces[piece_index] = path[new_index]

            # Check for captures
            for player in players:
                if player.color != self.color:
                    for i, piece in enumerate(player.pieces):
                        if piece == self.pieces[piece_index]:
                            player.pieces[i] = PLAYER_START_POSITIONS[player.color][i]
                            player.path_index[i] = -1

    def check_win(self):
        finish_path = PLAYER_FINISH_PATHS[self.color]
        return all(piece in finish_path for piece in self.pieces)


# Dice Roll Function
def roll_dice():
    return random.randint(1, 6)


# Function to Draw Text on Board
def draw_text(WIN, text, x, y, color=(255, 255, 255)):
    # Ensure text is a string
    rendered_text = FONT.render(str(text), True, color)
    WIN.blit(rendered_text, (x, y))


# Draw Board Function
def draw_board(WIN, players, current_player, dice_value=None):
    WIN.blit(BOARD_IMAGE, (0, 0))
    for player in players:
        player.draw(WIN)
    turn_text = f"Turn: {players[current_player].color.capitalize()}"
    draw_text(WIN, turn_text, 120, 200, COLORS[players[current_player].color])
    if dice_value is not None:
        dice_text = f"Dice Roll: {dice_value}"
        draw_text(WIN, dice_text, 490, 750, (255, 255, 255))
    pygame.display.update()


# Function to select number of players
def select_number_of_players(WIN):
    selected_option = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(PLAYER_OPTIONS)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(PLAYER_OPTIONS)
                elif event.key == pygame.K_RETURN:
                    if selected_option < 3:  # If selected 2, 3, or 4 players
                        start_game(
                            selected_option + 2, WIN
                        )  # Convert to actual number of players
                    elif selected_option == 3:  # Back to Menu
                        running = False

        draw_player_selection(WIN, selected_option)
        pygame.time.Clock().tick(FPS)


# Main game loop
def main():
    WIN = init_game()
    bg_image = load_background_image()
    clock = pygame.time.Clock()

    # Load meme images
    meme_images = load_meme_images()

    running = True
    selected_option = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(MENU_OPTIONS)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(MENU_OPTIONS)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # New Game
                        select_number_of_players(WIN)
                    elif selected_option == 1:  # How to Play
                        show_how_to_play()
                    elif selected_option == 2:  # Quit
                        running = False
                    elif selected_option == 3:  # I'm Feeling Lucky
                        # Show a random meme image
                        random_meme = random.choice(meme_images)
                        show_meme_image(WIN, random_meme)

        draw_menu(WIN, selected_option)
        clock.tick(FPS)

    pygame.quit()


def show_winner_screen(winner_color):
    WIN = init_game()  # Initialize a new window for the winner screen
    font = pygame.font.Font(None, 74)
    message = f".:{winner_color.capitalize()} WINS!:."

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to quit
                    running = False
                elif event.key == pygame.K_RETURN:  # Press Enter to return to menu
                    running = False

        # Fill the background
        WIN.fill((0, 0, 0))  # Black background
        # Render the winning message
        text = font.render(message, True, (255, 255, 255))  # White text
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        WIN.blit(text, text_rect)

        pygame.display.update()


# Start the game with the selected number of players
def start_game(num_players, WIN):
    print(f"Starting a new game with {num_players} players...")

    global BOARD_IMAGE
    BOARD_IMAGE = pygame.transform.scale(
        pygame.image.load("bg.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    players = [Player("red"), Player("yellow"), Player("green"), Player("blue")][
        :num_players
    ]
    current_player = 0
    dice_value = None

    running = True
    while running:
        draw_board(WIN, players, current_player, dice_value)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Roll dice
                    dice_value = roll_dice()
                    print(
                        f"Player {players[current_player].color} rolled a {dice_value}"
                    )
                    draw_board(WIN, players, current_player, dice_value)

                    # Select a piece to move
                    piece_index = select_piece_to_move(
                        WIN, players[current_player], dice_value
                    )

                    # Move the selected piece
                    players[current_player].move(piece_index, dice_value, players)

                    if players[current_player].check_win():
                        print(f"🎉 {players[current_player].color} WINS!")
                        show_winner_screen(
                            players[current_player].color
                        )  # Show winner screen
                        running = False

                    if dice_value != 6:
                        current_player = (current_player + 1) % num_players

        pygame.time.Clock().tick(30)

    pygame.quit()


# Function to show how to play
def show_how_to_play():
    WIN = init_game()  # Initialize a new window for instructions
    instructions = [
        "How to Play Mensch:",
        "",
        "1. The game is played with 2 to 4 players.",
        "2. Each player has 4 pieces of their color.",
        "3. Players take turns rolling a dice.",
        "4. You can only move a piece out of your home if you roll a 6.",
        "5. Move your pieces along the path to reach the finish area.",
        "6. If you land on a piece of another player, you can capture it.",
        "7. The first player to get all their pieces to the finish area wins.",
        "",
        "Press ESC to quit the game.",
    ]

    font = pygame.font.Font(None, 36)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to quit
                    running = False

        # Fill the background
        WIN.fill((0, 0, 0))  # Black background
        # Draw instructions
        for i, line in enumerate(instructions):
            text = font.render(line, True, (255, 255, 255))  # White text
            text_rect = text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 30)
            )
            WIN.blit(text, text_rect)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
