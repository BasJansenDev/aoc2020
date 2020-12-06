def part1():
    return sum([len(set(i.replace('\n',''))) for i in inputAsList()])
def part2():
    return sum([len(set.intersection(*map(set,i.split('\n')))) for i in inputAsList()])

def inputAsList():
    f = open('input')
    return f.read().split('\n\n')

print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))