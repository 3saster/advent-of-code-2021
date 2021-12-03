from collections import Counter

def Part1(data):
    transpose = [''.join(b) for b in zip(*data)]
    gamma_rate   = ''.join( [Counter(num).most_common()[0][0]  for num in transpose] )
    epsilon_rate = ''.join( [Counter(num).most_common()[-1][0] for num in transpose] )
    return int(gamma_rate,2) * int(epsilon_rate,2)


def Part2(data):
    oxygen = data
    CO2    = data

    for i in range(len(data[0])):
        most_com = Counter([num[i] for num in oxygen]).most_common()
        most_com = most_com[0][0] if (len(most_com)<2 or most_com[0][1]!=most_com[1][1]) else '1'
        oxygen = [o for o in oxygen if o[i]==most_com]

        least_com = Counter([num[i] for num in CO2]).most_common()
        least_com = least_com[-1][0] if (len(least_com)<2 or least_com[-1][1]!=least_com[-2][1]) else '0'
        CO2 = [o for o in CO2 if o[i]==least_com]

    return int(oxygen[0],2) * int(CO2[0],2)