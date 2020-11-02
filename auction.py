from collections import deque
import random 
##27.02.2020 09:55 как же сдесь мало кометраиев
## нужно больше крови(в среде (родной) коментарии красные)
##15.04.2020 14:43 жизнь тлен и даже наличие коментов енм еняет тогофакккта что ... fh,ep(20.06.2020 9:43)

##state   =0 - фолд
##        =1 - чек
##        =2 - колл
##        =3 - рейз
##        =4 - алл
##        =5 - ререйз
##        =6 - алл и не участвует последуешем повышении

def roadToEnd(Pls):##если в игре остался только один игрок способный продолжать торговлю дальше то 1 иначе 0 
    end=0
    for pl in Pls:
        if pl.state==0 or pl.state==4 or pl.state==6:
            end=end+1    
    if (end+1)==int((len(Pls)-5)/2):
        return 1
    else:
        return 0

def start(Pls,gg,auto=False):
##    gg=[[2, 12], [1, 5], [3, 12], [4, 12], [1, 12], [2, 8], [1, 2], [4, 5], [2, 9], [2, 7], [2, 4]]   
    around=0
    bank=0
    curCost=0
    endRoundId=int((len(gg)-5)/2)
##    Pls=deque()
##    Pls,bank,auto=False
##    for i in range(int((len(gg)-5)/2)):##тут
##        Pls.append(Player())##типо заполняю 
##        Pls[i].card=gg[5+2*i:5+2*(i+1)]##даю карты каждому игроку
##        Pls[i].id=i
##        Pls[i].state=9
##    for pl in Pls:
##        print(pl.card)
##        print(pl.id)

    end=0
    table=[]
    ##теперь есть масив обьектов представляюших каждого игрока Pls
    curCost=2
    
    Pls[0].bet=1
    Pls[0].wallet=Pls[0].wallet-Pls[0].bet
    Pls[0].roundBet+=Pls[0].bet
    bank=bank+Pls[0].bet
    Pls.rotate(-1)
    Pls[0].bet=2
    Pls[0].wallet=Pls[0].wallet-Pls[0].bet
    Pls[0].roundBet+=Pls[0].bet
    bank=bank+Pls[0].bet
    endRoundId=Pls[0].id
    print("start")
    while True:
##        print("id -- state - bet")
        print(Pls[0].id,"--",Pls[0].state,"-----",Pls[0].bet,"-----------------------")
        Pls.rotate(-1)
        if endRoundId==Pls[0].id:##тут типо оканчание круга торговли,
            around=around+1
            minBet=Pls[0].roundBet
            chBan=1#убейте плиз

            for i in Pls:#если кто пошел в алл ин значит нада разделить банк на до и после
                if i.state==4:
                    chBan=0
                    break
            ##30.10.2020 11:36 ктото в алл, переменая chBan=0 ,запускается цикл обработки банка    
            while chBan==0:##23.10.2020 13:52 моя не понимать как это работать хнык хнык <( 30.10.2020 11:30 памагыте хелп
                for pl in Pls:
                    print(pl.id,"\t",pl.state,"\t",pl.bet,"$\t",pl.wallet)
                if chBan==0:##30.10.2020 12:50 все еще не могу 30.10.2020 12:57 начинается просветление 30.10.2020 14:10 почему оно работает?
                    for i in Pls:#минимальная ставка в текушем круге, выделение минимальной ставки
                        if minBet<i.roundBet and not (i.state==6 or i.state==0):
                            minBet=i.roundBet
                    for i in Pls:#для текушей минимальной ставки
                        if not ((i.state==6) or (i.state==0)):##предполагаю , что ст=5 это значит что игрок израсходовал фишки и он не может продолжат текушюю торговля и соответственно претендовать на фишки каторые будут вложены в банк
                            if i.roundBet==minBet:
                                i.state=6
                                continue
                            ## и на кой черт ты увеличиваешь банк???
                            ## все текушие ставки складываю в банк потом при делениии все ставки
                            if minBet>i.roundBet:
                                bank+=i.roundBet##я не понимаю как но это строчка не ломает выходнуюю сумму всех слогаемых
                                i.roundBet=0
                            else:
                                bank+=minBet
                                i.roundBet=minBet
                ##я так понял \/ это чтоб банк разделяся пока есть что делить
                for i in Pls:#если кто пошел в алл ин значит нада разделить банк на до и после
                    if i.state==4:
                        chBan=0
                        break
                    else:##30.10.2020 12:36 мозг отказывается углублятся  вто как это работает, происходило зацикливание, непонимаю как оно должно вообше выхадить из цикла, пишу этот елсе
                        chBan=1
                t=input()
            
            if around==1:## 0- 0 карт на столе
                print("S2",gg[:3])
                table=gg[:3]
            if around==2:## 1- 3 карты на столе
                print("S3",gg[:4])
                table=gg[:4]
            if around==3:## 2- 4 карты на столе
                print("S4",gg[:5])
                table=gg[:5]
            if around==4:## 3- 5 карт на столе
                print("Ennd")
                return bank##конец торговли
            ## переход на следуюшую улицу или вообше выход и там покмане придумал
            ## а там просто сравнение карта тоесть алгоритм делает точто уже умеет
            ## смотреть затем чтоб непроверял игроков не принемашив участиев розыгрыше, и ли по иным причинам
            ##не имеющий прав участвовать в розыгреше
            ## вот читаю и думаю зачем писать так facenapalm
        for pl in Pls:
            if pl.state==0:
                end=end+1    
            if (end+1)==int((len(gg)-5)/2):
                return bank
        end=0
##  навыводить всю информацию каждому игроку о  текушем столе
##        print("id-",Pls[0].id)
##        if not (Pls[0].state==0 or Pls[0].state==4):
##            print(table)
##        print("id \t state \t bet \t wallet")
##        for pl in Pls:
##            print(pl.id,"\t",pl.state,"\t",pl.bet,"$\t",pl.wallet)
        if Pls[0].state==0 or Pls[0].state==4 or Pls[0].state==6 or roadToEnd(Pls):
            continue
        else:
            move=0
            if curCost==Pls[0].bet:
##                BetZer(Pls,auto)
                if auto:
                    move=random.choice(["ch","r"])
                else:
                    print(Pls[0].card)
                    while (True):
                        print("check(ch) \t raise")
                        move=input()
                        if not (move=="ch" or move=="r"):
                            print("incorrect")
                        else:
                            break
                if move=="ch":
                    Pls[0].state=1
                    continue
                if move=="r":##rais фунциюю all in можно сделать также
                    if auto:
                        bet=random.randrange(5,7)
                    else:
                        while True:
                            bet=input()##ток добавь к параметрам класса парметр текушихших вишек -сор не понял, вишек ?мб фишек, ток зачем? стоит обьяснять раз и без этого работает)
                            if "all"==bet:
##                                Pls[0].state=4
                                bet=Pls[0].wallet
                                break
                            if str.isdigit(bet):
                                bet=int(bet)
                                break
                            else:
                                print("non number")
                    if bet>=Pls[0].wallet:
                        bet=Pls[0].wallet
                        Pls[0].state=4
                        Pls[0].wallet=0
                    else:
                        Pls[0].wallet=Pls[0].wallet-bet
##                        Pls[0].wallet=Pls[0].wallet-(curCost-Pls[0].bet)
                    Pls[0].roundBet+=bet
                    Pls[0].state=3
                    bank=bank+bet
                    curCost=curCost+bet## прибаляю бет так как выбор между чек и реиз значит реиз повыщает текушую ставку на столе
##                    Pls[0].wallet=Pls[0].wallet-(curCost-Pls[0].bet)
                    Pls[0].bet+=bet##сделано одельно, чтоб в случии, ошибки были видны @)
                    endRoundId=Pls[0].id
                    continue#ch and r 
            else:##я хочу аписать что нормальное но не могу , какого ...
##                BetNotZer(Pls,auto)# f , r , c
                if auto:
                    move=random.choice(["f","c","r"])
                else:
                    while (True):
                        print(Pls[0].card)
                        print(" fall \t call  \t raise")
                        move=input()
                        if not (move=="f" or move=="c" or move=="r"):
                            print("incorrect")
                        else:
                            break
                if move=="f": ##fall
                    Pls[0].state=0
                    continue
                if move=="c" or move=="r":
                    if Pls[0].wallet<=(curCost-Pls[0].bet):
                        Pls[0].roundBet+=Pls[0].wallet
                        bank=bank+Pls[0].wallet
##                        Pls[0].wallet=0
                        Pls[0].state=4
                        Pls[0].bet+=Pls[0].wallet
                        Pls[0].wallet=0 ##23.10.2020 14:18 должно равняться нулю ттк все фишки ушли на кол 
                        continue
                    else:
                        Pls[0].roundBet+=(curCost-Pls[0].bet)
                        bank=bank+(curCost-Pls[0].bet)##call
                        Pls[0].state=2 ##2 or 1 thinking about it                    
                        Pls[0].wallet=Pls[0].wallet-(curCost-Pls[0].bet)
                        Pls[0].bet=curCost
                    if not move=="r":
                        continue
                if move=="r":##rais фунциюю all in можно сделать также
##                    bank=bank+(curCost-Pls[0].bet)##call
                    if auto:
                        bet=random.randrange(5,7)
                    else:
                        while True:
                            bet=input()##ток добавь к параметрам класса парметр текушихших вишек -сор не понял, вишек ?мб фишек, ток зачем? стоит обьяснять раз и без этого работает) -ТАК ОН ВРОДЕ ЕСТЬ
                            if "all"==bet:
                                Pls[0].state=4
                                bet=Pls[0].wallet
                                break
                            if str.isdigit(bet):
                                bet=int(bet)
                                break
                            else:
                                print("non number")
                    Pls[0].state=5
                    if bet>=Pls[0].wallet:
                        bet=Pls[0].wallet
                        Pls[0].state=4
                        Pls[0].wallet=0
                    else:
                        Pls[0].wallet=Pls[0].wallet-bet
##                         Pls[0].wallet=Pls[0].wallet-(curCost-Pls[0].bet)
                    bank=bank+bet
                    Pls[0].roundBet+=bet
                    curCost=curCost+bet                            
                    Pls[0].bet+=bet##сделано одельно, чтоб в случии, ошибки были видны @)
                    endRoundId=Pls[0].id
                    continue


##k,t=main()
##print("{",k)
##print("id \t state \t bet \t wallet")
##for pl in t:
##    print(pl.id,"\t",pl.state,"\t",pl.bet,"$\t",pl.wallet)
