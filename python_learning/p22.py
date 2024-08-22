# Program tp print X shape of N lines.

num_lines = int(input('Enter number of lines to draw the X shape: '))

for i in range(1, num_lines + 1):
    for j in range(1, num_lines + 1):
        if i == j or j == num_lines - i + 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()