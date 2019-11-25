import gener
import fle
import st
import fullH
import Arrr
import fair
import fullCombHand as ch
import com as compare
#def ButiOut(y)

class table:
    com=[]
    Plaers=[]
    winner=[]

class Plaer:
##    позиция за столом 
    position=[]
##  карты игрока  
    card=[]
##  состояние пока не продуман?( , не участвует в раздаче ,не участвует в розыгрыше банка и .?. 
    state=[]

def gRound(allcards):
    Plaers=Plaer()
    for i in range(int((len(allcards)-5)/2)):
        ## вот как сука сделать temp=Plaer() который не будет привязан
        ## хотел сделать список обьектов неполучилось
        ## rft;t 'nj ujdyj
##        temp=Plaer()
##        curGame.Plaers.append(allcards[5+2*i:5+2*(i+1)])##получаю карты игрока
##        temp.card.append(allcards[5+2*i:5+2*(i+1)])
##        temp.position=i
##        Plaers.append(copy(temp))
        Plaers.card.append(allcards[5+2*i:5+2*(i+1)])
        Plaers.position.append(i)
    for i in range(len(Plaers.card)):
        print ("Your cards is : ",Plaers.card[i],Plaers.position[i])
##    =input()
##    print(o+2)
## разделим игру на круги торговли
##первый круг
##    карты розданый на столе 0 карт
##второй круг
##    на столе 3 карты
##третий круг
##    на столе 4 карты
##четвертый круг
##    на столе 5 карт
##
##действия игроков делятся на
##    имеюшие и не имеюшие послдесвия
##    чек и фолд и не имею раиз алл ин
##    в случае кола требуется проверить наличие равных ставок у всех игроков
##
##раунзаканчивается когда
##последний игрок делает действие не имеюшее последсвии
##или
##    если он елат
##        то последним игроко становится человек ходивший передним
##блин это не все
##
##если н участвуюших игроков == 1 розгрыш банка заканчивается
##оставший ся игрок объявлен побиделем и полуает банк
##
##статус игрока сидяшего за столом
##    0 не участвует в розгрыше
##    1 сделал чек устаивает текушее сотаяние хочет продолжить
##    2 раиз посил сатвка значит
##        продолжит игру
##            если все постоят не меньшего иначе победитель ,
##                вслучае не достака игровой
##                    валют игроку передлагается пойти в алл ин
##    3 call уровнял ставку готов
##    4 сделал алин или ставка совпадает с предыдушим
## ааа , мне нехочется это делать
## 25.11.2019 16:09 плохая метка
## слудшими пожеланиями не дожить до завтра, удачи
    ## call(уровнять), rais on {n}(), allin (поставить , но это врядли буду реализовывать хотя нет придется( )
## chech(оставить ставку без повышения), fold(сбросить карты, и выйти из текушей игры(не стол))
## leav покинуть стол но до этого ещё далеко ) (
def main():
    com=["fleshRoal","stritFlesh","Kare","FullHouse",
         "Flush","Straight","Set","2pair","pair","Kiker"]
    gg=[[2, 2], [2, 3], [1, 5], [2, 10], [3, 8], [1,4],[2,4],[3, 4], [4, 4],[1,7],[2,1]]
    combHand=[]
    for i in range(1):
    ##    allcards=gg
        NPlaer=3
        allcards=gener.gg(NPlaer)
        curGame=table()
        curGame.com=allcards[:5]##5 карт из сгенрированой группы обшие 
        curGame.winner.append([10,10,10])
        print(curGame.com)
        gRound(allcards)
        for i in range(int((len(allcards)-5)/2)):
            curGame.Plaers.append(allcards[5+2*i:5+2*(i+1)])##получаю карты игрока
            ##    theHighest(comb,combHand)
            PLC=curGame.com+curGame.Plaers[i]##формирую массив всех карт игрока (рука+стол)
##            print("Plyer "+str(i+1)+" -",curGame.Plaers[i])
            number,combHand=ch.pure(PLC,combHand)##вывод исхода карт для игрока, number-номер комбинации combHand-карты комбинации
            print("-",com[number],combHand)

            if curGame.winner[0][0]>number:
                curGame.winner.clear()
                curGame.winner.append([number,i,combHand.copy()])
            else:
                if curGame.winner[0][0]==number:
                    temp=compare.compare(curGame,curGame.winner[0][1],i)
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
        else :
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


    
main()
