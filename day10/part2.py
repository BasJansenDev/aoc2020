import time

tribonacci = [1,1,2,4,7,13]

def getCumulativeCombinations(lists):
    # Due to the lists of differences always consisting of ones, the combinations follow the tribonacci pattern
    # [n] = 1
    # [n,n+1] = 2
    # [n,n+1,n+2] = 4
    # [n,...,n+3] = 7
    # [n,...,n+4] = 13
    cnt = 1
    for numbers in lists:
        cnt *= tribonacci[len(numbers)]
    return cnt

def main():
    input = inputAsIntList()
    input += [0,max(input)+3]
    input.sort()
    diff = [int(input[i+1])-int(input[i]) for i in range(len(input)-1)]
    lists = []
    currlst = []
    for i in range(0,len(diff)):
        if(diff[i] < 3):
            currlst.append(diff[i])
        else:
            if(len(currlst) > 0):
                lists.append(currlst)
                currlst = []
    res = getCumulativeCombinations(lists)
    return res


def inputAsIntList():
    f = open('input')
    lst = f.read().splitlines()
    for i in range(0,len(lst)):
        lst[i] = int(lst[i])
    return lst

print('Part 2: ' + str(main()))