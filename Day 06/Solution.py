from collections import Counter, defaultdict

def parseData(data):
    fish = [int(d) for d in data[0].split(',')]
    return defaultdict(lambda: 0, Counter(fish))
    
def nextDay(fish):
    nextFish=defaultdict(lambda: 0,{k-1:v for k,v in fish.items() if k>=0})
    nextFish[8] += nextFish[-1]
    nextFish[6] += nextFish[-1]
    nextFish[-1] = 0
    return nextFish




def Part1(data):
    fish = parseData(data)
    for _ in range(80):
        fish = nextDay(fish)

    return sum(fish.values())

def Part2(data):
    fish = parseData(data)
    for _ in range(256):
        fish = nextDay(fish)

    return sum(fish.values())