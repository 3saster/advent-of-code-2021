from collections import Counter,defaultdict

def parseData(data):
    return [[int(n) for n in d] for d in data]     

def flatten(list):
    return [n for sub in list for n in sub]

class node:
    def __init__(self,coord,neighbors,risk):
        self.coord = coord
        self.neighbors = neighbors
        self.risk = risk
        self.startRisk = -1

class graph:
    def __init__(self,points):
        self.nodeDict = dict()
        for y in range(len(points)):
            for x in range(len(points[0])):
                self.nodeDict[(x,y)] = node((x,y),[],risk=points[y][x])

        keys = self.nodeDict.keys()
        for v in keys:
            if (p := (v[0]+1,v[1])) in keys: self.nodeDict[v].neighbors.append( self.nodeDict[p] )
            if (p := (v[0]-1,v[1])) in keys: self.nodeDict[v].neighbors.append( self.nodeDict[p] )
            if (p := (v[0],v[1]+1)) in keys: self.nodeDict[v].neighbors.append( self.nodeDict[p] )
            if (p := (v[0],v[1]-1)) in keys: self.nodeDict[v].neighbors.append( self.nodeDict[p] )

    # Dijkstra's algorithm
    def shortestPath(self,start):
        curNode = self.nodeDict[start]
        curNode.startRisk = 0

        unvisited = {curNode.coord}
        unmarked = {self.nodeDict[n].coord for n in self.nodeDict.keys()} - {curNode.coord}

        while curNode != None:
            for neigh in curNode.neighbors:
                if neigh.coord in unmarked:
                    neigh.startRisk = neigh.risk + curNode.startRisk
                    unmarked -= {neigh.coord}
                    unvisited.add(neigh.coord)
                else:
                    neigh.startRisk = min(neigh.risk + curNode.startRisk, neigh.startRisk)
            unvisited -= {curNode.coord}
            neighRisks = [(n,self.nodeDict[n].startRisk) for n in unvisited-unmarked]
            if len(neighRisks) > 0:
                curNode = self.nodeDict[ min(neighRisks,key=lambda s:s[1])[0] ]
            else:
                curNode = None





def Part1(data):
    points = parseData(data)
    caveGraph = graph(points)
    caveGraph.shortestPath((0,0))

    end = max(caveGraph.nodeDict.keys(),key=lambda s:sum(s))
    return caveGraph.nodeDict[end].startRisk

def Part2(data):
    points = parseData(data)

    shift = lambda n,k : ( (n-1+k)%9 )+1
    bigPoints = [flatten([[shift(n,i) for n in row] for i in range(5)]) for row in points]
    bigPoints = [list(map(lambda r: shift(r,i//len(bigPoints)),row)) for i,row in enumerate(bigPoints*5)]

    caveGraph = graph(bigPoints)
    caveGraph.shortestPath((0,0))

    end = max(caveGraph.nodeDict.keys(),key=lambda s:sum(s))
    return caveGraph.nodeDict[end].startRisk