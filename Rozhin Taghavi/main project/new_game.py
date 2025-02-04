import pygame
import board as board  # فایل صفحه بازی
import choose_color

# def new_game():
#     pygame.init()
#     WIDTH, HEIGHT = 600, 600
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))

#     bg_color = (223, 198, 153)
#     BLACK = (0, 0, 0)
#     BLUE = (0, 0, 255)
#     font = pygame.font.Font(None, 40)

#     menu_options = ["2", "3", "4"]  # انتخاب تعداد بازیکنان
#     selected_option = 0

#     running = True
#     while running:

#         screen.fill(bg_color)
#         text = font.render("Choeese the number of the Players:", True, BLACK)
#         screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 100))


#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_DOWN:
#                     selected_option = (selected_option + 1) % len(menu_options)

#                 if event.key == pygame.K_UP:
#                     selected_option = (selected_option - 1) % len(menu_options)

#                 if event.key == pygame.K_RETURN:
#                     player_count = int(menu_options[selected_option])  # دریافت تعداد بازیکنان
#                     player_colors = choose_color.choose_colors(player_count)  # اجرای انتخاب رنگ
#                     board.board(player_colors)  # ارسال رنگ‌ها به صفحه بازی
#                     running = False

#         for i, option in enumerate(menu_options):
#             color = BLUE if i == selected_option else BLACK
#             text = font.render(str(option), True, color)
#             screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 60))

#         pygame.display.update()

#     pygame.quit()



def new_game():
    pygame.init()
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    bg_color = (223, 198, 153)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    font = pygame.font.Font(None, 40)

    menu_options = ["2", "3", "4"]  # انتخاب تعداد بازیکنان
    selected_option = 0

    running = True
    while running:

        screen.fill(bg_color)
        text = font.render("Choose the number of Players:", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)

                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)

                if event.key == pygame.K_RETURN:
                    player_count = int(menu_options[selected_option])  # دریافت تعداد بازیکنان
                    player_colors = choose_color.choose_colors(player_count)  # اجرای انتخاب رنگ
                    board.board(player_count, player_colors)  # ارسال تعداد بازیکنان و رنگ‌ها به صفحه بازی
                    running = False

        for i, option in enumerate(menu_options):
            color = BLUE if i == selected_option else BLACK
            text = font.render(str(option), True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 60))

        pygame.display.update()

    # pygame.quit()
