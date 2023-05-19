import pygame
import time
from random import randint
pygame.init()
run=True
screen=pygame.display.set_mode((490,490))
grey=(120,120,120)
white=(255,255,255)
red=(200,0,0)
blue=(0,0,200)
piecearray=['wking','wqueen','wrook','wbishop','bknight','wpawn']

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
pieces={'pawn':1,'bishop':3,'knight':3,'rook':5,'queen':9,'king':100}
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
    
def PawnMove(movecount,Row,Column,StrGrid):
    array=[]
    multiplier=SignChange(movecount)
    if movecount%2==0 and Column==6 and StrGrid[Column-multiplier][Row]=='empty' and StrGrid[Column-multiplier*2][Row]=='empty':      
        array.append(str(Row)+'+'+str(Column-(multiplier*2)))
        
    if movecount%2==1 and Column==1 and StrGrid[Column-multiplier][Row]=='empty' and StrGrid[Column-multiplier*2][Row]=='empty':
        array.append(str(Row)+'+'+str(Column-(multiplier*2)))
    try:
        if StrGrid[Column-multiplier][Row]=='empty':
            array.append(str(Row)+'+'+str(Column-multiplier))
    except:
        pass
    try:
        if StrGrid[Column-multiplier][Row-1]!='empty' and 0<=(Column-multiplier)<8 and 0<=Row-1<8:
            array.append(str(Row-1)+'+'+str(Column-multiplier))
    except:
        pass
    try:
        if StrGrid[Column-multiplier][Row+1]!='empty' and 0<=(Column-multiplier)<8 and 0<=Row+1<8:
            array.append(str(Row+1)+'+'+str(Column-multiplier))
    except:
        pass
    FriendlyFire(movecount,array)
    return array

def pawntoqueen():
    for Column in range(8):
        if StrGrid[0][Column]=='wpawn':
            return Column
    return False
                

def KnightMove(movecount,Row,Column,StrGrid):
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

def BishopMove(movecount,Row,Column,StrGrid):
    array=[]
    
    

    for i in range(2,8):
        try:
            if StrGrid[Column+i-1][Row+i-1]=='empty' and 0<=(Column+i)<8 and 0<=Row+i<8:
                array.append(str(Row+i)+'+'+str(Column+i))
            else:
                break
        except:
            pass
        
    for p in range(2,8):
        try:
            if StrGrid[Column-p+1][Row+p-1]=='empty' and 0<=(Column-p)<8 and 0<=Row+p<8:               
                array.append(str(Row+p)+'+'+str(Column-p))
            else:
                break
        except:
            pass
        
        
    for q in range(2,8):
        try:
            if StrGrid[Column-q+1][Row-q+1]=='empty' and 0<=(Column-q)<8 and 0<=Row-q<8:
                array.append(str(Row-q)+'+'+str(Column-q))
            else:
                break
        except:
            pass
        
    for z in range(2,8): 
        try:
            if StrGrid[Column+z-1][Row-z+1]=='empty' and 0<=(Column+z)<8 and 0<=Row-z<8:
                array.append(str(Row-z)+'+'+str(Column+z))
            else:
                break
        except:
            pass
    if 0<=(Column+1)<8 and 0<=Row+1<8:   
        array.append(str(Row+1)+'+'+str(Column+1))         
    if 0<=(Column-1)<8 and 0<=Row+1<8:
        array.append(str(Row+1)+'+'+str(Column-1)) 
    if 0<=(Column+1)<8 and 0<=Row-1<8:
        array.append(str(Row-1)+'+'+str(Column+1)) 
    if 0<=(Column-1)<8 and 0<=Row-1<8:
        array.append(str(Row-1)+'+'+str(Column-1)) 

    FriendlyFire(movecount,array)
    return array

def RookMove(movecount,Row,Column,StrGrid):
    array=[]
    for i in range(2,8):
        try:
            if StrGrid[Column+i-1][Row]=='empty'and 0<=(Column+i)<8 and 0<=Row<8:
                array.append(str(Row)+'+'+str(Column+i))
            else:
                break
        except:
            pass
    for p in range(2,8):
        try:
            if StrGrid[Column-p+1][Row]=='empty' and 0<=(Column-p)<8 and 0<=Row<8:        
                array.append(str(Row)+'+'+str(Column-p))
            else:
                break
        except:
            pass
    for o in range(2,8):
        try:
            if StrGrid[Column][Row+o-1]=='empty' and 0<=(Column)<8 and 0<=Row+o<8:
                array.append(str(Row+o)+'+'+str(Column))
            else:
                break
        except:
            pass
    for y in range(2,8):
        try:
            if StrGrid[Column][Row-y+1]=='empty' and 0<=(Column)<8 and 0<=Row-y<8:
                array.append(str(Row-y)+'+'+str(Column))
            else:
                break
        except:
            pass
    if 0<=(Column)<8 and 0<=Row+1<8:   
        array.append(str(Row+1)+'+'+str(Column))         
    if 0<=(Column)<8 and 0<=Row-1<8:
        array.append(str(Row-1)+'+'+str(Column)) 
    if 0<=(Column+1)<8 and 0<=Row<8:
        array.append(str(Row)+'+'+str(Column+1)) 
    if 0<=(Column-1)<8 and 0<=Row<8:
        array.append(str(Row)+'+'+str(Column-1)) 
    FriendlyFire(movecount,array)
    return array

def KingMove(movecount,Row,Column,StrGrid):
    array=[]
    for i in range(-1,2):
        for p in range(-1,2):
            if 0<=(Column+p)<8 and 0<=Row+i<8:
                if i!=0 or p!=0:
                    array.append(str(Row+i)+'+'+str(Column+p))
    FriendlyFire(movecount,array)
    if StrGrid[7][5]=='empty' and StrGrid[7][6]=='empty' and StrGrid[7][7]=='wrook' and StrGrid[7][4]=='wking':
        array.append(str(7)+'+'+str(6))
    return array

def QueenMove(movecount,Row,Column,StrGrid):
    array=[]
    for i in range(2,8):
        try:
            if StrGrid[Column+i-1][Row]=='empty'and 0<=(Column+i)<8 and 0<=Row<8:
                array.append(str(Row)+'+'+str(Column+i))
            else:
                break
        except:
            pass
    for p in range(2,8):
        try:
            if StrGrid[Column-p+1][Row]=='empty' and 0<=(Column-p)<8 and 0<=Row<8:        
                array.append(str(Row)+'+'+str(Column-p))
            else:
                break
        except:
            pass
    for o in range(2,8):
        try:
            if StrGrid[Column][Row+o-1]=='empty' and 0<=(Column)<8 and 0<=Row+o<8:
                array.append(str(Row+o)+'+'+str(Column))
            else:
                break
        except:
            pass
    for y in range(2,8):
        try:
            if StrGrid[Column][Row-y+1]=='empty' and 0<=(Column)<8 and 0<=Row-y<8:
                array.append(str(Row-y)+'+'+str(Column))
            else:
                break
        except:
            pass
    if 0<=(Column)<8 and 0<=Row+1<8:   
        array.append(str(Row+1)+'+'+str(Column))         
    if 0<=(Column)<8 and 0<=Row-1<8:
        array.append(str(Row-1)+'+'+str(Column)) 
    if 0<=(Column+1)<8 and 0<=Row<8:
        array.append(str(Row)+'+'+str(Column+1)) 
    if 0<=(Column-1)<8 and 0<=Row<8:
        array.append(str(Row)+'+'+str(Column-1)) 
        
        
    

    for v in range(2,8):
        try:
            if StrGrid[Column+v-1][Row+v-1]=='empty' and 0<=(Column+v)<8 and 0<=Row+v<8:
                array.append(str(Row+v)+'+'+str(Column+v))
            else:
                break
        except:
            pass
        
    for n in range(2,8):
        try:
            if StrGrid[Column-n+1][Row+n-1]=='empty' and 0<=(Column-n)<8 and 0<=Row+n<8:               
                array.append(str(Row+n)+'+'+str(Column-n))
            else:
                break
        except:
            pass
        
        
    for q in range(2,8):
        try:
            if StrGrid[Column-q+1][Row-q+1]=='empty' and 0<=(Column-q)<8 and 0<=Row-q<8:
                array.append(str(Row-q)+'+'+str(Column-q))
            else:
                break
        except:
            pass
        
    for z in range(2,8): 
        try:
            if StrGrid[Column+z-1][Row-z+1]=='empty' and 0<=(Column+z)<8 and 0<=Row-z<8:
                array.append(str(Row-z)+'+'+str(Column+z))
            else:
                break
        except:
            pass
    if 0<=(Column+1)<8 and 0<=Row+1<8:   
        array.append(str(Row+1)+'+'+str(Column+1))         
    if 0<=(Column-1)<8 and 0<=Row+1<8:
        array.append(str(Row+1)+'+'+str(Column-1)) 
    if 0<=(Column+1)<8 and 0<=Row-1<8:
        array.append(str(Row-1)+'+'+str(Column+1)) 
    if 0<=(Column-1)<8 and 0<=Row-1<8:
        array.append(str(Row-1)+'+'+str(Column-1)) 
    FriendlyFire(movecount,array)
    return array



        
def ValidMove(movecount,Row,Column,Strpiece,StrGrid):
    if Strpiece[1:]=='pawn':
        return PawnMove(movecount,Row,Column,StrGrid)
    elif Strpiece[1:]=='rook':
        return RookMove(movecount,Row,Column,StrGrid)
    elif Strpiece[1:]=='knight':
        return KnightMove(movecount,Row,Column,StrGrid)
    elif Strpiece[1:]=='bishop':
        return BishopMove(movecount,Row,Column,StrGrid)
    elif Strpiece[1:]=='king':
        return KingMove(movecount,Row,Column,StrGrid)
    elif Strpiece[1:]=='queen':
        return QueenMove(movecount,Row,Column,StrGrid)
        
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
    array=ValidMove(movecount,row,column,Strpiece,StrGrid)
    for items in array:
        Row=int(items[0])
        Column=int(items[2])
        if StrGrid[Column][Row]=='empty':
            pygame.draw.circle(screen,green,(35+Row*60,35+Column*60),15)
        else:
            
            pygame.draw.rect(screen,green,(5+Row*60,5+Column*60,60,60))
            screen.blit(Grid[Column][Row],(5+Row*60,5+Column*60))
            
def AfterClickCircle(movecount,row,column,piece):
    array=ValidMove(movecount,row,column,Strpiece,StrGrid)
    for items in array:
        Row=int(items[0])
        Column=int(items[2])
        OneSqaure(movecount,Row,Column)
        if StrGrid[Column][Row]!='empty':
             screen.blit(Grid[Column][Row],(5+Row*60,5+Column*60))
       
def LossCheckforBlack(movecount):
    if movecount%2==1:
        for Row in range(8):
            for Column in range(8):
            
                if StrGrid[Column][Row]=='bking':
                    return False
    
        return True
def LossCheckforWhite(movecount):
    if movecount%2==0:
        for Row in range(8):
            for Column in range(8):
            
                if StrGrid[Column][Row]=='wking':
                    return False
        return True
    
    
    
    
    
    
    
    
def RandomMove(movecount):
    xco=randint(0,7)
    yco=randint(0,7)
    while (StrGrid[yco][xco])[0]!='b':
                xco=randint(0,7)
                yco=randint(0,7)
    Strpiece=StrGrid[yco][xco]
    
    blackarray=ValidMove(movecount,xco,yco,Strpiece,StrGrid)
    while len(blackarray)==0:
        xco=randint(0,7)
        yco=randint(0,7)
        while (StrGrid[yco][xco])[0]!='b':
            xco=randint(0,7)
            yco=randint(0,7)
        Strpiece=StrGrid[yco][xco]
        blackarray=ValidMove(movecount,xco,yco,Strpiece,StrGrid)
    number1=xco+yco
    piece=Grid[yco][xco]

    if number1%2==0:
        colour=white
    else:
        colour = grey   
    randomnumber=randint(0,len(blackarray)-1)
    print(Strpiece,blackarray[randomnumber])
    thing=blackarray[randomnumber]
    number=int(thing[0])+int(thing[2])
    if number%2==0:
        colour1=white
    else:
        colour1 = grey 
    pygame.draw.rect(screen,colour1,(5+int(thing[0])*60,5+int(thing[2])*60,60,60))
    screen.blit(piece,(5+int(thing[0])*60,5+int(thing[2])*60)) 
    Grid[yco][xco]=empty
    StrGrid[yco][xco]='empty'
    Grid[int(thing[2])][int(thing[0])]=piece
    StrGrid[int(thing[2])][int(thing[0])]=Strpiece

    pygame.draw.rect(screen,colour,(5+xco*60,5+yco*60,60,60))
    pygame.display.update()
        
        

    
    
    
    
    
    
    
    
    
    
def CalcHighestPiece(movecount):
    highest=0
    for Row in range(8):
        for Column in range(8):
            if StrGrid[Column][Row][0]=='b':
                array=ValidMove(movecount,Row,Column,StrGrid[Column][Row],StrGrid)
                if len(array)!=0:
                    for i in array:
                        
                        row=int(i[0])
                        column=int(i[2])
                        if StrGrid[column][row][0]=='w':
                            if pieces[StrGrid[column][row][1:]]>highest:
                                highest=pieces[StrGrid[column][row][1:]]
                                print(highest)
                                
                                Highest=str(Row)+str(Column)+str(row)+str(column)
    if highest>=0:
        Row=int(Highest[0])
        Column=int(Highest[1])
        row=int(Highest[2])
        column=int(Highest[3])
        number1=Row+Column
        piece=Grid[Column][Row]
        Strpiece=StrGrid[Column][Row]
        if number1%2==0:
            colour=white
        else:
            colour = grey   
        number=row+column
        if number%2==0:
            colour1=white
        else:
            colour1 = grey 
        pygame.draw.rect(screen,colour1,(5+row*60,5+column*60,60,60))
        screen.blit(piece,(5+row*60,5+column*60)) 
        Grid[Column][Row]=empty
        StrGrid[Column][Row]='empty'
        Grid[column][row]=piece
        StrGrid[column][row]=Strpiece
    
        pygame.draw.rect(screen,colour,(5+Row*60,5+Column*60,60,60))
        pygame.display.update()
        return True
    else:
        return False
    
def minimise(movecount,StrGrid):
    movearray=[]
    TempGrid=StrGrid
    highest=-10
    for Row in range(8):
        for Column in range(8):
            if StrGrid[Column][Row][0]=='b':
                Strpiece=StrGrid[Column][Row]
                array=ValidMove(movecount,Row,Column,Strpiece,StrGrid)
                if len(array)!=0:
                    for i in array:
                        
                        row=int(i[0])
                        column=int(i[2])
                        if StrGrid[column][row][0]=='w':
                            point=pieces[StrGrid[column][row][1:]]
                        else:
                            point=0
                        TempGrid=StrGrid
                        Temp=TempGrid[column][row]
                        TempGrid[column][row]=Strpiece
                        TempGrid[Column][Row]='empty'
                        movecount+=1
                        if maximise(TempGrid,point,movecount)>highest:
                            movearray=[]
                            movearray.append(str(Row)+str(Column)+str(row)+str(column))
                            highest=maximise(TempGrid,point,movecount)
                            Highest=movearray[0]
                        elif maximise(TempGrid,point,movecount)==highest:
                            movearray.append(str(Row)+str(Column)+str(row)+str(column))
                            Highest=movearray[randint(0,len(movearray)-1)]
                            
                            
                        
                        TempGrid[Column][Row]=Strpiece
                        TempGrid[column][row]=Temp
                        movecount-=1
    print(highest)

    Row=int(Highest[0])
    Column=int(Highest[1])
    row=int(Highest[2])
    column=int(Highest[3])
    number1=Row+Column
    piece=Grid[Column][Row]
    
    Strpiece=StrGrid[Column][Row]
    if number1%2==0:
        colour=white
    else:
        colour = grey   
    number=row+column
    if number%2==0:
        colour1=white
    else:
        colour1 = grey 
    pygame.draw.rect(screen,colour1,(5+row*60,5+column*60,60,60))
    screen.blit(piece,(5+row*60,5+column*60)) 
    Grid[Column][Row]=empty
    StrGrid[Column][Row]='empty'
    Grid[column][row]=piece
    StrGrid[column][row]=Strpiece

    pygame.draw.rect(screen,colour,(5+Row*60,5+Column*60,60,60))
    pygame.display.update()
    return True
                        
                            
def maximise(TempGrid,point,movecount):
    highest=0

    for Row in range(8):
        for Column in range(8):
            try:
                if TempGrid[Column][Row][0]=='w':
                    array=ValidMove(movecount,Row,Column,TempGrid[Column][Row],TempGrid)
    
                    if len(array)!=0:
                        for i in array:
                            
                            row=int(i[0])
                            column=int(i[2])
                            if TempGrid[column][row][0]=='b':
                                if pieces[TempGrid[column][row][1:]]>highest:
                                    highest=pieces[TempGrid[column][row][1:]]
            except:
                pass
                                
                            
    return point-highest
    
                            
                            
                            
                            
   
        
    
    
    
    
    
'''                                
def minimise():          
    for Row in range(8):
        for Column in range(8):
           
            if StrGrid[Column][Row][0]=='b':
                Strpiece=StrGrid[Column][Row]
                array=ValidMove(movecount,Row,Column,Strpiece)  
                for i in array:
                    TempGrid=Grid
                    row=int(i[0])
                    column=int(i[2])
                    if StrGrid[column][row]!='empty':                    
                        point=pieces[StrGrid[column][row][1:]]
                    else:
                        point=0
                    TempGrid[Column][Row]='empty'
                    TempGrid[column][row]=Strpiece
                    maximise(point)
                
def maximise(point):
    for Row in range(8):
        for Column in range(8):
            Strpiece=Grid[Column][Row]
            array=ValidMove(movecount,Row,Column,Strpiece)  
            for i in array:
                point-=pieces[StrGrid[column][row][1:]]
                                
'''                            
                            
                            
                            
                            
#return str(Row)+str(Column)+str(row)+str(column)
    
    
  
Endgame=True
while Endgame:
    if pawntoqueen()!=False:    
       tempColumn=pawntoqueen()
       StrGrid[0][tempColumn]='wqueen'
       Grid[0][tempColumn]=wqueen
       wob=move(movecount)
                            
       if StrGrid[tempColumn][0]==wob:
        
           number=tempColumn
           if number%2==0:
               colour=white
       else:
           colour = grey
       pygame.draw.rect(screen,colour,(5+tempColumn*60,5,60,60))
       
       screen.blit(wqueen,(5+tempColumn*60,5))
       pygame.display.update()
       

    if movecount%2==0:
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
                                print(ValidMove(movecount,row,column,Strpiece,StrGrid))
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
                                if var in ValidMove(movecount,row,column,Strpiece,StrGrid):
                                    if Strpiece[0]==wob:
                                        number1=Row1+Column1
                                        if number1%2==0:
                                            colour1=white
                                        else:
                                            colour1 = grey
                                        
                                            
                                        pygame.draw.rect(screen,colour1,(5+Row1*60,5+Column1*60,60,60))
        
        
                                        AfterClickCircle(movecount,row,column,piece)
                                        pygame.draw.rect(screen,colour1,(5+Row1*60,5+Column1*60,60,60))
                                        screen.blit(piece,(5+Row1*60,5+Column1*60)) 
                                        Grid[Column1][Row1]=piece
                                        StrGrid[Column1][Row1]=Strpiece
                                        pygame.display.update()
                                        movecount+=1
                                        '''
                                        if LossCheckforWhite(movecount)==True:
                                            print("white loses")
                                            Endgame=False
                                        if LossCheckforBlack(movecount)==True:
                                            print("black loses")
                                            Endgame=False
                                        '''
                                        
                                else:
                                    AfterClickCircle(movecount,row,column,piece)
                                    pygame.display.update()
                        statement=True
    if movecount%2==1:
        
        #minimse()
        #maximise()
        #minimise()
        if minimise(movecount,StrGrid) == True :
            print('ok')
        else:
            RandomMove(movecount)
            
        movecount+=1
        
        
        
        
        
        
        
        
        
        
        
time.sleep(7)                                    
pygame.quit()                       