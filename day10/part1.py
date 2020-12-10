def main():
    input = inputAsIntList()
    input += [0,max(input)+3]
    input.sort()
    diff = [int(input[i+1])-int(input[i]) for i in range(len(input)-1)]
    return diff.count(3)*diff.count(1)


def inputAsIntList():
    f = open('input')
    lst = f.read().splitlines()
    for i in range(0,len(lst)):
        lst[i] = int(lst[i])
    return lst

print('Part 1: ' + str(main()))