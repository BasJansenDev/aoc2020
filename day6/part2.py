def main():
    return sum([len(set.intersection(*map(set,i.split('\n')))) for i in inputAsList()])


def inputAsList():
    f = open('input')
    return f.read().split('\n\n')


print("Part 1: " + str(main()))