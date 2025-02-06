import pygame

# تعریف رنگ‌های قابل انتخاب


def choose_colors(num_players):
    COLORS = {
    "Red": (255, 0, 0),
    "Blue": (0, 0, 255),
    "Green": (0, 255, 0),
    "Yellow": (255, 255, 0)
}
    
    # pygame.init()
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Choose Colors")

    bg_color = (223, 198, 153)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 40)

    available_colors = list(COLORS.keys())  # لیست رنگ‌های قابل انتخاب
    selected_colors = []  # رنگ‌هایی که انتخاب شده‌اند
    current_player = 0  # بازیکنی که در حال انتخاب است
    selected_option = 0  # گزینه فعال در انتخاب رنگ

    running = True
    while running:
        screen.fill(bg_color)

        text = font.render(f"Player {current_player + 1}, choose your color:", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 100))

        # نمایش رنگ‌ها
        for i, color_name in enumerate(available_colors):
            color = COLORS[color_name] if i == selected_option else BLACK
            text = font.render(color_name, True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 60))

        # دریافت ورودی‌ها
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(available_colors)
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(available_colors)

                if event.key == pygame.K_RETURN:
                    selected_colors.append(COLORS[available_colors[selected_option]])
                    available_colors.pop(selected_option)

                    if len(selected_colors) == num_players:
                        running = False
                    else:
                        selected_option = 0
                        current_player += 1

        pygame.display.update()

    # pygame.quit()
    return selected_colors
