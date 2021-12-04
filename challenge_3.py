ch3_input = 'challenge_3_input.txt'

def challenge_1():
    answer_dict = {'gamma': [], 'epsilon': []}
    msb_dict = {0: 0, 1: 0, 2: 0, 3:0, 4:0, 5:0 , 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
    lsb_dict = {0: 0, 1: 0, 2: 0, 3:0, 4:0, 5:0 , 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
    for number in open(ch3_input).readlines():
        for i, digit in enumerate(number.strip()):
            if int(digit) & 1:
                msb_dict[i] += 1
            else:
                lsb_dict[i] += 1
    for key in msb_dict:
        if msb_dict[key] > 500:
            answer_dict['gamma'].append(1)
            answer_dict['epsilon'].append(0)
        else:
            answer_dict['epsilon'].append(1)
            answer_dict['gamma'].append(0)

    gamma = int((''.join(map(str, answer_dict['gamma']))),2)
    epsilon = int((''.join(map(str, answer_dict['epsilon']))),2)

    return(gamma * epsilon)


def challenge_2():
    answer_dict = {'oxygen': [], 'co2': []}
    oxy_holder = []
    co2_holder = []
    msb_dict = {0: 0, 1: 0, 2: 0, 3:0, 4:0, 5:0 , 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
    lsb_dict = {0: 0, 1: 0, 2: 0, 3:0, 4:0, 5:0 , 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
    for number in open(ch3_input).readlines():
        oxy_holder.append(number)
        co2_holder.append(number)
        for i, digit in enumerate(number.strip()):
            if int(digit) & 1:
                msb_dict[i] += 1
            else:
                lsb_dict[i] += 1
    for key in msb_dict:
        if msb_dict[key] > 500:
            answer_dict['gamma'].append(1)
            answer_dict['epsilon'].append(0)
        else:
            answer_dict['epsilon'].append(1)
            answer_dict['gamma'].append(0)
    for number in open(ch3_input).readlines():
        oxy_holder.append(number)


    gamma = int((''.join(map(str, answer_dict['gamma']))),2)
    epsilon = int((''.join(map(str, answer_dict['epsilon']))),2)



    print(lsb_dict)


    return