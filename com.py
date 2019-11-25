import fullCombHand as ch

def compare(Game,pl1,pl2):
##    print(pl1,pl2)
    PLC1=Game.com+Game.Plaers[pl1]
    PLC2=Game.com+Game.Plaers[pl2]
    hand1=[]
    hand2=[]
    number,hand1=ch.pure(PLC1,hand1)
    number,hand2=ch.pure(PLC2,hand2)
    if number==5:
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
