def main():
    lengths = []
    for i in inputAsList():
        i = i.replace('\n','')
        lengths.append(len(set(i)))
    return sum(lengths)

def inputAsList():
    f = open('input')
    return f.read().split('\n\n')


print("Part 1: " + str(main()))