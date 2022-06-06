# Write a Python program to count the number of even and odd numbers from a series of numbers
list=[1,2,3,4,5,6,7,8,9,10]
c=0
o=0
for n in list:
    if(n%2==0):
        c=c+1
    elif(n%2!=0):
        o=o+1
print("total number of even and odd number is",c,o)
