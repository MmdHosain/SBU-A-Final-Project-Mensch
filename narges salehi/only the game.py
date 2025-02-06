import pygame
from pygame import mixer
import random
import time

# Initializing pygame
#با استفاده از pygame.init() همه ماژول‌های Pygame لود می‌شوند.
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
#عدد روی تاس را ذخیره می‌کند
number = 1
#شماره بازیکن فعلی را مشخص می‌کند. این متغیر بین 4 بازیکن چرخش دارد (0 تا 3).
currentPlayer = 0
#مشخص می‌کند که آیا بازیکنی کشته شده یا نه.
playerKilled = False
diceRolled = False
winnerRank = []

# Rendering Text
font = pygame.font.Font('freesansbold.ttf', 11)
FONT = pygame.font.Font('freesansbold.ttf', 16)
currentPlayerText = font.render('Current Player', True, (0, 0, 0))
line = font.render('------------------------------------', True, (0, 0, 0))

#HOME: مختصات خانههای هر بازیکن.

#SAFE: مختصات نقاط امن روی تخته.

#position: موقعیت فعلی هر توکن.

#jump: نقاط پرش (Shortcutها).

#WINNER: موقعیت نهایی برای برد.

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

# Blit Token Movement
def show_token(x, y):
    #ن تابع برای نمایش توکن‌ها و حرکت دادن آن‌ها روی صفحه بازی استفاده می‌شود.
    #بعد از هر حرکت، تابع وضعیت جدید صفحه را به‌روز می‌کند.
    screen.fill((255, 255, 255))
    screen.blit(board, (0, 0))

    for i in SAFE[4:]:
        screen.blit(star, i)

    for i in range(len(position)):
        for j in position[i]:
            screen.blit(color[i], j)

#نمایش تصویر تاس
    screen.blit(DICE[number - 1], (605, 270))

# پخش صدا بر اساس وضعیت توکن
    if position[x][y] in WINNER:
        winnerSound.play()
    else:
        tokenSound.play()

#نمایش نوبت بازیکن فعلی
    screen.blit(color[currentPlayer], (620, 28))
    screen.blit(currentPlayerText, (600, 10))
    screen.blit(line, (592, 59))
#مایش رنکینگ بازیکنان
    for i in range(len(winnerRank)):
        rank = FONT.render(f'{i + 1}.', True, (0, 0, 0))
        screen.blit(rank, (600, 85 + (40 * i)))
        screen.blit(color[winnerRank[i]], (620, 75 + (40 * i)))

    pygame.display.update()
    time.sleep(0.5)

# Bliting in while loop
def blit_all():
    for i in SAFE[4:]:
        screen.blit(star, i)

    for i in range(len(position)):
        for j in position[i]:
            screen.blit(color[i], j)

    screen.blit(DICE[number - 1], (605, 270))

    screen.blit(color[currentPlayer], (620, 28))
    screen.blit(currentPlayerText, (600, 10))
    screen.blit(line, (592, 59))

# نمایش رتبه‌بندی بازیکنان برنده
    for i in range(len(winnerRank)):
        rank = FONT.render(f'{i + 1}.', True, (0, 0, 0))
        screen.blit(rank, (600, 85 + (40 * i)))
        screen.blit(color[winnerRank[i]], (620, 75 + (40 * i)))

#  آیا توکن فعلی می‌تواند به خانه‌ی پایانی (منطقه برنده) منتقل شود یا نه.
#x: شماره بازیکن (0 تا 3)
#y: شماره توکن بازیکن
def to_home(x, y):
    #بازیکن قرمز
    #اگر حرکت باعث شود که مختصات x توکن از مختصات خانه برنده 
    # عبور کند، False برمی‌گرداند.
    if (position[x][y][1] == 284 and position[x][y][0] <= 202 and x == 0) \
            and (position[x][y][0] + 38 * number > WINNER[x][0]):
        return False
    
    #  بازیکن زرد
    # به منطقه خانه پایانی زرد نزدیک شده است.
    elif (position[x][y][1] == 284 and 368 < position[x][y][0] and x == 2) \
            and (position[x][y][0] - 38 * number < WINNER[x][0]):
        return False
    # ازیکن سبز
    elif (position[x][y][0] == 284 and position[x][y][1] <= 202 and x == 1) \
            and (position[x][y][1] + 38 * number > WINNER[x][1]):
        return False
    #  بازیکن آبی
    elif (position[x][y][0] == 284 and position[x][y][1] >= 368 and x == 3) \
            and (position[x][y][1] - 38 * number < WINNER[x][1]):
        return False
    #اگر هیچ‌کدام از شرایط بالا برقرار نباشد، توکن می‌تواند به سمت خانه پایانی حرکت کند.
    return True

# این تابع مسئول مدیریت منطق حرکت توکن‌ها در بازی است. بسته به شرایط مختلف (در خانه بودن توکن، عدد تاس، مسیر حرکت) حرکت‌ها محاسبه و وضعیت صفحه بازی به‌روزرسانی می‌شود.
def move_token(x, y):
    global currentPlayer, diceRolled

    # یرون آوردن توکن از خانه
    #اگر توکن در خانه باشد و عدد تاس 6 باشد، توکن به نقطه امن اولیه منتقل می‌شود.
    if tuple(position[x][y]) in HOME[currentPlayer] and number == 6:
        position[x][y] = list(SAFE[currentPlayer])
        tokenSound.play()
        diceRolled = False

    # حرکت توکن در مسیر معمولی
    #اگر توکن در خانه نباشد، تاس ریست می‌شود.
    #گر عدد تاس 6 نباشد، نوبت به بازیکن بعدی داده می‌شود.
    elif tuple(position[x][y]) not in HOME[currentPlayer]:
        diceRolled = False
        if not number == 6:
            currentPlayer = (currentPlayer + 1) % 4

        # حرکت به سمت خانه برنده

        # R2
        #اگر توکن بازیکن قرمز روی ردیف خانه پایانی باشد
        #مختصات x آن در محدوده مشخص باشد، حرکت به سمت خانه برنده انجام می‌شود.
        if (position[x][y][1] == 284 and position[x][y][0] <= 202 and x == 0) \
                and (position[x][y][0] + 38 * number <= WINNER[x][0]):
            for i in range(number):
                position[x][y][0] += 38
                show_token(x, y)

        # Y2
        #مشابه بازیکن قرمز، ولی برای حرکت در جهت عکس.
        elif (position[x][y][1] == 284 and 368 < position[x][y][0] and x == 2) \
                and (position[x][y][0] - 38 * number >= WINNER[x][0]):
            for i in range(number):
                position[x][y][0] -= 38
                show_token(x, y)

        # G2
        elif (position[x][y][0] == 284 and position[x][y][1] <= 202 and x == 1) \
                and (position[x][y][1] + 38 * number <= WINNER[x][1]):
            for i in range(number):
                position[x][y][1] += 38
                show_token(x, y)
        # B2
        elif (position[x][y][0] == 284 and position[x][y][1] >= 368 and x == 3) \
                and (position[x][y][1] - 38 * number >= WINNER[x][1]):
            for i in range(number):
                position[x][y][1] -= 38
                show_token(x, y)

        # Other Paths
        else:
            for _ in range(number):

                # R1, Y3
                if (position[x][y][1] == 240 and position[x][y][0] < 202) \
                        or (position[x][y][1] == 240 and 368 <= position[x][y][0] < 558):
                    position[x][y][0] += 38
                # R3 -> R2 -> R1
                elif (position[x][y][0] == 12 and position[x][y][1] > 240):
                    position[x][y][1] -= 44

                # R3, Y1
                elif (position[x][y][1] == 328 and 12 < position[x][y][0] <= 202) \
                        or (position[x][y][1] == 328 and 368 < position[x][y][0]):
                    position[x][y][0] -= 38
                # Y3 -> Y2 -> Y1
                elif (position[x][y][0] == 558 and position[x][y][1] < 328):
                    position[x][y][1] += 44

                # G3, B1
                elif (position[x][y][0] == 240 and 12 < position[x][y][1] <= 202) \
                        or (position[x][y][0] == 240 and 368 < position[x][y][1]):
                    position[x][y][1] -= 38
                # G3 -> G2 -> G1
                elif (position[x][y][1] == 12 and 240 <= position[x][y][0] < 328):
                    position[x][y][0] += 44

                # B3, G1
                elif (position[x][y][0] == 328 and position[x][y][1] < 202) \
                        or (position[x][y][0] == 328 and 368 <= position[x][y][1] < 558):
                    position[x][y][1] += 38
                # B3 -> B2 -> B1
                elif (position[x][y][1] == 558 and position[x][y][0] > 240):
                    position[x][y][0] -= 44
#اگر توکن به یکی از نقاط پرش برسد، به مختصات مقصد منتقل می‌شود.
                else:
                    for i in jump:
                        if position[x][y] == list(i):
                            position[x][y] = list(jump[i])
                            break

                show_token(x, y)
# Killing Player
        if tuple(position[x][y]) not in SAFE:
            for i in range(len(position)):
                for j in range(len(position[i])):
                    if position[i][j] == position[x][y] and i != x:
                        position[i][j] = list(HOME[i][j])
                        killSound.play()
                        #در صورت برخورد، نوبت به بازیکن قبلی برمی‌گردد (با افزودن 3 به نوبت فعلی).
                        currentPlayer = (currentPlayer + 3) % 4

# Checking Winner
def check_winner():
    global currentPlayer
    if currentPlayer not in winnerRank:
        for i in position[currentPlayer]:
            if i not in WINNER:
                return
        winnerRank.append(currentPlayer)
    else:
        currentPlayer = (currentPlayer + 1) % 4

# Main LOOP
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(board, (0, 0))  # Bliting Board

    check_winner()

    for event in pygame.event.get():

        # Event QUIT
        if event.type == pygame.QUIT:
            running = False

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
                    currentPlayer = (currentPlayer + 1) % 4

            # Moving Player
            elif diceRolled:
                #مختصات تمامی توکن‌های بازیکن بررسی می‌شود
                for j in range(len(position[currentPlayer])):
                    if position[currentPlayer][j][0] <= coordinate[0] <= position[currentPlayer][j][0] + 31 \
                            and position[currentPlayer][j][1] <= coordinate[1] <= position[currentPlayer][j][1] + 31:
                        move_token(currentPlayer, j)
                        break

        # When KEY is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Use Spacebar to roll the dice
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
                        currentPlayer = (currentPlayer + 1) % 4

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