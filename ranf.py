import gener
##import fle
##import st
##import fullH
##import Arrr
##import fair

import auction
import CardReading as CR
from collections import deque

class Player:
    card=[]##карты в руке
    state=9##состояние чек или флл ин или фолд и т. д.
    bet=0##
    roundBet=0##
    wallet=20##кошелек
    id ##номер игрока за столом

class table:
    com=[]
    Plaers=[]
    winner=[]

def main():
##    com=["fleshRoal","stritFlesh","Kare","FullHouse",
##         "Flush","Straight","Set","2pair","pair","Kiker"]
##    gg=[[2, 4], [2, 12], [3, 1], [1, 3], [4, 12],[1, 7], [2, 6],[1, 10], [2, 3],[4, 4], [1, 11]] 

    NPlaer=3
    Pls=deque()
##    button=NPlaer ##23.10.2020 13:46 это че?зачем для чего не пронятно
    for i in range(NPlaer): 
        Pls.append(Player())##типо заполняю
        Pls[i].id=i

    for r in range(100000):
##        allcards=gg
        for i in range(NPlaer):##тут
            if Pls[i].wallet==0:
                sum=0
                for y in range(NPlaer):##тут
                    sum+=Pls[y].wallet
                if sum==60:
                    for y in range(NPlaer):##тут
                        Pls[y].wallet=20
                else :
                    print("!!!check bank!!!")
                    return 0
            if Pls[i].wallet<0:
                print("!!!zero down wallet!!!")
                return 0
##                return
        allcards=gener.gg(NPlaer)
        print(allcards[:5])

        for i in range(int((len(allcards)-5)/2)):##тут
            Pls[i].card=allcards[5+2*i:5+2*(i+1)]##даю карты каждому игроку
            Pls[i].state=9
            Pls[i].bet=0
        for pl in Pls:
            print("Player",pl.id,pl.card)

        bank=auction.start(Pls,allcards,True)
        print("BaNK=",bank)
        allcards=allcards[:5]
        Id=[]
        for pl in Pls:##выделение игроков оставшихся в игре
            print(pl.id,"\t",pl.state,"\t",pl.bet,"$\t",pl.wallet)
            if not pl.state==0:
                allcards=allcards+pl.card
                Id.extend([pl.id])
        print(Id)
        curGame=CR.winer(allcards,Id)
        payment(curGame,bank,Pls)##распределение bank по PLs.wallet
        for pl in Pls:
            print(pl.id,"\t",pl.bet,"$\t",pl.wallet)
        print("----------------------------------------------------------")

def payment(curGame,bank,Pls):
    com=["fleshRoal","stritFlesh","Kare","FullHouse",
     "Flush","Straight","Set","2pair","pair","Kiker"]
    for i in range(len(curGame.winner)):
        print("Player ",curGame.winner[i][1],"-",com[curGame.winner[i][0]])
    if (len(curGame.winner)>1):
        print("Plaers делят банк")
##            равная часть от банка * на количество игроков + нераспределеный остаток от суммы
## это верно , но не для всего
        for i in range(len(curGame.winner)):
            while True:
                if curGame.winner[i][1]==Pls[0].id:
                    Pls[0].wallet=Pls[0].wallet+bank//len(curGame.winner)
                    break
                else:
                    Pls.rotate(-1)
        if bank%len(curGame.winner):
                for i in range(bank%len(curGame.winner)):##распределяю по одному
                    for y in range(len(curGame.winner)):##ищу среди победителей игрока если нашел одаю, есди не нашел меняю игрока
                        if curGame.winner[y][1]==Pls[0].id:
                            Pls[0].wallet=Pls[0].wallet+1
                            break##текуший коин и беру другой если но есть, нет вы хожу
                    Pls.rotate(-1)
    else :
        for i in range(len(curGame.winner)):
            while True:
                if curGame.winner[i][1]==Pls[0].id:
                    Pls[0].wallet=Pls[0].wallet+bank//len(curGame.winner)
                    break
                else:
                    Pls.rotate(-1)
        
   ##        if number>2 and number<9:## вывод кикера с учетом текуших карт
    ##            print("kKk-",ch.CutAnd(PLC,combHand))
    # стрит флешь старшая карта
    # каре старшая карта
    # фулл хаус старшая среди троек , старшая среди 2, не нужен(13.03.2020)
    # флешь старшая карта,kiker не нужен(13.03.2020)
    # стрит старшая карта,kiker не нужен(13.03.2020)
    # тройка старшая карта, кикер
    # пара старшая карта, кикер

main()
