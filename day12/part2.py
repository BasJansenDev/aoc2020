def main():
    NSboat = 0
    EWboat = 0
    NSwp = 1
    EWwp = 10
    inp = inputAsList()
    for i in inp:
        motion = i[0]
        num = int(i[1:])
        if(motion == 'F'):
            EWboat += EWwp*num
            NSboat += NSwp*num
        elif(motion == 'L'):
            for i in range(int(num/90)):
                EWwp,NSwp = -NSwp,EWwp
        elif(motion == 'R'):
            for i in range(int(num/90)):
                EWwp,NSwp = NSwp,-EWwp
        elif(motion == 'N'):
            NSwp += num
        elif(motion == 'S'):
            NSwp -= num
        elif(motion == 'E'):
            EWwp += num
        elif(motion == 'W'):
            EWwp -= num
    return abs(EWboat) + abs(NSboat)

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 2: " + str(main()))