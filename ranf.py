import gener
import fle
import st
import fullH
import Arrr
import fair
import pullCombHand as ch
#def ButiOut(y)

class table:
    com=[]
    Plaers=[]
    winner=[]

def compare(Game,pl1,pl2):
    print(pl1,pl2)
    PLC1=Game.com+Game.Plaers[pl1]
    PLC2=Game.com+Game.Plaers[pl2]
    hand1=[]
    hand2=[]
    number,hand1=ch.pure(PLC1,hand1)
    number,hand2=ch.pure(PLC2,hand2)
    if number==5:
        start=1
    else:
        start=0
    for i in range(start,len(hand1)):
        if hand1[i][1]==1:
            hand1[i][1]=14
        if hand2[i][1]==1:
            hand2[i][1]=14
    for i in range(len(hand1)):
        if hand1[i][1]==hand2[i][1]:
            continue
        else:
            if hand1[i][1]>hand2[i][1]:
                return 0
            else:
                return 1
    k1=ch.CutAnd(PLC1,hand1)
    k2=ch.CutAnd(PLC2,hand2)
    print(k1,k2)
    for i in range(len(k1)):
        if k2[i][1]==k1[i][1]:
            continue
        else:
            if k1[i][1]>k2[i][1]:
                return 0
            else:
                return 1

com=["fleshRoal","stritFlesh","Kare","FullHouse",
     "Flush","Straight","Set","2pair","pair","Kiker"]
gg=[[2, 2], [2, 3], [2, 5], [2, 10], [3, 8], [3, 1], [4, 4],[1,4],[3,6]]
combHand=[]
for i in range(1):
    allcards=gg
##    NPlaer=2
##    comb=gener.gg(NPlaer)#по умолчанияю 2
##    allcards=gener.gg(2)
    curGame=table()
    curGame.com=allcards[:5]
    curGame.winner=10,10
    print(curGame.com)
    for i in range(int((len(allcards)-5)/2)):
        curGame.Plaers.append(allcards[5+2*i:5+2*(i+1)])
##    theHighest(comb,combHand)
        PLC=curGame.com+curGame.Plaers[i]
        print("Plyer "+str(i+1)+" -",curGame.Plaers[i])
        number,combHand=ch.pure(PLC,combHand)
        print("-",com[number],combHand)
        if curGame.winner[0]>number:
            curGame.winner=number,i,combHand
        else:  
            if curGame.winner[0]==number:
                if compare(curGame,curGame.winner[1],i):
                    curGame.winner=number,i,combHand
    
    print("Player ",curGame.winner[1]+1,"-",com[curGame.winner[0]])
##        if number>2 and number<9:## вывод кикера с учетом текуших карт
##            print("kKk-",ch.CutAnd(PLC,combHand))

# стрит флешь старшая карта
# каре старшая карта
# фулл хаус старшая среди троек , старшая среди 2, кикер
# флешь старшая карта,kiker
# стрит старшая карта,kiker
# тройка старшая карта, кикер
# пара старшая карта, кикер
