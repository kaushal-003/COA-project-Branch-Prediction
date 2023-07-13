import pandas as pd

pd.set_option('display.max_rows', 500)

PHT=[]
for i in range (0,64):
    PHT.append(1)

GHR='0000'
PC=0
# def brAdcomp(PC,num):
#     PC=PC+2+num
#     return PC
def decode(ins):
    if(ins[:6]=="001011" or ins[:6]=="001100"):
        return 1
    elif(ins[:6]=="001101" or ins[:6]=="001110"):
        return 2
    else: 
        return 0
def exe(ins,RS1):
    
    if(decode(ins)==2):
        return 0
    elif(decode(ins)==1):
        if(RS1==0 and ins[:6]=="001011"):
            return 0
        elif(RS1!=0 and ins[:6]=="001100"):
            return 0
        else:
            
            return 1
    else:
        return 0  
    

mis_pred=1

BHR='0000'



z=int(input("Enter a number to run a loop(max 1000)"))
while z<=1000:
    RS1=int(input("Enter value of RS1: "))
    PC=input("Enter PC address:    ")
    arr=input("enter instruction:  ")
    
    m=PC[30:31]
    t=m+BHR
    # print(t)
    x=int(t,2)
    # print(PHT[x]//2)
    y=PHT[x]//2
    print("branch_prediction:")
    if(y==0):
        print("Not taken")
    else:
        print("taken")
    
    if(PHT[x]//2==0):
        PHT[x]-=1
    else:
        PHT[x]+=1
    # if(PHT[x]>3):
    #     PHT[x]=1
    # elif(PHT[x]<0):
    #     PHT[x]=0
    mis_pred=exe(arr,RS1)
    print("mispredictionbit:")
    print(mis_pred)
    if(mis_pred==1):
        if(y==0):
            PHT[x]+=2
        else:
            PHT[x]-=2
    if(PHT[x]>3):
        PHT[x]=1
    elif(PHT[x]<0):
        PHT[x]=0
    if(mis_pred==0):
        if(y==0):
            BHR='0'+BHR[:3]
        else:
            BHR='1'+BHR[0:3]

    else:
        if(y==1):
            BHR='0'+BHR[0:3]
        else:
            BHR='1'+BHR[0:3]
    print("bhr: "+ BHR)
    data=pd.DataFrame(PHT)
    print(data)
    z+=1

