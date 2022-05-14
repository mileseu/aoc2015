import numpy as np
import re

data = open('input6.txt', 'r').read().split('\n')
example = 'toggle 461,550 through 564,900'
grid = np.zeros((1000,1000), dtype=int)
instructions = ['toggle', 'turn on', 'turn off']


def part_one():
    for line in data:
        digits = re.findall(r'\d+', line)
        delta_x = range(int(digits[0]), int(digits[2])+1)
        delta_y = range(int(digits[1]), int(digits[3])+1)

        if instructions[0] in line:
            for x in delta_x:
                for y in delta_y:
                    if grid[x,y] == 1:
                        grid[x,y] = 0
                    else:
                        grid[x,y] = 1

        elif instructions[1] in line:
            for x in delta_x:
                for y in delta_y:
                    grid[x,y] = 1

        elif instructions[2] in line:
            for x in delta_x:
                for y in delta_y:
                    grid[x,y] = 0

    count = np.count_nonzero(grid == 1)
    print('Total occurences of "1" in array: ', count)

def part_two():
    for line in data:
        digits = re.findall(r'\d+', line)
        delta_x = range(int(digits[0]), int(digits[2])+1)
        delta_y = range(int(digits[1]), int(digits[3])+1)

        if instructions[0] in line:
            for x in delta_x:
                for y in delta_y:
                    grid[x,y] += 2

        elif instructions[1] in line:
            for x in delta_x:
                for y in delta_y:
                    grid[x,y] += 1

        elif instructions[2] in line:
            for x in delta_x:
                for y in delta_y:
                    if grid[x,y] != 0:
                        grid[x,y] -= 1

    count = np.sum(grid)
    print('Sum of array: ', count)

part_two()