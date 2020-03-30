#=============================================================================#
#                       Homework 5: SKY PRIORITY                              #
#       SI 100B: Introduction to Information Science and Technology           #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 03/11/2020                           #
#=============================================================================#
# task2.py - write your code for task 2 here.
# =============================================================================#
#                       Homework 5: SKY PRIORITY                              #
#       SI 100B: Introduction to Information Science and Technology           #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 03/11/2020                           #
# =============================================================================#
# task1.py - write your code for task 1 here.
flightlist = input().split()
flightlist[2] = int(flightlist[2])
flightlist[1] = int(flightlist[1])#Sum Customer Of Flight
ECO = []
BUS = []
space1 = input()
numOfEco = int(input())
for x in range(numOfEco):#range0会怎么样
    shuru = input().split()#把input转换成列表
    shuru.append(1)
    shuru[0]=int(shuru[0])
    if shuru[2] == flightlist[0] :
        ECO.append(shuru)#0time1name2flight
ECO.sort(key=lambda z : int(z[0]))
space2=input()
numOfBus=int(input())
for x in range(numOfBus):
    shuru=input().split()
    shuru.append(0)
    shuru[0]=int(shuru[0])
    if(shuru[2]==flightlist[0]):
        BUS.append(shuru)
BUS.sort(key=lambda z:int(z[0]))
CustomerNum=len(ECO)+len(BUS)
allbus=CustomerNum//20+1
bus=[]
BusArriving=flightlist[2]#Bus到站时间初始值
people_gone_ECO=0
people_gone_BUS=0
bus.append(flightlist[2])
#######################################################################
y=allbus
while y>1:#y=NO.  of  bus
    peopleOnBus = []
    ECOcount = 0#count for people arriving before bus
    BUScount = 0
    for x in range(people_gone_ECO,len(ECO)):
        if(int(ECO[x][0]) <= BusArriving):#if time satisfied
            ECOcount += 1
    for x in range(people_gone_BUS,len(BUS)):
        if( int(BUS[x][0]) <= BusArriving ):
            BUScount+=1
    count=ECOcount+BUScount
    if count >= 20:#people waiting more than 20
        for x in range(people_gone_BUS , people_gone_BUS+BUScount):
            peopleOnBus.append(BUS[x])
        else:
            people_gone_BUS = x
        for x in range(people_gone_ECO,people_gone_ECO+20-BUScount):
            peopleOnBus.append(ECO[x])
        else:
            people_gone_ECO = x
        print(str(max(peopleOnBus[19][0], BusArriving))+":", end=" ")
        for i in range(19):
            print(peopleOnBus[i][1], end=" ")
        print(peopleOnBus[19][1])
        people_gone_BUS=people_gone_BUS+BUScount
        people_gone_ECO=people_gone_ECO+20-BUScount
        BusArriving+=600
        peopleOnBus=[]
        y=y-1
    else: #车到了人没齐并且后面还有人
        for x in range(people_gone_BUS , people_gone_BUS+BUScount):
            peopleOnBus.append(BUS[x])
        else:
            people_gone_BUS = x+1
        for x in range(people_gone_ECO,people_gone_ECO+ECOcount):
            peopleOnBus.append(ECO[x])
        else:
            people_gone_ECO = x+1
        if BUScount==0:
            people_gone_BUS=people_gone_BUS-1
        if ECOcount==0:
            people_gone_ECO=people_gone_ECO-1
        ECO_pointer=people_gone_ECO
        BUS_pointer=people_gone_BUS
        for x in range(20*(allbus-y),20*(allbus-y)+20-count):
            if ECO_pointer>=len(ECO):
                if BUS_pointer>=len(BUS):
                    break
                peopleOnBus.append(BUS[BUS_pointer])
                BUS_pointer = BUS_pointer + 1
            elif BUS_pointer>=len(BUS):
                if ECO_pointer>=len(ECO):
                    break
                peopleOnBus.append(ECO[ECO_pointer])
                ECO_pointer = ECO_pointer + 1
            elif BUS[BUS_pointer][0]<=ECO[ECO_pointer][0]:
                peopleOnBus.append(BUS[BUS_pointer])
                BUS_pointer=BUS_pointer+1
            else:
                peopleOnBus.append(ECO[ECO_pointer])
                ECO_pointer=ECO_pointer+1
        people_gone_BUS=BUS_pointer
        people_gone_ECO=ECO_pointer
        print(str(max(peopleOnBus[len(peopleOnBus) - 1][0], BusArriving)) + ":", end=" ")
        for i in range(len(peopleOnBus) - 1):
            print(peopleOnBus[i][1], end=" ")
        print(peopleOnBus[len(peopleOnBus) - 1][1])
        BusArriving=peopleOnBus[len(peopleOnBus)-1][0]+600
    y=y-1
    peopleOnBus.clear()
else:
    ECOcount = 0  # count for people arriving before bus
    BUScount = 0
    for x in range(people_gone_ECO, people_gone_ECO+ECOcount):
        if (int(ECO[x][0]) <= BusArriving):  # if time satisfied
            ECOcount += 1
    for x in range(people_gone_BUS, people_gone_BUS+BUScount):
        if (int(BUS[x][0]) <= BusArriving):
            BUScount += 1
    count = ECOcount + BUScount
    if count==CustomerNum%20 :
        for x in range(people_gone_BUS , len(BUS)):
            peopleOnBus.append(BUS[x])
        else:
            people_gone_BUS = x+1
        for x in range(people_gone_ECO , len(ECO)):
            peopleOnBus.append(ECO[x])
        else:
            people_gone_ECO = x+1
        peopleOnBus.sort(key=lambda z: int(z[0]))
        print(str(max(peopleOnBus[len(peopleOnBus)-1][0],BusArriving))+":",end=" ")
        for i in range (len(peopleOnBus)-1):
            print(peopleOnBus[i][1],end=" ")
        print(peopleOnBus[len(peopleOnBus)-1][1])
        BusArriving+=600
    else:
        ECOcount = 0  # count for people arriving before bus
        BUScount = 0
        for x in range(people_gone_ECO, len(ECO)):
            if (int(ECO[x][0]) <= BusArriving):  # if time satisfied
                ECOcount += 1
        for x in range(people_gone_BUS, len(BUS)):
            if (int(BUS[x][0]) <= BusArriving):
                BUScount += 1
        for x in range(people_gone_BUS, people_gone_BUS + BUScount):
            peopleOnBus.append(BUS[x])
        else:
            people_gone_BUS = x + 1
        for x in range(people_gone_ECO, people_gone_ECO + ECOcount):
            peopleOnBus.append(ECO[x])
#        if BUScount==0:
 #           people_gone_BUS=people_gone_BUS-1
 #       if ECOcount==0:
   #         people_gone_ECO=people_gone_ECO-1
        ECO_pointer = people_gone_ECO
        BUS_pointer = people_gone_BUS
        for x in range(20 * (allbus - 1), CustomerNum):
            if ECO_pointer >= len(ECO):
                if BUS_pointer >= len(BUS):
                    break
                peopleOnBus.append(BUS[BUS_pointer])
                BUS_pointer = BUS_pointer + 1
            elif BUS_pointer >= len(BUS):
                if ECO_pointer >= len(ECO):
                    break
                peopleOnBus.append(ECO[ECO_pointer])
                ECO_pointer = ECO_pointer + 1
            elif BUS[BUS_pointer][0] <= ECO[ECO_pointer][0]:
                peopleOnBus.append(BUS[BUS_pointer])
                BUS_pointer = BUS_pointer + 1
            else:
                peopleOnBus.append(ECO[ECO_pointer])
                ECO_pointer = ECO_pointer + 1
        people_gone_BUS = BUS_pointer
        people_gone_ECO = ECO_pointer
        print(str(max(peopleOnBus[CustomerNum % 20 - 1][0], BusArriving)) + ":", end=" ")
        for i in range(len(peopleOnBus) - 1):
            print(peopleOnBus[i][1], end=" ")
        print(peopleOnBus[len(peopleOnBus) - 1][1])
        BusArriving = peopleOnBus[len(peopleOnBus) - 1][0] + 600
    y = y - 1
    peopleOnBus.clear()














