def fR(comb, combHand):
##    if comb:
##        return False
    fl=[]
    temp=[]
    for y in range(4):
        for i in comb:
#            print(i)
            if i[0]==y:
#                print(y)
                temp.append(i)
        fl.append(temp.copy())
##        print(fl)
        temp.clear()
#    print(fl)
    for y in fl:
        if len(y)>4:
##            print("Flesh")
##            print(y)
            combHand.clear()
            combHand.extend(y)
            for m in combHand:
                if (m[1]==1):
                    combHand.append([m[0],14])
            combHand.sort()
            while not len(combHand)==5:
                combHand.remove(combHand[0])
            return combHand
    return False
