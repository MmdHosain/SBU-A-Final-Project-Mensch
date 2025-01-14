import random
import pygame
def die():
    return random.randint(1, 6)

def palSwap(surf, oColor, nColor):
    imCopy = pygame.Surface(surf.get_size())
    imCopy.fill(nColor)
    surf.set_colorkey(oColor)
    imCopy.blit(surf, (0, 0))

    return imCopy

pygame.init()

scrWidth = 800
scrHeight = 800

scr = pygame.display.set_mode((scrWidth, scrHeight,))
pygame.display.set_caption("DEMO")

#board
board = pygame.image.load('res/Board.png').convert()
board = pygame.transform.scale(board, (scrWidth, scrHeight))
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
yMarker = palSwap(markerIMG, (201, 42, 42), (200, 200, 50))
yMarker.set_colorkey((0, 0, 0))

clock = pygame.time.Clock()

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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 