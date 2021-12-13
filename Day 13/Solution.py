import re

def parseData(data):
    coord =  set([tuple(int(n) for n in d.split(',')) for d in data if ',' in d])
    folds = []
    for f in [d for d in data if '=' in d]:
        num = int(f.split('=')[-1])
        var = f.split('=')[0].split(' ')[-1]
        folds.append([var,num])
    return coord,folds

class foldClass:
    def __init__(self,grid):
        self.grid = grid

    def foldAlong(self,axis,num):
        newGrid = set()
        if axis=='x':
            for dot in self.grid:
                if dot[0] > num:
                    newGrid.add((2*num-dot[0],dot[1]))
                else:
                    newGrid.add(dot)
            self.grid = newGrid
        elif axis=='y':
            for dot in self.grid:
                if dot[1] > num:
                    newGrid.add((dot[0],2*num-dot[1]))
                else:
                    newGrid.add(dot)
            self.grid = newGrid

    def printGrid(self):
        outStr = ''
        for y in range( max([p[1] for p in self.grid])+1 ):
            for x in range( max([p[0] for p in self.grid])+1 ):
                outStr += '██' if (x,y) in self.grid else '  '
            outStr += '\n\t'
        return outStr

        
    


def Part1(data):
    coord,folds = parseData(data)
    paper = foldClass(coord)
    paper.foldAlong(*folds[0])
    
    return(len(paper.grid))

def Part2(data):
    coord,folds = parseData(data)
    paper = foldClass(coord)
    for f in folds:
        paper.foldAlong(*f)
    
    return paper.printGrid()