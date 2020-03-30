#=============================================================================#
#                       Homework 5: SKY PRIORITY                              #
#       SI 100B: Introduction to Information Science and Technology           #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 03/11/2020                           #
#=============================================================================#
# task1.py - write your code for task 1 here.
flightlist=input().split()
flightlist[2]=int(flightlist[2])
flighttuple=tuple(flightlist)
custFinList=[]
custOriList=[]
space=input()
num1=input()
num=int(num1)
for x in range(num):
    custOriList.append(input())
    custFinList.append(tuple(custOriList[x].split()))
deleting=0
all_check=0
while all_check<num:
    if(custFinList[all_check-deleting][2]!=flighttuple[0]):
        del custFinList[all_check - deleting]
        all_check=all_check+1
        deleting=deleting+1
    else:
        all_check=all_check+1
custFinList.sort(key=lambda x:int(x[0]))
n=len(custFinList)
count=0
cartimes=0
if(n<=0):
    print()
while n>=20:
    print(str(max(int(custFinList[cartimes*20+19][0]),600*cartimes+flighttuple[2]))+":",end=" ")
    for i in range(19):
        print(custFinList[cartimes*20+i][1],end=" ")
    print(custFinList[cartimes*20+19][1])
    n=n-20
    cartimes=cartimes+1
else:
    if n>0:
        print(str(max(int(custFinList[cartimes * 20 + n-1][0]), 600*cartimes+flighttuple[2])) + ":", end=" ")
        for i in range(n-1):
            print(custFinList[cartimes * 20 + i][1], end=" ")
        print(custFinList[cartimes * 20 + n-1][1])

    


