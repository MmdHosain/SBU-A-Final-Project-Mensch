import pygame
import sys
import random

# تنظیمات اولیه
pygame.init()
width, height = 800, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ludo Game")

# رنگ‌ها
cream = (255, 253, 208)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (200, 200, 200)

# مسیرهای بازی
path = [
    (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (5, 4), (4, 4),
    (4, 5), (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 7), 
    (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (4, 9), (4, 10), 
    (5, 10), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (7, 14),
    (8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (9, 10), (10, 10), 
    (10, 9), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (14, 7),
    (14, 6), (13, 6), (12, 6), (11, 6), (10, 6), (10, 5), (10, 4),
    (9, 4), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (7, 0), (6, 0)
]

# مسیرهای پایان برای هر بازیکن
final_paths = {
    "red": [(i, 7) for i in range(1, 5)],
    "blue": [(7, i) for i in range(13, 9, -1)],
    "green": [(i, 7) for i in range(13, 9, -1)],
    "yellow": [(7, i) for i in range(1, 5)]
}

# موقعیت شروع هر رنگ
start_positions = {
    "red": (1, 1),
    "blue": (1, 12),
    "green": (12, 12),
    "yellow": (12, 1)
}

# داده‌های بازیکنان
players = {
    "red": {"pieces": [-1, -1, -1, -1], "start_idx": 0},
    "blue": {"pieces": [-1, -1, -1, -1], "start_idx": 14},
    "green": {"pieces": [-1, -1, -1, -1], "start_idx": 28},
    "yellow": {"pieces": [-1, -1, -1, -1], "start_idx": 42},
}
turns = ["red", "blue", "green", "yellow"]
current_turn = 0

# تاس
dice_number = 1

# رسم صفحه
def draw_board():
    window.fill(cream)
    cell_size = width // 15
    radius = cell_size // 2 - 5

    # رسم مسیر بازی (خانه‌ها به صورت دایره)
    for pos in path:
        center = (pos[1] * cell_size + cell_size // 2, pos[0] * cell_size + cell_size // 2)
        pygame.draw.circle(window, grey, center, radius)
        pygame.draw.circle(window, black, center, radius, 2)

    # رسم مسیرهای پایان با رنگ مناسب
    for color, positions in final_paths.items():
        for pos in positions:
            center = (pos[1] * cell_size + cell_size // 2, pos[0] * cell_size + cell_size // 2)
            pygame.draw.circle(window, eval(color), center, radius)
            pygame.draw.circle(window, black, center, radius, 2)

    # رسم پایگاه‌ها
    for color, pos in start_positions.items():
        for i in range(4):
            row, col = pos[0] + (i // 2), pos[1] + (i % 2)
            center = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
            pygame.draw.circle(window, eval(color), center, radius)
            pygame.draw.circle(window, black, center, radius, 2)

    # رسم مهره‌ها به صورت مربع
    for color, data in players.items():
        for i, piece in enumerate(data["pieces"]):
            if piece == -1:  # مهره هنوز در خانه شروع است
                row, col = start_positions[color]
                center = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
            elif piece is not None and piece >= 0:  # مهره در مسیر
                row, col = path[piece]
                center = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
            else:
                continue  # اگر مهره‌ای نباشد، چیزی رسم نشود
           
            pygame.draw.rect(window, eval(color), (center[0] - radius, center[1] - radius, 2 * radius, 2 * radius))
            pygame.draw.rect(window, black, (center[0] - radius, center[1] - radius, 2 * radius, 2 * radius), 2)

# رسم تاس
def draw_dice():
    dice_size = 100
    dice_rect = pygame.Rect((width // 2 - dice_size // 2, height // 2 - dice_size // 2), (dice_size, dice_size))
    pygame.draw.rect(window, cream, dice_rect)
    pygame.draw.rect(window, black, dice_rect, 5)

    dot_positions = {
        1: [(0, 0)],
        2: [(-25, -25), (25, 25)],
        3: [(-25, -25), (0, 0), (25, 25)],
        4: [(-25, -25), (25, -25), (-25, 25), (25, 25)],
        5: [(-25, -25), (25, -25), (-25, 25), (25, 25), (0, 0)],
        6: [(-25, -25), (25, -25), (-25, 0), (25, 0), (-25, 25), (25, 25)],
    }

    for dx, dy in dot_positions[dice_number]:
        pygame.draw.circle(window, black, (width // 2 + dx, height // 2 + dy), 10)

    return dice_rect

# بررسی برنده
def check_winner():
    for color, data in players.items():
        if all(piece != -1 and piece >= len(path) - 4 for piece in data["pieces"]):
            return color
    return None

# نمایش برنده
def show_winner(winner):
    font = pygame.font.Font(None, 100)
    draw_text(f"{winner.capitalize()} Wins!", font, black, window, width // 2, height // 2)
    pygame.display.flip()
    pygame.time.wait(2000)  # نمایش پیغام برنده به مدت 2 ثانیه
    pygame.quit()
    sys.exit()  # پایان بازی بعد از اعلام برنده

# تابع برای نمایش متن
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# منوی اصلی با گزینه‌ها
def main_menu():
    running = True
    while running:
        window.fill(cream)
        
        # عنوان منو
        draw_text("mench Game", pygame.font.Font(None, 100), black, window, width // 2, height // 4)

        # گزینه‌های منو
        draw_text("New Game", pygame.font.Font(None, 50), black, window, width // 2, height // 2 - 50)
        draw_text("How to Play", pygame.font.Font(None, 50), black, window, width // 2, height // 2)
        draw_text("Exit", pygame.font.Font(None, 50), black, window, width // 2, height // 2 + 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # بررسی کلیک روی گزینه‌ها
                if width // 2 - 100 <= x <= width // 2 + 100:
                    if height // 2 - 75 <= y <= height // 2 - 25:  # New Game
                        run_game()
                    elif height // 2 - 25 <= y <= height // 2 + 25:  # How to Play
                        how_to_play()
                    elif height // 2 + 25 <= y <= height // 2 + 75:  # Exit
                        pygame.quit()
                        sys.exit()

# نمایش قوانین بازی
def how_to_play():
    running = True
    while running:
        window.fill(cream)
        draw_text("How to Play", pygame.font.Font(None, 50), black, window, width // 2, height // 4)

        # نمایش قوانین بازی
        font = pygame.font.Font(None, 30)
        draw_text("1. Each player must move all their pieces to the finish line.", font, black, window, width // 2, height // 3)
        draw_text("2. Players roll the dice to move their pieces.", font, black, window, width // 2, height // 3 + 40)
        draw_text("3. A roll of 6 allows a player to bring a piece into the game.", font, black, window, width // 2, height // 3 + 80)
        draw_text("4. The first player to move all their pieces to the finish line wins.", font, black, window, width // 2, height // 3 + 120)
        draw_text("5. Players take turns rolling the dice.", font, black, window, width // 2, height // 3 + 160)
        
        # پیام برای برگشت به منو
        draw_text("Click to return to the menu", font, black, window, width // 2, height // 2 + 150)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False  # برگشت به منو اصلی

# بازی اصلی
def run_game():
    global dice_number, current_turn
    running = True
    while running:
        window.fill(cream)
        draw_board()
        dice_rect = draw_dice()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if dice_rect.collidepoint(x, y):
                    dice_number = random.randint(1, 6)
                    move_piece()

        winner = check_winner()
        if winner:
            show_winner(winner)
            return

# حرکت مهره‌ها
def move_piece():
    global current_turn
    color = turns[current_turn]
    data = players[color]
    
    for i, piece in enumerate(data["pieces"]):
        if piece == -1 and dice_number == 6:  # ورود به بازی با تاس ۶
            data["pieces"][i] = data["start_idx"]
            break
        elif piece is not None and piece + dice_number < len(path):  # حرکت مهره در مسیر
            data["pieces"][i] += dice_number
            break
    
    current_turn = (current_turn + 1) % len(turns)

main_menu()
