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
                return -1
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
                return -1
            else:
                return 1
    return 0

com=["fleshRoal","stritFlesh","Kare","FullHouse",
     "Flush","Straight","Set","2pair","pair","Kiker"]
gg=[[2, 2], [2, 3], [1, 5], [2, 10], [3, 8], [1,4],[2,4],[3, 4], [4, 4],[1,7],[2,1]]
combHand=[]
for i in range(1):
##    allcards=gg
    NPlaer=3
    allcards=gener.gg(NPlaer)
    curGame=table()
    curGame.com=allcards[:5]##последние 5 карт из сгенрированой группы обшие 
    curGame.winner.append([10,10,10])
    print(curGame.com)
    for i in range(int((len(allcards)-5)/2)):
        curGame.Plaers.append(allcards[5+2*i:5+2*(i+1)])##получаю карты игрока
        ##    theHighest(comb,combHand)
        PLC=curGame.com+curGame.Plaers[i]##формирую массив всех карт игрока (рука+стол)
        print("Plyer "+str(i+1)+" -",curGame.Plaers[i])
        number,combHand=ch.pure(PLC,combHand)##вывод исхода карт для игрока, number-номер комбинации combHand-карты комбинации
        print("-",com[number],combHand)

        if curGame.winner[0][0]>number:
            curGame.winner.clear()
            curGame.winner.append([number,i,combHand.copy()])
        else:
            if curGame.winner[0][0]==number:
                temp=compare(curGame,curGame.winner[0][1],i)
                if temp==1:
                    curGame.winner.clear()
                    curGame.winner.append([number,i,combHand.copy()])
                else:
                    if temp==0:
                        curGame.winner.append([number,i,combHand.copy()])

    if (len(curGame.winner)>1):
        print("Plaers делят банк")
        for i in range(len(curGame.winner)):
            print("Player ",curGame.winner[i][1]+1,"-",com[curGame.winner[i][0]])
    print("Player ",curGame.winner[0][1]+1,"-",com[curGame.winner[0][0]])

##        if number>2 and number<9:## вывод кикера с учетом текуших карт
##            print("kKk-",ch.CutAnd(PLC,combHand))
# стрит флешь старшая карта
# каре старшая карта
# фулл хаус старшая среди троек , старшая среди 2, кикер
# флешь старшая карта,kiker
# стрит старшая карта,kiker
# тройка старшая карта, кикер
# пара старшая карта, кикер