import fullCombHand as ch

##ну и где коментарии
##сравниваю возрашает
##0 - равны
##-1 меньше
##1 больше
def compare(Game,pl1,pl2):
##    print(pl1,pl2)
    PLC1=Game.com+Game.Plaers[pl1]
    PLC2=Game.com+Game.Plaers[pl2]
    hand1=[]
    hand2=[]
    number,hand1=ch.pure(PLC1,hand1)
    number,hand2=ch.pure(PLC2,hand2)
    if number==5:## вот че это?смахивает на кастыль
        start=1
    else:
        start=0
    for i in range(start,len(hand1)):
        if hand1[i][1]==1:
            hand1[i][1]=14
        if hand2[i][1]==1:
            hand2[i][1]=14
    for i in range(len(hand1)):
        if hand1[i][1]==hand2[i][1]:
            continue
        else:
            if hand1[i][1]>hand2[i][1]:
                return -1
            else:
                return 1
    ## в правила сказано что если в комбинации 5↓ 13 03 2020
##            карт кикир не играет роли, значИт банк делится
## значит если number=0,1,3,4,5 кикир не у ищется
    if not (number==0 or number==1 or number==3 or number==4 or number==5): 
        k1=ch.CutAnd(PLC1,hand1)
        k2=ch.CutAnd(PLC2,hand2)
    #    print(k1,k2)
        for i in range(len(k1)):
            if k2[i][1]==k1[i][1]:
                continue
            else:
                if k1[i][1]>k2[i][1]:
                    return -1
                else:
                    return 1
    return 0
