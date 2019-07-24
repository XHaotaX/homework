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
    winer=[]

com=["fleshRoal","stritFlesh","Kare","FullHouse",
     "Flush","Straight","Set","2pair","pair","Kiker"]
gg=[[2, 1], [2, 3], [2, 5], [2, 10], [3, 8], [3, 13], [4, 6]]
combHand=[]
for i in range(1):
##    comb=gg
##    NPlaer=2
##    comb=gener.gg(NPlaer)#по умолчанияю 2
    allcards=gener.gg(6)
    curGame=table()
    curGame.com=allcards[:5]
    print(curGame.com)
    for i in range(int((len(allcards)-5)/2)):
        curGame.Plaers=allcards[5+2*i:5+2*(i+1)]
##    theHighest(comb,combHand)
        PLC=curGame.com+curGame.Plaers
        print("Plyer "+str(i+1)+" -",curGame.Plaers)
        number,combHand=ch.pure(PLC,combHand)
        print("-",com[number],combHand)
##        if number>2 and number<9:## вывод кикера с учетом текуших карт
##            print("kKk-",ch.CutAnd(PLC,combHand))

# стрит флешь старшая карта
# каре старшая карта
# фулл хаус старшая среди троек , старшая среди 2, кикер
# флешь старшая карта,kiker
# стрит старшая карта,kiker
# тройка старшая карта, кикер
# пара старшая карта, кикер
