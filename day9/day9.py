import itertools

def main():
    inp = inputAsList()
    lst = inp[:25]
    lst = list(map(int,lst))
    for i in range(25,len(inp)):
        if(len(list(filter(lambda x : sum(x) == int(inp[i]),itertools.combinations(lst,2))))> 0):
            lst.pop(0)
            lst.append(int(inp[i]))
        else:
            return i,int(inp[i])

def main2():
    inp = inputAsList()
    res = main()
    lst = inp[:res[0]]
    lst = list(map(int,lst))
    for i in range(0,res[0]):
        currLst = [int(inp[i])]
        for j in range(i+1,res[0]):
            currLst.append(int(inp[j]))
            if(sum(currLst) == res[1]):
                return min(currLst),max(currLst)
            if(sum(currLst) > res[1]):
                break





def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 1: " + str(main()[1]))
print("Part 2: " + str(sum(main2())))