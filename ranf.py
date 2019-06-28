import gener
import fle
import st
import fullH
import Arrr
#def ButiOut(y)

def pair(comb,combHand):
    Pa=[]
    temp=[]
    for y in range(13):
        for i in comb:
            if i[1]==y:
                temp.append(i)
        Pa.append(temp.copy())
#        print(Pa)
        temp.clear()
#    print(Pa)
    for y in Pa:
        if len(y)>3:
##            print("Kare")
##            print(y)
            combHand.append([4,y[1]])
        else:
            if len(y)>2:
##                print("Set")
##                print(y)
                combHand.append([3,y[1]])
            else:
                if len(y)>1:
##                    print("Pair")
##                    print(y)
                    combHand.append([2,y[1]])
    for y in combHand:
        if y[0]==4:
            print("kare"+str(y))
    if fullH.fullHA(combHand):
        if len(combHand)>1:
            print(combHand)
        else:
            print("set")
            print(combHand)
        return combHand
    if Arrr.paiAAr(combHand):
        print(combHand)
        

        

com=["fleshRoal","stritFlesh","Kare","FullHouse",
     "Flush","Straight","Set","2pair","pair","Kiker"]
gg=[[4,9],[1,9],[1,12],[3,11],[1,10],[2,11],[1,11]]
combHand=[]
for i in range(10):
    comb=gg
#    comb=gener.gg()
    comb.sort()
    print(comb)
    pair(comb,combHand)
    if fle.fR(comb,combHand):
        print("flesh")
        print(combHand)
        if st.Straight(combHand,combHand):
            if combHand[4][1]==14:
                print("talalalalaaaaaaa")
            print("eehy")
    if st.Straight(comb, combHand):
        print ("Straight")
        print (str(combHand[0]) +"-"+ str(combHand[4]))
    combHand.clear()

# стрит флешь старшая карта
# каре старшая карта
# фулл хаус старшая среди троек , старшая среди 2, кикер
# флешь старшая карта
# стрит старшая карта
# тройка старшая карта, кикер
# пара старшая карта, кикер
