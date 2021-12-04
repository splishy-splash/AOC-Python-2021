ch1_input = 'challenge_1_input.txt'

def challenge_1():
    answer = 0
    previous = 0
    with open(ch1_input, 'r') as inputs:
        numbers = inputs.readlines()
        for i in numbers:
            if (int(i) > previous) and (previous != 0):
                answer += 1
            previous = int(i)
    return answer


def challenge_2():
    answer = 0
    previous = 0
    with open(ch1_input, 'r') as inputs:
        numbers = inputs.readlines()
        for count, i in enumerate(numbers):
            try:
                current = int(i) + int(numbers[count+1]) + int(numbers[count+2])
                if (current > previous) and (previous != 0):
                    answer += 1
            except IndexError:
                pass
            previous = current
    return answer