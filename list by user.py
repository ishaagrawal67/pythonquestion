'''lst=[]
b=int(input("enter the umber of element"))
for i in range(0,b):
    ele=int(input())
    lst.append(ele)
print(lst)'''

listA = []
n = int(input("Enter number of elements in the list : "))
for i in range(0, n):
   print("Enter element No-{}: ".format(i+1))
   elm = int(input())
   listA.append(elm) # adding the element
print("The entered list is: \n",listA)