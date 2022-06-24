rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))

print("Rectangle Star Pattern")
for i in range(rows):
    for j in range(columns):
        print('*', end = '  ')
    print()
