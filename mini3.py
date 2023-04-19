num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 < num2 and num1 < num3:
    max_num = num1
elif num2 < num1 and num2 < num3:
    min_num = num2
else:
    min_num = num3

print("The minimum number is", min_num)
