def Part1(data):
    changes = 0
    for i in range(1,len(data)):
        if data[i]-data[i-1] > 0 : changes += 1
    return changes

def Part2(data):
    window = [ data[i]+data[i+1]+data[i+2] for i in range(len(data)-2) ]
    return Part1(window)