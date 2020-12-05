import re

def check(min,max,string):
    while(len(string) > 1):
        if (string.startswith('F') or string.startswith('L')):
            max = min + int((max-min)/2)
            string = string[1:]
        else:
            min = min + round((max - min) / 2)
            string = string[1:]
    if(string.startswith('F') or string.startswith('L')):
        return min
    else:
        return max

def main():
    inp = inputAsList()
    mx = 0
    for i in inp:
        mx = max(mx,(check(0,127,re.sub('[LR]','',i)) * 8 + check(0,7,re.sub('[FB]','',i))))
    return mx

def oneliner():
    return max([int("".join(str(a) for a in b), 2) for b in [[ord(z) % 7 % 2 for z in y] for y in inputAsList()]])

def inputAsList():
    f = open('input')
    return f.read().splitlines()

print("Part 1: " + str(main()))
print("Part 1: " + str(oneliner()))