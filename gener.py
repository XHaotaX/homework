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
