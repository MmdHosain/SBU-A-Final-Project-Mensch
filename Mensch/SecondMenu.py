
import pygame
import FirstMenu as fir
import ThirdMenu as thir
import titles
import sounds


pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)
RED = (230, 0, 0)
BIEGE = (200, 174, 126)
YELLOW = (255, 230, 0)
GREEN = (0, 150, 0)

font = pygame.font.Font(None, 48)
                        
def second_menu(screen, WIDTH, HEIGHT, click_volume , music_volume ):
    
    player_count = 4
    bot_count = 0
    selected_option = 0  # 0 for players, 1 for bots, 2 for confirm, 3 for back

    running = True
    while running:
        screen.fill(BIEGE)
        
        lobby = 2
        titles.Main_title(screen,WIDTH,lobby)
        
        
        # Display player and bot counts
        
        if selected_option == 0 :
            player_color = BLACK
        else :
            player_color = WHITE
        if selected_option == 1 :
            bot_color = BLACK
        else :
            bot_color = WHITE
        
        player_text = font.render(f"Players: {player_count}", True, player_color)
        bot_text = font.render(f"Bots: {bot_count}", True, bot_color)
        screen.blit(player_text, (75, 150))
        screen.blit(bot_text, (75, 200))
        
        
        # Display confirm and back buttons
        if selected_option == 2 :
            confirm_color = GREEN
        else :
            confirm_color = WHITE
        if selected_option == 3:
            back_color= RED
        else :
            back_color = WHITE
        
        confirm_text = font.render("Confirm", True, confirm_color)
        back_text = font.render("Back", True, back_color)
        screen.blit(confirm_text, (75, 250))
        screen.blit(back_text, (75, 300))
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 4
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 4
                elif event.key == pygame.K_RIGHT:
                    if selected_option == 0:
                        if player_count < 4 and player_count + bot_count < 4:
                            player_count += 1
                    elif selected_option == 1:
                        if bot_count < 4 and player_count + bot_count < 4:
                            bot_count += 1
                elif event.key == pygame.K_LEFT:
                    if selected_option == 0:
                        if player_count > 0:
                            player_count -= 1
                    elif selected_option == 1:
                        if bot_count > 0:
                            bot_count -= 1
                elif event.key == pygame.K_RETURN:
                    if selected_option == 2:
                        if player_count + bot_count >= 2: 
                            sounds.menu_click_sound_effect(click_volume)
                            thir.color_selecting(player_count, bot_count, player_count + bot_count ,screen, WIDTH, HEIGHT,click_volume , music_volume)  # Send client to color selecting section
                            return player_count, bot_count  # Confirm selection
                    elif selected_option == 3:
                        sounds.menu_click_sound_effect(click_volume)
                        fir.Lobby(screen, WIDTH, HEIGHT,click_volume , music_volume )  # Go back to first lobby
                        return
                elif event.key == pygame.K_ESCAPE:
                    sounds.menu_click_sound_effect(click_volume)
                    fir.Lobby(screen, WIDTH, HEIGHT,click_volume , music_volume)  # Go back to first lobby
                    return
        
        pygame.display.flip()

    pygame.quit()



