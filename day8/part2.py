def getLoopList():
    inp = inputAsList()
    pcList = []
    loopList = []
    pc = 0
    acc = 0
    while pc < len(inputAsList()):
        if (pc not in pcList):
            pcList.append(pc)
        else:
            if pc not in loopList:
                loopList.append(pc)
            else:
                return loopList
        i = inp[pc].split(' ')
        if (i[0] == 'acc'):
            acc += int(i[1])
            pc += 1
        elif (i[0] == 'jmp'):
            pc += int(i[1])
        else:
            pc += 1

def main():
    inp = inputAsList()
    for l in getLoopList():
        print(l)
        pc = 0
        acc = 0
        pcList = []
        while pc < len(inputAsList()):
            i = inp[pc].split(' ')
            if(pc == l):
                if i[0] == 'jmp':
                    i[0] = 'nop'
                elif i[0] == 'nop':
                    i[0] = 'jmp'
            if(pc not in pcList):
                pcList.append(pc)
            else:
                break
            if(i[0] == 'acc'):
                acc += int(i[1])
                pc += 1
            elif(i[0] == 'jmp'):
                pc += int(i[1])
            else:
                pc += 1
        if(pc >= len(inputAsList())):
            return acc

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 2: " + str(main()))