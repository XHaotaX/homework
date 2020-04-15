from collections import deque
##27.02.2020 09:55 как же сдесь мало кометраиев
## нужно больше крови
class Player:
    card=[]
    state=0
    bet=0
    wallet=1500##кошелек
    id
    
def main():
    gg=[[2, 12], [1, 5], [3, 12], [4, 12], [1, 12], [2, 8], [1, 2], [4, 5], [2, 9], [2, 7], [2, 4]]   
    around=0
    bank=0
    bb=2
##    or
##    bakr=bb+mbb
    curCost=0
    endRoundId=int((len(gg)-5)/2)
    Pls=deque()
    
    for i in range(int((len(gg)-5)/2)):##тут
##        pl=Player()##типо заполняю 
##        pl.card.append(gg[5+2*i:5+2*(i+1)])##даю карты каждому игроку
##        pl.id=i
##        Pls.append(pl)
        Pls.append(Player())
        Pls[i].card=gg[5+2*i:5+2*(i+1)]
##        Pls.##даю карты каждому игроку
        Pls[i].id=i
        Pls[i].state=9
    for pl in Pls:
        print(pl.card)
        print(pl.id)
    end=0
    table=[]
    ##теперь есть масив обьектов представляюших каждого игрока Pls
    curCost=2
    
    Pls[0].bet=1
    Pls[0].wallet=Pls[0].wallet-Pls[0].bet
    bank=bank+Pls[0].bet
    Pls.rotate(-1)
    Pls[0].bet=2
    Pls[0].wallet=Pls[0].wallet-Pls[0].bet
    bank=bank+Pls[0].bet
    endRoundId=Pls[0].id
    print("start")
    while True:
        Pls.rotate(-1)
        print("id-",Pls[0].id)
        if endRoundId==Pls[0].id:##тут типо оканчание круга торговли,
            around=around+1
            if around==1:
                print(gg[:3])
                table=gg[:3]
            if around==2:
                print(gg[:4])
                table=gg[:4]
            if around==3:
                print(gg[:5])
                table=gg[:5]
            if around==4:
                return bank,Pls##конец торговли
 #            0- 0 карт на столе
##            1- 3 карты на столе
##            2- 4 карты на столе
##            3- 5 карт на столе
            ## переход на следуюшую улицу или вообше выход и там покмане придумал
            ## а там просто сравнение карта тоесть алогритм делает точто уже умеет
            ## смотреть затем чтоб непроверял игроков не принемашив участиев розыгрыше, и ли по иным причинам
            ##не имеющий прав участвовать в розыгреше
            
        for pl in Pls:
            if pl.state==0:
                end=end+1    
            if (end+1)==int((len(gg)-5)/2):
                return bank,Pls
        end=0
##  навыводить всю информацию каждому игроку о  текушем столе
        if not (Pls[0].state==0 or Pls[0].state==4):
            print(table)
            print("id \t state \t bet \t wallet")
            for pl in Pls:
                print(pl.id,"\t",pl.state,"\t",pl.bet,"$\t",pl.wallet)
        if Pls[0].state==0 or Pls[0].state==4:
            continue
        else:
            move=0
            print(Pls[0].card)
            if curCost==Pls[0].bet:
                print(" fall \t check(ch) \t raise")
                while (True):
                    move=input()
                    if not (move=="f" or move=="ch" or move=="r"):
                        print("incorrect")
                    else:
                        break
                if move=="f": ##fall
                    Pls[0].state=0
                    continue
                if move=="ch":
                    Pls[0].state=1
                    continue
                if move=="r":##rais фунциюю all in можно сделать также
                    while True:
                        state=3
                        bet=input("You is push r.\nBB bet pls:")##ток добавь к параметрам класса парметр текушихших вишек
                        if "all"==bet:
                            print("all")
                            Pls[0].state=4
                            bet=100
                            break
                        if str.isdigit(bet):
                            bet=int(bet)
                            break
                        else:
                           print("non number")
                    bank=bank+bet
                    curCost=curCost+bet
                    Pls[0].wallet=Pls[0].wallet-(curCost-Pls[0].bet)
                    Pls[0].bet=Pls[0].bet+bet##сделано одельно, чтоб в случии, ошибки были видны @)
                    endRoundId=Pls[0].id
                    continue
            else:
                print(" fall \t call  \t raise")
                while (True):
                    move=input()
                    if not (move=="f" or move=="c" or move=="r"):
                        print("incorrect")
                    else:
                        break
                if move=="f": ##fall
                    Pls[0].state=0
                    continue
                if move=="c":
                    bank=bank+(curCost-Pls[0].bet)##call
                    Pls[0].wallet=Pls[0].wallet-(curCost-Pls[0].bet)
                    Pls[0].bet=curCost
                    Pls[0].state=2 ##2 or 1 thinking about it
                    continue
                if move=="r":##rais фунциюю all in можно сделать также
                    while True:
                        state=3
                        bank=bank+(curCost-Pls[0].bet)##call
##                        Pls[0].bet=curCost
                        bet=input()##ток добавь к параметрам класса парметр текушихших вишек
                        if "all"==bet:
                            print("all")
                            Pls[0].state=4
                            bet=Pls[0].wallet
                            break
                        if str.isdigit(bet):
                            bet=int(bet)

                            break
                        else:
                            print("non number")
                    bank=bank+bet
##                    if bet+Pls[0].bet>curCost:##нужно дорроотать , это в тех случая когда нехватает денег
##                        curCost=bet+Pls[0].bet
##                    else:
                    curCost=curCost+bet                            
                    Pls[0].wallet=Pls[0].wallet-(curCost-Pls[0].bet)
##                    Pls[0].bet=curCost
                    Pls[0].bet=curCost##сделано одельно, чтоб в случии, ошибки были видны @)
                    endRoundId=Pls[0].id
                    continue
    for pl in Pls:
        if not pl.state==0:
            print(pl.id,"\t",pl.state,"\t",pl.bet,"$\t",pl.wallet)

k,t=main()
print("{",k)
print("id \t state \t bet \t wallet")
for pl in t:
    print(pl.id,"\t",pl.state,"\t",pl.bet,"$\t",pl.wallet)
    
