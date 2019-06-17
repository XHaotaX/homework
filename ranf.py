import random as r

#def ButiOut(y)

def gg():
    comb=[]
    cm=[]
    cch=[]
    m =["♥","♦","♣","♠"]
    k=7
    while len(comb)<k:
        mn=r.randint(1,4)
##       if mn==1:
##            mn="♥"
##        else :
##            if mn==2:
##                mn="♦"
##            else:
##                if mn==3:
##                    mn="♣"
##                else:
##                    if mn==4:
##                        mn="♠"
        che=r.randint(1,13)
##        if che==1:
##            che="A"
##        else :
##            if che==2:
##                che="J"
##            else:
##                if che==3:
##                    che="Q"
##                else:
##                    if che==4:
##                        che="K"
##                    else:
##                        che=str(che)
       # print(mn+che)     
        if comb.count(str(mn)+str(che)):
            #print(str(mn)+str(che))
            k=k
        else:
            cm.append(mn)
            cch.append(che)
            comb.append(str(mn)+str(che))
    temp=[]
    for i in range(k):
        temp.append([cm[i],cch[i]])
    return temp

def fR(comb, combHand):
    fl=[]
    temp=[]
    for y in range(4):
        for i in comb:
#            print(i)
            if i[0]==y:
#                print(y)
                temp.append(i)
        fl.append(temp.copy())
#        print(fl)
        temp.clear()
#    print(fl)
    for y in fl:
        if len(y)>4:
            print("Flesh")
            print(y)
            combHand.append(y)
            return True
    return False

def pair(comb, combHand):
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
    cOnF=0
    for y in Pa:
        if len(y)>3:
            print("Kare")
            print(y)
            combHand.append(y)
        else:
            if len(y)>2:
                print("Set")
                print(y)
                combHand.append(y)
            else:
                if len(y)>1:
                    print("Pair")
                    print(y)
                    combHand.append(y)
                    
def Straight(comb, combHand):
    temp=[]
    result=[]
    for m in comb:
        if (m[1]==1):
            comb.append([m[0],14])
    for m in comb:
        temp.append(m)
        i=0
        while i<len(comb):
            c=comb[i]
            if (m[1]+1==c[1]):
                if (len(temp)==5):
                    temp=temp[1:]
                temp.append(c)
                m=c
                i=0
            else:
                i=i+1
        if len(temp)==5:
#            print ("Straight")
#            print (temp)
            result=temp.copy()
        temp.clear()
    if len(result)==5:
        if fR(result,combHand):
            if result[4][1]==14:
                print("OMG, FLESHROAL")
            else:
                print("Woaw, STRITFLESH")
        else:
            print ("Straight")
        print (result)
        
com=["fleshRoal","stritFlesh","Kare","FullHouse",
     "Flush","Straight","Set","pair","Kiker"]
#gg=[[1,13],[1,9],[1,12],[1,11],[1,10],[3,5],[1,8]]
combHand=[]
for i in range(10):
    comb=gg()
    print(comb)
    fR(comb,combHand)
    pair(comb,combHand)
    Straight(comb.copy(), combHand)
