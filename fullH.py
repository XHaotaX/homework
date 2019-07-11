def fullHA(combHand):#False нет даже сета, 1 аргумент сет , 2 если есть пара
    temp=[]
    t=[]
    k=0
    print(combHand)
    #сет
    for y in combHand:
        if y[0]==3:
            t.clear()
            t.extend(y)
            k=3
    if k==3:
        for y in combHand:
            print(y)
            if y[0]==3 and y[1][0][1]>t[1][0][1]:
                t.clear()
                t.extend(y)
        temp.extend(t)
    else:
        return False
    #пара к сету
#    print("--")
#    print(combHand)
    for y in combHand:
#        print(y)
        if y[0]==2:
            t.clear()
            t.extend(y)
            k=5
    if k==5:
        for y in combHand:
#            print("-")
#            print(t[0][1][1])
            if y[0]==2 and y[1][0][1]>t[1][0][1]:
                t.clear()
                t.extend(y)
        temp.extend(t)
    combHand.clear()
    combHand.extend(temp)
    return combHand

    #fullha/^\
                
    #       |
