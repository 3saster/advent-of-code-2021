from collections import defaultdict
from copy import deepcopy
import functools

def parseData(data):
    return [d.split('-') for d in data]
    

class cavePath:
    def __init__(self, caveGraph):
        self.caveGraph = caveGraph

    @functools.lru_cache(maxsize=None)
    def cavePaths(self,visitSet,start='start',smallVisits=1):
        if(start == 'end'):
            return [['end']]

        visits = {k:v for k,v in visitSet}

        paths = []
        for c in self.caveGraph[start]:
            if c != c.lower() or (c == c.lower() and max(visits.values()) < smallVisits or visits[c] < 1):
                newVisits = deepcopy(visits)
                # if cave is small
                if c == c.lower(): 
                    newVisits[c] += 1
                paths = paths + [[start]+p for p in self.cavePaths(frozenset(newVisits.items()),c,smallVisits)]
        return paths

        
    


def Part1(data):
    global caveGraph
    global visits

    caves = parseData(data)
    caveGraph = defaultdict(lambda : set())
    for c in caves:
        if(c[0] != 'end' and c[1] != 'start'): caveGraph[ c[0] ].add( c[1] )
        if(c[1] != 'end' and c[0] != 'start'): caveGraph[ c[1] ].add( c[0] )
    caveGraph = dict(caveGraph)

    visits = {k:0 for k in caveGraph.keys()}
    visits['end'] = 0

    caveClass = cavePath(caveGraph)
    return len(caveClass.cavePaths(frozenset(visits.items()),smallVisits=1))

def Part2(data):
    caveClass = cavePath(caveGraph)
    return len(caveClass.cavePaths(frozenset(visits.items()),smallVisits=2))