from collections import deque
from statistics import median

def parseData(data):
    return [d for d in data]

PAIR_DICT = {')':'(', ']':'[', '}':'{', '>':'<'}
def findIncorrect(line):
    pairStack = deque()
    for ch in line:
        if ch in PAIR_DICT.values():
            pairStack.append(ch)
        else:
            if pairStack.pop() != PAIR_DICT[ch]:
                return ch
    return ''

def fixMissing(line):
    pairStack = deque()
    for ch in line:
        if ch in PAIR_DICT.values():
            pairStack.append(ch)
        else:
            pairStack.pop()
    REVERSE_PAIR = {v:k for k,v in PAIR_DICT.items()}
    correction = [REVERSE_PAIR[ch] for ch in reversed(pairStack)]
    return "".join(correction)

SCORE_DICT = {')':1, ']':2, '}':3, '>':4}
def scoreFixed(correction):
    score = 0
    for ch in correction:
        score = 5*score + SCORE_DICT[ch]
    return score





def Part1(data):
    lines = parseData(data)
    POINT_DICT = {')':3, ']':57, '}':1197, '>':25137, '':0}
    errors = [POINT_DICT[findIncorrect(l)] for l in lines]
    return sum(errors)

def Part2(data):
    lines = parseData(data)
    valid = [l for l in lines if findIncorrect(l)=='']

    fixed = [fixMissing(l) for l in valid]
    scores = [scoreFixed(l) for l in fixed]
    return median(scores)