
def main(n):
    input = [0,13,1,8,6,15]
    dict = {}
    for i in range(len(input)):
        dict[input[i]] = i
    nextValue = 0
    for i in range(len(input),n-1):
        currValue = nextValue
        if nextValue in dict:
            nextValue = i - dict.get(nextValue)
        else:
            nextValue = 0
        dict[currValue] = i
    return nextValue

print("Part 1: " + str(main(2020)))
print("Part 2: " + str(main(30000000)))