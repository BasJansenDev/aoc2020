import re

def calculateMask(newMask):
    maskDict = {}
    for i in range(len(newMask)):
        if (newMask[i] == '1' or newMask[i] == '0'):
            maskDict[i] = int(newMask[i])
    return maskDict

def calculateValue(value, currMask):
    val = [int(digit) for digit in bin(value)[2:].zfill(36)]
    for bit in currMask:
        val[bit] = int(currMask[bit])
    out = 0
    for bit in val:
        out = (out << 1) | bit
    return out

def main():
    input = inputAsList()
    memory = {}
    maskDict = {}
    for i in input:
        i = i.split('=')
        if(i[0].strip(' ') == 'mask'):
            maskDict = calculateMask(i[1].strip(' '))
        else:
            address = int(re.search(r'\d+', i[0]).group())
            memory[address] = calculateValue(int(i[1].strip(' ')),maskDict)
    return sum(memory.values())

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 1: " + str(main()))