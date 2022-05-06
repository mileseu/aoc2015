import re
#open text file, read mode | read file and split by new line
data = open('input2.txt', 'r').read().split('\n')

split_data = []
for i in range(len(data)):
    split_data.append(re.split('x', data[i]))

present_dimensions = []
for strings in split_data:
    temp_list = []
    for i in range(3):
        temp_list.append(int(strings[i]))
    present_dimensions.append(temp_list)


def total_wrapping_size():
    wrapping_paper = 0
    for dimensions in present_dimensions:
        l = dimensions[0]
        w = dimensions[1]
        h = dimensions[2]
        surface_area = (2*l*w) + (2*w*h) + (2*h*l)
        smallest_list = [l*w, l*h, w*h]
        smallest = min(smallest_list)
        wrapping_paper += surface_area + smallest
    return wrapping_paper

print(total_wrapping_size())


def total_ribbon_length():
    ribbon_length = 0
    for dims in present_dimensions:
        l = dims[0]
        w = dims[1]
        h = dims[2]
        list = sorted([l, w, h])
        smallest = list[0]
        second = list[1]
        ribbon_length += (2*smallest + 2*second) + (l*w*h)
    return ribbon_length

print(total_ribbon_length())