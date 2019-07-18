def paiAAr(combHand):
    t=[]
#    combHand.clear()
##    print(combHand)
    for y in combHand:
        if y[0]==2:
            t.extend(y)
    combHand.clear()
    if len(t)==2:
        t.remove(t[0]) 
        combHand.extend(t[0])
#        print("pair")
        return combHand
    if len(t)>=4:
        while len(t)>4:
            t.remove(t[0])
        combHand.extend(t[1])
        combHand.extend(t[3])
#        print("2pair")
        return combHand
    return False    
