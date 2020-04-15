def pair(comb,combHand):##полный отстой , передалть возми функцию для пар и впихни её сюда ,ну а по ка да кастыль полсе этой функции
    Pa=[]
    temp=[]
    for y in range(14):
        for i in comb:
 ##           print(i)
            if i[1]==y:
                temp.append(i)
        Pa.append(temp.copy())##сздесь какая то ерудна пока оставил так так носли тыснова тут то проверь может сттоит поднять этостроку в иф(начальное предположение)
#        print(Pa)
        temp.clear()
#    print(Pa)
    for y in Pa:
        if len(y)>3:
##            print("Kare")
##            print(y)
            combHand.extend([4,y])
        else:
            if len(y)>2:
##                print("Set")
##                print(y)
                combHand.append([3,y])
            else:
                if len(y)>1:
##                    print("Pair")
##                    print(y)
                    combHand.append([2,y])
    return combHand
