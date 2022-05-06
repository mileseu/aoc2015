data = open('input3.txt', 'r').read()

#terrible solution, will fix at some point but probably not.

def count_houses(directions):
    x = 0
    y = 0
    position = (x, y)
    houses = {position: 1}
    houses_more_than_one = 0
    for arrow in directions:
        if arrow == "^":
            y += 1
            position = (x, y)
            if position in houses:
                houses[position] += 1
            else:
                houses[position] = 1
        elif arrow == ">":
            x += 1
            position = (x, y)
            if position in houses:
                houses[position] += 1
            else:
                houses[position] = 1
        elif arrow == "v":
            y -= 1
            position = (x, y)
            if position in houses:
                houses[position] += 1
            else:
                houses[position] = 1
        elif arrow == "<":
            x -= 1
            position = (x, y)
            if position in houses:
                houses[position] += 1
            else:
                houses[position] = 1
    present_delivered = houses.values()
    for number in present_delivered:
        if number >= 1:
            houses_more_than_one +=1
    print(houses_more_than_one)

def double_santas(directions):
    santa_x = 0
    santa_y = 0
    robot_x = 0
    robot_y = 0
    santa_position = (santa_x, santa_y)
    robot_position = (robot_x, robot_y)
    houses = {santa_position: 1}

    for i in range(0, len(directions), 2):
        if directions[i] == "^":
            santa_y += 1
            santa_position = (santa_x, santa_y)
            if santa_position in houses:
                houses[santa_position] += 1
            else:
                houses[santa_position] = 1
        elif directions[i] == ">":
            santa_x += 1
            santa_position = (santa_x, santa_y)
            if santa_position in houses:
                houses[santa_position] += 1
            else:
                houses[santa_position] = 1
        elif directions[i] == "v":
            santa_y -= 1
            santa_position = (santa_x, santa_y)
            if santa_position in houses:
                houses[santa_position] += 1
            else:
                houses[santa_position] = 1
        elif directions[i] == "<":
            santa_x -= 1
            santa_position = (santa_x, santa_y)
            if santa_position in houses:
                houses[santa_position] += 1
            else:
                houses[santa_position] = 1
    for i in range(1, len(directions), 2):
        if directions[i] == "^":
            robot_y += 1
            robot_position = (robot_x, robot_y)
            if robot_position in houses:
                houses[robot_position] += 1
            else:
                houses[robot_position] = 1
        elif directions[i] == ">":
            robot_x += 1
            robot_position = (robot_x, robot_y)
            if robot_position in houses:
                houses[robot_position] += 1
            else:
                houses[robot_position] = 1
        elif directions[i] == "v":
            robot_y -= 1
            robot_position = (robot_x, robot_y)
            if robot_position in houses:
                houses[robot_position] += 1
            else:
                houses[robot_position] = 1
        elif directions[i] == "<":
            robot_x -= 1
            robot_position = (robot_x, robot_y)
            if robot_position in houses:
                houses[robot_position] += 1
            else:
                houses[robot_position] = 1
    present_delivered = len(houses.values())
    print(present_delivered)

count_houses(data)
double_santas(data)
