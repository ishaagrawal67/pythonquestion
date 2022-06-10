a=int(input("enter the first number"))
b=int(input("enter the first number"))
for i in range(a,b+1):
    if(i%5==0 and i%7==0):
        print(i,end=",")