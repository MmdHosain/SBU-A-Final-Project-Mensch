import pygame
import random
import sys

pygame.init()
def play_background_music():
 pygame.mixer.init()
 pygame.mixer.music.load("/Users/hana/Desktop/uni/BP/mench/music.wav")
 pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mench")


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (200, 200, 0)
GRAY = (150, 150, 150)
LIGHT_RED = (255, 104, 101)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 102)
# home positions
home_positions = {
    "red": [(480, 120), (520, 120), (480, 160), (520, 160)],
    "yellow": [(80, 120), (120, 120), (80, 160), (120, 160)],
    "green": [(80, 460), (120, 460), (80, 500), (120, 500)],
    "blue": [(480, 460), (520, 460), (480, 500), (520, 500)],
}

# مسیر حرکت مهره‌ها (مطابق قوانین استاندارد منچ)
path_positions = [
    (50,250),(100, 250), (150, 250), (200, 250), (250, 250), (250, 200), (250, 150), (250, 100), (250, 50), (300, 50),
    (350, 50), (350, 100), (350, 150), (350, 200), (350, 250), (400, 250), (450, 250), (500, 250), (550, 250), (550, 300),
    (550, 350), (500, 350), (450, 350), (400, 350), (350, 350), (350, 400), (350, 450), (350, 500), (350, 550), (300, 550),
    (250, 550), (250, 500), (250, 450), (250, 400), (250, 350), (200, 350), (150, 350), (100, 350), (50, 350), (50, 300)

]
road = {
    "yellow" : [
    (50, 250), (100, 250), (150, 250), (200, 250), (250, 250), (250, 200), (250, 150), (250, 100), (250, 50), (300, 50),
    (350, 50), (350, 100), (350, 150), (350, 200), (350, 250), (400, 250), (450, 250), (500, 250), (550, 250), (550, 300),
    (550, 350), (500, 350), (450, 350), (400, 350), (350, 350), (350, 400), (350, 450), (350, 500), (350, 550), (300, 550),
    (250, 550), (250, 500), (250, 450), (250, 400), (250, 350), (200, 350), (150, 350), (100, 350), (50, 350), (50, 300),
    (100,300),(150,300),(200,300),(250,300)],


    "red" : [(350, 50), (350, 100), (350, 150), (350, 200), (350, 250), (400, 250), (450, 250), (500, 250), (550, 250), (550, 300),
    (550, 350), (500, 350), (450, 350), (400, 350), (350, 350), (350, 400), (350, 450), (350, 500), (350, 550), (300, 550),
    (250, 550), (250, 500), (250, 450), (250, 400), (250, 350), (200, 350), (150, 350), (100, 350), (50, 350), (50, 300),
    (50, 250), (100, 250), (150, 250), (200, 250), (250, 250), (250, 200), (250, 150), (250, 100), (250, 50), (300, 50),
    (250,50),(200,50),(150,50),(100,50)],
    

    "green" : [(250, 550), (250, 500), (250, 450), (250, 400), (250, 350), (200, 350), (150, 350), (100, 350), (50, 350), (50, 300),
               (50, 250), (100, 250), (150, 250), (200, 250), (250, 250), (250, 200), (250, 150), (250, 100), (250, 50), (300, 50),
    (350, 50), (350, 100), (350, 150), (350, 200), (350, 250), (400, 250), (450, 250), (500, 250), (550, 250), (550, 300),
    (550, 350), (500, 350), (450, 350), (400, 350), (350, 350), (350, 400), (350, 450), (350, 500), (350, 550), (300, 550),
    (300,500),(300,450),(300,400),(300,350)],

    "blue" : [(550, 350), (500, 350), (450, 350), (400, 350), (350, 350), (350, 400), (350, 450), (350, 500), (350, 550), (300, 550),
    (250, 550), (250, 500), (250, 450), (250, 400), (250, 350), (200, 350), (150, 350), (100, 350), (50, 350), (50, 300),
    (50, 250), (100, 250), (150, 250), (200, 250), (250, 250), (250, 200), (250, 150), (250, 100), (250, 50), (300, 50),
    (350, 50), (350, 100), (350, 150), (350, 200), (350, 250), (400, 250), (450, 250), (500, 250), (550, 250), (550, 300),
    (500,300),(450,300),(400,300),(350,300)]
}

#safe path ha ۴
safe_paths = {
    "red": [(300, 100), (300, 150), (300, 200), (300, 250)],  
    "yellow": [(100, 300), (150, 300), (200, 300), (250, 300)], 
    "green": [(300, 500), (300, 450), (300, 400), (300, 350)],  
    "blue": [(500, 300), (450, 300), (400, 300), (350, 300)]  
}


#model mohmmad hosseini
players = {
    "red": [0, 0, 0, 0],
    "yellow": [0, 0, 0, 0],
    "green": [0, 0, 0, 0],
    "blue": [0, 0, 0, 0],
}
colors_ls = ["yellow", "red", "blue", "green"]
turn = 0
current_player = colors_ls[turn]
def draw_board():  
    screen.fill(GRAY)  

#rasm masir sefid
    for pos in path_positions:  
        pygame.draw.circle(screen, WHITE, pos, 20)  

#rasm safe path ha
    for color, path in safe_paths.items():  
        for pos in path:  
            pygame.draw.circle(screen, eval(color.upper()), pos, 20)  

#rasm home position
    pygame.draw.circle(screen, LIGHT_RED, (500, 140), 50)  
    pygame.draw.circle(screen, LIGHT_YELLOW, (100, 140), 50)  
    pygame.draw.circle(screen, LIGHT_GREEN, (100, 480), 50)  
    pygame.draw.circle(screen, LIGHT_BLUE, (500, 480), 50)  

#rasm mohre ha ba shomareh
    font = pygame.font.Font(None, 30)  # taain character baraye shomareh gozari
    for color, pieces in players.items():  
        for i, step in enumerate(pieces):  
            if step == 0:  # hanooz dar khaneh shorou hast
                x, y = home_positions[color][i]  
            elif step <= len(path_positions):  
                x, y = road[color][step - 1]  
            else:  # safe path
                safe_step = step - len(path_positions) - 1  
                if safe_step < len(safe_paths[color]):  
                    x, y = safe_paths[color][safe_step]  
                else:  
                    continue  

# rasm mohre ha 
            pygame.draw.circle(screen, eval(color.upper()), (x, y), 15)  

# rasm shomareh 
            text = font.render(str(i + 1), True, WHITE)  
            text_rect = text.get_rect(center=(x, y))  # markaz kardan
            screen.blit(text, text_rect)  # namayesh shomareh

def roll_dice():
    return random.randint(1, 6)
 #zadan mohreh gheir hamrang   
def check_for_collision(player, piece_index):  
    piece_position = players[player][piece_index]  
    current_position = None  

    if piece_position == 0:  # hanooz dar noghteh shorou 
        return  

    # mohasebe mogheiat feli mohre 
    if piece_position <= len(path_positions):  
        current_position = road[player][piece_position - 1]  
    else:  
        safe_step = piece_position - len(path_positions) - 1  
        if safe_step < len(safe_paths[player]):  
            current_position = safe_paths[player][safe_step]  
    
    # barresi har mohre digar
    for other_color, other_pieces in players.items():  
        if other_color != player:  # faghat gheir hamrang ha 
            for i, step in enumerate(other_pieces):  
                if step > 0:  # agar harekat karde bashad 
                    other_position = None  
                    if step <= len(path_positions):  
                        other_position = road[other_color][step - 1]  
                    else:  
                        safe_step = step - len(path_positions) - 1  
                        if safe_step < len(safe_paths[other_color]):  
                            other_position = safe_paths[other_color][safe_step]  

                    # barresi barkhord 
                    if current_position == other_position:  
                        # bargardandan be home position
                        players[other_color][i] = 0  # harekat be khane shorou
 #barrresi inke aya mohre bazikon mitavanad be mogheiat jadid dar safe path beravad ya kheir:
def can_move_to_safe_path(current_position, new_position, player):  


# barresi mohre haye dar home position
    for index, piece_position in enumerate(players[player]):  
        if piece_position > len(path_positions):  # faghat mohreh haye mojoud dar safe path
            if piece_position == new_position:  
                 
                return current_position == piece_position + 1  
 #barresi inkeh aya mogheiat ba mohre gheir hamrang eshghal shode ya na:
    return True  
def is_position_occupied(position, player):  

    for color, pieces in players.items():  
        if color != player:  
            for piece_position in pieces:  
                if piece_position > 0:  
                    
                    current_position = None  
                    if piece_position <= len(path_positions):  
                        current_position = road[color][piece_position - 1]  
                    else:  
                        safe_step = piece_position - len(path_positions) - 1  
                        if safe_step < len(safe_paths[color]):  
                            current_position = safe_paths[color][safe_step]  

                    if current_position == position:  
                        return True  
    return False  

def move_piece(player, piece_index, steps):  
   #harekat mohre va barres inke aya mogheiat eshghal shode ya kheir
    if players[player][piece_index] == 0 and steps == 6:  
        players[player][piece_index] = 1 
    elif players[player][piece_index] > 0:  
        new_position = players[player][piece_index] + steps  
        
        
        if new_position > len(path_positions) + len(safe_paths[player]):  
            new_position = len(path_positions) + len(safe_paths[player])  

        if new_position <= len(path_positions):  
            position_to_check = road[player][new_position - 1]  
        else:  
            safe_step = new_position - len(path_positions) - 1  
            position_to_check = safe_paths[player][safe_step]  


        if new_position > len(path_positions) and not can_move_to_safe_path(players[player][piece_index], new_position, player):  
            print("this move is not allowed")  
            return  


        if not is_position_occupied(position_to_check, player):  
            players[player][piece_index] = new_position 
            print(f"piece {piece_index + 1} from {player} to {position_to_check}  moved.")  
        else:  
            print(f"position {position_to_check} was already filled<unsuccesfull")


def game_loop():
    global turn, current_playe, dice_result



running = True
dice_result = 0
play_background_music()
def check_winner():  
    for color, pieces in players.items():  
 
        if all(step > len(path_positions) for step in pieces):  
            return color  
    return None  

while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            sys.exit()  

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:  
                pygame.quit()  
                sys.exit()  

            if event.key == pygame.K_SPACE:  
                current_player = colors_ls[turn]  
                turn = (turn + 1) % len(colors_ls)  # Cycle through players  
                dice_result = roll_dice()  

            # Move the selected piece  
            for i in range(4):  
                if event.key == getattr(pygame, f'K_{i + 1}') and dice_result > 0:
                    move_piece(current_player, i, dice_result)  
                    dice_result = 0  # Reset dice after moving  

    # Draw the game board  
    screen.fill(GRAY)  
    draw_board()  

    # Check for winner  
    winner = check_winner()  
    print(winner)
    if winner:  
        font = pygame.font.Font(None, 60)  
        text = font.render(f"{winner.capitalize()} Wins!", True, BLACK)  
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))  # Center the text 
        pygame.display.update()
        pygame.time.delay(6000) 
    else:  
        # Display the dice result  
        font = pygame.font.Font(None, 40)  
        text = font.render(f"Dice: {dice_result}", True, WHITE)  
        screen.blit(text, (450, 550))  

    pygame.display.flip()  
    
# Terminate the program safely  
pygame.quit()  
sys.exit()
 