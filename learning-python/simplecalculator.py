num = float(input("enter a number: "))
operator = input("please enter the operator here(+,-,*,%): ")
num2 = float(input("enter the 2nd number: "))

if operator == "+" :
    print(num + num2)
elif operator == "-" :
    print(num - num2)
elif operator == "*" :
    print(num * num2)
elif operator == "%" :
    print(num * num2)
else:
    print("Please enter a valid operator! ")