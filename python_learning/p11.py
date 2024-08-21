# Program to find Sum of digits of a number.

input_num = (input('Enter the number to find the sum: '))

total = 0
for i in input_num:
    total += int(i)
    
print(f'The sum of {input_num} is: {total}')
