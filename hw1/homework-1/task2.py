#=============================================================================#
#                       Homework 5: SKY PRIORITY                              #
#       SI 100B: Introduction to Information Science and Technology           #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 03/11/2020                           #
#=============================================================================#
# task2.py - write your code for task 2 here.
flightlist = input().split()
flightlist[2] = int(flightlist[2])
flightlist[1] = int(flightlist[1]) #Sum Customer Of Flight
ECO = []
BUS = []
space1 = input()
numOfEco = int(input())
for x in range(numOfEco): #range0会怎么样
    shuru = input().split() #把input转换成列表
    shuru[0] = int(shuru[0])
    if shuru[2] == flightlist[0]:
        ECO.append(shuru) #0time1name2flight
ECO.sort(key=lambda z : int(z[0]))
space2=input()
numOfBus=int(input())
for x in range(numOfBus):
    shuru=input().split()
    shuru.append(0)
    shuru[0]=int(shuru[0])
    if shuru[2] == flightlist[0]:
        BUS.append(shuru)
BUS.sort(key=lambda z:int(z[0]))
CustomerNum=len(ECO)+len(BUS)
allbus=CustomerNum//20+1
cartime=0
bus=[]
people_gone_ECO=0
people_gone_BUS=0
people_gone_BUS_temp=0
people_gone_ECO_temp=0
bus.append(flightlist[2])#Bus到站时间初始值
peopleOnBus=[]
####################################################################################以上为输入
while cartime < allbus:
    people_gone_BUS_temp=people_gone_BUS
    people_gone_ECO_temp=people_gone_ECO
    for i in range(people_gone_BUS,min(people_gone_BUS+20,len(BUS))):
        if BUS[i][0] <= bus[cartime]:
            peopleOnBus.append(BUS[i])
            people_gone_BUS_temp+=1
        else:
            break
    for i in range(people_gone_ECO,min(people_gone_ECO+20-len(peopleOnBus),len(ECO))):
        if ECO[i][0] <= bus[cartime]:
            peopleOnBus.append(ECO[i])
            people_gone_ECO_temp+=1
        else:
            break
    while len(peopleOnBus) < 20:
        if people_gone_BUS_temp >= len(BUS):
            if people_gone_ECO_temp >= len(ECO):
                break
            peopleOnBus.append(ECO[people_gone_ECO_temp])
            people_gone_ECO_temp += 1
        elif people_gone_ECO_temp >=len(ECO):
            if people_gone_BUS_temp >= len(BUS):
                break
            peopleOnBus.append(BUS[people_gone_BUS_temp])
            people_gone_BUS_temp += 1
        elif BUS[people_gone_BUS_temp][0] <= ECO[people_gone_ECO_temp][0]:
            peopleOnBus.append(BUS[people_gone_BUS_temp])
            people_gone_BUS_temp += 1
        else:
            peopleOnBus.append(ECO[people_gone_ECO_temp])
            people_gone_ECO_temp += 1
    else:
        people_gone_ECO = people_gone_ECO_temp
        people_gone_BUS = people_gone_BUS_temp
    print(str(max(int(peopleOnBus[len(peopleOnBus)-1][0]),bus[cartime]))+":",end=" ")
    for i in range(len(peopleOnBus) - 1):
        print(peopleOnBus[i][1], end=" ")
    print(peopleOnBus[len(peopleOnBus) - 1][1])
    bus.append(max(int(peopleOnBus[len(peopleOnBus)-1][0]),bus[cartime])+600)
    cartime+=1
    peopleOnBus.clear()



