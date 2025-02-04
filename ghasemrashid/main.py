import pygame
import pygame.mixer
import sys
import random 
import os
pygame.init()
#main screen codes
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo Menu")
#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
DARK_GRAY = (100, 100, 100)
BLUE = (0,200, 255)
RED = (255, 50, 50)
GREEN = (0, 255, 0)
YELLOW = (255,250,00)

font = pygame.font.Font(None, 40)

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, "assets")
ludo_icon= pygame.image.load(os.path.join(assets_dir, "ludo.png"))
background_image = pygame.image.load(os.path.join(assets_dir, "background.jpg"))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
player_color = None

pygame.mixer.init()
dice_roll_sound = pygame.mixer.Sound(os.path.join(assets_dir, "dice-95077.mp3"))
main_sound = pygame.mixer.Sound(os.path.join(assets_dir, "The_Tajik_Boy_Як_ханда_кун_эй_гул_یک_خنده_کن_ای_گل.mp3"))

dice_images = {
    1: pygame.image.load(os.path.join(assets_dir, "dice1.png")),
    2: pygame.image.load(os.path.join(assets_dir, "dice2.png")),
    3: pygame.image.load(os.path.join(assets_dir, "dice3.png")),
    4: pygame.image.load(os.path.join(assets_dir, "dice4.png")),
    5: pygame.image.load(os.path.join(assets_dir, "dice5.png")),
    6: pygame.image.load(os.path.join(assets_dir, "dice6.png"))
}



for i in range(1, 7):
    dice_images[i] = pygame.transform.scale(dice_images[i], (100, 100))


def main_menu():
    main_sound.play(-1)
    main_sound.set_volume(0.2)
    ludo_icon = pygame.image.load(os.path.join(assets_dir, "ludo.png"))
    ludo_icon = pygame.transform.scale(ludo_icon, (100, 100))
    
    selected_option = 0
    options = ["New Game", "How to Play", "Exit"]
    
    while True:
        screen.fill(BLACK)
        screen.blit(ludo_icon, ((WIDTH) // 2 - 50, 100))
        
        font1 = pygame.font.SysFont("Bold", 60)
        colors = [RED, GREEN, BLUE, YELLOW]
        textx = 345
        
        for i, letter in enumerate("Ludo"):
            text = font1.render(letter, True, colors[i])
            screen.blit(text, (textx + (i * 30), 220))
        
        mx, my = pygame.mouse.get_pos()
        
        button_rects = [
            pygame.Rect(300, 290, 200, 50),
            pygame.Rect(300, 390, 200, 50),
            pygame.Rect(300, 490, 200, 50)
        ]
        
        button_colors = [DARK_GRAY] * 3
        button_colors[selected_option] = BLUE
        
        for i, rect in enumerate(button_rects):
            pygame.draw.rect(screen, button_colors[i], rect)
            draw_text(f"{i + 1}. {options[i]}", font, BLACK if i == selected_option else WHITE, screen, 400, rect.y + 25)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint((mx, my)):
                        selected_option = i
                        if selected_option == 0:
                            new_game()
                        elif selected_option == 1:
                            how_to_play_screen()
                        elif selected_option == 2:
                            pygame.quit()
                            sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 3 
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 3 
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        new_game()
                    elif selected_option == 1:
                        how_to_play_screen()
                    elif selected_option == 2:
                        pygame.quit()
                        sys.exit()
        
        pygame.display.update()

def new_game():
    global player_color
    while True:
        screen.fill(BLACK)
        draw_text("Choose Your Color", font, WHITE, screen, WIDTH // 2, 50)
        draw_text("Press 'B' to go back", font, WHITE, screen, WIDTH // 2, HEIGHT - 50)
        draw_text("DEMO version , only 4 Player mode", font, WHITE, screen, WIDTH // 2, HEIGHT - 180)

        mx, my = pygame.mouse.get_pos()
        
        button_radius = 60
        
        blue_button = pygame.Rect(250, 100, 100, 100)
        red_button = pygame.Rect(450, 100, 100, 100)
        green_button = pygame.Rect(250, 250, 100, 100)
        yellow_button = pygame.Rect(450, 250, 100, 100)
        
        pygame.draw.circle(screen, BLUE, (300, 150), button_radius)
        pygame.draw.circle(screen, RED, (500, 150), button_radius)
        pygame.draw.circle(screen, GREEN, (300, 300), button_radius)
        pygame.draw.circle(screen, YELLOW, (500, 300), button_radius)
        
        draw_text("1.Blue", font, WHITE, screen,300, 150)
        draw_text("2.Red", font, WHITE, screen, 500, 150)
        draw_text("3.Green", font, WHITE, screen,300, 300)
        draw_text("4.Yellow", font, WHITE, screen,500, 300)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return  
                elif event.key == pygame.K_1:
                    player_color = BLUE
                    game_screen()
                elif event.key == pygame.K_2:
                    player_color = RED
                    game_screen()
                elif event.key == pygame.K_3:
                    player_color = GREEN
                    game_screen()
                elif event.key == pygame.K_4:
                    player_color = YELLOW
                    game_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if blue_button.collidepoint((mx, my)):
                    player_color = BLUE
                    game_screen()
                if red_button.collidepoint((mx, my)):
                    player_color = RED
                    game_screen()
                if green_button.collidepoint((mx, my)):
                    player_color = GREEN
                    game_screen()
                if yellow_button.collidepoint((mx, my)):
                    player_color = YELLOW
                    game_screen()
        
        pygame.display.update()
def how_to_play_screen():
    while True:
        screen.fill(BLACK)
        
      
        draw_text("How to Play", font, WHITE, screen,400, 50)
        draw_text("Ludo is a popular board game for 2-4 players.", font, WHITE, screen,400, 150)
        draw_text("the goal is to move the pieces around the board.", font, WHITE, screen,400, 200)
        #draw_text("Roll the dice and choose to either move a piece or bring a new piece", font, WHITE, screen, WIDTH // 2, 250)
        draw_text("Press SPACE or click to roll the dice.", font, WHITE, screen,400, 300)
        draw_text("Use 'New Piece' or 'Move Piece' options when rolling a 6", font, WHITE, screen,400, 350)
        #draw_text("Avoid landing on opponents' pieces.", font, WHITE, screen, WIDTH // 2, 400)
        draw_text("The first player to get all their pieces to the center wins!", font, WHITE, screen,400, 450)
        draw_text("subscribe konid", font, WHITE, screen,400, 550)

        
        back_button = pygame.Rect(100,700, 600, 50)
        pygame.draw.rect(screen, GRAY, back_button)
        draw_text("1.Back to Menu", font, WHITE, screen,400,725)

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint((mx, my)):
                    return 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main_menu()
        pygame.display.update()
def game_screen():
    flag=False
    turn=1
    global player_color
    global dice_number
    dice_number = None
    
    while True:
        screen.blit(background_image, (0, 0))
        
        draw_pieces()
        
        dice_button = pygame.Rect((WIDTH // 2 - 35), HEIGHT // 2 - 35, 70, 70)                
        if dice_number is not None:            
            scaled_dice_image = pygame.transform.scale(dice_images[dice_number], (70,70))           
            screen.blit(scaled_dice_image, (WIDTH // 2 - 35, HEIGHT // 2 - 35, 70, 70))
        player_colors = {1: "Red", 2: "Blue", 3: "Green", 4: "Yellow"}
        draw_text(f"Turn: {player_colors[turn]}", font, BLACK, screen, WIDTH //2, 27)
        pygame.display.update()
        if flag:
            piecetogame(turn, dice_number)
            
            winner = check_winner()
            if winner:
                show_winner(winner)
                return 
            flag = False
            turn += 1
            if turn == 5:
                turn = 1              
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and dice_button.collidepoint(event.pos) or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    dice_roll_sound.play()
                    dice_roll_sound.set_volume(1)
                    flag = True
                    
                    dice_number = random.randint(1, 6)


pieces = {'R1': [RED, (50,50), 'rest'], 'R2': [RED, (130,50), 'rest'], 'R3': [RED, (130,130),'rest' ], 'R4': [RED, (50, 130),'rest'], 
          'B1': [BLUE, (WIDTH - 50, 50),'rest'], 'B2': [BLUE, (WIDTH - 130, 50),'rest'], 'B3': [BLUE, (WIDTH - 130, 130),'rest'], 'B4': [BLUE, (WIDTH - 50, 130),'rest'], 
          'G1': [GREEN, (WIDTH - 50, HEIGHT - 50),'rest'], 'G2': [GREEN, (WIDTH - 130, HEIGHT - 50),'rest'], 'G3': [GREEN, (WIDTH - 130, HEIGHT - 130),'rest'], 'G4': [GREEN, (WIDTH - 50, HEIGHT - 130),'rest'], 
          'Y1': [YELLOW, (50, HEIGHT - 50),'rest'], 'Y2': [YELLOW, (130, HEIGHT - 50),'rest'], 'Y3': [YELLOW, (50, HEIGHT - 130),'rest'], 'Y4': [YELLOW, (130, HEIGHT - 130),'rest']}

bluepath=[(467,66),(467,132),(467,198),(467,264),(467,334)
         ,(533,334),(599,334),(665,334),(731,334),(731,400)
         ,(731,466),(665,466),(599,466),(533,466),(466,466)
         ,(466,532),(466,600),(466,666),(466,732),(400,732)
         ,(334,732),(334,666),(334,600),(334,534),(334,468)
         ,(266,468),(200,468),(134,468),(66,468),(66,400)
         ,(66,334),(134,334),(200,334),(266,334),(332,334)
         ,(332,266),(332,200),(332,134),(332,66),(400,66)
         ,(400,134),(400,200),(400,266),(400,334)]

redpath=[(66,334),(134,334),(200,334),(266,334),(332,334)
         ,(332,266),(332,200),(332,134),(332,66),(400,66)
         ,(467,66),(467,132),(467,198),(467,264),(467,334)
         ,(533,334),(599,334),(665,334),(731,334),(731,400)
         ,(731,466),(665,466),(599,466),(533,466),(466,466)
         ,(466,532),(466,600),(466,666),(466,732),(400,732)
         ,(334,732),(334,666),(334,600),(334,534),(334,468)
         ,(266,468),(200,468),(134,468),(66,468),(66,400)
         ,(134,400),(200,400),(266,400),(332,400)]

yellowpath=[(334,732),(334,666),(334,600),(334,534),(334,468)
         ,(266,468),(200,468),(134,468),(66,468),(66,400)
         ,(66,334),(134,334),(200,334),(266,334),(332,334)
         ,(332,266),(332,200),(332,134),(332,66),(400,66)
         ,(467,66),(467,132),(467,198),(467,264),(467,334)
         ,(533,334),(599,334),(665,334),(731,334),(731,400)
         ,(731,466),(665,466),(599,466),(533,466),(466,466)
         ,(466,532),(466,600),(466,666),(466,732),(400,732)
         ,(400,666),(400,600),(400,534),(400,468)]

greenpath=[(731,466),(665,466),(599,466),(533,466),(466,466)
         ,(466,532),(466,600),(466,666),(466,732),(400,732)
         ,(334,732),(334,666),(334,600),(334,534),(334,468)
         ,(266,468),(200,468),(134,468),(66,468),(66,400)
         ,(66,334),(134,334),(200,334),(266,334),(332,334)
         ,(332,266),(332,200),(332,134),(332,66),(400,66)
         ,(467,66),(467,132),(467,198),(467,264),(467,334)
         ,(533,334),(599,334),(665,334),(731,334),(731,400)
         ,(665,400),(600,400),(534,400),(464,400)]

def draw_pieces():
    piece_radius = 20
    font = pygame.font.Font(None, 30)
    
    for piece in pieces:
        color, position, state = pieces[piece]
        pygame.draw.circle(screen, color, position, piece_radius)
        
        
        text_surface = font.render(piece[1], True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=position)
        screen.blit(text_surface, text_rect)
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def piecetogame(turn, dice_number):
    global pieces_list, paths
    temp = 0   
    paths = {"R": redpath, "B": bluepath, "G": greenpath, "Y": yellowpath}
    pieces_list = {"R": ["R1", "R2", "R3", "R4"], 
                   "B": ["B1", "B2", "B3", "B4"], 
                   "G": ["G1", "G2", "G3", "G4"], 
                   "Y": ["Y1", "Y2", "Y3", "Y4"]}

    color_keys = {1: "R", 2: "B", 3: "G", 4: "Y"}
    color_letter = color_keys[turn]
    path = paths[color_letter]
    out_pieces = [p for p in pieces_list[color_letter] if pieces[p][2] == "rest"]
    in_game_pieces = [p for p in pieces_list[color_letter] if pieces[p][2] == "startpoint"]

    valid_pieces = [piece for piece in in_game_pieces if can_move(piece, dice_number, path, in_game_pieces)]

    if dice_number == 6 and out_pieces:
        choice, selected_piece = six_choice_screen(turn, out_pieces, in_game_pieces)

        if choice == "new":
            piece_key = out_pieces[0]
            pieces[piece_key][1] = path[temp]
            pieces[piece_key][2] = "startpoint"
        elif choice == "move" and selected_piece and can_move(selected_piece, dice_number, path, in_game_pieces):
            piece_key = selected_piece
            current_index = path.index(pieces[piece_key][1])
            new_index = min(current_index + dice_number, len(path) - 1)
            new_position = path[new_index]

            
            collided_piece = check_collision(piece_key, new_position)
            if collided_piece:
                
                pieces[collided_piece][1] = get_home_position(collided_piece)
                pieces[collided_piece][2] = "rest"

            pieces[piece_key][1] = new_position

    elif in_game_pieces:
        if not valid_pieces:
            return "skip_turn"
        
        selected_piece = choose_piece_screen(turn, in_game_pieces)
        if selected_piece and can_move(selected_piece, dice_number, path, in_game_pieces):
            piece_key = selected_piece
            current_index = path.index(pieces[piece_key][1])
            new_index = min(current_index + dice_number, len(path) - 1)
            new_position = path[new_index]

            
            collided_piece = check_collision(piece_key, new_position)
            if collided_piece:
                pieces[collided_piece][1] = get_home_position(collided_piece)
                pieces[collided_piece][2] = "rest"

            pieces[piece_key][1] = new_position
    winner = check_winner()
    col = WHITE
    if winner == "Red":
        col = RED
    elif winner == "Blue":
        col = BLUE
    elif winner == "Green":
        col = GREEN
    elif winner == "Yellow":
        col = YELLOW               
    if winner:
        font2 = pygame.font.SysFont("Bold", 100)
        screen.fill(BLACK)
        draw_text(f"{winner} WON!", font2, col, screen, WIDTH // 2, HEIGHT // 2)
        pygame.display.update()
        pygame.time.delay(6000)
        pygame.quit()
        sys.exit()        

    return "continue"


def choose_piece_screen(turn, in_game_pieces):
    selected_piece = None
    paths = {1: redpath, 2: bluepath, 3: greenpath, 4: yellowpath}
    running = True

    mini_width, mini_height = 300,300
    mini_screen = pygame.Surface((mini_width, mini_height))

    player_colors = {1: "Red", 2: "Blue", 3: "Green", 4: "Yellow"}

    while running:
        mini_screen.fill(BLACK)
        draw_text(f"{player_colors[turn]} rolled a {dice_number}!", font, WHITE, mini_screen, mini_width // 2, 30)

        mx, my = pygame.mouse.get_pos()
        piece_buttons = []

        
        valid_pieces = [piece for piece in in_game_pieces if can_move(piece, dice_number, paths[turn], in_game_pieces)]
        
        for i, piece in enumerate(valid_pieces):
            btn_rect = pygame.Rect(mini_width // 2 - 80, 60 + i * 50, 160, 40)
            piece_buttons.append((btn_rect, piece))
            pygame.draw.rect(mini_screen, GRAY, btn_rect)
            draw_text(f"{i+1}. {piece}", font, WHITE, mini_screen, mini_width // 2, 80 + i * 50)

        screen.blit(mini_screen, ((WIDTH - mini_width) // 2, (HEIGHT - mini_height) // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn_rect, piece in piece_buttons:
                    if btn_rect.collidepoint((mx - (WIDTH - mini_width) // 2, my - (HEIGHT - mini_height) // 2)):
                        selected_piece = piece
                        running = False
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_4:
                    index = event.key - pygame.K_1
                    if 0 <= index < len(valid_pieces):
                        selected_piece = valid_pieces[index]
                        running = False

    return selected_piece
def six_choice_screen(turn, out_pieces, in_game_pieces):
    choice = None 
    selected_piece = None 
    running = True
    mini_width, mini_height = 300, 400
    mini_screen = pygame.Surface((mini_width, mini_height))
    player_colors = {1: "Red", 2: "Blue", 3: "Green", 4: "Yellow"}

    
    home_is_empty = not is_home_empty(turn, in_game_pieces)

    while running:
        mini_screen.fill(BLACK)
        draw_text(f"{player_colors[turn]} rolled a 6!", font, WHITE, mini_screen,150, 30)
        draw_text("Choose an option:", font, WHITE, mini_screen,150, 70)
        mx, my = pygame.mouse.get_pos()
        new_piece_button = pygame.Rect(70, 100, 160, 40)
        move_piece_button = pygame.Rect(60, 160, 180, 50)

        
        new_piece_color = BLUE if home_is_empty and new_piece_button.collidepoint((mx, my)) else GRAY
        move_piece_color = RED if move_piece_button.collidepoint((mx, my)) else GRAY

        pygame.draw.rect(mini_screen, new_piece_color, new_piece_button)
        pygame.draw.rect(mini_screen, move_piece_color, move_piece_button)
        draw_text("1.New Piece", font, WHITE, mini_screen,150, 120)
        draw_text("2.Move Piece", font, WHITE, mini_screen,150, 185)

        if choice == "move" and len(in_game_pieces) > 1:
            draw_text("Select a piece:", font, WHITE, mini_screen,150, 235)
            piece_buttons = []
            for i, piece in enumerate(in_game_pieces):
                btn_rect = pygame.Rect(70, 260 + i * 40, 160, 30)
                piece_buttons.append((btn_rect, piece))
                pygame.draw.rect(mini_screen, GRAY, btn_rect)
                draw_text(piece, font, WHITE, mini_screen,150, 275 + i * 40)

        screen.blit(mini_screen, ((WIDTH - mini_width) // 2, (HEIGHT - mini_height) // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and home_is_empty and out_pieces:
                    choice = "new"
                    running = False
                elif event.key == pygame.K_2 and in_game_pieces:
                    choice = "move"
                    if len(in_game_pieces) == 1:
                        selected_piece = in_game_pieces[0]
                        running = False
                elif event.key in range(pygame.K_3, pygame.K_7):
                    index = event.key - pygame.K_3
                    if 0 <= index < len(in_game_pieces):
                        selected_piece = in_game_pieces[index]
                        running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_piece_button.collidepoint((mx - (WIDTH - mini_width) // 2, my - (HEIGHT - mini_height) // 2)) and home_is_empty and out_pieces:
                    choice = "new"
                    running = False
                elif move_piece_button.collidepoint((mx - (WIDTH - mini_width) // 2, my - (HEIGHT - mini_height) // 2)) and in_game_pieces:
                    choice = "move"
                    if len(in_game_pieces) == 1:
                        selected_piece = in_game_pieces[0]
                        running = False
                elif choice == "move":
                    for btn_rect, piece in piece_buttons:
                        if btn_rect.collidepoint((mx - (WIDTH - mini_width) // 2, my - (HEIGHT - mini_height) // 2)):
                            selected_piece = piece
                            running = False
    
    return choice, selected_piece


def can_move(piece, dice_number, path, in_game_pieces):
    piece_position = pieces[piece][1]
    current_index = path.index(piece_position)
    new_index = current_index + dice_number    
    if new_index >= len(path):
        return False
    destination_position = path[new_index]
    for other_piece in in_game_pieces:
        if pieces[other_piece][1] == destination_position and pieces[other_piece][2] == "startpoint":
            if pieces[other_piece][0][0] == pieces[piece][0][0]:
                return False
    return True
def get_home_position(piece_key):
    home_positions = {
        "R": [(50,50), (130,50), (130,130), (50, 130)],
        "B": [(WIDTH - 50, 50), (WIDTH - 130, 50), (WIDTH - 130, 130), (WIDTH - 50, 130)],
        "G": [(WIDTH - 50, HEIGHT - 50), (WIDTH - 130, HEIGHT - 50), (WIDTH - 130, HEIGHT - 130), (WIDTH - 50, HEIGHT - 130)],
        "Y": [(50, HEIGHT - 50), (130, HEIGHT - 50), (50, HEIGHT - 130), (130, HEIGHT - 130)]
    }
    
    color = piece_key[0]  # گرفتن حرف اول برای رنگ
    piece_index = int(piece_key[1]) - 1  # گرفتن شماره مهره (مثلاً "R1" -> 0, "R2" -> 1)
    
    return home_positions[color][piece_index]
def is_home_empty(turn, in_game_pieces):
        
    home_positions = {
        1:(66,334),
        2:(467,66),
        3:(731,466),
        4:(334,732)
    }
    home_position = home_positions[turn]
    
    
    for piece in in_game_pieces:
        if pieces[piece][1] == home_position and pieces[piece][2] == "startpoint":
            return True  
    return False


def check_collision(piece_key, new_position):
    for other_piece, data in pieces.items():
        if other_piece != piece_key and data[1] == new_position:
            if pieces[other_piece][0] != pieces[piece_key][0]:
                return other_piece
    return None
def check_winner():
    red_final = [(134,400),(200,400),(266,400),(332,400)]
    blue_final = [(400,134),(400,200),(400,266),(400,334)]
    yellow_final = [(400,666),(400,600),(400,534),(400,468)]
    green_final = [(665,400),(600,400),(534,400),(464,400)]
    red_pieces = ['R1','R2','R3','R4']
    if all(pieces[p][1] in red_final for p in red_pieces):
         return "Red"
    blue_pieces = ['B1','B2','B3','B4']
    if all(pieces[p][1] in blue_final for p in blue_pieces):
         return "Blue"
    yellow_pieces = ['Y1','Y2','Y3','Y4']
    if all(pieces[p][1] in yellow_final for p in yellow_pieces):
         return "Yellow"
    green_pieces = ['G1','G2','G3','G4']
    if all(pieces[p][1] in green_final for p in green_pieces):
         return "Green"
    
    return None
def show_winner(winner_color):    
    running = True
     
    while running:
        draw_text(f"{winner_color} WON!", font, WHITE , screen, 400,400)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
    main_menu()







                    




main_menu()





