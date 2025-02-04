

import pygame
import sys
from dice import roll_dice, draw_dice
import random
from movement import check_winner, move_piece, check_collision
from music import music


# Initialize pygame


def board(player_count, player_colors):

    # pygame.init()

    # تنظیمات صفحه
    screen_size = 800
    cell_size = screen_size // 15
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Mensch")



    # رنگ‌ها
    bg_color = (223, 198, 153)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    light_red = (255, 182, 193)
    light_blue = (173, 216, 230)
    light_green = (144, 238, 144)
    light_yellow = (255, 255, 224)
    colors = [red, blue, green, yellow]
    colors_light = [light_red, light_blue, light_green, light_yellow]





    start_positions = {
        red: [(1,1), (1,2), (2,1), (2,2)],   # قرمز
        green: [(12,12), (12,13), (13,12), (13,13)], # آبی
        yellow: [(1,12), (1,13), (2,12), (2,13)],   # سبز
        blue: [(12,1), (12,2), (13,1), (13,2)], # زرد
    }




    player_positions = {color: list(start_positions[color]) for color in player_colors}


    current_player_index = 0
    selected_piece_index = 0  # شماره مهره انتخاب شده از ۴ مهره
    player_dice_roll = roll_dice()
    



    def draw_circle(surface, color, position):
        pygame.draw.circle(surface, color, position, cell_size // 2.5)
        pygame.draw.circle(surface, black, position, cell_size // 2.5, 1)


    # تابع رسم مربع به ۴ دایره
    def draw_square_as_circles(surface, color, top_left, size):
        # محاسبه موقعیت‌های چهار گوشه
        positions = [
            (top_left[0] + size // 4, top_left[1] + size // 4),  # گوشه بالا چپ
            (top_left[0] + 3 * size // 4, top_left[1] + size // 4),  # گوشه بالا راست
            (top_left[0] + size // 4, top_left[1] + 3 * size // 4),  # گوشه پایین چپ
            (top_left[0] + 3 * size // 4, top_left[1] + 3 * size // 4),  # گوشه پایین راست
        ]
        
        # رسم دایره‌ها
        for pos in positions:
            draw_circle(surface, color, pos)

    # تابع رسم مثلث
    def draw_triangle(surface, color, points):
        pygame.draw.polygon(surface, color, points)









    def draw_board():
        screen.fill((223, 198, 153))  # رنگ پس‌زمینه

        # خانه‌های ابتدایی
        starting_squares = {
            red: (1, 1),
            blue: (12, 1),
            green: (12, 12),
            yellow: (1, 12),
        }
        
        for color, position in starting_squares.items():
            draw_square_as_circles(screen, bg_color, (position[0] * cell_size, position[1] * cell_size), cell_size * 2)

        # مسیرهای رنگی
        colored_paths = [
            [(x, 7) for x in range(3, 7)],  # قرمز
            [(7, x) for x in range(3, 7)],  # آبی
            [(x, 7) for x in range(8, 12)],  # سبز
            [(7, x) for x in range(8, 12)]  # زرد        
        ]
        for color, path in zip(colors_light, colored_paths):
            for pos in path:
                draw_circle(screen, color, (pos[0] * cell_size + cell_size // 2, pos[1] * cell_size + cell_size // 2))

        
        
        # مسیر سفید (فضای بین مسیرهای رنگی)
        white_path = [
            [(x, 8) for x in range(2, 7)],   # سفید بالا
            [(2,7)],
            [(7,2)],
            [(12,7)],
            [(7,12)],
            [(6, x) for x in range(2, 6)],   # سفید بالا
            [(x, 6) for x in range(8, 13)],  # سفید راست
            [(x,6) for x in range(2, 7)],   # سفید چپ
            [(6, x) for x in range(9, 13)],   # سفید پایین
            [(x, 8) for x in range(8, 13)],  # سفید پایین
            [(8, x) for x in range(2, 6)],   # سفید چپ
            [(8, x) for x in range(9, 13)]   # سفید راست
        ]

        
        for path in white_path:
            for pos in path:
                draw_circle(screen, white, (pos[0] * cell_size + cell_size // 2, pos[1] * cell_size + cell_size // 2))


        colored_circles = [
            [(2,6)],
            [(8,2)],
            [(12,8)],
            [(6,12)]
        ]
        for color, circle in zip(colors_light, colored_circles):
            for pos in circle:
                draw_circle(screen, color, (pos[0] * cell_size + cell_size // 2, pos[1] * cell_size + cell_size // 2))
        

        # مثلث‌ها
        triangle_points = [
            [(2 * cell_size, 4 * cell_size), (4 * cell_size, 5 * cell_size), (2* cell_size, 6* cell_size)],  # مثلث قرمز
            [(9 * cell_size, 2 * cell_size), (10 * cell_size, 4 * cell_size), (11 * cell_size, 2* cell_size)],  # مثلث آبی
            [(13 * cell_size, 9 * cell_size), (11 * cell_size, 10 * cell_size), (13 * cell_size, 11 * cell_size)],  # مثلث سبز
            [(4 * cell_size, 13 * cell_size), (5 * cell_size, 11 * cell_size), (6 * cell_size, 13 * cell_size)]  # مثلث زرد
        ]

        for points in triangle_points:
            draw_triangle(screen, black, points)



        
        
        

        # 🔹 نمایش یک ناحیه برای اطلاعات بازیکن و تاس
        pygame.draw.rect(screen, (255, 255, 255), (screen_size - 180, 10, 170, 50))  # پس‌زمینه‌ی نمایش اطلاعات
        pygame.draw.rect(screen, (0, 0, 0), (screen_size - 180, 10, 170, 50), 2)  # حاشیه‌ی مشکی


    def draw_pieces():
        """ رسم مهره‌های بازیکنان """
        for color, pieces in player_positions.items():
            for i, (x, y) in enumerate(pieces):
                position = (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2)
                pygame.draw.circle(screen, color, position, cell_size // 2.5)
                pygame.draw.circle(screen, black, position, cell_size // 2.5, 1)  # حاشیه مشکی
                
                # اگر این مهره‌ی انتخاب‌شده‌ی بازیکن جاری است، آن را مشخص کنیم
                if color == player_colors[current_player_index] and i == selected_piece_index:
                    pygame.draw.circle(screen, white, position, cell_size // 3, 2)




    

    running = True
    while running:
        screen.fill(bg_color)

        draw_board()
        draw_pieces()
        draw_dice(screen, player_dice_roll, current_player_index, player_colors, screen_size)  
        
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    new_position = move_piece(1, 0, player_positions, selected_piece_index, current_player_index, player_colors, start_positions, screen)
                    check_collision(player_positions, player_colors[current_player_index], new_position, start_positions)
                    winner = check_winner(player_positions, start_positions, screen)

                    if winner:
                        running = False


                elif event.key == pygame.K_LEFT:
                    new_position = move_piece(-1, 0, player_positions, selected_piece_index, current_player_index, player_colors, start_positions, screen)
                    check_collision(player_positions, player_colors[current_player_index], new_position, start_positions)
                    winner = check_winner(player_positions, start_positions, screen)

                    if winner:
                        running = False



                elif event.key == pygame.K_UP:
                    new_position = move_piece(0, -1, player_positions, selected_piece_index, current_player_index, player_colors, start_positions, screen)
                    check_collision(player_positions, player_colors[current_player_index], new_position, start_positions)
                    winner = check_winner(player_positions, start_positions, screen)

                    if winner:
                        running = False



                elif event.key == pygame.K_DOWN:
                    new_position = move_piece(0, 1, player_positions, selected_piece_index, current_player_index, player_colors, start_positions, screen)
                    check_collision(player_positions, player_colors[current_player_index], new_position, start_positions)
                    winner = check_winner(player_positions, start_positions, screen)
                    
                    if winner:
                        running = False



                elif event.key == pygame.K_1:
                    selected_piece_index = 0

                elif event.key == pygame.K_2:
                    selected_piece_index = 1

                elif event.key == pygame.K_3:
                    selected_piece_index = 2

                elif event.key == pygame.K_4:
                    selected_piece_index = 3

                elif event.key == pygame.K_SPACE:  # پایان نوبت
                    
                    if player_dice_roll != 6:
                        current_player_index = (current_player_index + 1) % len(player_colors)
                    player_dice_roll = roll_dice()

                    selected_piece_index = 0

    pygame.quit()
    