#Program to find biggest (smallest) digit in a number.

input_num = input('Enter a number to find the biggest digit: ')
big_dig = '0'

for i in input_num:
    #big_num = i
    if i > big_dig:
        big_dig = i

print(f'The biggest digit in {input_num} is: {big_dig}')