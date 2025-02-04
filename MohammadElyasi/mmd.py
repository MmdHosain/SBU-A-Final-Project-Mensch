

import pygame
import random
import time
pygame.init()
width=800
height=600
dispaly=pygame.display.set_mode((width,height))
pygame.display.set_caption('have a good time')
sat=pygame.time.Clock()
posedina=pygame.image.load('images/posedina.png').convert()
yellow=pygame.image.load('images/zuti.png').convert()
blue=pygame.image.load('images/plavi.png').convert()
red=pygame.image.load('images/crveni.png').convert()
green=pygame.image.load('images/zeleni.png').convert()
white=pygame.image.load('images/bijeli.png').convert()
pose=pygame.image.load('images/menu.png').convert()
h0p=pygame.image.load('images/hover0play.png').convert()
h1p=pygame.image.load('images/hover1play.png').convert()
h0e=pygame.image.load('images/hover0exit.png').convert()
h1e=pygame.image.load('images/hover1exit.png').convert()
r1=pygame.image.load('images/1.png').convert()
r2=pygame.image.load('images/2.png').convert()
r3=pygame.image.load('images/3.png').convert()
r4=pygame.image.load('images/4.png').convert()
r5=pygame.image.load('images/5.png').convert()
r6=pygame.image.load('images/6.png').convert()
h1h=pygame.image.load('images/h1h.png').convert()
h0h=pygame.image.load('images/h0h.png').convert()
ro1=pygame.image.load('images/roll1.png').convert()
ro2=pygame.image.load('images/roll2.png').convert()
ro3=pygame.image.load('images/roll3.png').convert()
ro4=pygame.image.load('images/roll4.png').convert()
yellowulaz=pygame.image.load('images/zutiulaz.png').convert()
blueulaz=pygame.image.load('images/plaviulaz.png').convert()
redulaz=pygame.image.load('images/crveniulaz.png').convert()
greenulaz=pygame.image.load('images/zeleniulaz.png').convert()
yellowizlaz=pygame.image.load('images/zutiizlaz.png').convert()
blueizlaz=pygame.image.load('images/plaviizlaz.png').convert()
redizlaz=pygame.image.load('images/crveniizlaz.png').convert()
greenizlaz=pygame.image.load('images/zeleniizlaz.png').convert()
yellowkucica=pygame.image.load('images/zutakucica.png').convert()
bluekucica=pygame.image.load('images/plavakucica.png').convert()
redkucica=pygame.image.load('images/crvenakucica.png').convert()
greenkucica=pygame.image.load('images/zelenakucica.png').convert()
w1=pygame.image.load('images/win1.png').convert()
w2=pygame.image.load('images/win2.png').convert()
w3=pygame.image.load('images/win3.png').convert()
w4=pygame.image.load('images/win4.png').convert()



# لود و پخش موزیک
pygame.mixer.init()
pygame.mixer.music.load("relax.mp3")  # فایل موزیک را در کنار کد قرار دهید
pygame.mixer.music.set_volume(0.5)  # تنظیم میزان صدا (0.0 تا 1.0)
pygame.mixer.music.play(-1)  # پخش موزیک به صورت نامحدود

# متغیر برای وضعیت موزیک (فعال یا متوقف)
music_paused = False  

def how_to_play():
    """نمایش صفحه راهنمای بازی با متن واقعی"""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # بازگشت به منو با دکمه Escape
        
        dispaly.fill((0, 0, 0))  # پس‌زمینه سیاه
        font = pygame.font.Font(None, 36)
        title = font.render("How to Play", True, (255, 255, 0))
        dispaly.blit(title, (300, 50))
        
        instructions = [
            "1. Each player rolls the dice to move their pieces.",
            "2. To leave the base, you must roll a 6.",
            "3. If you land on an opponent’s piece, they return to base.",
            "4. The goal is to get all pieces to the safe zone.",
            "5. Press ESC to return to the menu."
        ]
        
        y_offset = 120
        for line in instructions:
            text = font.render(line, True, (255, 255, 255))
            dispaly.blit(text, (100, y_offset))
            y_offset += 40
        
        pygame.display.update()

def menu():
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        
        dispaly.blit(pose, [0, 0])
        mispose = pygame.mouse.get_pos()
        misklick = pygame.mouse.get_pressed()

        if 200 <= mispose[0] <= 600 and 150 <= mispose[1] <= 250:
            dispaly.blit(h1p, [200, 150])
        else:
            dispaly.blit(h0p, [200, 150])
        
        if 200 <= mispose[0] <= 600 and 300 <= mispose[1] <= 400:
            dispaly.blit(h1h, [200, 300])  # استفاده از آیکون جدید برای How to Play
        else:
            dispaly.blit(h0h, [200, 300])
        
        if 200 <= mispose[0] <= 600 and 450 <= mispose[1] <= 500:
            dispaly.blit(h1e, [200, 450])
        else:
            dispaly.blit(h0e, [200, 450])
        
        if misklick[0] == 1:
            if 200 <= mispose[0] <= 600 and 150 <= mispose[1] <= 250:
                main()
                end = True
            elif 200 <= mispose[0] <= 600 and 300 <= mispose[1] <= 400:
                how_to_play()
            elif 200 <= mispose[0] <= 600 and 450 <= mispose[1] <= 500:
                pygame.quit()
                exit()
        
        pygame.display.update()


def win1():
    end=False
    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=True
                
        dispaly.blit(w1,[0,0])
        misklick=pygame.mouse.get_pressed()
        if misklick[0]==1:
            menu()
            end=True

def win2():
    end=False
    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=True
                
        dispaly.blit(w2,[0,0])
        misklick=pygame.mouse.get_pressed()
        if misklick[0]==1:
            menu()
            end=True
            
def win3():
    end=False
    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=True
                
        dispaly.blit(w3,[0,0])
        misklick=pygame.mouse.get_pressed()
        if misklick[0]==1:
            menu()
            end=True

def win4():
    end=False
    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=True
                
        dispaly.blit(w4,[0,0])
        misklick=pygame.mouse.get_pressed()
        if misklick[0]==1:
            menu()
            end=True
        

# مقداردهی اولیه pygame فقط یک بار
pygame.mixer.init()

# بارگذاری صدا فقط یک بار در ابتدای برنامه
dice_roll_sound = pygame.mixer.Sound('s.wav')  # از فرمت WAV یا OGG استفاده کنید
pygame.mixer.music.set_volume(0.5) 
# اختصاص یک کانال مشخص برای کنترل صدا
channel = pygame.mixer.Channel(1)  # کانال 1 را برای این صدا استفاده می‌کنیم

# تابع پرتاب تاس
def roll(tas):
    global setup
    global setup2
    
    # بررسی کنیم که صدا در حال حاضر پخش نمی‌شود
    if not channel.get_busy():
        channel.play(dice_roll_sound)  # پخش صدا فقط اگر قبلاً پخش نشده باشد

    tas = random.randint(setup, setup2)  # تولید عدد تصادفی

    # نمایش تصویر مرتبط با مقدار تاس
    if tas == 1:
        posedina.blit(r1, [377, 277])
    elif tas == 2:
        posedina.blit(r2, [377, 277])
    elif tas == 3:
        posedina.blit(r3, [377, 277])
    elif tas == 4:
        posedina.blit(r4, [377, 277])
    elif tas == 5:
        posedina.blit(r5, [377, 277])
    elif tas == 6:
        posedina.blit(r6, [377, 277])

    return tas





def blitanje(staraxkoor,staraykoor):
    if staraxkoor==333 and staraykoor==533:
        posedina.blit(yellowizlaz,[staraxkoor,staraykoor])
    elif staraxkoor==133 and staraykoor==283:
        posedina.blit(blueulaz,[staraxkoor,staraykoor])
    elif staraxkoor==133 and staraykoor==233:
        posedina.blit(blueizlaz,[staraxkoor,staraykoor])
    elif staraxkoor==383 and staraykoor==33:
        posedina.blit(redulaz,[staraxkoor,staraykoor])
    elif staraxkoor==433 and staraykoor==33:
        posedina.blit(redizlaz,[staraxkoor,staraykoor])
    elif staraxkoor==633 and staraykoor==283:
        posedina.blit(greenulaz,[staraxkoor,staraykoor])
    elif staraxkoor==633 and staraykoor==333:
        posedina.blit(greenizlaz,[staraxkoor,staraykoor])
    elif staraxkoor==383 and staraykoor==533:
        posedina.blit(yellowulaz,[staraxkoor,staraykoor])
    elif (staraxkoor==383 and staraykoor==483) or (staraxkoor==383 and staraykoor==433) or (staraxkoor==383 and staraykoor==383) or (staraxkoor==383 and staraykoor==333):
        posedina.blit(yellowkucica,[staraxkoor,staraykoor])
    elif (staraxkoor==183 and staraykoor==283) or (staraxkoor==233 and staraykoor==283) or (staraxkoor==283 and staraykoor==283) or (staraxkoor==333 and staraykoor==283):
        posedina.blit(bluekucica,[staraxkoor,staraykoor])
    elif (staraxkoor==383 and staraykoor==83) or (staraxkoor==383 and staraykoor==133) or (staraxkoor==383 and staraykoor==183) or (staraxkoor==383 and staraykoor==233):
        posedina.blit(redkucica,[staraxkoor,staraykoor])
    elif (staraxkoor==583 and staraykoor==283) or (staraxkoor==533 and staraykoor==283) or (staraxkoor==483 and staraykoor==283) or (staraxkoor==433 and staraykoor==283):
        posedina.blit(greenkucica,[staraxkoor,staraykoor])
    else:
        posedina.blit(white,[staraxkoor,staraykoor])
    return

def check_turn(plyr, tas, home_pieces):

    
    if tas == 6:
        return plyr 
    elif any(piece in home_pieces for piece in [1000, 2000, 3000, 4000]):
        return plyr 
    else:
        return (plyr % 4) + 1  


def main():
    global setup
    global setup2
    xkoor={1:333,2:333,3:333,4:333,5:333,6:283,7:233,8:183,9:133,10:133,11:133,12:183,13:233,14:283,15:333,16:333,17:333,18:333,19:333,20:383,21:433,22:433,23:433,24:433,25:433,26:483,27:533,28:583,29:633,30:633,31:633,32:583,33:533,34:483,35:433,36:433,37:433,38:433,39:433,40:383,41:383,42:383,43:383,44:383,51:183,52:233,53:283,54:333,61:383,62:383,63:383,64:383,71:583,72:533,73:483,74:433,1000:157,2000:207,3000:157,4000:207,5000:157,6000:207,7000:157,8000:207,9000:559,10000:609,11000:559,12000:609,13000:559,14000:609,15000:559,16000:609}
    ykoor={1:533,2:483,3:433,4:383,5:333,6:333,7:333,8:333,9:333,10:283,11:233,12:233,13:233,14:233,15:233,16:183,17:133,18:83,19:33,20:33,21:33,22:83,23:133,24:183,25:233,26:233,27:233,28:233,29:233,30:283,31:333,32:333,33:333,34:333,35:333,36:383,37:433,38:483,39:533,40:533,41:483,42:433,43:383,44:333,51:283,52:283,53:283,54:283,61:83,62:133,63:183,64:233,71:283,72:283,73:283,74:283,1000:458,2000:458,3000:508,4000:508,5000:58,6000:58,7000:108,8000:108,9000:58,10000:58,11000:108,12000:108,13000:458,14000:458,15000:508,16000:508}
    y1,y2,y3,y4=1000,2000,3000,4000 
    b1,b2,b3,b4=5000,6000,7000,8000
    r1,r2,r3,r4=9000,10000,11000,12000
    g1,g2,g3,g4=13000,14000,15000,16000
    b1u,b2u,b3u,b4u=0,0,0,0
    r1u,r2u,r3u,r4u=0,0,0,0
    g1u,g2u,g3u,g4u=0,0,0,0
    my1,my2,my3,my4=1000,2000,3000,4000 
    mb1,mb2,mb3,mb4=5000,6000,7000,8000
    mr1,mr2,mr3,mr4=9000,10000,11000,12000
    mg1,mg2,mg3,mg4,=13000,14000,15000,16000
    bry,brb,brr,brg=0,0,0,0
    pocy,pocb,pocr,pocg=0,0,0,0
    tas=0
    setup=1
    setup2=6
    plyr=1
    first=0 
    roldrop=0 
    gucci=0 
    end=False
    posedina.blit(yellow,[157,458])
    posedina.blit(yellow,[207,458])
    posedina.blit(yellow,[157,508])
    posedina.blit(yellow,[207,508])
    posedina.blit(green,[559,458])
    posedina.blit(green,[609,458])
    posedina.blit(green,[559,508])
    posedina.blit(green,[609,508])
    posedina.blit(blue,[157,58])
    posedina.blit(blue,[207,58])
    posedina.blit(blue,[157,108])
    posedina.blit(blue,[207,108])
    posedina.blit(red,[559,58])
    posedina.blit(red,[609,58])
    posedina.blit(red,[559,108])
    posedina.blit(red,[609,108])
    player=1
    movement=''
    staraxkoor=100000
    staraykoor=100000
    
    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=True
        mispose=pygame.mouse.get_pos()
        misklick=pygame.mouse.get_pressed()
        if roldrop==1:
            tas = roll(tas)
            player = check_turn(player, tas, [y1, y2, y3, y4])
            if first==0:
                if player%4==1:
                    posedina.blit(ro1,[377,277])
                if player%4==2:
                    posedina.blit(ro2,[377,277])
                if player%4==3:
                    posedina.blit(ro3,[377,277])
                if player%4==0 and player>0:
                    posedina.blit(ro4,[377,277])

            if misklick[0]==1 and mispose[0]>=377 and mispose[0]<=422 and mispose[1]>=277 and mispose[1]<=322:
                roll(tas)
                tas=roll(tas)
                first=1
            if misklick[0]==0 and first==1:
                roldrop=0
                setup=1
                if player==0:
                    player=plyr
                    if plyr==1:
                        bry=bry+1
                    if plyr==2:
                        brb=brb+1
                    if plyr==3:
                        brr=brr+1
                    if plyr==4:
                        brg=brg+1
   
        if player%4==1:
            if pocy==0:
                gucci=0
                if tas!=6:
                    first=0
                    player=0
                    tas=0
                    roldrop=1
                    posedina.blit(ro1,[377,277])
                    if bry==2:
                        setup=6
                        pocy=1
                else:
                    pocy=1
            if pocy==1 and gucci==1:
                first=0
                roldrop=1
                posedina.blit(ro1,[377,277])
                gucci=0
            if tas==1000:
                gucci=1
            if (tas==6 and (y1==1000 or y2==2000 or y3==3000 or y4==4000)) or (y1+tas<45 and y1+tas!=y2 and y1+tas!=y3 and y1+tas!=y4) or (y2+tas<45 and y2+tas!=y1 and y2+tas!=y3 and y2+tas!=y4) or (y3+tas<45 and y3+tas!=y1 and y3+tas!=y2 and y3+tas!=y4) or (y4+tas<45 and y4+tas!=y1 and y4+tas!=y2 and y4+tas!=y3):
                mispose=pygame.mouse.get_pos()
                misklick=pygame.mouse.get_pressed()
                if misklick[0]==1 and mispose[0]>=xkoor[y1] and mispose[0]<=xkoor[y1]+33 and mispose[1]>=ykoor[y1] and mispose[1]<=ykoor[y1]+33:
                    movement='Y1'
                    staraxkoor=xkoor[y1]
                    staraykoor=ykoor[y1]
                if misklick[0]==1 and mispose[0]>=xkoor[y2] and mispose[0]<=xkoor[y2]+33 and mispose[1]>=ykoor[y2] and mispose[1]<=ykoor[y2]+33:
                    movement='Y2'
                    staraxkoor=xkoor[y2]
                    staraykoor=ykoor[y2]
                if misklick[0]==1 and mispose[0]>=xkoor[y3] and mispose[0]<=xkoor[y3]+33 and mispose[1]>=ykoor[y3] and mispose[1]<=ykoor[y3]+33:
                    movement='Y3'
                    staraxkoor=xkoor[y3]
                    staraykoor=ykoor[y3]
                if misklick[0]==1 and mispose[0]>=xkoor[y4] and mispose[0]<=xkoor[y4]+33 and mispose[1]>=ykoor[y4] and mispose[1]<=ykoor[y4]+33:
                    movement='Y4'
                    staraxkoor=xkoor[y4]
                    staraykoor=ykoor[y4]
                if tas<6:
                    if y1<1000 and movement=='Y1' and y1+tas<45 and y1+tas!=y2 and y1+tas!=y3 and y1+tas!=y4:
                        y1=y1+tas
                        posedina.blit(yellow,[xkoor[y1],ykoor[y1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y2<1000 and movement=='Y2' and y2+tas<45 and y2+tas!=y1 and y2+tas!=y3 and y2+tas!=y4:
                        y2=y2+tas
                        posedina.blit(yellow,[xkoor[y2],ykoor[y2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y3<1000 and movement=='Y3' and y3+tas<45 and y3+tas!=y1 and y3+tas!=y2 and y3+tas!=y4:
                        y3=y3+tas
                        posedina.blit(yellow,[xkoor[y3],ykoor[y3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y4<1000 and movement=='Y4' and y4+tas<45 and y4+tas!=y1 and y4+tas!=y2 and y4+tas!=y3:
                        y4=y4+tas
                        posedina.blit(yellow,[xkoor[y4],ykoor[y4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                if tas==6:
                    if y1<1000 and movement=='Y1' and y1+tas<45 and y1+tas!=y2 and y1+tas!=y3 and y1+tas!=y4:
                        y1=y1+tas
                        posedina.blit(yellow,[xkoor[y1],ykoor[y1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y2<1000 and movement=='Y2' and y2+tas<45 and y2+tas!=y1 and y2+tas!=y3 and y2+tas!=y4:
                        y2=y2+tas
                        posedina.blit(yellow,[xkoor[y2],ykoor[y2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y3<1000 and movement=='Y3' and y3+tas<45 and y3+tas!=y1 and y3+tas!=y2 and y3+tas!=y4:
                        y3=y3+tas
                        posedina.blit(yellow,[xkoor[y3],ykoor[y3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y4<1000 and movement=='Y4' and y4+tas<45 and y4+tas!=y1 and y4+tas!=y2 and y4+tas!=y3:
                        y4=y4+tas
                        posedina.blit(yellow,[xkoor[y4],ykoor[y4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y1==1000 and movement=='Y1' and (y2!=1 and y3!=1 and y4!=1):
                        y1=1
                        posedina.blit(yellow,[xkoor[y1],ykoor[y1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y2==2000 and movement=='Y2' and (y1!=1 and y3!=1 and y4!=1):
                        y2=1
                        posedina.blit(yellow,[xkoor[y2],ykoor[y2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y3==3000 and movement=='Y3' and (y1!=1 and y2!=1 and y4!=1):
                        y3=1
                        posedina.blit(yellow,[xkoor[y3],ykoor[y3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if y4==4000 and movement=='Y4' and (y1!=1 and y2!=1 and y3!=1):
                        y4=1
                        posedina.blit(yellow,[xkoor[y4],ykoor[y4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                if y1==b1 or y2==b1 or y3==b1 or y4==b1:
                    b1=mb1
                    posedina.blit(blue,[xkoor[mb1],ykoor[mb1]])
                if y1==b2 or y2==b2 or y3==b2 or y4==b2:
                    b2=mb2
                    posedina.blit(blue,[xkoor[mb2],ykoor[mb2]])
                if y1==b3 or y2==b3 or y3==b3 or y4==b3:
                    b3=mb3
                    posedina.blit(blue,[xkoor[mb3],ykoor[mb3]])
                if y1==b4 or y2==b4 or y3==b4 or y4==b4:
                    b4=mb4
                    posedina.blit(blue,[xkoor[mb4],ykoor[mb4]])
                if y1==r1 or y2==r1 or y3==r1 or y4==r1:
                    r1=mr1
                    posedina.blit(red,[xkoor[mr1],ykoor[mr1]])
                if y1==r2 or y2==r2 or y3==r2 or y4==r2:
                    r2=mr2
                    posedina.blit(red,[xkoor[mr2],ykoor[mr2]])
                if y1==r3 or y2==r3 or y3==r3 or y4==r3:
                    r3=mr3
                    posedina.blit(red,[xkoor[mr3],ykoor[mr3]])
                if y1==r4 or y2==r4 or y3==r4 or y4==r4:
                    r4=mr4
                    posedina.blit(red,[xkoor[mr4],ykoor[mr4]])
                if y1==g1 or y2==g1 or y3==g1 or y4==g1:
                    g1=mg1
                    posedina.blit(green,[xkoor[mg1],ykoor[mg1]])
                if y1==g2 or y2==g2 or y3==g2 or y4==g2:
                    g2=mg2
                    posedina.blit(green,[xkoor[mg2],ykoor[mg2]])
                if y1==g3 or y2==g3 or y3==g3 or y4==g3:
                    g3=mg3
                    posedina.blit(green,[xkoor[mg3],ykoor[mg3]])
                if y1==g4 or y2==g4 or y3==g4 or y4==g4:
                    g4=mg4
                    posedina.blit(green,[xkoor[mg4],ykoor[mg4]])
                if gucci==1 and tas==6:
                    player=player-1
                    tas=1000
            else:
                if player!=1 and player!=0 and roldrop==0:
                    player=player+1
                    gucci=1
                    tas=1000
            if (y1==41 or y1==42 or y1==43 or y1==44) and (y2==41 or y2==42 or y2==43 or y2==44) and (y3==41 or y3==42 or y3==43 or y3==44) and (y4==41 or y4==42 or y4==43 or y4==44):
                win1()
                end=True
                
        if player%4==2:
            if pocb==0:
                if brb==0:
                    tas=0
                plyr=2
            if pocb==0:
                gucci=0
                if tas!=6:
                    first=0
                    player=0
                    roldrop=1
                    posedina.blit(ro2,[377,277])
                    if brb==2:
                        setup=6
                        pocb=1
                else:
                    pocb=1
            if pocb==1 and gucci==1:
                first=0
                roldrop=1
                posedina.blit(ro2,[377,277])
                gucci=0
            if tas==1000:
                gucci=1
            if (tas==6 and (b1==5000 or b2==6000 or b3==7000 or b4==8000)) or (b1+tas+40!=b2 and b1+tas+40!=b3 and b1+tas+40!=b4 and b1u==1) or (b2+tas+40!=b1 and b2+tas+40!=b3 and b2+tas+40!=b4 and b2u==1) or (b3+tas+40!=b1 and b3+tas+40!=b2 and b3+tas+40!=b4 and b3u==1) or (b4+tas+40!=b1 and b4+tas+40!=b2 and b4+tas+40!=b3 and b4u==1) or (b1<100 and b1+tas<55 and b1+tas!=b2 and b1+tas!=b3 and b1+tas!=b4 and b1u==0) or (b2<100 and b2+tas<55 and b2+tas!=b1 and b2+tas!=b3 and b2+tas!=b4 and b2u==0) or (b3<100 and b3+tas<55 and b3+tas!=b1 and b3+tas!=b2 and b3+tas!=b4 and b3u==0) or (b4<100 and b4+tas<55 and b4+tas!=b1 and b4+tas!=b2 and b4+tas!=b3 and b4u==0):
                mispose=pygame.mouse.get_pos()
                misklick=pygame.mouse.get_pressed()
                if misklick[0]==1 and mispose[0]>=xkoor[b1] and mispose[0]<=xkoor[b1]+33 and mispose[1]>=ykoor[b1] and mispose[1]<=ykoor[b1]+33:
                    movement='B1'
                    staraxkoor=xkoor[b1]
                    staraykoor=ykoor[b1]
                if misklick[0]==1 and mispose[0]>=xkoor[b2] and mispose[0]<=xkoor[b2]+33 and mispose[1]>=ykoor[b2] and mispose[1]<=ykoor[b2]+33:
                    movement='B2'
                    staraxkoor=xkoor[b2]
                    staraykoor=ykoor[b2]
                if misklick[0]==1 and mispose[0]>=xkoor[b3] and mispose[0]<=xkoor[b3]+33 and mispose[1]>=ykoor[b3] and mispose[1]<=ykoor[b3]+33:
                    movement='B3'
                    staraxkoor=xkoor[b3]
                    staraykoor=ykoor[b3]
                if misklick[0]==1 and mispose[0]>=xkoor[b4] and mispose[0]<=xkoor[b4]+33 and mispose[1]>=ykoor[b4] and mispose[1]<=ykoor[b4]+33:
                    movement='B4'
                    staraxkoor=xkoor[b4]
                    staraykoor=ykoor[b4]
                if tas<6:
                    if b1<1000 and movement=='B1' and (b1+tas+40!=b2 and b1+tas+40!=b3 and b1+tas+40!=b4) and b1+tas<55 and b1+tas!=b2 and b1+tas!=b3 and b1+tas!=b4 and not (b1u==1 and b1+tas>14):
                        b1=b1+tas
                        if b1>40 and b1u==0:
                            b1=b1-40
                            b1u=1
                        if b1>10 and b1<15 and b1u==1:
                            if b1==11:
                                b1=51
                                b1u=0
                            if b1==12:
                                b1=52
                                b1u=0
                            if b1==13:
                                b1=53
                                b1u=0
                            if b1==14:
                                b1==54
                                b1u=0
                        posedina.blit(blue,[xkoor[b1],ykoor[b1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b2<1000 and movement=='B2' and (b2+tas+40!=b1 and b2+tas+40!=b3 and b2+tas+40!=b4) and b2+tas<55 and b2+tas!=b1 and b2+tas!=b3 and b2+tas!=b4 and not (b2u==1 and b2+tas>14):
                        b2=b2+tas
                        if b2>40 and b2u==0:
                            b2=b2-40
                            b2u=1
                        if b2>10 and b2<15 and b2u==1:
                            if b2==11:
                                b2=51
                                b2u=0
                            if b2==12:
                                b2=52
                                b2u=0
                            if b2==13:
                                b2=53
                                b2u=0
                            if b2==14:
                                b2=54
                                b2u=0
                        posedina.blit(blue,[xkoor[b2],ykoor[b2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b3<1000 and movement=='B3' and (b3+tas+40!=b1 and b3+tas+40!=b2 and b3+tas+40!=b4) and b3+tas<55 and b3+tas!=b1 and b3+tas!=b2 and b3+tas!=b4 and not (b3u==1 and b3+tas>14):
                        b3=b3+tas
                        if b3>40 and b3u==0:
                            b3=b3-40
                            b3u=1
                        if b3>10 and b3<15 and b3u==1:
                            if b3==11:
                                b3=51
                                b3u=0
                            if b3==12:
                                b3=52
                                b3u=0
                            if b3==13:
                                b3=53
                                b3u=0
                            if b3==14:
                                b3=54
                                b3u=0
                        posedina.blit(blue,[xkoor[b3],ykoor[b3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b4<1000 and movement=='B4' and (b4+tas+40!=b1 and b4+tas+40!=b2 and b4+tas+40!=b3) and b4+tas<55 and b4+tas!=b1 and b4+tas!=b2 and b4+tas!=b3 and not (b4u==1 and b4+tas>14):
                        b4=b4+tas
                        if b4>40 and b4u==0:
                            b4=b4-40
                            b4u=1
                        if b4>10 and b4<15 and b4u==1:
                            if b4==11:
                                b4=51
                                b4u=0
                            if b4==12:
                                b4=52
                                b4u=0
                            if b4==13:
                                b4=53
                                b4u=0
                            if b4==14:
                                b4=54
                                b4u=0
                        posedina.blit(blue,[xkoor[b4],ykoor[b4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                if tas==6:
                    if b1<1000 and movement=='B1' and (b1+tas+40!=b2 and b1+tas+40!=b3 and b1+tas+40!=b4) and b1+tas<55 and b1+tas!=b2 and b1+tas!=b3 and b1+tas!=b4 and not (b1u==1 and b1+tas>14):
                        b1=b1+tas
                        if b1>40 and b1u==0:
                            b1=b1-40
                            b1u=1
                        if b1>10 and b1<15 and b1u==1:
                            if b1==11:
                                b1=51
                                b1u=0
                            if b1==12:
                                b1=52
                                b1u=0
                            if b1==13:
                                b1=53
                                b1u=0
                            if b1==14:
                                b1==54
                                b1u=0
                        posedina.blit(blue,[xkoor[b1],ykoor[b1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b2<1000 and movement=='B2' and (b2+tas+40!=b1 and b2+tas+40!=b3 and b2+tas+40!=b4) and b2+tas<55 and b2+tas!=b1 and b2+tas!=b3 and b2+tas!=b4 and not (b2u==1 and b2+tas>14):
                        b2=b2+tas
                        if b2>40 and b2u==0:
                            b2=b2-40
                            b2u=1
                        if b2>10 and b2<15 and b2u==1:
                            if b2==11:
                                b2=51
                                b2u=0
                            if b2==12:
                                b2=52
                                b2u=0
                            if b2==13:
                                b2=53
                                b2u=0
                            if b2==14:
                                b2==54
                                b2u=0
                        posedina.blit(blue,[xkoor[b2],ykoor[b2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b3<1000 and movement=='B3' and (b3+tas+40!=b1 and b3+tas+40!=b2 and b3+tas+40!=b4) and b3+tas<55 and b3+tas!=b1 and b3+tas!=b2 and b3+tas!=b4 and not (b3u==1 and b3+tas>14):
                        b3=b3+tas
                        if b3>40 and b3u==0:
                            b3=b3-40
                            b3u=1
                        if b3>10 and b3<15 and b3u==1:
                            if b3==11:
                                b3=51
                                b3u=0
                            if b3==12:
                                b3=52
                                b3u=0
                            if b3==13:
                                b3=53
                                b3u=0
                            if b3==14:
                                b3=54
                                b3u=0
                        posedina.blit(blue,[xkoor[b3],ykoor[b3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b4<1000 and movement=='B4' and (b4+tas+40!=b1 and b4+tas+40!=b2 and b4+tas+40!=b3) and b4+tas<55 and b4+tas!=b1 and b4+tas!=b2 and b4+tas!=b3 and not (b4u==1 and b4+tas>14):
                        b4=b4+tas
                        if b4>40 and b4u==0:
                            b4=b4-40
                            b4u=1
                        if b4>10 and b4<15 and b4u==1:
                            if b4==11:
                                b4=51
                                b4u=0
                            if b4==12:
                                b4=52
                                b4u=0
                            if b4==13:
                                b4=53
                                b4u=0
                            if b4==14:
                                b4=54
                                b4u=0
                        posedina.blit(blue,[xkoor[b4],ykoor[b4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b1==5000 and movement=='B1' and (b2!=11 and b3!=11 and b4!=11):
                        b1=11
                        b1u=0
                        posedina.blit(blue,[xkoor[b1],ykoor[b1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b2==6000 and movement=='B2' and (b1!=11 and b3!=11 and b4!=11):
                        b2=11
                        b2u=0
                        posedina.blit(blue,[xkoor[b2],ykoor[b2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b3==7000 and movement=='B3' and (b1!=11 and b2!=11 and b4!=11):
                        b3=11
                        b3u=0
                        posedina.blit(blue,[xkoor[b3],ykoor[b3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if b4==8000 and movement=='B4' and (b1!=11 and b2!=11 and b3!=11):
                        b4=11
                        b4u=0
                        posedina.blit(blue,[xkoor[b4],ykoor[b4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                if b1==y1 or b2==y1 or b3==y1 or b4==y1:
                    y1=my1
                    posedina.blit(yellow,[xkoor[my1],ykoor[my1]])
                if b1==y2 or b2==y2 or b3==y2 or b4==y2:
                    y2=my2
                    posedina.blit(yellow,[xkoor[my2],ykoor[my2]])
                if b1==y3 or b2==y3 or b3==y3 or b4==y3:
                    y3=my3
                    posedina.blit(yellow,[xkoor[my3],ykoor[my3]])
                if b1==y4 or b2==y4 or b3==y4 or b4==y4:
                    y4=my4
                    posedina.blit(yellow,[xkoor[my4],ykoor[my4]])
                if b1==r1 or b2==r1 or b3==r1 or b4==r1:
                    r1=mr1
                    posedina.blit(red,[xkoor[mr1],ykoor[mr1]])
                if b1==r2 or b2==r2 or b3==r2 or b4==r2:
                    r2=mr2
                    posedina.blit(red,[xkoor[mr2],ykoor[mr2]])
                if b1==r3 or b2==r3 or b3==r3 or b4==r3:
                    r3=mr3
                    posedina.blit(red,[xkoor[mr3],ykoor[mr3]])
                if b1==r4 or b2==r4 or b3==r4 or b4==r4:
                    r4=mr4
                    posedina.blit(red,[xkoor[mr4],ykoor[mr4]])
                if b1==g1 or b2==g1 or b3==g1 or b4==g1:
                    g1=mg1
                    posedina.blit(green,[xkoor[mg1],ykoor[mg1]])
                if b1==g2 or b2==g2 or b3==g2 or b4==g2:
                    g2=mg2
                    posedina.blit(green,[xkoor[mg2],ykoor[mg2]])
                if b1==g3 or b2==g3 or b3==g3 or b4==g3:
                    g3=mg3
                    posedina.blit(green,[xkoor[mg3],ykoor[mg3]])
                if b1==g4 or b2==g4 or b3==g4 or b4==g4:
                    g4=mg4
                    posedina.blit(green,[xkoor[mg4],ykoor[mg4]])
                if gucci==1 and tas==6:
                    player=player-1
                    tas=1000
            else:
                if player!=2 and roldrop==0:
                    player=player+1
                    gucci=1
                    tas=1000

            if (b1==51 or b1==52 or b1==53 or b1==54) and (b2==51 or b2==52 or b2==53 or b2==54) and (b3==51 or b3==52 or b3==53 or b3==54) and (b4==51 or b4==52 or b4==53 or b4==54):
                win2()
                end=True

        if player%4==3:
            if brr==0:
                tas=0
            plyr=3
            if pocr==0:
                gucci=0
                if tas!=6:
                    first=0
                    player=0
                    roldrop=1
                    posedina.blit(ro3,[377,277])
                    if brr==2:
                        setup=6
                        pocr=1
                else:
                    pocr=1
            if pocr==1 and gucci==1:
                first=0
                roldrop=1
                posedina.blit(ro3,[377,277])
                gucci=0
            if tas==1000:
                gucci=1
            if (tas==6 and (r1==9000 or r2==10000 or r3==11000 or r4==12000)) or (r1+tas+40!=r2 and r1+tas+40!=r3 and r1+tas+40!=r4 and r1u==1) or (r2+tas+40!=r1 and r2+tas+40!=r3 and r2+tas+40!=r4 and r2u==1) or (r3+tas+40!=r1 and r3+tas+40!=r2 and r3+tas+40!=r4 and r3u==1) or (r4+tas+40!=r1 and r4+tas+40!=r2 and r4+tas+40!=r3 and r4u==1) or (r1<100 and r1+tas<65 and r1+tas!=r2 and r1+tas!=r3 and r1+tas!=r4 and r1u==0) or (r2<100 and r2+tas<65 and r2+tas!=r1 and r2+tas!=r3 and r2+tas!=r4 and r2u==0) or (r3<100 and r3+tas<65 and r3+tas!=r1 and r3+tas!=r2 and r3+tas!=r4 and r3u==0) or (r4<100 and r4+tas<65 and r4+tas!=r1 and r4+tas!=r2 and r4u==0):
                mispose=pygame.mouse.get_pos()
                misklick=pygame.mouse.get_pressed()
                if misklick[0]==1 and mispose[0]>=xkoor[r1] and mispose[0]<=xkoor[r1]+33 and mispose[1]>=ykoor[r1] and mispose[1]<=ykoor[r1]+33:
                    movement='R1'
                    staraxkoor=xkoor[r1]
                    staraykoor=ykoor[r1]
                if misklick[0]==1 and mispose[0]>=xkoor[r2] and mispose[0]<=xkoor[r2]+33 and mispose[1]>=ykoor[r2] and mispose[1]<=ykoor[r2]+33:
                    movement='R2'
                    staraxkoor=xkoor[r2]
                    staraykoor=ykoor[r2]
                if misklick[0]==1 and mispose[0]>=xkoor[r3] and mispose[0]<=xkoor[r3]+33 and mispose[1]>=ykoor[r3] and mispose[1]<=ykoor[r3]+33:
                    movement='R3'
                    staraxkoor=xkoor[r3]
                    staraykoor=ykoor[r3]
                if misklick[0]==1 and mispose[0]>=xkoor[r4] and mispose[0]<=xkoor[r4]+33 and mispose[1]>=ykoor[r4] and mispose[1]<=ykoor[r4]+33:
                    movement='R4'
                    staraxkoor=xkoor[r4]
                    staraykoor=ykoor[r4]
                if tas<6:
                    if r1<1000 and movement=='R1' and (r1+tas+40!=r2 and r1+tas+40!=r3 and r1+tas+40!=r4) and r1+tas<65 and r1+tas!=r2 and r1+tas!=r3 and r1+tas!=r4 and not (r1u==1 and r1+tas>24):
                        r1=r1+tas
                        if r1>40 and r1u==0:
                            r1=r1-40
                            r1u=1
                        if r1>20 and r1<25 and r1u==1:
                            if r1==21:
                                r1=61
                                r1u=0
                            if r1==22:
                                r1=62
                                r1u=0
                            if r1==23:
                                r1=63
                                r1u=0
                            if r1==24:
                                r1=64
                                r1u=0
                        posedina.blit(red,[xkoor[r1],ykoor[r1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r2<1000 and movement=='R2' and (r2+tas+40!=r1 and r2+tas+40!=r3 and r2+tas+40!=r4) and r2+tas<65 and r2+tas!=r1 and r2+tas!=r3 and r2+tas!=r4 and not (r2u==1 and r2+tas>24):
                        r2=r2+tas
                        if r2>40 and r2u==0:
                            r2=r2-40
                            r2u=1
                        if r2>20 and r2<25 and r2u==1:
                            if r2==21:
                                r2=61
                                r2u=0
                            if r2==22:
                                r2=62
                                r2u=0
                            if r2==23:
                                r2=63
                                r2u=0
                            if r2==24:
                                r2=64
                                r2u=0
                        posedina.blit(red,[xkoor[r2],ykoor[r2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r3<1000 and movement=='R3' and (r3+tas+40!=r1 and r3+tas+40!=r2 and r3+tas+40!=r4) and r3+tas<65 and r3+tas!=r1 and r3+tas!=r2 and r3+tas!=r4 and not (r3u==1 and r3+tas>24):
                        r3=r3+tas
                        if r3>40 and r3u==0:
                            r3=r3-40
                            r3u=1
                        if r3>20 and r3<25 and r3u==1:
                            if r3==21:
                                r3=61
                                r3u=0
                            if r3==22:
                                r3=62
                                r3u=0
                            if r3==23:
                                r3=63
                                r3u=0
                            if r3==24:
                                r3=64
                                r3u=0
                        posedina.blit(red,[xkoor[r3],ykoor[r3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r4<1000 and movement=='R4' and (r4+tas+40!=r1 and r4+tas+40!=r2 and r4+tas+40!=r3) and r4+tas<65 and r4+tas!=r1 and r4+tas!=r2 and r4+tas!=r3 and not (r4u==1 and r4+tas>24):
                        r4=r4+tas
                        if r4>40 and r4u==0:
                            r4=r4-40
                            r4u=1
                        if r4>20 and r4<25 and r4u==1:
                            if r4==21:
                                r4=61
                                r4u=0
                            if r4==22:
                                r4=62
                                r4u=0
                            if r4==23:
                                r4=63
                                r4u=0
                            if r4==24:
                                r4=64
                                r4u=0
                        posedina.blit(red,[xkoor[r4],ykoor[r4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                if tas==6:
                    if r1<1000 and movement=='R1' and (r1+tas+40!=r2 and r1+tas+40!=r3 and r1+tas+40!=r4) and r1+tas<65 and r1+tas!=r2 and r1+tas!=r3 and r1+tas!=r4 and not (r1u==1 and r1+tas>24):
                        r1=r1+tas
                        if r1>40:
                            r1=r1-40
                            r1u=1
                        if r1>20 and r1<25 and r1u==1:
                            if r1==21:
                                r1=61
                                r1u=0
                            if r1==22:
                                r1=62
                                r1u=0
                            if r1==23:
                                r1=63
                                r1u=0
                            if r1==24:
                                r1=64
                                r1u=0
                        posedina.blit(red,[xkoor[r1],ykoor[r1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r2<1000 and movement=='R2' and (r2+tas+40!=r1 and r2+tas+40!=r3 and r2+tas+40!=r4) and r2+tas<65 and r2+tas!=r1 and r2+tas!=r3 and r2+tas!=r4 and not (r2u==1 and r2+tas>24):
                        r2=r2+tas
                        if r2>40:
                            r2=r2-40
                            r2u=1
                        if r2>20 and r2<25 and r2u==1:
                            if r2==21:
                                r2=61
                                r2u=0
                            if r2==22:
                                r2=62
                                r2u=0
                            if r2==23:
                                r2=63
                                r2u=0
                            if r2==24:
                                r2=64
                                r2u=0
                        posedina.blit(red,[xkoor[r2],ykoor[r2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r3<1000 and movement=='R3' and (r3+tas+40!=r1 and r3+tas+40!=r2 and r3+tas+40!=r4) and r3+tas<65 and r3+tas!=b1 and r3+tas!=r2 and r3+tas!=r4 and not (r3u==1 and r3+tas>24):
                        r3=r3+tas
                        if r3>40:
                            r3=r3-40
                            r3u=1
                        if r3>20 and r3<25 and r3u==1:
                            if r3==21:
                                r3=61
                                r3u=0
                            if r3==22:
                                r3=62
                                r3u=0
                            if r3==23:
                                r3=63
                                r3u=0
                            if r3==24:
                                r3=64
                                r3u=0
                        posedina.blit(red,[xkoor[r3],ykoor[r3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r4<1000 and movement=='R4' and (r4+tas+40!=r1 and r4+tas+40!=r2 and r4+tas+40!=r3) and r4+tas<65 and r4+tas!=r1 and r4+tas!=r2 and r4+tas!=r3 and not (r4u==1 and r4+tas>24):
                        r4=r4+tas
                        if r4>40:
                            r4=r4-40
                            r4u=1
                        if r4>20 and r4<25 and r4u==1:
                            if r4==21:
                                r4=61
                                r4u=0
                            if r4==22:
                                r4=62
                                r4u=0
                            if r4==23:
                                r4=63
                                r4u=0
                            if r4==24:
                                r4=64
                                r4u=0
                        posedina.blit(red,[xkoor[r4],ykoor[r4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r1==9000 and movement=='R1' and (r2!=21 or r3!=21 or r4!=21):
                        r1=21
                        r1u=0
                        posedina.blit(red,[xkoor[r1],ykoor[r1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r2==10000 and movement=='R2' and (r1!=21 or r3!=21 or r4!=21):
                        r2=21
                        r2u=0
                        posedina.blit(red,[xkoor[r2],ykoor[r2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r3==11000 and movement=='R3' and (r1!=21 or r2!=21 or r4!=21):
                        r3=21
                        r3u=0
                        posedina.blit(red,[xkoor[r3],ykoor[r3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if r4==12000 and movement=='R4' and (r1!=21 or r2!=21 or r3!=21):
                        r4=21
                        r4u=0
                        posedina.blit(red,[xkoor[r4],ykoor[r4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                if r1==y1 or r2==y1 or r3==y1 or r4==y1:
                    y1=my1
                    posedina.blit(yellow,[xkoor[my1],ykoor[my1]])
                if r1==y2 or r2==y2 or r3==y2 or r4==y2:
                    y2=my2
                    posedina.blit(yellow,[xkoor[my2],ykoor[my2]])
                if r1==y3 or r2==y3 or r3==y3 or r4==y3:
                    y3=my3
                    posedina.blit(yellow,[xkoor[my3],ykoor[my3]])
                if r1==y4 or r2==y4 or r3==y4 or r4==y4:
                    y4=my4
                    posedina.blit(yellow,[xkoor[my4],ykoor[my4]])
                if r1==b1 or r2==b1 or r3==b1 or r4==b1:
                    b1=mb1
                    posedina.blit(blue,[xkoor[mb1],ykoor[mb1]])
                if r1==b2 or r2==b2 or r3==b2 or r4==b2:
                    b2=mb2
                    posedina.blit(blue,[xkoor[mb2],ykoor[mb2]])
                if r1==b3 or r2==b3 or r3==b3 or r4==b3:
                    b3=mb3
                    posedina.blit(blue,[xkoor[mb3],ykoor[mb3]])
                if r1==b4 or r2==b4 or r3==b4 or r4==b4:
                    b4=mb4
                    posedina.blit(blue,[xkoor[mb4],ykoor[mb4]])
                if r1==g1 or r2==g1 or r3==g1 or r4==g1:
                    g1=mg1
                    posedina.blit(green,[xkoor[mg1],ykoor[mg1]])
                if r1==g2 or r2==g2 or r3==g2 or r4==g2:
                    g2=mg2
                    posedina.blit(green,[xkoor[mg2],ykoor[mg2]])
                if r1==g3 or r2==g3 or r3==g3 or r4==g3:
                    g3=mg3
                    posedina.blit(green,[xkoor[mg3],ykoor[mg3]])
                if r1==g4 or r2==g4 or r3==g4 or r4==g4:
                    g4=mg4
                    posedina.blit(green,[xkoor[mg4],ykoor[mg4]])
                if gucci==1 and tas==6:
                    player=player-1
                    tas=1000
            else:
                if player!=3 and roldrop==0:
                    player=player+1
                    gucci=1
                    tas=1000
            if (r1==61 or r1==62 or r1==63 or r1==64) and (r2==61 or r2==62 or r2==63 or r2==64) and (r3==61 or r3==62 or r3==63 or r3==64) and (r4==61 or r4==62 or r4==63 or r4==64):
                win3()
                end=True
                    
        if player%4==0 and player>0:
            if brg==0:
                tas=0
            plyr=4
            if pocg==0:
                gucci=0
                if tas!=6:
                    player=0
                    roldrop=1
                    posedina.blit(ro4,[377,277])
                    first=0
                    if brg==2:
                        setup=6
                        pocg=1
                else:
                    pocg=1
            if pocg==1 and gucci==1:
                first=0
                roldrop=1
                posedina.blit(ro4,[377,277])
                gucci=0
            if tas==1000:
                gucci=1
            if (tas==6 and (g1==13000 or g2==14000 or g3==15000 or g4==16000)) or (g1+tas+40!=g2 and g1+tas+40!=g3 and g1+tas+40!=g4 and g1u==1) or (g2+tas+40!=g1 and g2+tas+40!=g3 and g2+tas+40!=g4 and g2u==1) or (g3+tas+40!=g1 and g3+tas+40!=g2 and g3+tas+40!=g4 and g3u==1) or (g4+tas+40!=g1 and g4+tas+40!=g2 and g4+tas+40!=g3 and g4u==1) or (g1<100 and g1+tas<75 and g1+tas!=g2 and g1+tas!=g3 and g1+tas!=g4 and g1u==0) or (g2<100 and g2+tas<75 and g2+tas!=g1 and g2+tas!=g3 and g2+tas!=g4 and g2u==0) or (g3<100 and g3+tas<75 and g3+tas!=g1 and g3+tas!=g2 and g3+tas!=g4 and g3u==0) or (g4<100 and g4+tas<75 and g4+tas!=g1 and g4+tas!=g2 and g4+tas!=g3 and g4u==0):
                mispose=pygame.mouse.get_pos()
                misklick=pygame.mouse.get_pressed()
                if misklick[0]==1 and mispose[0]>=xkoor[g1] and mispose[0]<=xkoor[g1]+33 and mispose[1]>=ykoor[g1] and mispose[1]<=ykoor[g1]+33:
                    movement='G1'
                    staraxkoor=xkoor[g1]
                    staraykoor=ykoor[g1]
                if misklick[0]==1 and mispose[0]>=xkoor[g2] and mispose[0]<=xkoor[g2]+33 and mispose[1]>=ykoor[g2] and mispose[1]<=ykoor[g2]+33:
                    movement='G2'
                    staraxkoor=xkoor[g2]
                    staraykoor=ykoor[g2]
                if misklick[0]==1 and mispose[0]>=xkoor[g3] and mispose[0]<=xkoor[g3]+33 and mispose[1]>=ykoor[g3] and mispose[1]<=ykoor[g3]+33:
                    movement='G3'
                    staraxkoor=xkoor[g3]
                    staraykoor=ykoor[g3]
                if misklick[0]==1 and mispose[0]>=xkoor[g4] and mispose[0]<=xkoor[g4]+33 and mispose[1]>=ykoor[g4] and mispose[1]<=ykoor[g4]+33:
                    movement='G4'
                    staraxkoor=xkoor[g4]
                    staraykoor=ykoor[g4]
                if tas<6:
                    if g1<1000 and movement=='G1' and (g1+tas+40!=g2 and g1+tas+40!=g3 and g1+tas+40!=g4) and g1+tas<75 and g1+tas!=g2 and g1+tas!=g3 and g1+tas!=g4 and not (g1u==1 and g1+tas>34):
                        g1=g1+tas
                        if g1>40:
                            g1=g1-40
                            g1u=1
                        if g1>30 and g1<35 and g1u==1:
                            if g1==31:
                                g1=71
                                g1u=0
                            if g1==32:
                                g1=72
                                g1u=0
                            if g1==33:
                                g1=73
                                g1u=0
                            if g1==34:
                                g1=74
                                g1u=0
                        posedina.blit(green,[xkoor[g1],ykoor[g1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g2<1000 and movement=='G2' and (g2+tas+40!=g1 and g2+tas+40!=g3 and g2+tas+40!=g4) and g2+tas<75 and g2+tas!=g1 and g2+tas!=g3 and g2+tas!=g4 and not (g2u==1 and g2+tas>34):
                        g2=g2+tas
                        if g2>40:
                            g2=g2-40
                            g2u=1
                        if g2>30 and g2<35 and g2u==1:
                            if g2==31:
                                g2=71
                                g2u=0
                            if g2==32:
                                g2=72
                                g2u=0
                            if g2==33:
                                g2=73
                                g2u=0
                            if g2==34:
                                g2=74
                                g2u=0
                        posedina.blit(green,[xkoor[g2],ykoor[g2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g3<1000 and movement=='G3' and (g3+tas+40!=g1 and g3+tas+40!=g2 and g3+tas+40!=g4) and g3+tas<75 and g3+tas!=g1 and g3+tas!=g2 and g3+tas!=g4 and not (g3u==1 and g3+tas>34):
                        g3=g3+tas
                        if g3>40:
                            g3=g3-40
                            g3u=1
                        if g3>30 and g3<35 and g3u==1:
                            if g3==31:
                                g3=71
                                g3u=0
                            if g3==32:
                                g3=72
                                g3u=0
                            if g3==33:
                                g3=73
                                g3u=0
                            if g3==34:
                                g3=74
                                g3u=0
                        posedina.blit(green,[xkoor[g3],ykoor[g3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g4<1000 and movement=='G4' and (g4+tas+40!=g1 and g4+tas+40!=g2 and g4+tas+40!=g3) and g4+tas<75 and g4+tas!=g1 and g4+tas!=g2 and g4+tas!=g3 and not (g4u==1 and g4+tas>34):
                        g4=g4+tas
                        if g4>40:
                            g4=g4-40
                            g4u=1
                        if g4>30 and g4<35 and g4u==1:
                            if g4==31:
                                g4=71
                                g4u=0
                            if g4==32:
                                g4=72
                                g4u=0
                            if g4==33:
                                g4=73
                                g4u=0
                            if g4==34:
                                g4=74
                                g4u=0
                        posedina.blit(green,[xkoor[g4],ykoor[g4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                if tas==6:
                    if g1<1000 and movement=='G1' and (g1+tas+40!=g2 and g1+tas+40!=g3 and g1+tas+40!=g4) and g1+tas<75 and g1+tas!=g2 and g1+tas!=g3 and g1+tas!=g4 and not (g1u==1 and g1+tas>34):
                        g1=g1+tas
                        if g1>40:
                            g1=g1-40
                            g1u=1
                        if g1>30 and g1<35 and g1u==1:
                            if g1==31:
                                g1=71
                                g1u=0
                            if g1==32:
                                g1=72
                                g1u=0
                            if g1==33:
                                g1=73
                                g1u=0
                            if g1==34:
                                g1=74
                                g1u=0
                        posedina.blit(green,[xkoor[g1],ykoor[g1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g2<1000 and movement=='G2' and (g2+tas+40!=g1 and g2+tas+40!=g3 and g2+tas+40!=g4) and g2+tas<75 and g2+tas!=g1 and g2+tas!=g3 and g2+tas!=g4 and not (g2u==1 and g2+tas>34):
                        g2=g2+tas
                        if g2>40:
                            g2=g2-40
                            g2u=1
                        if g2>30 and g2<35 and g2u==1:
                            if g2==31:
                                g2=71
                                g2u=0
                            if g2==32:
                                g2=72
                                g2u=0
                            if g2==33:
                                g2=73
                                g2u=0
                            if g2==34:
                                g2=74
                                g2u=0
                        posedina.blit(green,[xkoor[g2],ykoor[g2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g3<1000 and movement=='G3' and (g3+tas+40!=g1 and g3+tas+40!=g2 and g3+tas+40!=g4) and g3+tas<75 and g3+tas!=g1 and g3+tas!=g2 and g3+tas!=g4 and not (g3u==1 and g3+tas>34):
                        g3=g3+tas
                        if g3>40:
                            g3=g3-40
                            g3u=1
                        if g3>30 and g3<35 and g3u==1:
                            if g3==31:
                                g3=71
                                g3u=0
                            if g3==32:
                                g3=72
                                g3u=0
                            if g3==33:
                                g3=73
                                g3u=0
                            if g3==34:
                                g3=74
                                g3u=0
                        posedina.blit(green,[xkoor[g3],ykoor[g3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g4<1000 and movement=='G4' and (g4+tas+40!=g1 and g4+tas+40!=g2 and g4+tas+40!=g3) and g4+tas<75 and g4+tas!=g1 and g4+tas!=g2 and g4+tas!=g3 and not (g4u==1 and g4+tas>34):
                        g4=g4+tas
                        if g4>40:
                            g4=g4-40
                            g4u=1
                        if g4>30 and g4<35 and g4u==1:
                            if g4==31:
                                g4=71
                                g4u=0
                            if g4==32:
                                g4=72
                                g4u=0
                            if g4==33:
                                g4=73
                                g4u=0
                            if g4==34:
                                g4=74
                                g4u=0
                        posedina.blit(green,[xkoor[g4],ykoor[g4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g1==13000 and movement=='G1' and (g2!=31 or g3!=31 or g4!=31):
                        g1=31
                        g1u=0
                        posedina.blit(green,[xkoor[g1],ykoor[g1]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g2==14000 and movement=='G2' and (g1!=31 or g3!=31 or g4!=31):
                        g2=31
                        g2u=0
                        posedina.blit(green,[xkoor[g2],ykoor[g2]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g3==15000 and movement=='G3' and (g1!=31 or g2!=31 or g4!=31):
                        g3=31
                        g3u=0
                        posedina.blit(green,[xkoor[g3],ykoor[g3]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                    if g4==16000 and movement=='G4' and (g1!=31 or g2!=31 or g3!=31):
                        g4=31
                        g4u=0
                        posedina.blit(green,[xkoor[g4],ykoor[g4]])
                        blitanje(staraxkoor,staraykoor)
                        player=player+1
                        movement=''
                        gucci=1
                if g1==y1 or g2==y1 or g3==y1 or g4==y1:
                    y1=my1
                    posedina.blit(yellow,[xkoor[my1],ykoor[my1]])
                if g1==y2 or g2==y2 or g3==y2 or g4==y2:
                    y2=my2
                    posedina.blit(yellow,[xkoor[my2],ykoor[my2]])
                if g1==y3 or g2==y3 or g3==y3 or g4==y3:
                    y3=my3
                    posedina.blit(yellow,[xkoor[my3],ykoor[my3]])
                if g1==y4 or g2==y4 or g3==y4 or g4==y4:
                    y4=my4
                    posedina.blit(yellow,[xkoor[my4],ykoor[my4]])
                if g1==b1 or g2==b1 or g3==b1 or g4==b1:
                    b1=mb1
                    posedina.blit(blue,[xkoor[mb1],ykoor[mb1]])
                if g1==b2 or g2==b2 or g3==b2 or g4==b2:
                    b2=mb2
                    posedina.blit(blue,[xkoor[mb2],ykoor[mb2]])
                if g1==b3 or g2==b3 or g3==b3 or g4==b3:
                    b3=mb3
                    posedina.blit(blue,[xkoor[mb3],ykoor[mb3]])
                if g1==b4 or g2==b4 or g3==b4 or g4==b4:
                    b4=mb4
                    posedina.blit(blue,[xkoor[mb4],ykoor[mb4]])
                if g1==r1 or g2==r1 or g3==r1 or g4==r1:
                    r1=mr1
                    posedina.blit(red,[xkoor[mr1],ykoor[mr1]])
                if g1==r2 or g2==r2 or g3==r2 or g4==r2:
                    r2=mr2
                    posedina.blit(red,[xkoor[mr2],ykoor[mr2]])
                if g1==r3 or g2==r3 or g3==r3 or g4==r3:
                    r3=mr3
                    posedina.blit(red,[xkoor[mr3],ykoor[mr3]])
                if g1==r4 or g2==r4 or g3==r4 or g4==r4:
                    r4=mr4
                    posedina.blit(red,[xkoor[mr4],ykoor[mr4]])
                if gucci==1 and tas==6:
                    player=player-1
                    tas=1000
            else:
                if player!=4 and roldrop==0:
                    player=player+1
                    gucci=1
                    tas=1000

            if (g1==71 or g1==72 or g1==73 or g1==74) and (g2==71 or g2==72 or g2==73 or g2==74) and (g3==71 or g3==72 or g3==73 or g3==74) and (g4==71 or g4==72 or g4==73 or g4==74):
                win4()
                end=True

        dispaly.blit(posedina,[0,0])
        pygame.display.update()
        sat.tick(60)
    pygame.quit()
menu()
