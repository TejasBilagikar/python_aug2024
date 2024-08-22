# Program to print the Equi Lateral Triangle of N lines.

import math

n_lines = int(input('Enter the number of lines for a Equilateral triangle: '))

space_count = n_lines - 1
sym_count = 1
line_count = n_lines

while line_count != 0:
    print('  ' * space_count, end='')
    print('* ' * sym_count)
    sym_count += 2
    space_count -= 1
    line_count -= 1
    