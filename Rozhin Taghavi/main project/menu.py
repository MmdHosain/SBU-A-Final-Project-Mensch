import pygame
import new_game
import how_play
from music import music
from setting import settings

def menu():  
    pygame.init()

    # تنظیمات صفحه
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MENSCH")

    # رنگ‌ها
    bg_color = (223, 198, 153)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    # فونت       
    font = pygame.font.Font(None, 40)
    font2 = pygame.font.Font(None, 80)



    # گزینه‌های منو
    menu_options = ["NEW GAME", "HOW TO PLAY", "SETTINGS", "EXIT"]
    selected_option = 0  # گزینه فعال

    running = True
    while running:
        screen.fill(bg_color)
        
        music()
        # دریافت ور ودی‌ها
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)  # حرکت به پایین
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)  # حرکت به بالا
                if event.key == pygame.K_RETURN:  # زدن Enter برای انتخاب


                    if selected_option == 0:
                        new_game.new_game()

                    elif selected_option == 1:
                        how_play.how_play()
                         
                    elif selected_option == 2:
                        settings(screen, WIDTH, HEIGHT) 
                    
                    elif selected_option == 3:
                        running = False
                        


        text = font2.render("MENSCH", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 100))

        # نمایش گزینه‌های منو
        for i, option in enumerate(menu_options):
            color = BLUE if i == selected_option else BLACK  # گزینه فعال آبی باشد
            text = font.render(option, True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 250 + i * 60))

        pygame.display.update()

    # pygame.quit() 
print("komak")
if __name__ == "__main__":
    menu()