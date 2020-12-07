import re
dic = {}
def dictSearch(key, str,bool):
    if key == "nootherbag":
        return False
    elif str in dic[key]:
        return True
    else:
        for value in dic[key].split(','):
            bool |= dictSearch(value.rstrip('s'),str,bool)
        return bool

def main():
    for j in [i.split('contain') for i in inputAsList()]:
        dic[re.sub(r'[ .0-9]', '', j[0]).rstrip('s')] = re.sub(r'[ .0-9]', '', j[1])
    count = 0
    for key in dic.keys():
        if(dictSearch(key, 'shinygoldbag',False)):
            count += 1
    return count

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 1: " + str(main()))