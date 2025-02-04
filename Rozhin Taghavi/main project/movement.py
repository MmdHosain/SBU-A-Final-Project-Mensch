# game_functions.py

import pygame
from dice import roll_dice



red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

def check_winner(player_pieces, start_positions, screen):
    """ بررسی می‌کند که آیا همه ۴ مهره یک بازیکن روی نقاط برنده قرار دارند یا نه """
    winning_positions = {
        (255, 0, 0): [(6, 7), (5, 7), (4, 7), (3, 7)],  # مسیر برنده برای قرمز
        (0, 0, 255): [(7, 3), (7, 4), (7, 5), (7, 6)],  # مسیر برنده برای آبی
        (0, 255, 0): [(11, 7), (10, 7), (9, 7), (8, 7)],  # مسیر برنده برای سبز
        (255, 255, 0): [(7, 8), (7, 9), (7, 10), (7, 11)],  # مسیر برنده برای زرد
    }

    for color, pieces in player_pieces.items():
        # بررسی اینکه آیا همه مهره‌های این رنگ روی نقاط برنده قرار دارند
        if all(pos in pieces for pos in winning_positions[color]):
            if color == red :
                str_current_color = "RED"
            elif color == green :
                str_current_color = "GREEN"
            elif color == blue :
                str_current_color = "BLUE"
            elif color == yellow :
                str_current_color = "YELLOW"
            # نمایش پیغام برنده شدن روی صفحه
            font = pygame.font.Font(None, 40)
            winner_text = font.render(f"PLAYER {str_current_color} WON THE GAME! ", True, black)  # سفید
            screen.blit(winner_text, (screen.get_width() // 2 - winner_text.get_width() // 2, screen.get_height() // 2))
            pygame.display.update()
            pygame.time.wait(2000)  # صبر برای نمایش پیغام به مدت 2 ثانیه
            return color  # بازیکن برنده را برمی‌گرداند

    return None  # اگر هیچ بازیکنی برنده نشده باشد

def move_piece(dx, dy, player_positions, selected_piece_index, current_player_index, player_colors, start_positions, screen):
    current_color = player_colors[current_player_index]  # رنگ بازیکن فعلی
    old_position = player_positions[current_color][selected_piece_index]  # موقعیت قبلی مهره
    new_position = (old_position[0] + dx, old_position[1] + dy)  # موقعیت جدید

    # به‌روزرسانی مکان مهره
    player_positions[current_color][selected_piece_index] = new_position

    # چک کردن برنده شدن پس از هر حرکت
    # winner = check_winner(player_positions, start_positions, screen)
   
    
    # if winner:
    #     print(f" PLAYER {str_current_color} WON THE GAME! ")
    #     pygame.time.delay(2000)  # تاخیر برای نمایش پیغام برنده شدن

    return new_position  # اینو اضافه کن که موقعیت جدید رو برگردونه


def check_collision(player_positions, current_color, new_position, start_positions):
    """ بررسی می‌کند که آیا مهره‌ی دیگری در این موقعیت قرار دارد یا نه.
        اگر مهره‌ای پیدا شد، آن را به خانه‌ی اولیه‌ی خودش برمی‌گرداند. """

    for color, pieces in player_positions.items():
        if color != current_color:  # بررسی فقط روی مهره‌های بازیکنان دیگر
            for i, piece in enumerate(pieces):
                if piece == new_position:  # اگر دو مهره در یک خانه باشند
                    print(f"⚠️ مهره‌ی {color} به خانه‌ی شروع خودش برمی‌گردد!")
                    
                    # پیدا کردن یک خانه‌ی خالی در ناحیه‌ی شروع بازیکن
                    for start_pos in start_positions[color]:
                        if start_pos not in pieces:  # اگر این خانه خالی باشد
                            player_positions[color][i] = start_pos  # مهره را به خانه‌ی جدید بفرست
                            return
