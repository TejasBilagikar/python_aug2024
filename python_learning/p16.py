# Program to reverse a number.

input_num = int(input('Enter a number to reverse it: '))
new_num = 0
temp_num = input_num
while temp_num != 0:
    digit = temp_num % 10
    temp_num = temp_num // 10
    new_num = new_num * 10 + digit
    print(f'The reversal of {input_num} is {new_num}')