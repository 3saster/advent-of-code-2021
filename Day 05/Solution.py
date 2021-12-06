from collections import defaultdict
from math import gcd, dist

def parseData(data):
    return [[list(map(int,coord.split(','))) for coord in str.split(' -> ')] for str in data ]
    
def getSlopes(lines):
    slopes = [[v2-v1 for v1,v2 in zip(l[0],l[1])] for l in lines]
    slopes = [list(map(lambda q: q//gcd(*s),s)) for s in slopes]
    return slopes





def Part1(data):
    lines = parseData(data)

    coordGrid = defaultdict(lambda: 0)
    slopes = getSlopes(lines)

    for line,slope in zip(lines,slopes):
        if sum(map(abs,slope)) == 1:
            pos = line[0]
            while pos != line[1]:
                coordGrid[tuple(pos)] += 1
                pos = list(map(sum,zip(pos,slope)))
            coordGrid[tuple(pos)] += 1

    return sum(1 for cross in coordGrid.values() if cross >= 2)

def Part2(data):
    lines = parseData(data)

    coordGrid = defaultdict(lambda: 0)
    slopes = getSlopes(lines)

    for line,slope in zip(lines,slopes):
        pos = line[0]
        while pos != line[1]:
            coordGrid[tuple(pos)] += 1
            pos = list(map(sum,zip(pos,slope)))
        coordGrid[tuple(pos)] += 1

    return sum(1 for cross in coordGrid.values() if cross >= 2)