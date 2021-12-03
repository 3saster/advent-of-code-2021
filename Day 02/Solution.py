def Part1(data):
    [x,y] = [0,0]
    for [com,value] in data:
        if  (com == 'forward'): 
            x += value
        elif(com == 'up'):      
            y -= value
        elif(com == 'down'):    
            y += value
    return x*y

def Part2(data):
    [x,y] = [0,0]
    aim = 0
    for [com,value] in data:
        if  (com == 'forward'): 
            x += value
            y += aim*value
        elif(com == 'up'):      
            aim -= value
        elif(com == 'down'):    
            aim += value
    return x*y