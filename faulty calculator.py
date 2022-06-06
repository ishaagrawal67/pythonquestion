# write a python program to get a faulty calculator
# where operator is +,-,*,%,/
# and 57
print("enter the first number")
num1=int(input())
print("enter the second number")
num2=int(input())
print("enter the operator which you want to apply on the number","+,-,*,%,/")
operator=input()
if(num1==45 and num2==3 and operator=="*"):
    print(555)
elif(num1==56 and num2==9 and operator=="+"):
    print(77)
elif(num1==56 and num2==6 and operator=="/"):
    print(4)
elif(operator=="+"):
    num3=num1+num2
    print(num3)
elif(operator=="-"):
    num3= num1-num2
    print(num3)
elif(operator=="*"):
    num3=num1*num2
    print(num3)
elif(operator=="/"):
    num3=num1/num2
    print(num3)
else:
    print("unexpected operator in the calculator")