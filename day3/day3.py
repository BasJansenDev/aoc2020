
def main(right,down):
    inp = inputAsList()
    count = 0
    pos = 0
    for i in range(0,len(inp), down):
        if(inp[i][pos] == '#'):
            count +=1
        pos = (pos + right) % len(inp[i])
    return count

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print('Part 1 : ' + str(main(3,1)))
print('Part 2 : ' + str(main(1,1) * main(3,1) * main(5,1) * main(7,1) * main(1,2)))