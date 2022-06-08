#Write a program to find the sum of the digits of a number accepted from user
n=int(input("enter the number"))
s=0
while(n>0):
    d=n%10
    s=s+d
    n=n//10
print("sum of digits is: ",s)

