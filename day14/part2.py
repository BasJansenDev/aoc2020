import re
import itertools

def calculateMask(newMask):
    maskDict = {}
    for i in range(len(newMask)):
        if (newMask[i] == '1' or newMask[i] == 'X'):
            maskDict[i] = newMask[i]
    return maskDict

def calculateAddresses(value, combinations, maskDict):
    val = [int(digit) for digit in bin(value)[2:].zfill(36)]
    addresses = []
    for comb in combinations:
        xcount = 0
        out = 0
        for bit in maskDict:
            if(maskDict[bit] == 'X'):
                val[bit] = comb[xcount]
                xcount += 1
            else:
                val[bit] = int(maskDict[bit])
        for bit in val:
            out = (out << 1) | bit
        addresses.append(out)
    return addresses

def main():
    input = inputAsList()
    memory = {}
    maskDict = []
    combinations = []
    for i in input:
        i = i.split('=')
        if(i[0].strip(' ') == 'mask'):
            maskDict = calculateMask(i[1].strip(' '))
            combinations = list(itertools.product([0,1],repeat=i[1].strip(' ').count('X')))
        else:
            address = int(re.search(r'\d+', i[0]).group())
            addresses = calculateAddresses(address, combinations, maskDict)
            for addr in addresses:
                memory[addr] = int(i[1].strip(' '))
    return sum(memory.values())

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 2: " + str(main()))