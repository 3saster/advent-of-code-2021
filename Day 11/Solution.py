def parseData(data):
    return [[int(n) for n in row] for row in data]

def neighbors(oct,x,y):
    neigh = []
    [max_X,max_Y] = [len(oct[0]),len(oct)] 

    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if 0 <= x+i < max_X and 0 <= y+j < max_Y: 
                neigh.append((x+i,y+j))
    neigh.remove((x,y))

    return neigh

def advanceOctopus(octopus):
    flashes = 0
    advancedOct = [[oct+1  for oct in row] for row in octopus]

    flashingOct = [[i,j] for i in range(len(advancedOct)) for j in range(len(advancedOct[i])) if advancedOct[i][j]>=10]
    while len(flashingOct) > 0:
        for pos in flashingOct:
            advancedOct[pos[0]][pos[1]] -= 10
            flashes += 1
            for n in neighbors(advancedOct,*pos):
                advancedOct[n[0]][n[1]] += 1
            flashingOct = [[i,j] for i in range(len(advancedOct)) for j in range(len(advancedOct[i])) if advancedOct[i][j]>=10]

    # We rely on the fact an octupus only gain 9 energy in one round, and hence cannot flash more than once
    for i in range(len(advancedOct)):
        for j in range(len(advancedOct[i])):
            if advancedOct[i][j] < octopus[i][j]:
                advancedOct[i][j] = 0

    return advancedOct,flashes
    
    



def Part1(data):
    octopus = parseData(data)
    flashes = 0
    
    for _ in range(100):
        (octopus,f) = advanceOctopus(octopus)
        flashes += f
    return(flashes)

def Part2(data):
    octopus = parseData(data)
    totalOct = sum([1 for row in octopus for oct in row])
    
    (octopus,flashes) = advanceOctopus(octopus)
    steps = 1
    while flashes < totalOct:
        (octopus,flashes) = advanceOctopus(octopus)
        steps += 1
    return(steps)