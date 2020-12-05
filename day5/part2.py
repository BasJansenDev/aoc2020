import re


def check(min, max, string):
    while (len(string) > 1):
        if (string.startswith('F') or string.startswith('L')):
            max = min + int((max - min) / 2)
            string = string[1:]
        else:
            min = min + round((max - min) / 2)
            string = string[1:]
    if (string.startswith('F') or string.startswith('L')):
        return min
    else:
        return max


def main():
    inp = inputAsList()
    lst = []
    for i in inp:
        lst += [(check(0, 127, re.sub('[LR]', '', i)) * 8 + check(0, 7, re.sub('[FB]', '', i)))]
    return list(set(lst) ^ set(list(range(32, max(lst)))))[0]


def inputAsList():
    f = open('input')
    return f.read().splitlines()


print(main())
