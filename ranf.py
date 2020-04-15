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

def gRound(allcard):
    Plaers=Plaer()
    for i in range(int((len(allcard)-5)/2)):
        ## вот как сука сделать temp=Plaer() который не будет привязан
        ## хотел сделать список обьектов неполучилось
        ## rft;t 'nj ujdyj
##        temp=Plaer()
##        curGame.Plaers.append(allcards[5+2*i:5+2*(i+1)])##получаю карты игрока
##        temp.card.append(allcards[5+2*i:5+2*(i+1)])
##        temp.position=i
##        Plaers.append(copy(temp))
        Plaers.card.append(allcard[5+2*i:5+2*(i+1)])
        Plaers.position.append(i)
    for i in range(len(Plaers.card)):
        print ("Your cards is : ",Plaers.card[i],Plaers.position[i])
    Plaers.position.clear()
    Plaers.card.clear()
    Plaers.state.clear()
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
## 27.02.2020 09:48 плохая метка что это значит?
    ## слудшими пожеланиями не дожить до завтра, удачи
    ## call(уровнять), rais on {n}(), allin (поставить , но это врядли буду реализовывать хотя нет придется( )
## chech(оставить ставку без повышения), fold(сбросить карты, и выйти из текушей игры(не стол))
## leav покинуть стол но до этого ещё далеко ) (
def main():
    com=["fleshRoal","stritFlesh","Kare","FullHouse",
         "Flush","Straight","Set","2pair","pair","Kiker"]
    gg=[[2, 12], [1, 5], [3, 12], [4, 12], [1, 12], [2, 8], [1, 2], [4, 5], [2, 9], [2, 7], [2, 4]]   
    combHand=[]
    for r in range(1):
     ##   allcards=gg
        NPlaer=3
        allcards=gener.gg(NPlaer)
        curGame=table()
        curGame.com=allcards[:5]##5 карт из сгенрированой группы обшие 
        curGame.winner.append([10,10,10])
        print(allcards)
        gRound(allcards)
        for i in range(int((len(allcards)-5)/2)):
            curGame.Plaers.append(allcards[5+2*i:5+2*(i+1)])##получаю карты игрока
            ##    theHighest(comb,combHand)
            PLC=curGame.com+curGame.Plaers[i]##формирую массив всех карт игрока (рука+стол)
##            print("Plyer "+str(i+1)+" -",curGame.Plaers[i])
            number,combHand=ch.pure(PLC,combHand)##вывод исхода карт для игрока, number-номер комбинации combHand-карты комбинации
            ##както не поняятно , я понял13.03.2020
            ##вообшем сечайс ты в цикле
##            сдесь строкой выше мы нали на ивысшую кобинацию у тебя на руках
##            теперь строкой ниже мы проверяем  она равна она ниже или выше уже проверенх в этом цикле комбинаций
            print("-",com[number],combHand)

            if curGame.winner[0][0]>number:##help
                curGame.winner.clear()##чет тут скушно
                curGame.winner.append([number,i,combHand.copy()])##но когда есть коменты веселеле)
            else:##толь не захломляй плиз. !!!!СЮДА СМОТРИ СУКА!!!!, НЕ ЗАХЛОМЛЯЙ  ГОВНО-КОМЕНТАРИЯМ СВОЙ ГОВНО-КОД!!!!!!
                if curGame.winner[0][0]==number:
                    temp=compare.compare(curGame,curGame.winner[0][1],i)
                    ##сравниваю возрашает
                    ##0 - равны
                    ##-1 меньше
                    ##1 больше
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
        curGame.Plaers.clear()##это 
        curGame.com.clear()## полное 
        curGame.winner.clear()## нужна адекватная алтернатива
        ##но она покрайне мере работает без танцев с б, просто работае
        ##....
        
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
