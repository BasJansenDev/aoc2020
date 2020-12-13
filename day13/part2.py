
def alignmentCheck(depTime, nextBus):
    if((depTime+nextBus[1])%nextBus[0] ==0):
        return True
    else:
        return False

def main():
    buses = inputAsList()[1].split(',')
    busTuples = []
    for i in range(len(buses)):
        if(buses[i] != 'x'):
            busTuples.append((int(buses[i]),i))
    increments = int(buses[0])
    alignedBuses = 1
    depTime = int(buses[0])
    while alignedBuses != len(busTuples):
        depTime += increments
        if(alignmentCheck(depTime,busTuples[alignedBuses])):
            increments *= int(busTuples[alignedBuses][0])
            alignedBuses+=1
    return depTime

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 2: " + str(main()))