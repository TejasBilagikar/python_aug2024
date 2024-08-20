#Read a number from the user and check if the number is Even or not.

my_number = int(input('Enter a number to check if it is Even or not. '))

if my_number % 2 == 0:
    print(f'{my_number} is an Even number.')
else:
    print(f'{my_number} is not an Even')