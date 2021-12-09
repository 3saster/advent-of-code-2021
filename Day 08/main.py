from Solution import Part1,Part2

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    return [l.strip() for l in lines]

# Execution stuff
lines = readInput()

P1 = Part1(lines)
print("Part 1:")
print("\t" + str(P1))
print()

P2 = Part2(lines)
print("Part 2:")
print("\t" + str(P2))
print()