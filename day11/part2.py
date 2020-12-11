import copy

def checkAdjacent(seat,seats):
    cnt = 0
    for i in range(seat[0]-1,seat[0]+2):
        for j in range(seat[1]-1,seat[1]+2):
            if(0 <= j < len(seats[0]) and 0 <= i < len(seats) and (i,j) != seat and seats[i][j] == '#'):
                cnt +=1
    return cnt

deltas = [(-1,1),(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(1,-1),(1,1)]
def checkVisible(seat,seats):
    list = []
    for delta in deltas:
        x = seat[0]
        y = seat[1]
        while 0 <= x < len(seats)-1 and 0 <= y < len(seats[0])-1:
            x += delta[0]
            y += delta[1]
            if (seats[x][y] == 'L'):
                break
            elif (seats[x][y] == '#'):
                list.append((x,y))
                break
    return len(list)

def checkEmpty(seat,seats):
    return seats[seat[0]][seat[1]] == 'L' and checkVisible(seat,seats) == 0

def main():
    cop = []
    input = inputAsList()
    for i in range(len(input)):
        input[i] = [seat for seat in input[i]]
    while(cop != input):
        cop = copy.deepcopy(input)
        for row in range(len(input)):
            for seat in range(len(input[row])):
                if(input[row][seat] != '.'):
                    if(checkEmpty((row,seat),cop)):
                        input[row][seat] = '#'
                    if(input[row][seat] == '#' and checkVisible((row,seat),cop) >= 5):
                        input[row][seat] = 'L'
        for i in input:
            print(i)
        print()
    return sum([(*map(lambda x : x.count('#'),cop))])

def inputAsList():
    f = open('testInput')
    return f.read().splitlines()

print("Part 2: " + str(main()))