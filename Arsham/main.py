import random
import pygame
import time
turn = 0
whichDice = 0
hasPlayed = True
illigalMove = False
canPlay = True
def dice():
    return random.randint(0, 5)

def game(twoP = False):
    global turn
    global whichDice
    global hasPlayed
    global illigalMove
    global canPlay
    nPlayers = 4
    if twoP:
        nPlayers = 2
    if mouseRectOverlap(mx, my,\
                    dicePos[0], dicePos[1], dice1Img.get_width(),\
                            dice1Img.get_height()):
        if click and hasPlayed:
            whichDice = dice()
            tmpCtr = 0
            for j in range(4):
                if (ctr[turn][j] + whichDice + 1) in ctr[turn]\
                    or (ctr[turn][j] + whichDice + 1) > 40:
                    print(ctr[turn])
                    tmpCtr += 1
                    print(tmpCtr)
            if tmpCtr == 4:
                if whichDice == 5:
                    hasPlayed = True
                else:
                    canPlay = False
            tmpCtr = 0
            for i in range(4):
                if sMarkers[turn + 4][i] == startPos[turn][i]:
                    tmpCtr += 1
            if tmpCtr == 4: 
                if whichDice != 5:
                    canPlay = False
                else:
                    hasPlayed = False
            else:
                hasPlayed = False
    if not canPlay:
        if turn >= 3:
            turn = 0
            if twoP:
                turn = 1
        else:
            turn += 1
            if twoP:
                turn = 3
        canPlay = True
        print(canPlay)
    for i in range(4):
        if mouseRectOverlap(mx, my,\
                            sMarkers[turn + 4][i][0], sMarkers[turn + 4][i][1],\
                                rMarker.get_width(), rMarker.get_height()):
            if click and not hasPlayed and canPlay\
                and ctr[turn][i] + whichDice + 1 <= 40:

                # if not sMarkers[turn + 4][i] in gamePos\
                #     and not safePos[turn] in sMarkers[turn + 4][i]:
                if sMarkers[turn + 4][i] in endPos[turn]\
                    or sMarkers[turn + 4][i] in startPos[turn]:
                    print("not in game")
                    if sMarkers[turn + 4][i] in endPos[turn]:
                        if ctr[turn][i] + whichDice + 1 <= 40:
                            isEmpty = True
                            # i = 1
                            # j = 0
                            for j in range(4):
                                if j != i:
                                    # print(j)
                                    # print(i)
                                    # print(turn + 4)
                                    # print(turn)
                                    if sMarkers[turn + 4][j] == endPos[turn][ctr[turn][i] + whichDice + 1 - 36 - 1]:
                                        isEmpty = False
                            if isEmpty:
                                ctr[turn][i] += whichDice + 1
                                sMarkers[turn + 4][i] = endPos[turn][ctr[turn][i] - 36 - 1]
                            else:
                                illigalMove = True
                        else:
                            illigalMove = True
                    elif whichDice == 5:
                        # ctr[turn][i] = 1
                        sMarkers[turn + 4][i] = safePos[turn]
                        # sMarkers[turn + 4][i] = gamePos[8 + 10 * turn]
                    else:
                        illigalMove = True
                elif sMarkers[turn + 4][i] in gamePos:
                    print("in game")
                    # if sMarkers[turn + 4][i]
                    idx = gamePos.index(sMarkers[turn + 4][i])
                    # if ctr[turn][i] + whichDice + 1 == 
                    if ctr[turn][i] + whichDice + 1 > 36:
                        if ctr[turn][i] + whichDice + 1 <= 40:
                            isEmpty = True
                            for j in range(nPlayers):
                                for k in range(4):
                                    if sMarkers[j + 4][k] == endPos[turn][ctr[turn][i] + whichDice + 1 - 36 - 1]:
                                        isEmpty = False
                                        illigalMove = True
                            if isEmpty:
                                ctr[turn][i] += whichDice + 1
                                sMarkers[turn + 4][i] = endPos[turn][ctr[turn][i] - 36 - 1]
                    elif idx - whichDice - 1 < 0:
                        idx = idx - whichDice - 1
                        idx = len(gamePos) + idx
                        isEmpty = True
                        for j in range(nPlayers):
                            for k in range(4):
                                if sMarkers[j + 4][k] == gamePos[idx]:
                                    tmpj = j
                                    tmpk = k
                                    isEmpty = False
                        if isEmpty:
                            sMarkers[turn + 4][i] = gamePos[idx]
                            ctr[turn][i] += whichDice + 1
                        elif tmpj != turn:
                            print(startPos[tmpj][tmpk])
                            print(tmpj, tmpk)
                            print(turn, i)
                            # if sMarkers[tmpj + 4][tmpk] != gamePos[8 + 10 * turn]:
                            sMarkers[tmpj + 4][tmpk] = startPos[tmpj][tmpk]
                            sMarkers[turn + 4][i] = gamePos[idx]
                        else:
                            illigalMove = True
                    else:
                        idx = idx - whichDice - 1
                        isEmpty = True
                        for j in range(nPlayers):
                            for k in range(4):
                                if sMarkers[j + 4][k] == gamePos[idx]:
                                    tmpj = j
                                    tmpk = k
                                    isEmpty = False
                                    # illigalMove = True
                        if isEmpty:
                            ctr[turn][i] += whichDice + 1
                            sMarkers[turn + 4][i] = gamePos[idx]
                        elif tmpj != turn:
                            print(startPos[tmpj][tmpk])
                            print(tmpj, tmpk)
                            print(turn, i)
                            # if sMarkers[tmpj + 4][tmpk] != gamePos[8 + 10 * turn]:
                            sMarkers[tmpj + 4][tmpk] = startPos[tmpj][tmpk]
                            sMarkers[turn + 4][i] = gamePos[idx]
                        else:
                            illigalMove = True
                elif safePos[turn] == sMarkers[turn + 4][i]:
                    sMarkers[turn + 4][i] = gamePos[(7 + 9 * turn) - whichDice]
                        
                hasPlayed = True
                if whichDice != 5 and not illigalMove:
                    if turn >= 3:
                        turn = 0
                        if twoP:
                            turn = 1
                    else:
                        turn += 1
                        if twoP:
                            turn = 3
                elif illigalMove:
                    hasPlayed = False
                    illigalMove = False
                break

def drawText(text, font, col, surf, x, y):
    textObject = font.render(text, 1, col)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surf.blit(textObject, textRect)


def palSwap(surf, oColor, nColor):
    imCopy = pygame.Surface(surf.get_size())
    imCopy.fill(nColor)
    surf.set_colorkey(oColor)
    imCopy.blit(surf, (0, 0))
    imCopy.set_colorkey((0, 0, 0))

    return imCopy

def posInit(posList, padding, u = False, d = False, l = False, r = False, amount = 4):
    posListSize = len(posList) - 1
    i = posListSize
    while i < posListSize + amount:
        if u:
            posList.append((posList[i][0], posList[i][1] - padding))
        if d:
            posList.append((posList[i][0], posList[i][1] + padding))
        if l:
            posList.append((posList[i][0] - padding, posList[i][1]))
        if r:
            posList.append((posList[i][0] + padding, posList[i][1]))
        i += 1

def mouseRectOverlap(mx, my, rx, ry, rwidth, rheight):
    return mx >= rx\
           and my >= ry\
           and mx <= rx + rwidth\
           and my <= ry + rheight\
           
pygame.init()

# 0: menu | 1: help | 2: game | 3: pause
state = 0

scrWidth = 1000
scrHeight = 800
infoWidth = scrWidth - scrHeight
bgColor = (52, 78, 91)
font = pygame.font.SysFont("arialblack", 40)
textColor = (255, 255, 255)

scr = pygame.display.set_mode((scrWidth, scrHeight,))
pygame.display.set_caption("DEMO")

#board
board = pygame.image.load('res/Board.png').convert()
# board = pygame.transform.scale(board)
boardX = 0
boardY = 0
#marker
markerIMG = pygame.image.load('res/Marker.png').convert()
sMarkerIMG = pygame.transform.scale(markerIMG, (markerIMG.get_width() / 50, markerIMG.get_height() / 50))
markerIMG = pygame.transform.scale(markerIMG, (markerIMG.get_width() / 25, markerIMG.get_height() / 25))
#dice
diceImg = []
dice1Img = pygame.image.load('res/side_1.png').convert_alpha()
dice1Img = pygame.transform.scale(dice1Img, (dice1Img.get_width() / 25, dice1Img.get_height() / 25))
diceImg.append(dice1Img)
dice2Img = pygame.image.load('res/side_2.png').convert_alpha()
dice2Img = pygame.transform.scale(dice2Img, (dice2Img.get_width() / 25, dice2Img.get_height() / 25))
diceImg.append(dice2Img)
dice3Img = pygame.image.load('res/side_3.png').convert_alpha()
dice3Img = pygame.transform.scale(dice3Img, (dice3Img.get_width() / 25, dice3Img.get_height() / 25))
diceImg.append(dice3Img)
dice4Img = pygame.image.load('res/side_4.png').convert_alpha()
dice4Img = pygame.transform.scale(dice4Img, (dice4Img.get_width() / 25, dice4Img.get_height() / 25))
diceImg.append(dice4Img)
dice5Img = pygame.image.load('res/side_5.png').convert_alpha()
dice5Img = pygame.transform.scale(dice5Img, (dice5Img.get_width() / 25, dice5Img.get_height() / 25))
diceImg.append(dice5Img)
dice6Img = pygame.image.load('res/side_6.png').convert_alpha()
dice6Img = pygame.transform.scale(dice6Img, (dice6Img.get_width() / 25, dice6Img.get_height() / 25))
diceImg.append(dice6Img)

dicePos = (900 - dice1Img.get_width() / 2, 600)

markerSmplPos = [(825, 100), (865, 100), (905, 100), (945, 100)]
bigMarkerSmplPos = [(820, 100), (860, 100), (900, 100), (940, 100)]
sMarkers = []
rMarkerS = palSwap(sMarkerIMG, (201, 42, 42), (255, 100, 100))
sMarkers.append(rMarkerS)
yMarkerS = palSwap(sMarkerIMG, (201, 42, 42), (200, 200, 0))
sMarkers.append(yMarkerS)
gMarkerS = palSwap(sMarkerIMG, (201, 42, 42), (0, 255, 0))
sMarkers.append(gMarkerS)
bMarkerS = palSwap(sMarkerIMG, (201, 42, 42), (100, 100, 255))
sMarkers.append(bMarkerS)

sMarkerB = []
rMarkerSb = pygame.transform.scale(sMarkers[0],\
    (sMarkers[0].get_width() * 1.5, sMarkers[0].get_height() * 1.5))
sMarkerB.append(rMarkerSb)
yMarkerSb = pygame.transform.scale(sMarkers[1],\
    (sMarkers[1].get_width() * 1.5, sMarkers[1].get_height() * 1.5))
sMarkerB.append(yMarkerSb)
gMarkerSb = pygame.transform.scale(sMarkers[2],\
    (sMarkers[2].get_width() * 1.5, sMarkers[2].get_height() * 1.5))
sMarkerB.append(gMarkerSb)
bMarkerSb = pygame.transform.scale(sMarkers[3],\
    (sMarkers[3].get_width() * 1.5, sMarkers[3].get_height() * 1.5))
sMarkerB.append(bMarkerSb)

startPos = [[(52, 37), (117, 37), (52, 102), (117, 102)],\
             [(52, 635), (117, 635), (52, 700), (117, 700)],\
             [(717, 635), (652, 635), (717, 700), (652, 700)],\
             [(652, 37), (717, 37), (652, 102), (717, 102)]]
lrcrnPad = 83
udcrnPad = 100
btPad = 65
gMarkerPos = [(scrWidth - lrcrnPad - infoWidth, scrHeight - udcrnPad - btPad),\
     (scrWidth - lrcrnPad - btPad - infoWidth, scrHeight - udcrnPad - btPad),\
    (scrWidth - lrcrnPad - infoWidth, scrHeight - udcrnPad), (scrWidth - lrcrnPad - btPad - infoWidth, scrHeight - udcrnPad)]
gMarker = palSwap(markerIMG, (201, 42, 42), (0, 255, 0))
lrcrnPad -= markerIMG.get_width()
udcrnPad -= markerIMG.get_height() + 12
rMarkerPos = [(lrcrnPad, udcrnPad), (lrcrnPad + btPad, udcrnPad),\
    (lrcrnPad, udcrnPad + btPad), (lrcrnPad + btPad, udcrnPad + btPad)]
rMarker = palSwap(markerIMG, (201, 42, 42), (255, 100, 100))
lrcrnPad += markerIMG.get_width()
udcrnPad += markerIMG.get_height() + 12
udcrnPad -= markerIMG.get_height() + 12
bMarkerPos = [(scrWidth - lrcrnPad - btPad - infoWidth, udcrnPad),\
    (scrWidth - lrcrnPad - infoWidth, udcrnPad), (scrWidth - lrcrnPad - btPad - infoWidth, udcrnPad + btPad),\
        (scrWidth - lrcrnPad - infoWidth, udcrnPad + btPad)]
bMarker = palSwap(markerIMG, (201, 42, 42), (100, 100, 255))
udcrnPad += markerIMG.get_height() + 12
lrcrnPad -= markerIMG.get_width()
yMarkerPos = [(lrcrnPad, scrHeight - udcrnPad - btPad), (lrcrnPad + btPad, scrHeight - udcrnPad - btPad),\
    (lrcrnPad, scrHeight - udcrnPad), (lrcrnPad + btPad, scrHeight - udcrnPad)]
yMarker = palSwap(markerIMG, (201, 42, 42), (200, 200, 0))

print(startPos)

sMarkers.append(rMarkerPos)
sMarkers.append(yMarkerPos)
sMarkers.append(gMarkerPos)
sMarkers.append(bMarkerPos)

clock = pygame.time.Clock()

# game board initialization
gamePos = [(318, 20)]
cellY = 50
cellX = 50
cellP = 17
posInit(gamePos, cellY + cellP, d = True, amount = 4)
posInit(gamePos, cellY + cellP, l = True, amount = 3)
gamePos.append((50, 355))
posInit(gamePos, cellY + cellP, d = True, amount = 1)
posInit(gamePos, cellY + cellP, r = True, amount = 4)
posInit(gamePos, cellY + cellP, d = True, amount = 3)
gamePos.append((385, 690))
posInit(gamePos, cellY + cellP, r = True, amount = 1)
posInit(gamePos, cellY + cellP, u = True, amount = 4)
posInit(gamePos, cellY + cellP, r = True, amount = 3)
gamePos.append((720, 355))
posInit(gamePos, cellY + cellP, u = True, amount = 1)
posInit(gamePos, cellY + cellP, l = True, amount = 4)
posInit(gamePos, cellY + cellP, u = True, amount = 3)
gamePos.append((385, 20))

safePos = [(50, 288), (318, 690), (720, 422), (452, 20)]

bEndPos = [(384, 87)]
posInit(bEndPos, cellY + cellP, d = True, amount = 3)
yEndPos = [(384, 620)]
posInit(yEndPos, cellY + cellP, u = True, amount = 3)
rEndPos = [(117, 358)]
posInit(rEndPos, cellX + cellP, r = True, amount = 3)
gEndPos = [(653, 358)]
posInit(gEndPos, cellX + cellP, l = True, amount = 3)
endPos = [rEndPos, yEndPos, gEndPos, bEndPos]

dicePos = (875, 600)

# r, y, g, b
ctr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

startingPlayer = 0

running = True
#       r, y, g, b
won = False
winer = -1
click = False
newGamePressed = False
twoPlayer = False
while running:
    NewGame = pygame.Rect(scrWidth/2 - 150, 100, 300, 100)
    Help = pygame.Rect(scrWidth/2 - 150, 300, 300, 100)
    Exit = pygame.Rect(scrWidth/2 - 150, 500, 300, 100)
    ResumeGame = pygame.Rect(scrWidth/2 - 175, 100, 350, 100)
    Menue = pygame.Rect(scrWidth/2 - 150, 300, 300, 100)
    Quit = pygame.Rect(scrWidth/2 - 150, 500, 300, 100)
    twoP = pygame.Rect(150, 350, 300, 100)
    fourP = pygame.Rect(550, 350, 300, 100)


    mx, my = pygame.mouse.get_pos()
    for i in range(4):
        if not won:
            for j in range(4):
                if sMarkers[i + 4][j] not in endPos[i]:
                    won = False
                    break
                won = True
                winer = i
    if won:
        print(winer, "won!")
    if newGamePressed:
        if twoP.collidepoint((mx, my)):
            if click:
                twoPlayer = True
                turn = 1
                state = 2
        if fourP.collidepoint((mx, my)):
            if click:
                twoPlayer = False
                state = 2
    if state == 0:
        if NewGame.collidepoint((mx, my)):
            if click:
                scr.fill(bgColor)
                # drawText("tow player", font, textColor, scr, 150, 300)
                # drawText("four player", font, textColor, scr, 550, 300)
                # state = 2
                for i in range(4):
                    for j in range(4):
                        sMarkers[i + 4][j] = startPos[i][j]
                        ctr[i][j] = 0
                whichDice = 0
                newGamePressed = True
        if Help.collidepoint((mx, my)):
            if click:
                state = 1
        if Exit.collidepoint((mx, my)):
            if click:
                running = False
    if state == 3:
        if ResumeGame.collidepoint((mx, my)):
            if click:
                state = 2
        if Menue.collidepoint((mx, my)):
            if click:
                state = 0
        if Quit.collidepoint((mx, my)):
            if click:
                running = False

    if state == 2:
        newGamePressed = False
        game(twoPlayer)

    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state == 2:
                    state = 3
                elif state == 3:
                    state = 2
                else:
                    state = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    scr.fill(bgColor)

    if state == 2:
        scr.blit(board, (boardX, boardY))
        if not twoPlayer:
            for pos in gMarkerPos:
                scr.blit(gMarker, pos)
            for pos in rMarkerPos:
                scr.blit(rMarker, pos)
        for pos in bMarkerPos:
            scr.blit(bMarker, pos)
        for pos in yMarkerPos:
            scr.blit(yMarker, pos)

        scr.blit(diceImg[whichDice], dicePos)
    
        tmp = sMarkers[turn]
        sMarkers[turn] = sMarkerB[turn]
        sMarkerB[turn] = tmp
        if twoPlayer:
            for i in [1,3]:
                scr.blit(sMarkers[i], markerSmplPos[i])
        else:
            for i in range(4):
                scr.blit(sMarkers[i], markerSmplPos[i])
        tmp = sMarkers[turn]
        sMarkers[turn] = sMarkerB[turn]
        sMarkerB[turn] = tmp

    if state == 1:
        drawText("click on the dice to play!", font, textColor, scr, 210, 350)

    if state == 0:
        if newGamePressed:
            # pygame.draw.rect(scr, (255, 0, 0), Quit)
            # drawText("click on the dice to play!", font, textColor, scr, 210, 350)
            # drawText("click on the dice to play!", font, textColor, scr, 210, 350)
            pygame.draw.rect(scr, (255, 0, 0), twoP)
            drawText("tow player", font, textColor, scr, 180, 370)
            pygame.draw.rect(scr, (255, 0, 0), fourP)
            drawText("four player", font, textColor, scr, 580, 370)
        else:
            pygame.draw.rect(scr, (255, 0, 0,), NewGame)
            drawText("New Game", font, textColor, scr, scrWidth/2 - 120, 120)
            pygame.draw.rect(scr, (255, 0, 0,), Help)
            drawText("Help", font, textColor, scr, scrWidth/2 - 50, 320)
            pygame.draw.rect(scr, (255, 0, 0,), Exit)
            drawText("EXIT", font, textColor, scr, scrWidth/2 - 50, 520)

    if state == 3:
        pygame.draw.rect(scr, (255, 0, 0), ResumeGame)
        drawText("Resume Game", font, textColor, scr, scrWidth/2 - 160, 120)
        pygame.draw.rect(scr, (255, 0, 0), Menue)
        drawText("Menue", font, textColor, scr, scrWidth/2 - 70, 320)
        pygame.draw.rect(scr, (255, 0, 0), Quit)
        drawText("Quit Game", font, textColor, scr, scrWidth/2 - 120, 520)
    



    pygame.display.flip()
    clock.tick(60)

pygame.quit() 

