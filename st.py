import fle
def Straight(comb, combHand):
    temp=[]
    result=[]
    Cmp=[]
    Cmp=comb.copy()
    for m in comb:
        if (m[1]==1):
            Cmp.append([m[0],14])
    for m in Cmp:
        temp.append(m)
        i=0
        while i<len(comb):
            c=Cmp[i]
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

##    for m in Cmp:
##        if (m[1]==14):
##            Cmp.remove(m)
    if len(result)==5:
#            print ("Straight")
#        print (str(result[0]) +"-"+ str(result[4]))
        combHand.clear()
#        combHand=result.copy()
        combHand.extend(result)
        print(combHand)
        return combHand
    return False
