import copy

def checkAdjacent(seat,seats):
    cnt = 0
    for i in range(seat[0]-1,seat[0]+2):
        for j in range(seat[1]-1,seat[1]+2):
            if(j >= 0 and j < len(seats[0]) and i >= 0 and i < len(seats) and (i,j) != seat and seats[i][j] == '#'):
                cnt +=1
    return cnt

def checkEmpty(seat,seats):
    return seats[seat[0]][seat[1]] == 'L' and checkAdjacent(seat,seats) == 0


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
                    if(input[row][seat] == '#' and checkAdjacent((row,seat),cop) >= 4):
                        input[row][seat] = 'L'
    return sum([(*map(lambda x : x.count('#'),cop))])

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 1: " + str(main()))