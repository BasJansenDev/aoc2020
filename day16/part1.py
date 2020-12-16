
def ruleChecker(ticket,checkList):
    for check in checkList:
        if(int(check[0][0]) <= ticket <= int(check[0][1]) or int(check[1][0]) <= ticket <= int(check[1][1])):
            return True
    return False


def main():
    input = inputAsList()
    checkList = []
    for i in input[0].splitlines():
        check = i.split(':')[1].strip(' ').split(' or ')
        check = [check[0].split('-'),check[1].split('-')]
        checkList.append(check)
    invalidTicketList = []
    for tickets in input[2].split(':')[1].strip('\n').splitlines():
        for ticket in tickets.split(','):
            if(not ruleChecker(int(ticket),checkList)):
                invalidTicketList.append(int(ticket))
    return sum(invalidTicketList)


def inputAsList():
    f = open('input')
    return f.read().split('\n\n')

print("Part 1: " + str(main()))