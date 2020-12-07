import re
dic = {}
def dictSearch(key):
    lst = []
    for value in dic[key]:
        if(value[1]) == "nootherbags":
            lst.append(0)
        else:
            val = dictSearch(value[1].rstrip('s'))
            lst.append(int(value[0]) + (int(value[0]) * val))
    return sum(lst)

def main():
    for j in [i.split('contain') for i in inputAsList()]:
        dic[re.sub(r'[ .0-9]', '', j[0]).rstrip('s')] = [[re.sub(r'[ .a-z]', '', k),re.sub(r'[ .0-9]', '', k)] for k in j[1].split(',')]
    return dictSearch('shinygoldbag')

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 2: " + str(main()))