import pygame
import FirstMenu as fir
import SecondMenu as sec
import ThirdMenu as thir
import sounds
pygame.init()

# Initialize the screen
font = pygame.font.Font(None, 36)
WIDTH, HEIGHT = 300, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mensch")

#starting the background music
music_status = True
click_volume , music_volume = 0.5 , 0.5
sounds.bg_music(music_status,music_volume)



# Call the Lobby function from FirstMenu

fir.Lobby(screen, WIDTH, HEIGHT,click_volume , music_volume )

# Call the player and bot selector from secondmenu
player_count, bot_count = sec.second_menu(screen, WIDTH, HEIGHT)


# Call the color selector from ThirdMenu
total = player_count + bot_count
selected_colors = thir.color_selecting(player_count, bot_count, total, screen, WIDTH, HEIGHT)


pygame.quit()



