import copy
from functools import reduce

def structureData(input):
    checkDict = {}
    for i in input[0].splitlines():
        check = i.split(':')[1].strip(' ').split(' or ')
        check = [check[0].split('-'), check[1].split('-')]
        checkDict[i.split(':')[0]] = check
    ownTicket = input[1].split(':')[1].strip('\n').split(',')
    ticketList = input[2].split(':')[1].strip('\n').splitlines()
    for i in range(len(ticketList)):
        ticketList[i] = ticketList[i].split(',')
    return checkDict,ownTicket,ticketList

def getOptionsPerTicket(ticketList, checkDict):
    optionList = [set(checkDict.keys())] * len(ticketList[0])
    for tickets in ticketList:
        for ticket in range(len(tickets)):
            failedChecks = set()
            for check in checkDict:
                ranges = checkDict[check]
                if (not (int(ranges[0][0]) <= int(tickets[ticket]) <= int(ranges[0][1]) or int(ranges[1][0]) <= int(
                        tickets[ticket]) <= int(ranges[1][1]))):
                    failedChecks.add(check)
            if (len(failedChecks) != len(tickets) and len(failedChecks) != 0):
                newEntry = optionList[ticket] - failedChecks
                optionList[ticket] = newEntry
    return optionList

def getDisjointLists(optionList):
    last = []
    while last != optionList:
        last = copy.deepcopy(optionList)
        for i in range(len(optionList)):
            set2 = set()
            for j in range(len(optionList)):
                if(i != j):
                    set2.update(optionList[j])
            if(len(optionList[i] - set2) > 0):
                optionList[i] = optionList[i] - set2
    return optionList

def getResultValues(ownTicket,optionList):
    result = []
    for i in range(len(optionList)):
        if(optionList[i].pop().startswith('departure')):
            result.append(int(ownTicket[i]))
    return reduce(lambda x,y: x*y,result)

def main():
    input = inputAsList()
    checkDict,ownTicket,ticketList = structureData(input)
    optionList = getOptionsPerTicket(ticketList, checkDict)
    getDisjointLists(optionList)
    return getResultValues(ownTicket,optionList)

def inputAsList():
    f = open('input')
    return f.read().split('\n\n')

print("Part 2: " + str(main()))