import fle
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
        for m in comb:
            if (m[1]==14):
                comb.remove(m)
#            print ("Straight")
#        print (str(result[0]) +"-"+ str(result[4]))
        combHand.clear()
#        combHand=result.copy()
        combHand.extend(result)
        return combHand
    for m in comb:
        if (m[1]==14):
            comb.remove(m)
    return False
