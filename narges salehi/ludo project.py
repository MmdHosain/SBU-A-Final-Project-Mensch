import pygame
import sys
from pygame import mixer
import random
import time
import json

# Initializing pygame
pygame.init()
pygame.display.set_caption("Ludo Game")
screen = pygame.display.set_mode((680, 600))

# Loading Images
board = pygame.image.load('Board.jpg')
star = pygame.image.load('star.png')
one = pygame.image.load('1.png')
two = pygame.image.load('2.png')
three = pygame.image.load('3.png')
four = pygame.image.load('4.png')
five = pygame.image.load('5.png')
six = pygame.image.load('6.png')

red = pygame.image.load('red.png')
blue = pygame.image.load('blue.png')
green = pygame.image.load('green.png')
yellow = pygame.image.load('yellow.png')

DICE = [one, two, three, four, five, six]
color = [red, green, yellow, blue]

# Loading Sounds
killSound = mixer.Sound("Killed.wav")
tokenSound = mixer.Sound("Token Movement.wav")
diceSound = mixer.Sound("Dice Roll.wav")
winnerSound = mixer.Sound("Reached Star.wav")

# Initializing Variables
number = 1
currentPlayer = 0
playerKilled = False
diceRolled = False
winnerRank = []
num_players = 4  # Default number of players

# Rendering Text
font = pygame.font.Font('freesansbold.ttf', 11)
FONT = pygame.font.Font('freesansbold.ttf', 16)
currentPlayerText = font.render('Current Player', True, (0, 0, 0))
line = font.render('------------------------------------', True, (0, 0, 0))

# Initial settings
settings = {
    "sound": 50,  # Volume (0-100)
    "players": 2,  # Number of players
    "bots": 0,  # Number of bots
    "start_number": 6  # Starting number (1 or even)
}

# Sound control
def set_sound(volume):
    mixer.music.set_volume(volume / 100.0)

# Save and load settings
def save_settings():
    with open("settings.json", "w") as f:
        json.dump(settings, f)

def load_settings():
    global settings
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
    except FileNotFoundError:
        save_settings()


HOME = [[(110, 58), (61, 107), (152, 107), (110, 152)],  # Red
        [(466, 58), (418, 107), (509, 107), (466, 153)],  # Green
        [(466, 415), (418, 464), (509, 464), (466, 510)],  # Yellow
        [(110, 415), (61, 464), (152, 464), (110, 510)]]  # Blue

# Red      # Green    # Yellow    # Blue
SAFE = [(50, 240), (328, 50), (520, 328), (240, 520),
        (88, 328), (240, 88), (482, 240), (328, 482)]

position = [[[110, 58], [61, 107], [152, 107], [110, 152]],  # Red
            [[466, 58], [418, 107], [509, 107], [466, 153]],  # Green
            [[466, 415], [418, 464], [509, 464], [466, 510]],  # Yellow
            [[110, 415], [61, 464], [152, 464], [110, 510]]]  # Blue

jump = {(202, 240): (240, 202),  # R1 -> G3
        (328, 202): (368, 240),  # G1 -> Y3
        (368, 328): (328, 368),  # Y1 -> B3
        (240, 368): (202, 328)}  # B1 -> R3

# Red        # Green     # Yellow    # Blue
WINNER = [[240, 284], [284, 240], [330, 284], [284, 330]]

def move_token(x, y):
    global currentPlayer, diceRolled, playerKilled, num_players  # Added num_players to global

    # Check if token is in HOME and rolled 6
    if tuple(position[x][y]) in HOME[x] and number == 6:
        position[x][y] = list(SAFE[x * 2])
        tokenSound.play()
        diceRolled = False
        return

    # Main movement logic
    temp_pos = position[x][y].copy()
    for _ in range(number):
        # Check for jump points
        if tuple(temp_pos) in jump:
            temp_pos = list(jump[tuple(temp_pos)])
            continue

        # Movement based on player color
        if x == 0:  # Red
            if temp_pos[1] == 240 and temp_pos[0] < 328:
                temp_pos[0] += 38
            elif temp_pos[0] == 328 and temp_pos[1] > 240:
                temp_pos[1] -= 38
            else:
                temp_pos[0] += 38

        elif x == 1:  # Green
            if temp_pos[0] == 240 and temp_pos[1] < 328:
                temp_pos[1] += 38
            elif temp_pos[1] == 328 and temp_pos[0] > 240:
                temp_pos[0] -= 38
            else:
                temp_pos[1] += 38

        elif x == 2:  # Yellow
            if temp_pos[1] == 240 and temp_pos[0] > 240:
                temp_pos[0] -= 38
            elif temp_pos[0] == 240 and temp_pos[1] < 240:
                temp_pos[1] += 38
            else:
                temp_pos[0] -= 38

        elif x == 3:  # Blue
            if temp_pos[0] == 328 and temp_pos[1] > 240:
                temp_pos[1] -= 38
            elif temp_pos[1] == 240 and temp_pos[0] < 328:
                temp_pos[0] += 38
            else:
                temp_pos[1] -= 38

    # Check for collisions with other players' tokens
    playerKilled = False
    for p in range(num_players):  # Changed from range(4) to num_players
        if p == x:
            continue
        for t in range(4):
            if position[p][t] == temp_pos:
                position[p][t] = list(HOME[p][t])
                playerKilled = True
                killSound.play()

    # Update position
    position[x][y] = temp_pos 
    tokenSound.play()

    # Check for winner
    if position[x][y] == WINNER[x]:
        winnerSound.play()

    # Switch player if not 6
    if number != 6:
        diceRolled = False
        currentPlayer = (currentPlayer + 1) % num_players  # Use num_players here as well
    else:
        diceRolled = True  # Allow another roll for 6

# Check if Token Can Move to Home
def to_home(player, token_index):
    global position

    # Check if the token is in the winning area
    if position[player][token_index] in WINNER:
        return True
    return False

# Draw Menu
def draw_menu(selected_option):
    screen.fill((250, 160, 180))
    title_text = FONT.render('Ludo Game', True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(680 // 2, 150))
    screen.blit(title_text, title_rect)

    menu_options = ['New Game', 'How to Play', 'Exit']
    for index, option in enumerate(menu_options):
        if selected_option == index:
            text = FONT.render(option, True, (255, 255, 0))
        else:
            text = FONT.render(option, True, (255, 255, 255))
        text_rect = text.get_rect(center=(680 // 2, 250 + index * 50))
        screen.blit(text, text_rect)
    pygame.display.flip()

# Show Instructions
def show_instructions():
    screen.fill((250, 160, 180))
    instructions_text = FONT.render('How to Play', True, (255, 255, 255))
    instructions_rect = instructions_text.get_rect(center=(680 // 2, 150))
    screen.blit(instructions_text, instructions_rect)

    instruction_details = [
        "- Goal: Move all your pieces to the destination.",
        "- Rules:",
        "  1. You must roll a 6 to enter the path.",
        "  2. Move the pieces to the destination squares.",
        "  3. If a piece lands on an opponent's square, the opponent's piece goes back to start.",
        "  4. The game ends when a player fills all 4 destination squares.",
    ]

    for i, line in enumerate(instruction_details):
        instruction_text = FONT.render(line, True, (0, 0, 0))
        instruction_rect = instruction_text.get_rect(center=(680 // 2, 250 + i * 40))
        screen.blit(instruction_text, instruction_rect)

    back_text = FONT.render('Press Enter to Back', True, (0, 0, 0))
    back_rect = back_text.get_rect(center=(680 // 2, 450))
    screen.blit(back_text, back_rect)
    pygame.display.flip()

# Select Number of Players
def select_players():
    global num_players   
    selected_option = 0
    in_selection = True
    while in_selection:
        screen.fill((250, 160, 180))
        title_text = FONT.render('Select Number of Players', True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(680 // 2, 150))
        screen.blit(title_text, title_rect)

        options = ['2 Players', '3 Players', '4 Players']
        for i, opt in enumerate(options):
            if i == selected_option:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)
            text = FONT.render(opt, True, color)
            rect = text.get_rect(center=(680 // 2, 250 + i * 60))
            screen.blit(text, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 3
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 3
                elif event.key == pygame.K_RETURN:
                    num_players = selected_option + 2
                    return

# Start New Game
def start_new_game():
    global currentPlayer, winnerRank, num_players, position, color
    currentPlayer = 0
    winnerRank = []

    # Reset positions based on active players
    position = [HOME[i] for i in range(num_players)]
    color = [red, green, yellow, blue][:num_players]
    run_game()

# Check Winner
def check_winner():
    global currentPlayer, num_players
    if currentPlayer not in winnerRank:
        for i in position[currentPlayer]:
            if i not in WINNER:
                return
        winnerRank.append(currentPlayer)
    else:
        currentPlayer = (currentPlayer + 1) % num_players

# Blit All Elements
def blit_all():
    # Draw the board
    screen.blit(board, (0, 0))

    # Draw the dice
    screen.blit(DICE[number - 1], (605, 270))

    # Draw the tokens for each player
    for i in range(num_players):
        for j in range(len(position[i])):
            screen.blit(color[i], (position[i][j][0], position[i][j][1]))

    # Draw the current player text
    screen.blit(currentPlayerText, (550, 400))
    screen.blit(line, (550, 420))
    player_text = FONT.render(f'Player {currentPlayer + 1}', True, (0, 0, 0))
    screen.blit(player_text, (550, 440))

    # If there's a winner, display the winner text
    if winnerRank:
        winner_text = FONT.render(f'Player {winnerRank[0] + 1} Wins!', True, (255, 0, 0))
        screen.blit(winner_text, (550, 500))

# Run the Game Logic
def run_game():
    global number, diceRolled, currentPlayer, num_players
    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(board, (0, 0))  # Bliting Board

        check_winner()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # When MOUSEBUTTON is clicked
            if event.type == pygame.MOUSEBUTTONUP:
                coordinate = pygame.mouse.get_pos()

                # Rolling Dice
                if not diceRolled and (605 <= coordinate[0] <= 669) and (270 <= coordinate[1] <= 334):
                    number = random.randint(1, 6)
                    diceSound.play()
                    flag = True
                    for i in range(len(position[currentPlayer])):
                        if tuple(position[currentPlayer][i]) not in HOME[currentPlayer] and to_home(currentPlayer, i):
                            flag = False
                    if (flag and number == 6) or not flag:
                        diceRolled = True
                    else:
                        currentPlayer = (currentPlayer + 1) % num_players

                elif diceRolled:
                    for j in range(len(position[currentPlayer])):
                        if position[currentPlayer][j][0] <= coordinate[0] <= position[currentPlayer][j][0] + 31 \
                                and position[currentPlayer][j][1] <= coordinate[1] <= position[currentPlayer][j][1] + 31:
                            move_token(currentPlayer, j)
                            break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not diceRolled:
                        number = random.randint(1, 6)
                        diceSound.play()
                        flag = True
                        for i in range(len(position[currentPlayer])):
                            if tuple(position[currentPlayer][i]) not in HOME[currentPlayer] and to_home(currentPlayer, i):
                                flag = False
                        if (flag and number == 6) or not flag:
                            diceRolled = True
                        else:
                            currentPlayer = (currentPlayer + 1) % num_players

                elif event.key == pygame.K_1 and diceRolled:  # Use 1 to move token 1
                    move_token(currentPlayer, 0)
                elif event.key == pygame.K_2 and diceRolled:  # Use 2 to move token 2
                    move_token(currentPlayer, 1)
                elif event.key == pygame.K_3 and diceRolled:  # Use 3 to move token 3
                    move_token(currentPlayer, 2)
                elif event.key == pygame.K_4 and diceRolled:  # Use 4 to move token 4
                    move_token(currentPlayer, 3)

        blit_all()
        pygame.display.update()

# Main Menu Loop
def main_menu():
    selected_option = 0
    in_menu = True

    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 3
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 3
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        select_players()
                        start_new_game()
                    elif selected_option == 1:
                        show_instructions()
                        waiting_for_enter = True
                        while waiting_for_enter:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_RETURN:
                                        waiting_for_enter = False
                        continue
                    elif selected_option == 2:
                        pygame.quit()
                        sys.exit()

        draw_menu(selected_option)

# Start the Game
main_menu() 