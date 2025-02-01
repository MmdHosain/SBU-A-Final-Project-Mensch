import pygame
import visuals
import dice
import sounds
import random
road_map_x = tuple([40, 90, 140, 190, 240, 240, 240, 240, 240, 300, 
                360, 360, 360, 360, 360, 410, 460, 510, 560,560, 
                560, 510, 460, 410, 360, 360, 360, 360, 360, 300,
                240, 240, 240, 240, 240, 190, 140, 90, 40, 40])

road_map_y = tuple([250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 50,
              100, 150, 200, 250, 250, 250, 250, 250, 300, 350, 350,
              350, 350, 350,400, 450, 500, 550, 550, 550, 500, 450, 
              400, 350,350, 350, 350, 350, 300])

cordinates = ((40, 250), (90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50),
              (360, 50), (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
              (560, 350), (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
              (240, 550), (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300))

road_map = {
"red" : ((40, 250), (90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50),
              (360, 50), (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
              (560, 350), (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
              (240, 550), (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300),
              (90, 300), (140, 300), (190, 300), (240, 300)),

"green" : ((360, 50), (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
              (560, 350), (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
              (240, 550), (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300),
              (40, 250),(90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50), 
              (300, 100), (300, 150), (300, 200), (300, 250)),

"yellow" : ((560, 350), (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
              (240, 550), (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300),
              (40, 250), (90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50),
              (360, 50), (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
              (510,300), (460, 300), (410,300), (360, 300)),

"blue" : ((240, 550), (240, 500), (240, 450), (240, 400), (240, 350), 
              (190, 350), (140, 350), (90, 350), (40, 350), (40, 300),
              (40, 250), (90, 250), (140, 250), (190, 250), (240, 250), 
              (240, 200), (240, 150), (240, 100), (240, 50), (300, 50),
              (360, 50), (360, 100), (360, 150), (360, 200), (360, 250), 
              (410, 250), (460, 250), (510, 250), (560, 250), (560, 300), 
              (560, 350), (510, 350), (460, 350), (410, 350), (360, 350), 
              (360, 400), (360, 450), (360, 500), (360, 550), (300, 550), 
              (300, 500), (300, 450), (300, 400), (300, 350))
}


# Colors
RED = (230, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 150, 0)
YELLOW = (255, 230, 0)
WHITE = (255, 255, 255)
BIEGE = (200, 174, 126)
LIGHT_RED = (255, 102, 102)
LIGHT_BLUE = (102, 178, 255)
LIGHT_GREEN = (102, 255, 102)
LIGHT_YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)

# Coordinates for the pieces

# Player pieces
player_pieces = {
    "red": {"piece1": None, "piece2": None, "piece3": None, "piece4": None},
    "blue": {"piece1": None, "piece2": None, "piece3": None, "piece4": None},
    "green": {"piece1": None, "piece2": None, "piece3": None, "piece4": None},
    "yellow": {"piece1": None, "piece2": None, "piece3": None, "piece4": None}
}



# def dice_loc(screen_board,):
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_d:
                
                # dice_number = dice.dice_roll(screen_board)
                
                

#                 # print(dice_number)   
               
#         elif .type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#             if 260 <= mouse_pos[0] <= 340 and 260 <= mouse_pos[1] <= 340:
                
#                 dice_number = dice.dice_roll(screen_board)  # use dice by click on it
                
            





def draw_pieces(screen, positions, color):
    for pos in positions:
        pygame.draw.circle(screen, color, pos, 20)

def draw_starting_piece(screen, position, color):
    pygame.draw.circle(screen, color, position, 20)
    pygame.draw.circle(screen, WHITE, position, 10)

def roll_dice():
    return random.randint(1, 6)

def ask_to_add_piece(screen, color):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Add a {color} piece? (Y/N)", True, BLACK)
    text_rect = text_surface.get_rect(center=(300, 300))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

    waiting_for_response = True
    while waiting_for_response:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False

def move_piece(screen, color, piece):
    if player_pieces[color][piece] is not None:
        player_pieces[color][piece] += 1
        if player_pieces[color][piece] >= len(road_map[color]):
            player_pieces[color][piece] = len(road_map[color]) - 1
          # Draw the main board
        for piece in player_pieces["red"]:
            if player_pieces["red"][piece] is not None:
                draw_pieces(screen, [road_map["red"][player_pieces["red"][piece]]], RED)
        for piece in player_pieces["blue"]:
            if player_pieces["blue"][piece] is not None:
                draw_pieces(screen, [road_map["blue"][player_pieces["blue"][piece]]], BLUE)
        for piece in player_pieces["green"]:
            if player_pieces["green"][piece] is not None:
                draw_pieces(screen, [road_map["green"][player_pieces["green"][piece]]], GREEN)
        for piece in player_pieces["yellow"]:
            if player_pieces["yellow"][piece] is not None:
                draw_pieces(screen, [road_map["yellow"][player_pieces["yellow"][piece]]], YELLOW)
        pygame.display.flip()
        
def move(screen, dice_number, turn ) :
    colors = ["red", "green", "blue", "yellow"]
    current_color = colors[turn-1]
    
    if dice_number == 6:
        if ask_to_add_piece(screen, current_color):
            for piece in player_pieces[current_color]:
                if player_pieces[current_color][piece] is None:
                    player_pieces[current_color][piece] = 0
                    if current_color == "red":
                        draw_starting_piece(screen, road_map["red"][0], LIGHT_RED)
                    elif current_color == "blue":
                        draw_starting_piece(screen, road_map["blue"][0], LIGHT_BLUE)
                    elif current_color == "green":
                        draw_starting_piece(screen, road_map["green"][0], LIGHT_GREEN)
                    elif current_color == "yellow":
                        draw_starting_piece(screen, road_map["yellow"][0], LIGHT_YELLOW)
                    break
    else:
        for piece in player_pieces[current_color]:
            if player_pieces[current_color][piece] is not None:
                move_piece(screen, current_color, piece)
                break
def main(screen):
    clock = pygame.time.Clock()

    
    running = True
    
    turn = 1
    dice_number = 0
    
    flag = False

    while running :
        if flag :
            move(screen , dice_number, turn)
            flag = False
            turn += 1
            if turn  == 5: 
                turn = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    dice_number = dice.dice_roll(screen)
                    flag  = True
        
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        #     elif event.type == pygame.KEYDOWN:
        
        #             print(f"Dice rolled: {dice_number}")
        #             if dice_number == 6:
        #                 if ask_to_add_piece(screen, current_color):
        #                     for piece in player_pieces[current_color]:
        #                         if player_pieces[current_color][piece] is None:
        #                             player_pieces[current_color][piece] = 0
        #                             if current_color == "red":
        #                                 draw_starting_piece(screen, road_map["red"][0], LIGHT_RED)
        #                             elif current_color == "blue":
        #                                 draw_starting_piece(screen, road_map["blue"][0], LIGHT_BLUE)
        #                             elif current_color == "green":
        #                                 draw_starting_piece(screen, road_map["green"][0], LIGHT_GREEN)
        #                             elif current_color == "yellow":
        #                                 draw_starting_piece(screen, road_map["yellow"][0], LIGHT_YELLOW)
        #                             break
        #             else:
        #                 for piece in player_pieces[current_color]:
        #                     if player_pieces[current_color][piece] is not None:
        #                         move_piece(screen, current_color, piece)
        #                         break
            
                   
                        
                        
                        
                        
                        

      
        for piece in player_pieces["red"]:
            if player_pieces["red"][piece] is not None:
                draw_pieces(screen, [road_map["red"][player_pieces["red"][piece]]], RED)
        for piece in player_pieces["blue"]:
            if player_pieces["blue"][piece] is not None:
                draw_pieces(screen, [road_map["blue"][player_pieces["blue"][piece]]], BLUE)
        for piece in player_pieces["green"]:
            if player_pieces["green"][piece] is not None:
                draw_pieces(screen, [road_map["green"][player_pieces["green"][piece]]], GREEN)
        for piece in player_pieces["yellow"]:
            if player_pieces["yellow"][piece] is not None:
                draw_pieces(screen, [road_map["yellow"][player_pieces["yellow"][piece]]], YELLOW)

        pygame.display.flip()
        clock.tick(1)  # Control the frame rate

    pygame.quit()

