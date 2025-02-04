import pygame

def settings(screen, WIDTH, HEIGHT):
    """صفحه تنظیمات برای کنترل موسیقی"""
    running = True
    volume = 0.5  # حجم اولیه صدای موسیقی
    pygame.mixer.music.set_volume(volume)  # تنظیم اولیه حجم صدا

    font = pygame.font.Font(None, 28)
    bg_color = (223, 198, 153)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # کاهش صدا
                    volume = max(0.0, volume - 0.1)
                    pygame.mixer.music.set_volume(volume)
                if event.key == pygame.K_RIGHT:  # افزایش صدا
                    volume = min(1.0, volume + 0.1)
                    pygame.mixer.music.set_volume(volume)
                if event.key == pygame.K_m:  # قطع موسیقی
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()  # قطع موسیقی
                    else:
                        pygame.mixer.music.unpause()  # ادامه موسیقی
                if event.key == pygame.K_ESCAPE:  # برگشت به صفحه منو با دکمه ESC
                    running = False  # بسته شدن صفحه تنظیمات

        # نمایش تنظیمات
        screen.fill(bg_color)  # رنگ پس‌زمینه تنظیمات
        text = font.render(f"Volume: {int(volume * 100)}%", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 20))

        text = font.render("Press LEFT to decrease, RIGHT to increase, M to mute/unmute", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 40))

        text = font.render("Press ESC to go back to Menu", True, (0, 0, 0))  # پیام برای ESC
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 80))

        pygame.display.update()
