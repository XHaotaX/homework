def paiAAr(combHand):
    t=[]
#    combHand.clear()
    for y in combHand:
        if y[0]==2:
            t.extend(y)
    combHand.clear()
    if len(t)==2:
        combHand.extend(t)
        print("pair")
        return combHand
    if len(t)>=4:
        while len(t)>4:
            t.remove(t[0])
        combHand.extend(t)
        print("2pair")
        return combHand
    return False    
