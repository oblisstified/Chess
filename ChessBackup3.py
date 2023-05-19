import pygame
pygame.init()
run=True
screen=pygame.display.set_mode((490,490))
grey=(120,120,120)
white=(255,255,255)
red=(200,0,0)
blue=(0,0,200)

pygame.draw.rect(screen,(0,0,0),(5,5,490,490))
count=0
colour=white
othercolour=grey
green=(0,200,0)
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

def SquareColour(colour,othercolour,count):
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
def OneSqaure(movecount,row,column):
    if (row+column)%2==0:
        pygame.draw.rect(screen,white,(5+60*row,5+60*column,60,60))
    elif (row+column)%2==1:
        pygame.draw.rect(screen,grey,(5+60*row,5+60*column,60,60))
        
SquareColour(colour,othercolour,count)

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
    
    
def SignChange(movecount):
    if movecount%2==0:
        return 1
    else:
        return -1
    
def PawnMove(movecount,Row,Column):
    array=[]
    multiplier=SignChange(movecount)
    if movecount%2==0 and Column==6 and StrGrid[Column-multiplier][Row]=='empty':      
        array.append(str(Row)+'+'+str(Column-(multiplier*2)))
        
    elif movecount%2==1 and Column==1 and StrGrid[Column-multiplier][Row]=='empty':
        array.append(str(Row)+'+'+str(Column-(multiplier*2)))
    if StrGrid[Column-multiplier][Row]=='empty':
        array.append(str(Row)+'+'+str(Column-multiplier))
    try:
        if StrGrid[Column-multiplier][Row-1]!='empty':
            array.append(str(Row-1)+'+'+str(Column-multiplier))
    except:
        pass
    try:
        if StrGrid[Column-multiplier][Row+1]!='empty':
            array.append(str(Row+1)+'+'+str(Column-multiplier))
    except:
        pass
    FriendlyFire(movecount,array)
    return array

def KnightMove(movecount,Row,Column):
    array=[]
    if 0<=(Column+2)<8 and 0<=Row+1<8:
        array.append(str(Row+1)+'+'+str(Column+2))
    if 0<=(Column-2)<8 and 0<=Row+1<8:
        array.append(str(Row+1)+'+'+str(Column-2))
    if 0<=(Column+2)<8 and 0<=Row-1<8:
        array.append(str(Row-1)+'+'+str(Column+2))
    if 0<=(Column-2)<8 and 0<=Row-1<8:
        array.append(str(Row-1)+'+'+str(Column-2))
    if 0<=(Column-1)<8 and 0<=Row+2<8:
        array.append(str(Row+2)+'+'+str(Column-1))
    if 0<=(Column+1)<8 and 0<=Row+2<8:
        array.append(str(Row+2)+'+'+str(Column+1))
    if 0<=(Column-1)<8 and 0<=Row-2<8:
        array.append(str(Row-2)+'+'+str(Column-1))
    if 0<=(Column+1)<8 and 0<=Row-2<8:
        array.append(str(Row-2)+'+'+str(Column+1))
    FriendlyFire(movecount,array)
    return array

def BishopMove(movecount,Row,Column):
    array=[]
    for i in range(1,8):
        try:
            if StrGrid[Column+i-1][Row+i-1]=='empty' and 0<=(Column+i)<8 and 0<=Row+i<8:
                array.append(str(Row+i)+'+'+str(Column+i))
            else:
                break
        except:
            pass
        
    for p in range(1,8):
        try:
            if StrGrid[Column-p+1][Row+p-1]=='empty' and 0<=(Column-p)<8 and 0<=Row+p<8:               
                array.append(str(Row+p)+'+'+str(Column-p))
            else:
                break
        except:
            pass
        
        
    for q in range(1,8):
        try:
            if StrGrid[Column-q+1][Row-q+1]=='empty' and 0<=(Column-q)<8 and 0<=Row-q<8:
                array.append(str(Row-q)+'+'+str(Column-q))
            else:
                break
        except:
            pass
        
    for z in range(1,8): 
        try:
            if StrGrid[Column+z-1][Row-z+1]=='empty' and 0<=(Column+z)<8 and 0<=Row-z<8:
                array.append(str(Row-z)+'+'+str(Column+z))
            else:
                break
        except:
            pass
    FriendlyFire(movecount,array)
    return array

def RookMove(movecount,Row,Column):
    array=[]
    for i in range(1,8):
        try:
            if StrGrid[Column+i-1][Row]=='empty'and 0<=(Column+i)<8 and 0<=Row<8:
                array.append(str(Row)+'+'+str(Column+i))
            else:
                break
        except:
            pass
    for p in range(1,8):
        try:
            if StrGrid[Column-p+1][Row]=='empty' and 0<=(Column-p)<8 and 0<=Row<8:        
                array.append(str(Row)+'+'+str(Column-p))
            else:
                break
        except:
            pass
    for o in range(1,8):
        try:
            if StrGrid[Column][Row+o-1]=='empty' and 0<=(Column)<8 and 0<=Row+o<8:
                array.append(str(Row+o)+'+'+str(Column))
            else:
                break
        except:
            pass
    for y in range(1,8):
        try:
            if StrGrid[Column][Row-y+1]=='empty' and 0<=(Column)<8 and 0<=Row-y<8:
                array.append(str(Row-y)+'+'+str(Column))
            else:
                break
        except:
            pass
    FriendlyFire(movecount,array)
    return array

def KingMove(movecount,Row,Column):
    array=[]
    for i in range(-1,2):
        for p in range(-1,2):
            if 0<=(Column+p)<8 and 0<=Row+i<8:
                array.append(str(Row+i)+'+'+str(Column+p))
    FriendlyFire(movecount,array)
    return array

def QueenMove(movecount,Row,Column):
    array=[]
    for i in range(1,8):
        try:
            if StrGrid[Column+i-1][Row]=='empty'and 0<=(Column+i)<8 and 0<=Row<8:
                array.append(str(Row)+'+'+str(Column+i))
            else:
                break
        except:
            pass
    for p in range(1,8):
        try:
            if StrGrid[Column-p+1][Row]=='empty' and 0<=(Column-p)<8 and 0<=Row<8:        
                array.append(str(Row)+'+'+str(Column-p))
            else:
                break
        except:
            pass
    for o in range(1,8):
        try:
            if StrGrid[Column][Row+o-1]=='empty' and 0<=(Column)<8 and 0<=Row+o<8:
                array.append(str(Row+o)+'+'+str(Column))
            else:
                break
        except:
            pass
    for y in range(1,8):
        try:
            if StrGrid[Column][Row-y+1]=='empty' and 0<=(Column)<8 and 0<=Row-y<8:
                array.append(str(Row-y)+'+'+str(Column))
            else:
                break
        except:
            pass

    for a in range(1,8):
        try:
            if StrGrid[Column+a-1][Row+a-1]=='empty' and 0<=(Column+a)<8 and 0<=Row+a<8:
                array.append(str(Row+a)+'+'+str(Column+a))
            else:
                break
        except:
            pass
        
    for s in range(1,8):
        try:
            if StrGrid[Column-s+1][Row+s-1]=='empty' and 0<=(Column-s)<8 and 0<=Row+s<8:               
                array.append(str(Row+s)+'+'+str(Column-s))
            else:
                break
        except:
            pass
        
        
    for d in range(1,8):
        try:
            if StrGrid[Column-d+1][Row-d+1]=='empty' and 0<=(Column-d)<8 and 0<=Row-d<8:
                array.append(str(Row-d)+'+'+str(Column-d))
            else:
                break
        except:
            pass
        
    for f in range(1,8): 
        try:
            if StrGrid[Column+f-1][Row-f+1]=='empty' and 0<=(Column+f)<8 and 0<=Row-f<8:
                array.append(str(Row-f)+'+'+str(Column+f))
            else:
                break
        except:
            pass
    FriendlyFire(movecount,array)
    return array



        
def ValidMove(movecount,Row,Column,Strpiece):
    if Strpiece[1:]=='pawn':
        return PawnMove(movecount,Row,Column)
    elif Strpiece[1:]=='rook':
        return RookMove(movecount,Row,Column)
    elif Strpiece[1:]=='knight':
        return KnightMove(movecount,Row,Column)
    elif Strpiece[1:]=='bishop':
        return BishopMove(movecount,Row,Column)
    elif Strpiece[1:]=='king':
        return KingMove(movecount,Row,Column)
    elif Strpiece[1:]=='queen':
        return QueenMove(movecount,Row,Column)
        
def wKingPosition():
    for Row in range(8):
        for Column in range(8):
            if StrGrid[Column][Row]=='wking':
                return str(Row)+'+'+str(Column)
def bKingPosition():
    for Row in range(8):
        for Column in range(8):
            if StrGrid[Column][Row]=='bking':
                return str(Row)+'+'+str(Column)

def FriendlyFire(movecount,array):
    wob=move(movecount)
    if wob=='w':
        for Row in range(8):
            for Column in range(8):
                if (StrGrid[Column][Row])[0]=='w' and str(Row)+'+'+str(Column) in array:
                    del array[array.index(str(Row)+'+'+str(Column))]
    elif wob=='b':
        for Row1 in range(8):
            for Column1 in range(8):
                if (StrGrid[Column1][Row1])[0]=='b' and str(Row1)+'+'+str(Column1) in array:
                    del array[array.index(str(Row1)+'+'+str(Column1))]
    return array
        
def NextMoveCircle(movecount,row,column,Strpiece):
    array=ValidMove(movecount,row,column,Strpiece)
    for items in array:
        Row=int(items[0])
        Column=int(items[2])
        if StrGrid[Column][Row]=='empty':
            pygame.draw.circle(screen,green,(35+Row*60,35+Column*60),15)
        else:
            
            pygame.draw.rect(screen,green,(5+Row*60,5+Column*60,60,60))
            screen.blit(Grid[Column][Row],(5+Row*60,5+Column*60))
            
def AfterClickCircle(movecount,row,column,piece):
    array=ValidMove(movecount,row,column,Strpiece)
    for items in array:
        Row=int(items[0])
        Column=int(items[2])
        OneSqaure(movecount,Row,Column)
        if StrGrid[Column][Row]!='empty':
             screen.blit(Grid[Column][Row],(5+Row*60,5+Column*60))
       
        
        
while True:
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type ==pygame.MOUSEBUTTONDOWN and event.button == 1:
            for Row in range(8):
                for Column in range(8):
                    count=0
                    statement=True
                    if 5+Row*60<mouse[0]<65+Row*60 and 5+Column*60<mouse[1]<65+Column*60 and StrGrid[Column][Row]!='empty':
                        
                        piece=Grid[Column][Row]
                        Strpiece=StrGrid[Column][Row]
                        wob=move(movecount)
                        
                        if Strpiece[0]==wob:

                            number=Row+Column
                            if number%2==0:
                                colour=white
                            else:
                                colour = grey
                            column=Column
                            row=Row
                            
                            pygame.draw.rect(screen,colour,(5+Row*60,5+Column*60,60,60))
                            Grid[Column][Row]=empty
                            StrGrid[Column][Row]='empty'
                            NextMoveCircle(movecount,row,column,Strpiece)
                            pygame.display.update()
                            print(ValidMove(movecount,row,column,Strpiece))
                    else:
                        statement=False
                            

                        
                        
        if event.type ==pygame.MOUSEBUTTONUP and event.button == 1:
            for Row1 in range(8):
                for Column1 in range(8):
                    if 5+Row1*60<mouse[0]<65+Row1*60 and 5+Column1*60<mouse[1]<65+Column1*60 and statement==True:
                        var=str(Row1)+'+'+str(Column1)
                        if Column1==column and Row1==row and move(movecount)==Strpiece[0]:

                            AfterClickCircle(movecount,row,column,Strpiece)
                            screen.blit(piece,(5+row*60,5+column*60)) 
                            StrGrid[column][row]=Strpiece
                            Grid[column][row]=piece
                            pygame.display.update()
                            break
                            
                        
                        else:
                            if var in ValidMove(movecount,row,column,Strpiece):
                                if Strpiece[0]==wob:
                                    number1=Row1+Column1
                                    if number1%2==0:
                                        colour1=white
                                    else:
                                        colour1 = grey
                                    
                                        
                                    pygame.draw.rect(screen,colour1,(5+Row1*60,5+Column1*60,60,60))
    
    
                                    AfterClickCircle(movecount,row,column,piece)
                                    screen.blit(piece,(5+Row1*60,5+Column1*60)) 
                                    Grid[Column1][Row1]=piece
                                    StrGrid[Column1][Row1]=Strpiece
                                    pygame.display.update()
                                    movecount+=1
                                    
                            else:
                                AfterClickCircle(movecount,row,column,piece)
                                pygame.display.update()
                    statement=True
                                      
                        