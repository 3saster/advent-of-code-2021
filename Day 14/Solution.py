import re
from collections import Counter

def parseData(data):
    poly = data[0]
    rules = [d.split(' -> ') for d in data[2:]]
    return poly,rules

class polymer:
    def __init__(self,poly,rules):
        self.poly = poly
        self.rules = rules

    def advance(self):
        for r in self.rules:
            while r[0] in self.poly:
                self.poly = self.poly.replace(r[0],r[0][0]+r[1].lower()+r[0][1])
        self.poly = self.poly.upper()

        
    


def Part1(data):
    poly,rules = parseData(data)
    polymerTemplate = polymer(poly,rules)
    for _ in range(10):
        polymerTemplate.advance()
    count = Counter(polymerTemplate.poly).most_common()
    return( count[0][1] - count[-1][1] )

def Part2(data):
    poly,rules = parseData(data)
    polymerTemplate = polymer(poly,rules)
    for _ in range(40):
        polymerTemplate.advance()
    count = Counter(polymerTemplate.poly).most_common()
    return( count[0][1] - count[-1][1] )