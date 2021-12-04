ch2_input = 'challenge_2_input.txt'

def challenge_1():
    directions = {'forward': 0, 'up': 0}
    with open(ch2_input,'r') as input_file:
        for i in input_file.readlines():
            current = i.strip().split(' ')
            if current[0] == 'forward':
                directions['forward'] += int(current[1])
            if current[0] == 'down':
                directions['up'] += int(current[1])
            if current[0] == 'up':
                directions['up'] -= int(current[1])
    return directions['forward'] * directions['up']


def challenge_2():
    aim = 0
    horizontal = 0
    depth = 0
    with open(ch2_input,'r') as input_file:
        for i in input_file.readlines():
            current = i.strip().split(' ')
            if current[0] == 'forward':
                horizontal += int(current[1])
                depth = depth + (aim * int(current[1]))
            if current[0] == 'down':
                aim += int(current[1])
            if current[0] == 'up':
                aim -= int(current[1])
    return(horizontal * depth)
