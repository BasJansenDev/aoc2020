def main():
    input = inputAsList()
    depTime = int(input[0])
    buses = input[1].split(',')
    minTime = float("inf")
    minBus = float("inf")
    for bus in buses:
        if(bus == 'x'):
            continue
        else:
            minTmp = min(minTime,int(bus)-(depTime%int(bus)))
            if(minTmp != minTime):
                minTime = minTmp
                minBus = int(bus)

    return minTime*minBus

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 1: " + str(main()))