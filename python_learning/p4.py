#Program to Accept three distinct numbers and find smallest among them.

#number1, number2, number3 = input("Enter three numbers separated by space: ").split()
number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
number3 = int(input('Enter third number: '))

smallest_num = number1
if number2 < smallest_num:
    smallest_num = number2
elif number3 < smallest_num:
    smallest_num = number3

print(f"The smallest number is {smallest_num}")
