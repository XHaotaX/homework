from collections import deque

class Plaer:
    card=[]
    state=0
    bet=0
    id
    
def main():
   
    bank=0
    or
    bakr=bb+mbb
    curCost=0
    endRoundId=n
    Pls=deque()
    
    for i in nP##тут
        pl=Plaer()##типо заполняю 
        pl.card.append(gg[5+n+(1-2)])##даю карты каждому игроку
        pl.id=i
        Pls.append(pl)
        
    ##теперь есть масив обьектов представляюших каждого игрока Pls

    Pls[0].bet=bb
    Pls[1].bet=bb/2
    
    for pl in Pls
    
        if endRoundId==pl.id:##тут типо оканчание круга торговли,
            ## переход на следуюшую улицу или вообше выход и там покмане придумал            
            return 1

        if Pls.state=0
            continue
        move=0
        print(pl.card)
        move=input()
        if move=0: ##fall
            pl.state=0
            continue
        if move=1:
            pl.state=1
            continue
        if move=2:
            bank=bank+(curCost-pl.bet)
            pl.bet=curCost
            pl.state=2 ##2 or 1 thinking about it
            continue
        if move=3:##rais фунциюю all in можно сделать также
            bet=input()##ток добавь к параметрам класса парметр текушихших вишек
            bank=bank+bet
            curCost=curCost+bet
            pl.bet=pl.bet+bet##сделано одельно чтоб в случии ошибки были видны @)
            endRoundId=pl.id         
