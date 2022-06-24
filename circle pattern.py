#row =6
#col=4
for i in range(6):
    for j in range(4):
        if((j == 0 or j == 4-1) and (i!=0 and i!=6-1)) :
            print('*',end='')   #end='' so that print statement should not change the line.
        elif( ((i==0 or i==6-1) and (j>0 and j<4-1))):
            print('*',end='')
        else:
            print(end=' ')  #to print the space.
    print()