import re
def dictSearch(key, dic, str,count):
    if key == "nootherbag":
        return 0
    elif str in dic[key]:
        return 1
    else:
        for value in dic[key].split(','):
            count += dictSearch(value.rstrip('s'),dic,str,count)
        return count

def main():
    inp = inputAsList()
    ls = [i.split('contain') for i in inp]
    dic = {}
    for j in ls:
        dic[re.sub(r'[ .0-9]', '', j[0]).rstrip('s')] = re.sub(r'[ .0-9]', '', j[1])
    count = 0
    for key in dic.keys():
        if(dictSearch(key, dic,'shinygoldbag',0) > 0):
            count += 1
    return count

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 1: " + str(main()))