# Program to Find Odd placed Even digits in a number.

input_num = int(input('Enter a Number to find Odd placed Even digits in a number:'))

num = str(input_num)
odd_placed_even_num = ''
for i in range(len(num)+1):
    if i % 2 == 0:
        if int(num[i]) % 2 == 0:
            odd_placed_even_num += num[i]

total = 0


print('Odd placed digits in number is',odd_placed_even_num)
