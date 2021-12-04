def parseData(data):
    numbers = [int(d) for d in data[0].split(',')]
    
    boards = [[]]
    b = 0
    for i in  range(2,len(data)):
        if data[i] == '':
            b += 1
            boards.append([])
        else:
            boards[b].append([int(d) for d in data[i].split(' ') if d!=''])

    return numbers,boards

def isWin(matches):
    winners = []
    for i,board in enumerate(matches):
        if max([sum(row) for row in board]) == 5 or max([sum(row) for row in list(zip(*board))]) == 5:
            winners.append(i)
    return winners
    





def Part1(data):
    numbers,boards = parseData(data)

    matches = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
    n = -1
    while len(winner:=isWin(matches)) == 0:
        n += 1
        for b in range(len(boards)):
            for i in range(5): 
                for j in range(5):
                    if boards[b][i][j] == numbers[n]: matches[b][i][j] = 1

    winBoard = boards[winner[0]]
    unmarkedSum = sum([winBoard[i][j] for i in range(5) for j in range(5) if matches[winner[0]][i][j] == 0])
    return numbers[n] * unmarkedSum

def Part2(data):
    numbers,boards = parseData(data)
    
    matches = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
    n = -1
    wonBoards = []
    while len(winners:=isWin(matches)) < len(boards):
        [wonBoards.append((b,n)) for b in winners if b not in [w[0] for w in wonBoards]]
        n += 1
        for b in range(len(boards)):
            for i in range(5): 
                for j in range(5):
                    if boards[b][i][j] == numbers[n]: matches[b][i][j] = 1
    [wonBoards.append((b,n)) for b in winners if b not in [w[0] for w in wonBoards]]

    lastBoard = boards[wonBoards[-1][0]]
    unmarkedSum = sum([lastBoard[i][j] for i in range(5) for j in range(5) if matches[wonBoards[-1][0]][i][j] == 0])
    return numbers[wonBoards[-1][1]] * unmarkedSum