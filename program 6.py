# Write a program to print first 10 even numbers.
print("enter the number you want to print even number")
n=int(input())
for i in range(0,n+1):
    if(i%2==0):
        print(i)