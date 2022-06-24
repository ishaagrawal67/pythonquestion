def calculate(exp):
    total=0
    for item in exp:
        total=total+item
    return total
tom_list=[100,2000,300,300]
joe_list=[90,80,870]
calculate_tom=calculate(tom_list)
calculate_joe=calculate(joe_list)
print("sum of tom list is ",calculate_tom)
print("sum oof joe list is :",calculate_joe)
