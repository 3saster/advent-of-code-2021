from functools import reduce

def parseData(data):
    return [[int(n) for n in d] for d in data]

# Get valid neighbors to a point
def neighbors(heights,x,y):
    neigh = []
    [max_X,max_Y] = [len(heights[0]),len(heights)] 

    if x-1 >= 0    : neigh.append((x-1,y+0))
    if x+1 < max_X : neigh.append((x+1,y+0))
    if y-1 >= 0    : neigh.append((x+0,y-1))
    if y+1 < max_Y : neigh.append((x+0,y+1))

    return neigh

# Neighbors that are taller and not 9
def tallerNeighbors(heights,x,y):
    curr = heights[y][x]
    return {n for n in neighbors(heights,x,y) if heights[n[1]][n[0]] != 9 and heights[n[1]][n[0]] > curr}

# Determines if (x,y) is a low point
def isLow(heights,x,y):
    [max_X,max_Y] = [len(heights[0]),len(heights)] 
    curr = heights[y][x]

    for coor in neighbors(heights,x,y):
        if not(curr < heights[coor[1]][coor[0]]): return False
    return True

# Determines size of basin from (x,y)
def basinSize(heights,x,y):
    basinSet = {(x,y)}
    basinSet2 = basinSet.union(tallerNeighbors(heights,x,y))
    while basinSet2 != basinSet:
        newPoints = basinSet2 - basinSet
        basinSet = basinSet2
        for coor in newPoints:
            basinSet2 = basinSet2.union(tallerNeighbors(heights,*coor))
    return len(basinSet)





def Part1(data):
    heights = parseData(data)
    lowPoints = []

    for y in range(len(heights)):
        for x in range(len(heights[0])):
            if isLow(heights,x,y):
                lowPoints.append(heights[y][x])
    return sum(lowPoints) + len(lowPoints)

def Part2(data):
    heights = parseData(data)
    lowPoints = []

    for y in range(len(heights)):
        for x in range(len(heights[0])):
            if isLow(heights,x,y):
                lowPoints.append([x,y])

    basinSizes = [basinSize(heights,*l) for l in lowPoints]
    return reduce(lambda a,b: a*b, sorted(basinSizes)[-3:])