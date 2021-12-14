from collections import Counter,defaultdict

def parseData(data):
    poly = data[0]
    rules = [d.split(' -> ') for d in data[2:]]
    return poly,rules

class polymer:
    def __init__(self,poly,rules):
        # dictionary of how many of each pair appear in the polymer
        self.poly = defaultdict(lambda:0)
        for i in range(len(poly)-1):
            self.poly[poly[i:i+2]] += 1
        # dictionary with the two pairs certain pairs produce
        self.rules = {r[0]:[ r[0][0]+r[1],r[1]+r[0][1] ] for r in rules}
        # dictionary of how many of each single letter appear in the polymer
        self.counts = defaultdict(lambda:0,Counter(poly))

    def advance(self):
        matched = {k:v for k,v in self.poly.items() if k in self.rules.keys()}
        for pair,num in matched.items():
            # remove all matched pairs
            self.poly[pair] -= num 
            # add newly generated pairs
            self.poly[self.rules[pair][0]] += num
            self.poly[self.rules[pair][1]] += num
            # add newly generated letters
            self.counts[self.rules[pair][0][1]] += num

        
    


def Part1(data):
    poly,rules = parseData(data)
    polymerTemplate = polymer(poly,rules)
    for _ in range(10):
        polymerTemplate.advance()
    count = polymerTemplate.counts.values()
    return( max(count)-min(count) )

def Part2(data):
    poly,rules = parseData(data)
    polymerTemplate = polymer(poly,rules)
    for _ in range(40):
        polymerTemplate.advance()
    count = polymerTemplate.counts.values()
    return( max(count)-min(count) )