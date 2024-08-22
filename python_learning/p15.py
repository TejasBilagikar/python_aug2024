# Program to find Sum of even(odd) digits in a number.

input_num = int(input('Enter a number to find sum of even digits in it: '))
total = 0
temp_num = input_num
while temp_num != 0:
    digit = temp_num % 10
    temp_num = temp_num // 10
    if digit % 2 == 0:             # for Odd digits:- if digit % 2 != 0: 
        total += digit
print(f'The sum of the even digits in {input_num} is: {total}')