dirs = ['E','S','W','N']

def main():
    dir = 0
    NS = 0
    EW = 0
    inp = inputAsList()
    for i in inp:
        motion = i[0]
        num = int(i[1:])
        if(motion == 'F'):
            motion = dirs[dir%4]
        if(motion == 'L'):
            dir -=1*(int(num/90))
        elif(motion == 'R'):
            dir += 1*(int(num/90))
        elif(motion == 'N'):
            NS += num
        elif(motion == 'S'):
            NS -= num
        elif(motion == 'E'):
            EW += num
        elif(motion == 'W'):
            EW -= num
    return abs(EW) + abs(NS)

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 1: " + str(main()))