print("enter the number")
num=int(input())
fact=1
if(num<0):
    print("no factorial find")
elif num==0:
    print ("the factorial of 0 is 1")
else:
    for i in range (1,num+1):
        fact=fact*i
    print("factorial of ",num," is ",fact)

