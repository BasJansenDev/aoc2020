def main():
    return sum([len(set(i.replace('\n',''))) for i in inputAsList()])

def inputAsList():
    f = open('input')
    return f.read().split('\n\n')


print("Part 1: " + str(main()))