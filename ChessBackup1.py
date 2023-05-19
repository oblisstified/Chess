import pygame
pygame.init()
run=True
screen=pygame.display.set_mode((490,490))
grey=(120,120,120)
white=(255,255,255)

pygame.draw.rect(screen,(0,0,0),(5,5,490,490))
count=0
colour=white
othercolour=grey
for Row in range(5,485,60):
    for Column in range(5,485,120):
        
        pygame.draw.rect(screen,colour,(Column,Row,60,60))
        pygame.draw.rect(screen,othercolour,(Column+60,Row,60,60))
    count+=1
    if count%2==0:
        colour=white
        othercolour=grey
    else:
        colour=grey
        othercolour=white
bpawn=pygame.image.load('bpawn.png')
wpawn=pygame.image.load('wpawn.png')
wrook=pygame.image.load('wrook.png')
brook=pygame.image.load('brook.png')
bknight=pygame.image.load('bknight.png')
wknight=pygame.image.load('wknight.png')
bbishop=pygame.image.load('bbishop.png')
wbishop=pygame.image.load('wbishop.png')
bking=pygame.image.load('bking.png')
wking=pygame.image.load('wking.png')
bqueen=pygame.image.load('bqueen.png')
wqueen=pygame.image.load('wqueen.png')
empty='nothing'
for pawn in range(5,485,60):
    screen.blit(bpawn,(pawn,65))
    screen.blit(wpawn,(pawn,365))
for rook in range(5,426,420):
    screen.blit(brook,(rook,5))
    screen.blit(wrook,(rook,425))
for knight in range(65,366,300):
    screen.blit(bknight,(knight,5))
    screen.blit(wknight,(knight,425))
for bishop in range(125,306,180):
    screen.blit(bbishop,(bishop,5))
    screen.blit(wbishop,(bishop,425))
screen.blit(bking,(245,5))
screen.blit(wking,(245,425))
screen.blit(bqueen,(185,5))
screen.blit(wqueen,(185,425))
pygame.display.update()


Grid=[[brook,bknight,bbishop,bqueen,bking,bbishop,bknight,brook],
      [bpawn,bpawn,bpawn,bpawn,bpawn,bpawn,bpawn,bpawn],
      [empty,empty,empty,empty,empty,empty,empty,empty],
      [empty,empty,empty,empty,empty,empty,empty,empty],
      [empty,empty,empty,empty,empty,empty,empty,empty],
      [empty,empty,empty,empty,empty,empty,empty,empty],
      [wpawn,wpawn,wpawn,wpawn,wpawn,wpawn,wpawn,wpawn],
      [wrook,wknight,wbishop,wqueen,wking,wbishop,wknight,wrook]]


StrGrid=[['brook','bknight','bbishop','bqueen','bking','bbishop','bknight','brook'],
      ['bpawn','bpawn','bpawn','bpawn','bpawn','bpawn','bpawn','bpawn'],
      ['empty','empty','empty','empty','empty','empty','empty','empty'],
      ['empty','empty','empty','empty','empty','empty','empty','empty'],
      ['empty','empty','empty','empty','empty','empty','empty','empty'],
      ['empty','empty','empty','empty','empty','empty','empty','empty'],
      ['wpawn','wpawn','wpawn','wpawn','wpawn','wpawn','wpawn','wpawn'],
      ['wrook','wknight','wbishop','wqueen','wking','wbishop','wknight','wrook']]
movecount=0
def move(movecount): 
    if movecount%2==0:
        return 'w'
    else:
        return 'b'
def ValidMoveRow(piece,Row):   
    if piece[1:]=='pawn':
        return Row
    
    
    
def ValidMoveColumn(piece,Column,movecount):
    if piece[1:]=='pawn':
        if movecount%2==0:           
            return Column-1
        else:
            return Column+1
    
    
    
def SignChange(movecount):
    if movecount%2==0:
        return 1
    else:
        return -1
        
    


while True:
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type ==pygame.MOUSEBUTTONDOWN and event.button == 1:
            for Row in range(8):
                for Column in range(8):
                    count=0
                    if 5+Row*60<mouse[0]<65+Row*60 and 5+Column*60<mouse[1]<65+Column*60:
                        
                        piece=Grid[Column][Row]
                        Strpiece=StrGrid[Column][Row]
                        wob=move(movecount)
                        
                        if Strpiece[0]==wob:

                            number=Row+Column
                            if number%2==0:
                                colour=white
                            else:
                                colour = grey
                            pygame.draw.rect(screen,colour,(5+Row*60,5+Column*60,60,60))
                            Grid[Column][Row]=empty
                            StrGrid[Column][Row]='empty'
                            pygame.display.update()
                            column=Column
                            row=Row

                        
                        
        if event.type ==pygame.MOUSEBUTTONUP and event.button == 1:
            for Row1 in range(8):
                for Column1 in range(8):
                    if 5+Row1*60<mouse[0]<65+Row1*60 and 5+Column1*60<mouse[1]<65+Column1*60:
                        if Column1==ValidMoveColumn(Strpiece,column,movecount) and Row1==ValidMoveRow(Strpiece,row):
                            if Strpiece[0]==wob:
                                number1=Row1+Column1
                                if number1%2==0:
                                    colour1=white
                                else:
                                    colour1 = grey
                                pygame.draw.rect(screen,colour1,(5+Row1*60,5+Column1*60,60,60))
                                screen.blit(piece,(5+Row1*60,5+Column1*60))
                                Grid[Column1][Row1]=piece
                                StrGrid[Column1][Row1]=Strpiece
                               
                                print(StrGrid)
                                pygame.display.update()
                                movecount+=1
                                        
                        