
def main(right,down):
    inp = inputAsList()
    count = 0
    pos = 0
    for i in range(0,len(inp), down):
        if(inp[i][pos] == '#'):
            count +=1
        pos = (pos + right) % len(inp[i])
    return count

def oneliner(data,right,down):
    return len(list(filter(lambda v : data[0::down][v][(v*right) % len(data[0])] == "#",[i for i in range(0,round(len(data)/down))])))

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print('Part 1 : ' + str(main(3,2)))
print('Part 1 : ' + str(oneliner(inputAsList(),3,2)))
print('Part 2 : ' + str(main(1,1) * main(3,1) * main(5,1) * main(7,1) * main(1,2)))
print('Part 2 : ' + str(oneliner(inputAsList(),1,1) * oneliner(inputAsList(),3,1) * oneliner(inputAsList(),5,1) * oneliner(inputAsList(),7,1) * oneliner(inputAsList(),1,2)))