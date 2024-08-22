# Program to Print X shape inside Hollow Square.

num_lines = int(input('Enter number of lines to draw the shape: '))

for i in range(1, num_lines + 1):
    for j in range(1, num_lines + 1):
        if i == 1 or i == num_lines or j == 1 or j == num_lines or i == j or j == num_lines - i + 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
