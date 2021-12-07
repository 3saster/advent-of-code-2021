def parseData(data):
    return [int(d) for d in data[0].split(',')]
    
def crabDist1(crabs, pos):
    return sum([abs(c-pos) for c in crabs])

def crabDist2(crabs, pos):
    triag = lambda n: n*(n+1)//2
    return sum([triag(abs(c-pos)) for c in crabs])




def Part1(data):
    crabs = parseData(data)
    fuelCost = {p:crabDist1(crabs,p) for p in range(min(crabs),max(crabs))}
    minFuel = min(fuelCost.items(),key=lambda x:x[1])

    return minFuel[1]

def Part2(data):
    crabs = parseData(data)
    fuelCost = {p:crabDist2(crabs,p) for p in range(min(crabs),max(crabs))}
    minFuel = min(fuelCost.items(),key=lambda x:x[1])

    return minFuel[1]