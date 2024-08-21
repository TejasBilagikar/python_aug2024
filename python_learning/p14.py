#Program to find second smallest digit in a number.

input_num = int(input('Enter a number to find the second smallest digit in it: '))
temp_num = input_num
small_dig = smallest_dig = 9

while temp_num != 0:
    dig = temp_num % 10
    temp_num = temp_num // 10
    if dig < smallest_dig:
        small_dig = smallest_dig
        smallest_dig = dig
    if dig < small_dig and dig != smallest_dig:
        small_dig = dig

print(f'The second smallest digit in {input_num} is: {small_dig}')
