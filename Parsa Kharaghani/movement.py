import pygame
import dice
import sounds
import visuals
import FirstMenu as fir
import confirmation as conf
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 230, 0)
GREEN = (0, 150, 0)
BIEGE = (200, 174, 126)
LIGHT_GREEN = (144, 238, 144)
LIGHT_RED = (255, 104, 101)
LIGHT_BLUE = (173, 216, 230)
LIGHT_YELLOW = (255, 255, 102)



road_map_x = tuple([40, 90, 140, 190, 240, 240, 240, 240, 240, 300, 
                360, 360, 360, 360, 360, 410, 460, 510, 560,560, 
                560, 510, 460, 410, 360, 360, 360, 360, 360, 300,
                240, 240, 240, 240, 240, 190, 140, 90, 40, 40])

road_map_y = tuple([250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 50,
              100, 150, 200, 250, 250, 250, 250, 250, 300, 350, 350,
              350, 350, 350,400, 450, 500, 550, 550, 550, 500, 450, 
              400, 350,350, 350, 350, 350, 300])

all_cordinates = ((40, 250), (90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50),
              (360, 50), (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
              (560, 350), (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
              (240, 550), (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300))


road_map = {
"red" :[(40, 250), (90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50),
              (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
               (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
               (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300),
              (90, 300), (140, 300), (190, 300), (240, 300)],

"green" : [(360, 50), (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
               (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
              (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300),
              (90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50), 
              (300, 100), (300, 150), (300, 200), (300, 250)],

"yellow" : [(560, 350), (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
               (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300),
               (90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50),
               (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
              (510,300), (460, 300), (410,300), (360, 300)],

"blue" : [(240, 550), (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300),
               (90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50),
              (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
               (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
              (300, 500), (300, 450), (300, 400), (300, 350)]
}

starting_sections = {
    
    "red" :[(50, 40) ,(120, 40),(50, 120) ,(120,120)],
    "blue" : [(50, 560),(120, 560),(50, 480),(120, 480)],
    "green": [(550, 40), (480, 120),(480, 40),(550, 120)],
    "yellow" :[(550, 560),(480, 560), (480, 480),(550 ,480)]    
}



# Player pieces
player_pieces = {
    "red": {"piece1": None, "piece2": None, "piece3": None, "piece4": None},
    "blue": {"piece1": None, "piece2": None, "piece3": None, "piece4": None},
    "green": {"piece1": None, "piece2": None, "piece3": None, "piece4": None},
    "yellow": {"piece1": None, "piece2": None, "piece3": None, "piece4": None}
}

red_counter = -1
green_counter = -1
blue_counter = -1
yellow_counter= -1



updated_info = {
    "red" : {"piece1":(0,0), "piece2":(0,0), "piece3":(0,0), "piece4":(0,0)},
    "green" : {"piece1":(0,0), "piece2":(0,0), "piece3":(0,0), "piece4":(0,0)},
    "blue" : {"piece1":(0,0), "piece2":(0,0), "piece3":(0,0), "piece4":(0,0)},
   "yellow" : {"piece1":(0,0), "piece2":(0,0), "piece3":(0,0), "piece4":(0,0)}
}


def draw_pieces(screen, positions, color):
    
    for pos in positions:
        pygame.draw.circle(screen, color, pos, 15)

def draw_starting_piece(screen, position, color, current_color):
    if current_color == "red" :
        pygame.draw.circle(screen, BIEGE, starting_sections[current_color][red_counter] , 15)
    elif current_color == "green":
        pygame.draw.circle(screen, BIEGE, starting_sections[current_color][green_counter] , 15)
    elif current_color == "blue" :
        pygame.draw.circle(screen, BIEGE, starting_sections[current_color][blue_counter] , 15)
    elif current_color == "yellow" :
        pygame.draw.circle(screen, BIEGE, starting_sections[current_color][yellow_counter] , 15)
        

    pygame.draw.circle(screen, color, position, 15)
    

def ask_move_piece(screen, current_color, piece, dice_number, piece_on_board_ls):
    font = pygame.font.Font(None, 18)
    text_surface = font.render(f" Please select Your piece  ", True, BLACK)
    text_rect = text_surface.get_rect(center=(480, 180))
    screen.fill(BIEGE, text_rect)
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    
    waiting_for_response = True
    response = None
    while waiting_for_response:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    response = "piece1"
                    waiting_for_response = False
                    return waiting_for_response, response
                
                elif event.key == pygame.K_2:
                    response = "piece2"
                    waiting_for_response = False
                    return waiting_for_response, response
                
                elif event.key == pygame.K_3:
                    response = "piece3"
                    waiting_for_response = False
                    return waiting_for_response, response
                
                elif event.key == pygame.K_4:
                    response = "piece4"
                    waiting_for_response = False
                    return waiting_for_response, response
                else :
                    waiting_for_response = True
                    
                
                    
        
        
    # Clear the prompt after response
    screen.fill(BIEGE, text_rect)
    
    

def ask_to_add_piece(screen, color):
    font = pygame.font.Font(None, 26)
    text_surface = font.render(f"Add a {color} piece? (Y)", True, BLACK)
    text_rect = text_surface.get_rect(center=(490, 210))
    screen.blit(text_surface, text_rect)
    pygame.display.update()

    waiting_for_response = True
    response = False
    while waiting_for_response:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    response = True
                    waiting_for_response = False
                else :

                    None_counter = 0
                    for piece in player_pieces[color]:
                        
                        if player_pieces[color][piece]  == None:
                            None_counter += 1
                    
                    if None_counter == 4:
                        pass
                        
                    elif None_counter <= 3:
                    
                        
                        while waiting_for_response:
                            piece_on_board_ls = []
                            for pieces , keys in player_pieces[color].items():
                                if keys is not None:
                                    piece_on_board_ls.append(pieces)
                            waiting_for_response , selected_piece = ask_move_piece(screen, color, piece, 6 , piece_on_board_ls)
                            
                            move_piece(screen, color, selected_piece, 6)






    # Clear the prompt after response
    screen.fill(BIEGE, text_rect)
    
    pygame.display.update()

    return response
    
def attack_check(color, new_loc,screen): 
    if color == "red":
        Current_color = RED
    elif color == "green":
        Current_color = GREEN
    elif color == "blue":
        Current_color = BLUE
    elif color == "yellow":
        Current_color = YELLOW
        
    new_cordinate = road_map[color][new_loc]
    
    print(updated_info)
    print(player_pieces)
    colors_ls =  ["red", "green", "blue", "yellow"]
    colors_ls.remove(color)
    for cl in colors_ls: 
        
        
        for pieces,crds in updated_info[cl].items():
            
            if [new_cordinate] == crds :
                
                print("in attack order")
                updated_info[cl][pieces] = (0,0)
                player_pieces[cl][pieces] = None
                if cl == "red" :
                    global red_counter
                    red_counter -= 1
                elif cl == "green" :
                    global green_counter
                    green_counter -= 1
                elif cl == "blue" :
                    global blue_counter
                    blue_counter -= 1
                elif cl == "yellow" :
                    global yellow_counter
                    yellow_counter -= 1
                    
                pygame.draw.circle(screen,WHITE , new_cordinate , 20)
                
                if cl == "red" :
                    pygame.draw.circle(screen,RED , starting_sections[cl][red_counter] , 20)
                    pygame.draw.circle(screen,Current_color, new_cordinate , 15)
                    
                elif cl == "green":
                    pygame.draw.circle(screen, GREEN, starting_sections[cl][green_counter] , 20)
                    pygame.draw.circle(screen, Current_color, new_cordinate , 15)
                elif cl == "blue" :
                    pygame.draw.circle(screen, BLUE, starting_sections[cl][blue_counter] , 20)
                    pygame.draw.circle(screen, Current_color, new_cordinate , 15)
                    
                elif cl == "yellow" :
                    pygame.draw.circle(screen, YELLOW, starting_sections[cl][yellow_counter] , 20)
                    pygame.draw.circle(screen, Current_color, new_cordinate , 15)
                    break
            
                        
                
                
                
                
                
                
            
            
            

def move_piece(screen, color, piece, dice_number):
    if player_pieces[color][piece] is not None:
          
        if player_pieces[color][piece] == 0 :
            if color == "red" :
                pygame.draw.circle(screen, LIGHT_RED ,road_map[color][player_pieces[color][piece]], 20)
            elif color == "green" : 
                pygame.draw.circle(screen, LIGHT_GREEN,road_map[color][player_pieces[color][piece]], 20)
            elif color == "blue" :
                pygame.draw.circle(screen, LIGHT_BLUE ,road_map[color][player_pieces[color][piece]], 20)
            elif color == "yellow" :
                pygame.draw.circle(screen, LIGHT_YELLOW ,road_map[color][player_pieces[color][piece]], 20)
        else :
            if player_pieces[color][piece] < 37 :
                pygame.draw.circle(screen, WHITE ,road_map[color][player_pieces[color][piece]], 20)
            else : pass
            
        
        
        player_pieces[color][piece] += dice_number
        
        
        
                
       # Ensure the piece's position is within the bounds of the road map
        if player_pieces[color][piece] >= len(road_map[color]):
            player_pieces[color][piece] -= dice_number
                


    try :
        if player_pieces[color][piece] is not None :
            if   player_pieces[color][piece] < 37 :
                if player_pieces["red"][piece] is not None:
                
                
                    updated_info["red"][piece]=[road_map["red"][player_pieces["red"][piece]]]
                
                
                
            
                    draw_pieces(screen, [road_map["red"][player_pieces["red"][piece]]], RED)
            
                if player_pieces["blue"][piece] is not None:
                    
                    updated_info["blue"][piece] = [road_map["blue"][player_pieces["blue"][piece]]]
                    
                    
                    
                    draw_pieces(screen, [road_map["blue"][player_pieces["blue"][piece]]], BLUE)
            
                if player_pieces["green"][piece] is not None:
                    
                    updated_info["green"][piece] = [road_map["green"][player_pieces["green"][piece]]]
                    
                    
                    
                    draw_pieces(screen, [road_map["green"][player_pieces["green"][piece]]], GREEN)
            
                if player_pieces["yellow"][piece] is not None:
                    
                    updated_info["yellow"][piece] = [road_map["yellow"][player_pieces["yellow"][piece]]]
                    
                    
                    
                    draw_pieces(screen, [road_map["yellow"][player_pieces["yellow"][piece]]], YELLOW)
                
                
                attack_check(color, player_pieces[color][piece], screen)
            else : pass
            pygame.display.flip()
    except IndexError :
        pass
        
            
        
def move(screen, dice_number, turn, str_selected_colors) :
    
    current_color = str_selected_colors[turn-1]
    font = pygame.font.Font(None, 26)
    text_surface = font.render((f"Extra Turn"), True, BLACK)
    text_rect = text_surface.get_rect(center=(180, 220))
    
    screen.fill(BIEGE, text_rect)
    
    
    if dice_number == 6:
   
        
        screen.blit(text_surface, text_rect)
       
        for piece in player_pieces[current_color]:
                    if  player_pieces[current_color][piece] == 0 :
                        
                        for piece in player_pieces[current_color]:
                            if player_pieces[current_color][piece] is not None:
                               
                                break
            
        if ask_to_add_piece(screen, current_color, ) and player_pieces[current_color][piece] ==  None:
            for piece in player_pieces[current_color]:
                        
                if player_pieces[current_color][piece] is None :
                    player_pieces[current_color][piece] = 0
                   
                    if current_color == "red":
                        global red_counter 
                        red_counter += 1
                        draw_starting_piece(screen, road_map["red"][0], LIGHT_RED, current_color)
                    elif current_color == "blue":
                        global blue_counter 
                        blue_counter += 1
                        draw_starting_piece(screen, road_map["blue"][0], LIGHT_BLUE, current_color)
                    elif current_color == "green":
                        global green_counter 
                        green_counter += 1
                        draw_starting_piece(screen, road_map["green"][0], LIGHT_GREEN, current_color)
                    elif current_color == "yellow":
                        global yellow_counter 
                        yellow_counter += 1
                        draw_starting_piece(screen, road_map["yellow"][0], LIGHT_YELLOW, current_color)
                    break
        else :
            move_piece(screen, current_color, piece, dice_number)
    else:
        None_counter = 0
        for piece in player_pieces[current_color]:
            
            if player_pieces[current_color][piece]  == None:
                None_counter += 1
       
                
        if None_counter == 4:
            pass
            
        elif None_counter <= 3:
            waiting_for_response = True
            
            while waiting_for_response:
                piece_on_board_ls = []
                for pieces , keys in player_pieces[current_color].items():
                    if keys is not None:
                        piece_on_board_ls.append(pieces)
                waiting_for_response , selected_piece = ask_move_piece(screen, current_color, piece, dice_number, piece_on_board_ls)
                
                move_piece(screen, current_color, selected_piece, dice_number)
            
                
        
                
               
    
 
 
def handle_piece_selection_with_keys(screen, event, color, selected_piece_index, dice_number, flag):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            move_piece(screen, color, "piece1", dice_number)
            flag = True
        elif event.key == pygame.K_2:
            move_piece(screen, color, "piece2", dice_number)
            flag = True
            
        elif event.key == pygame.K_3:
            move_piece(screen, color, 'piece3', dice_number)
            flag = True
        elif event.key == pygame.K_4:
            move_piece(screen, color, 'piece4', dice_number)
            flag = True
            
        else :
            flag = False
       
        return flag
    
    
 

def main(screen, str_selected_colors, click_volume , music_volume):
    running = True
    turn = 1
    dice_number = 0
    pieces = ["piece1", "piece2", "piece3", "piece4"]
    flag = False
    

    
    while running:
       
            
                    
        
        
        
        
                    
                    
        
        current_color = str_selected_colors[turn-1]
        for pieces , index in player_pieces[current_color].items() :
            print(f"{current_color} : {index}")
            print(len(road_map[current_color]) - 1)
            if index == len(road_map[current_color]) - 1 :
                road_map[current_color].pop()
                print(len(road_map[current_color]))
                
        if len(road_map[current_color]) == 37 :
            screen.fill(BIEGE)
            font = pygame.font.Font(None, 80)
            text_surface = font.render(f"{current_color} Win", True, BLACK)
            text_rect = text_surface.get_rect(center=(300, 300))
            screen.blit(text_surface, text_rect)
        elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    WIDTH, HEIGHT = 300, 400
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    fir.Lobby(screen, WIDTH, HEIGHT, click_volume, music_volume)
        
        if flag:
            if dice_number == 6 :
                move(screen, dice_number, turn, str_selected_colors)
                flag = False
                
                
            else :
                move(screen, dice_number, turn, str_selected_colors)
                flag = False
                turn += 1
                if turn == len(str_selected_colors) + 1:
                    turn = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    WIDTH, HEIGHT = 300, 400
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    fir.Lobby(screen, WIDTH, HEIGHT, click_volume, music_volume)
                
                font = pygame.font.Font(None, 26)
                upper_current_color = current_color.upper()
                text_surface = font.render((f"   {upper_current_color}'s Turn   "), True, BLACK)
                text_rect = text_surface.get_rect(center=(300, 20))
                
                screen.fill(BIEGE, text_rect)
                if event.key == pygame.K_SPACE:
                    
                    screen.blit(text_surface, text_rect)
                    
                    
                    dice_number = dice.dice_roll(screen)
                    
                    flag = True
               
                pygame.display.update()

        pygame.display.flip()
        
    
         
    pygame.quit()
