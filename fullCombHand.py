import gener
import fle
import st
import fullH
import Arrr
import fair

##какойто заопарк ищи pure

def CutAnd(comb,combHand):
    temp=comb.copy()
##    чет не уверен что но работает правииьно не трогаю 13.03.2020
    for i in temp:
        if i[1]==1:
            i[1]=14
    for i in combHand:
        temp.remove(i)
    return Kiker(temp)

def Kiker(comb):
    k=0
    for y in range(len(comb)):
        if comb[y][1]==1 or comb[y][1]>comb[k][1] and not comb[k][1]==1:
            k=y
    return [comb[k]]

def pure(comb,combHand):#вывод сильнейшей комбинации
    combHand.clear()
    if fle.fR(comb,combHand):
        if st.Straight(combHand,combHand):##сдесь идет проврека на стрит-флеш 
            if combHand[4][1]==14:
                return 0,combHand##
            else:
                return 1,combHand##
    combHand.clear()
    fair.pair(comb,combHand)
    for y in combHand: ## пусть будет не трогай , если мвссив пустой не выдает ошибки 
        if y==4:
            return 2,combHand[combHand.index(y)+1]
        
    if fullH.fullHA(combHand):  
        if len(combHand)>3:
            return 3,combHand
    combHand.clear()
    
    if fle.fR(comb,combHand):
        return 4,combHand

    if st.Straight(comb, combHand):
        return 5,combHand
    
    combHand.clear()
    fair.pair(comb,combHand)

    if fullH.fullHA(combHand):
        return 6,combHand
    
    combHand.clear()
    fair.pair(comb,combHand)
    if Arrr.paiAAr(combHand):
        if len(combHand)==2:
            return 8,combHand
        if len(combHand)==4:
            return 7,combHand
    combHand.clear()
    return 9,Kiker(comb)

##вывод всех комбинаций
def theHighest(comb,combHand):
    combHand.clear()
##    флешь флешь флешь
    if fle.fR(comb,combHand):
        print("flesh")
        print(combHand)
        ##        нашли флешь проверяем не стрили он ;(
        if st.Straight(combHand,combHand):
            ##            коль стрит да еще и высший  №1
            if combHand[4][1]==14:
                print("talalalalaaaaaaa")
        ##            пррсто стир флешь №2
            print("eehy")
##        елсе №5
    combHand.clear()  
    fair.pair(comb,combHand)# находим все пул из 4 3 2 кард    
    for y in combHand:# №3 проверка на каре
        if y[0]==4:
            print("kare"+str(y))
        
    if fullH.fullHA(combHand):# запускается после fair.pair, ищем фулхаус
        #если есть хотябы сет вернет combHand, иначе False  
        if len(combHand)>3:
            print(combHand)#№4
        else:
            print("set")#№7
            print(combHand)
    combHand.clear()        
    fair.pair(comb,combHand)# находим все пул из 4 3 2 кард   
    #ишем пары , чем больше тем луче)
    if Arrr.paiAAr(combHand):#надо подумать можно ли сделать луче
        if len(combHand)==2:
            print("pair")
        if len(combHand)==4:
            print("2pair")
        print(combHand)

##проверка на стрит №6
    if st.Straight(comb, combHand):
        print ("Straight")
        print (str(combHand[0]) +"-"+ str(combHand[4]))
    combHand.clear()
