from collections import Counter

def parseData(data):
    return [[num.split(' ') for num in d.split(' | ')] for d in data]

def decodeDisplay(input):
    dig = input[0]
    out = input[1]
    
    numbers = {k:'' for k in range(0,10)}
    for num,segs in zip([1,4,7,8],[2,4,3,7]):
        numbers[num] = [d for d in dig if len(d)==segs][0]

    [_235,_069] =  [[d for d in dig if len(d)==l] for l in [5,6]]

    # (3) contains 1 but 2 and 5 do not
    for n in _235:
        if set(numbers[1]).issubset(n):
            numbers[3] = n
            _235.remove(n)
            break
    # (9) contains 3 but 0 and 6 do not
    for n in _069:
        if set(numbers[3]).issubset(n):
            numbers[9] = n
            _069.remove(n)
            break
    # (0) contains 1 but 6 does not
    for n in _069:
        if set(numbers[1]).issubset(n):
            numbers[0] = n
            _069.remove(n)
            break
    # (6) is leftover in _069
    numbers[6] = _069[0]
    # 6 contains (5) but not 2
    for n in _235:
        if set(n).issubset(numbers[6]):
            numbers[5] = n
            _235.remove(n)
            break
    # (2) is leftover in _235
    numbers[2] = _235[0]

    # reverse the dict
    mapping = {"".join(sorted(v)):k for k,v in numbers.items()}
    # map segments to number
    mappedOut = [mapping["".join(sorted(s))] for s in out]
    return int("".join([str(i) for i in mappedOut]))





def Part1(data):
    display = parseData(data)
    output = [d[1] for d in display]
    outLength = [len(str) for out in output for str in out]
    countOut = Counter(outLength)

    # segments for 1,4,7,9, respectively
    return countOut[2]+countOut[4]+countOut[3]+countOut[7]

def Part2(data):
    display = parseData(data)
    out = [decodeDisplay(d) for d in display]

    return sum(out)