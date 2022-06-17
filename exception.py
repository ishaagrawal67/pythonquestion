n=int(input("enter a number"))
try:
    if(n<0):
        print('number is negative')
except:
    print("find the factoril of that number")
    fct=1
    for i in range(1,n+1):
        fct=fct*i
    print(fct)


