from Solution import Part1,Part2
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')

def formatTime(start,end):
    delta_us=(end - start)*1000000

    us=int(delta_us % 1000)
    ms=int((delta_us / 1000) % 1000)
    s =int((delta_us / 1000000) % 60)
    m =int((delta_us / 60000000) % 60)
    h =int(delta_us / 3600000000)

    # Goal: always show around 3 digits of accuracy
    if h > 0:
        timer_show=f"{h}h {m}m"
    elif m > 0:
        timer_show=f"{m}m {s}s"
    elif s >= 10:
        timer_show=f"{s}.{ms // 100} s"
    elif s > 0:
        timer_show=f"{s}.{ms:03} s"
    elif ms >= 100:
        timer_show=f"{ms} ms"
    elif ms > 0:
        timer_show=f"{ms}.{us // 100} ms"
    else:
        timer_show=f"{us} µs"

    return timer_show

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    data = [l.strip().split(' ') for l in lines]
    return [ [d[0],int(d[1])] for d in data]

# Execution stuff
lines = readInput()

tic = time.perf_counter()
P1 = Part1(lines)
toc = time.perf_counter()
print("Part 1:")
print("\t" + str(P1))
print("\t"+formatTime(tic,toc))
print()

tic = time.perf_counter()
P2 = Part2(lines)
toc = time.perf_counter()
print("Part 2:")
print("\t" + str(P2))
print("\t"+formatTime(tic,toc))
print()