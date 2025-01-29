import random
import pygame
import time
def die():
    return random.randint(1, 6)

def palSwap(surf, oColor, nColor):
    imCopy = pygame.Surface(surf.get_size())
    imCopy.fill(nColor)
    surf.set_colorkey(oColor)
    imCopy.blit(surf, (0, 0))

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

pygame.init()

scrWidth = 800
scrHeight = 800

scr = pygame.display.set_mode((scrWidth, scrHeight,))
pygame.display.set_caption("DEMO")

#board
board = pygame.image.load('res/Board.png').convert()
# board = pygame.transform.scale(board)
boardX = 0
boardY = 0
#marker
markerIMG = pygame.image.load('res/Marker.png').convert()
markerIMG = pygame.transform.scale(markerIMG, (markerIMG.get_width() / 25, markerIMG.get_height() / 25))
lrcrnPad = 83
udcrnPad = 100
btPad = 65
gMarkerPos = [(scrWidth - lrcrnPad, scrHeight - udcrnPad - btPad),\
     (scrWidth - lrcrnPad - btPad, scrHeight - udcrnPad - btPad),\
    (scrWidth - lrcrnPad, scrHeight - udcrnPad), (scrWidth - lrcrnPad - btPad, scrHeight - udcrnPad)]
gMarker = palSwap(markerIMG, (201, 42, 42), (0, 255, 0))
gMarker.set_colorkey((0, 0, 0))
lrcrnPad -= markerIMG.get_width()
udcrnPad -= markerIMG.get_height() + 12
rMarkerPos = [(lrcrnPad, udcrnPad), (lrcrnPad + btPad, udcrnPad),\
    (lrcrnPad, udcrnPad + btPad), (lrcrnPad + btPad, udcrnPad + btPad)]
rMarker = palSwap(markerIMG, (201, 42, 42), (255, 100, 100))
rMarker.set_colorkey((0, 0, 0))
lrcrnPad += markerIMG.get_width()
udcrnPad += markerIMG.get_height() + 12
udcrnPad -= markerIMG.get_height() + 12
bMarkerPos = [(scrWidth - lrcrnPad - btPad, udcrnPad),\
    (scrWidth - lrcrnPad, udcrnPad), (scrWidth - lrcrnPad - btPad, udcrnPad + btPad),\
        (scrWidth - lrcrnPad, udcrnPad + btPad)]
bMarker = palSwap(markerIMG, (201, 42, 42), (100, 100, 255))
bMarker.set_colorkey((0, 0, 0))

udcrnPad += markerIMG.get_height() + 12
lrcrnPad -= markerIMG.get_width()
yMarkerPos = [(lrcrnPad, scrHeight - udcrnPad - btPad), (lrcrnPad + btPad, scrHeight - udcrnPad - btPad),\
    (lrcrnPad, scrHeight - udcrnPad), (lrcrnPad + btPad, scrHeight - udcrnPad)]
yMarker = palSwap(markerIMG, (201, 42, 42), (200, 200, 0))
yMarker.set_colorkey((0, 0, 0))

clock = pygame.time.Clock()

# game board initialization
gamePos = [(318, 20)]
cellY = 50
cellX = 50
cellP = 17
posInit(gamePos, cellY + cellP, d = True, amount = 4)
posInit(gamePos, cellY + cellP, l = True, amount = 4)
posInit(gamePos, cellY + cellP, d = True, amount = 2)
posInit(gamePos, cellY + cellP, r = True, amount = 4)
posInit(gamePos, cellY + cellP, d = True, amount = 4)
posInit(gamePos, cellY + cellP, r = True, amount = 2)
posInit(gamePos, cellY + cellP, u = True, amount = 4)
posInit(gamePos, cellY + cellP, r = True, amount = 4)
posInit(gamePos, cellY + cellP, u = True, amount = 2)
posInit(gamePos, cellY + cellP, l = True, amount = 4)
posInit(gamePos, cellY + cellP, u = True, amount = 4)
posInit(gamePos, cellY + cellP, l = True, amount = 2)

bEndPos = [(384, 87)]
posInit(bEndPos, cellY + cellP, d = True, amount = 3)
yEndPos = [(384, 620)]
posInit(yEndPos, cellY + cellP, u = True, amount = 3)
rEndPos = [(117, 358)]
posInit(rEndPos, cellX + cellP, r = True, amount = 3)
gEndPos = [(653, 358)]
posInit(gEndPos, cellX + cellP, l = True, amount = 3)



running = True
while running:
    scr.blit(board, (boardX, boardY))
    for pos in gMarkerPos:
        scr.blit(gMarker, pos)
    for pos in rMarkerPos:
        scr.blit(rMarker, pos)
    for pos in bMarkerPos:
        scr.blit(bMarker, pos)
    for pos in yMarkerPos:
        scr.blit(yMarker, pos)
    for pos in gamePos:
        scr.blit(yMarker, pos)
    for pos in bEndPos:
        scr.blit(bMarker, pos)
    for pos in yEndPos:
        scr.blit(bMarker, pos)
    for pos in rEndPos:
        scr.blit(bMarker, pos)
    for pos in gEndPos:
        scr.blit(bMarker, pos)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 