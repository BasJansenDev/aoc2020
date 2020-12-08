def main():
    inp = inputAsList()
    pcList = []
    pc = 0
    acc = 0
    while pc < len(inputAsList()):
        if(pc not in pcList):
            pcList.append(pc)
        else:
            return acc
        i = inp[pc].split(' ')
        if(i[0] == 'acc'):
            acc += int(i[1])
            pc += 1
        elif(i[0] == 'jmp'):
            pc += int(i[1])
        else:
            pc += 1

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 1: " + str(main()))