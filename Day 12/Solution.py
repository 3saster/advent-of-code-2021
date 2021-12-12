from collections import defaultdict
from copy import deepcopy

def parseData(data):
    return [d.split('-') for d in data]
    
def cavePaths(caveGraph,visits,start='start',smallVisits=1):
    if(start == 'end'):
        return [['end']]
    if len(caveGraph[start]) == 0:
        return [[start]]

    paths = []
    for c in caveGraph[start]:
        if c != c.lower() or (c == c.lower() and max(visits.values()) < smallVisits or visits[c] < 1):
            newVisits = deepcopy(visits)
            # if cave is small
            if c == c.lower(): 
                newVisits[c] += 1
            paths = paths + [[start]+p for p in cavePaths(caveGraph,newVisits,c,smallVisits)]
    return paths

        
    



def Part1(data):
    caves = parseData(data)
    caveGraph = defaultdict(lambda : set())
    for c in caves:
        if(c[0] != 'end' and c[1] != 'start'): caveGraph[ c[0] ].add( c[1] )
        if(c[1] != 'end' and c[0] != 'start'): caveGraph[ c[1] ].add( c[0] )
    caveGraph = dict(caveGraph)

    visits = {k:0 for k in caveGraph.keys()}
    visits['end'] = 0

    validPaths = [p for p in cavePaths(caveGraph,visits,smallVisits=1) if p[-1]=='end']
    return len(validPaths)

def Part2(data):
    caves = parseData(data)
    caveGraph = defaultdict(lambda : set())
    for c in caves:
        if(c[0] != 'end' and c[1] != 'start'): caveGraph[ c[0] ].add( c[1] )
        if(c[1] != 'end' and c[0] != 'start'): caveGraph[ c[1] ].add( c[0] )
    caveGraph = dict(caveGraph)

    visits = {k:0 for k in caveGraph.keys()}
    visits['end'] = 0
    
    validPaths = [p for p in cavePaths(caveGraph,visits,smallVisits=2) if p[-1]=='end']
    return len(validPaths)