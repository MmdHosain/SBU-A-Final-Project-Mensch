import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mensch Game")

# Load Board Image
BOARD_IMAGE = pygame.transform.scale(pygame.image.load("IM.jpg"), (WIDTH, HEIGHT))

# Define Colors
COLORS = {"red": (255, 0, 0), "yellow": (255, 255, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Define Font for Text
FONT = pygame.font.Font(None, 43)
menu_items = ["1. New Game", "2. How to Play", "3. Exit"]
selected_index = 0

# Menu Game Function
def menu():
    global selected_index
    while True:
        WIN.fill((0, 0, 0))
        title_text = FONT.render("Main Menu", True, (255, 255, 255))
        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        for i, item in enumerate(menu_items):
            color = "yellow" if i == selected_index else WHITE
            menu_text = FONT.render(item, True, color)
            WIN.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, 200 + i * 60))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if menu_items[selected_index] == "1. New Game":
                        return
                    elif menu_items[selected_index] == "2. How to Play":
                        how_to_play()
                    elif menu_items[selected_index] == "3. Exit":
                        pygame.quit()
                        exit()

# How to play
def how_to_play():
    instructions = [
        "How to Play:",
        "1. Press SPACE to roll the dice.",
        "2. Use keys 1-4 to select a piece.",
        "3. Reach the goal with all pieces to win!",
        "4.Press ESC to return to the menu."
    ]
    while True:
        WIN.fill((0, 0, 0))
        for i, line in enumerate(instructions):
            draw_text(line, 50, 100 + i * 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "Menu"

# Select Number of Players
def player_selection():
    options = ["1. 2 Players", "2. 4 Players"]
    selected_option = 0

    while True:
        WIN.fill((0, 0, 0))
        title_text = FONT.render("Select Number of Players", True, (255, 255, 255))
        WIN.blit(title_text, (WIDTH//2 - title_text.get_width() // 2, 100))

        for i, option in enumerate(options):
            color = "yellow" if i == selected_option else WHITE
            option_text = FONT.render(option, True, color)
            WIN.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, 200 + i * 60))    

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return 2 if selected_option == 0 else 4
                elif event.key == pygame.K_ESCAPE:
                    return "Menu"

# Select Colors for Players
def color_selection(player_number):
    chosen_colors = []  # لیست رنگ‌های انتخاب‌شده

    for i in range(player_number):
        colors = [color for color in COLORS.keys() if color not in chosen_colors]
        selected_index = 0

        selecting = True
        while selecting:
            WIN.fill((0, 0, 0))  # پاک کردن صفحه برای جلوگیری از کشیده شدن متن‌ها روی هم

            # نمایش عنوان برای انتخاب رنگ
            title_text = FONT.render(f"Player {i + 1}, Choose Your Color", True, (255, 255, 255))
            WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

            # نمایش رنگ‌ها به صورت لیست
            for j, color in enumerate(colors):
                color_display = COLORS[color] if j == selected_index else GRAY  # تغییر رنگ انتخاب‌شده
                color_text = FONT.render(color.capitalize(), True, color_display)
                WIN.blit(color_text, (WIDTH // 2 - color_text.get_width() // 2, 150 + j * 60))  # تغییر y برای هر رنگ

            pygame.display.update()

            # مدیریت رویدادها
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_index = (selected_index - 1) % len(colors)  # حرکت به بالا
                    elif event.key == pygame.K_DOWN:
                        selected_index = (selected_index + 1) % len(colors)  # حرکت به پایین
                    elif event.key == pygame.K_RETURN:
                        chosen_colors.append(colors[selected_index])  # ذخیره رنگ انتخاب‌شده
                        selecting = False  # پایان انتخاب برای بازیکن فعلی
                    elif event.key == pygame.K_ESCAPE:
                        return []  # بازگشت به منو

    return chosen_colors

# Dice Roll Function
def roll_dice():
    return random.randint(1, 6)

# Function to Draw Text on Board
def draw_text(text, x, y, color = WHITE):
    rendered_text = FONT.render(text, True, color)
    WIN.blit(rendered_text, (x, y))

# Draw Board Function
def draw_board(players, current_player, dice_value = None):
    WIN.blit(BOARD_IMAGE, (0, 0))

    #Draw all players
    for player in players:
        player.draw()
        for i, pos in enumerate(player.pieces):
            draw_text(str(i + 1), pos[0] - 10, pos[1] - 10, WHITE)

    #Show current players's turn
    turn_text = f"Turn: {players[current_player].color.capitalize()}"
    draw_text(turn_text, 120, 200, COLORS[players[current_player].color])

    #Show last rolled dice value
    if dice_value is not None:
        draw_text(f"Dice Roll: {dice_value}", 550, 200, WHITE)

    pygame.display.update()


# Player Class
class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = [pos for pos in PLAYER_START_POSITIONS[color]]
        self.path_index = [-1, -1, -1, -1]  # -1 means still in home

    def draw(self):
        for pos in self.pieces:
            pygame.draw.circle(WIN, (0, 0, 0), pos, 31)
            pygame.draw.circle(WIN, COLORS[self.color], pos, 25)

    def move(self, piece_index, steps, players):
        """ Move a piece along the path, handling captures and finishing paths """
        path = PLAYER_PATHS[self.color]

        if self.path_index[piece_index] == -1:  # if piece is in home
            if steps == 6:  # Can only move out on a 6
                self.path_index[piece_index] = 0
                self.pieces[piece_index] = path[0]
        else:
            new_index = self.path_index[piece_index] + steps

            if new_index >= len(path):
                return
            # بررسی اشغال بودن خانه های رنگی
            target_position = path[new_index]
            for color, start_positions in PLAYER_START_POSITIONS.items():
                if color != self.color and target_position in start_positions:
                    return

            if target_position in PLAYER_FINISH_PATHS[self.color]:
                for player in players:
                    if target_position in player.pieces:
                        return
            else:
                for player in players:
                    if player.color != self.color:
                        for i, piece in enumerate(player.pieces):
                            if piece == target_position:
                                player.pieces[i] = PLAYER_START_POSITIONS[player.color][i]
                                player.path_index[i] = -1
                    
            self.path_index[piece_index] = new_index
            self.pieces[piece_index] = target_position

            if new_index < len(BASE_PATH):
                for player in players:
                    if player.color != self.color:
                        for i, piece in enumerate(player.pieces):
                            if piece == self.pieces[piece_index]:
                                player.pieces[i] = PLAYER_START_POSITIONS[player.color][i]
                                player.path_index[i] = -1

            #Check for captures
            for player in players:
                if player.color != self.color:
                    for i, piece in enumerate(player.pieces):
                        if piece == self.pieces[piece_index]:
                            player.pieces[i] = PLAYER_START_POSITIONS[player.color][i]
                            player.path_index[i] = -1
    def check_win(self):
        """ Check if all pieces are in the finishing area """
        finish_path = PLAYER_FINISH_PATHS[self.color]
        return all(piece in finish_path for piece in self.pieces)

# Display Winner Message Function
def display_winner_message(winner_color):
    WIN.fill((0, 0, 0))  # پاک کردن صفحه

    # پیام تبریک به بازیکن برنده
    winner_text = FONT.render(f"Player {winner_color.capitalize()} Wins!", True, COLORS[winner_color])
    WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2 - 300))

    # پیام برای خروج از بازی
    continue_text = FONT.render("Press ESC to Exit", True, WHITE)
    WIN.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT // 2 - 100))

    pygame.display.update()
    


# Define Player Home Positions
PLAYER_START_POSITIONS = {
    "red": [(67, 67), (134, 67), (67, 134), (134, 134)],
    "yellow": [(67, 667), (134, 667), (67, 735), (134, 735)],
    "green": [(669, 667), (735, 667), (670, 735), (735, 735)],
    "blue": [(669, 67), (735, 67), (669, 133), (735, 133)],
}
# Define Base Path and Player Paths
BASE_PATH = [
    (67, 334), (134, 334), (201, 334), (268, 334), (335, 334), 
    (335, 267), (335, 200), (335, 133), (335, 66), (402, 66),
    (469, 66), (469, 133), (469, 200), (469, 267), (469, 334),
    (536, 334), (603, 334), (670, 334), (737, 334), (737, 401),
    (737, 468), (670, 468), (603, 468), (536, 468), (469, 468),
    (469, 535), (469, 602), (469, 669), (469, 736), (400, 736),
    (333, 736), (333, 669), (333, 602), (333, 535), (333, 468),
    (266, 468), (199, 468), (132, 468), (65, 468), (65, 401),
]  # Last position before finishing paths

# Define Finishing Paths
PLAYER_FINISH_PATHS = {
    "red": [(134, 401), (201, 401), (268, 401), (335, 401)],  
    "yellow": [(400, 669), (400, 602), (400, 535), (400, 468)],
    "green": [(670, 401), (603, 401), (536, 401), (469, 401)],
    "blue": [(402, 133), (402, 200), (402, 267), (402, 334)]
}

# Define Paths for Each Player
PLAYER_PATHS = {
    "red": BASE_PATH[:40] + PLAYER_FINISH_PATHS["red"],  
    "yellow": BASE_PATH[30:] + BASE_PATH[:30] + PLAYER_FINISH_PATHS["yellow"],  
    "green": BASE_PATH[20:] + BASE_PATH[:20] + PLAYER_FINISH_PATHS["green"],  
    "blue": BASE_PATH[10:] + BASE_PATH[:10] + PLAYER_FINISH_PATHS["blue"],  
}


# Main Game Loop
def main():
    menu()
    num_players = player_selection()  # انتخاب تعداد بازیکنان
    player_colors_list = color_selection(num_players)  # انتخاب رنگ بازیکنان
    players = [Player(color) for color in player_colors_list]

    clock = pygame.time.Clock()
    current_player = 0
    dice_value = None
    selected_piece = None
    valid_pieces = []
    running = True
    
    while running:
        draw_board(players, current_player, dice_value)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dice_value is None:
                    dice_value = roll_dice()
                    print(f"Player {players[current_player].color} rolled a {dice_value}")
                    valid_pieces = [
                        i for i in range(4)
                        if players[current_player].path_index[i] == -1 or
                        (
                            players[current_player].path_index[i] + dice_value < len(PLAYER_PATHS[players[current_player].color]) and
                            (
                                PLAYER_PATHS[players[current_player].color][players[current_player].path_index[i] + dice_value] not in [
                                    pos for color, positions in PLAYER_START_POSITIONS.items() if color != players[current_player].color for pos in positions
                                ] and
                                (
                                    PLAYER_PATHS[players[current_player].color][players[current_player].path_index[i] + dice_value] not in [
                                        pos for player in players for pos in player.pieces
                                    ] if PLAYER_PATHS[players[current_player].color][players[current_player].path_index[i] + dice_value] in PLAYER_FINISH_PATHS[players[current_player].color]
                                    else True
                                )
                            )
                        )
                    ]
                    if not valid_pieces:
                        draw_board(players, current_player, dice_value)
                        pygame.display.update()
                        pygame.time.delay(1500)
                        dice_value = None
                        current_player = (current_player + 1) % num_players

                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    index = event.key - pygame.K_1
                    if index in valid_pieces:
                        selected_piece = index

                elif event.key == pygame.K_RETURN and selected_piece is not None:
                    players[current_player].move(selected_piece, dice_value, players)

                    if players[current_player].check_win():
                        winner_color = players[current_player].color
                        print(f"Player {winner_color} wins!")
                        display_winner_message(winner_color)

                        waiting = True
                        while waiting:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    waiting = False
                                    running = False
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                    waiting = False
                                    running = False


                    selected_piece = None
                    valid_pieces = []

                    if dice_value != 6:
                        current_player = (current_player + 1) % num_players

                    dice_value = None
                    
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()