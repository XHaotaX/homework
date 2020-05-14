import fullCombHand as ch
import com as compare

class table:
    com=[]
    Plaers=[]
    winner=[]

def winer(allcards,Id):
    com=["fleshRoal","stritFlesh","Kare","FullHouse",##нужно для выывода инфы можно убрать
     "Flush","Straight","Set","2pair","pair","Kiker"]
    combHand=[]
    curGame=table()
    curGame.Plaers.clear()##это 
    curGame.com.clear()## полное 
    curGame.winner.clear()## нужна адекватная алтернатива

    curGame.com=allcards[:5]##5 карт из сгенрированой группы обшие 
    curGame.winner.append([10,10,10])

    for i in range(int((len(allcards)-5)/2)):##здесь творится весь ад , все котлы тут +-(нужно делится @)
        curGame.Plaers.append(allcards[5+2*i:5+2*(i+1)])##получаю карты игрока
        ##    theHighest(comb,combHand)
        PLC=curGame.com+curGame.Plaers[i]##формирую массив всех карт игрока (рука+стол)
##            print("Plyer "+str(i+1)+" -",curGame.Plaers[i])
        number,combHand=ch.pure(PLC,combHand)##вывод исхода карт для игрока, number-номер комбинации combHand-карты комбинации
        ##както не поняятно , я понял13.03.2020
        ##вообшем сечайс ты в цикле
##            сдесь строкой выше мы нали на ивысшую кобинацию у тебя на руках
##            теперь строкой ниже мы проверяем  она равна, она ниже или выше уже проверенх в этом цикле комбинаций
        print("-",com[number],combHand)##нужно для выывода инфы можно убрать

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

##    if (len(curGame.winner)>1):
##        print("Plaers делят банк")
##        for i in range(len(curGame.winner)):
##            print("Player ",curGame.winner[i][1]+1,"-",com[curGame.winner[i][0]])
##    else :
##        print("Player ",curGame.winner[0][1]+1,"-",com[curGame.winner[0][0]])
    for i in range(len(curGame.winner)):
        curGame.winner[i][1]=Id[curGame.winner[i][1]]
    return curGame
