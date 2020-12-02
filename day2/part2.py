import re
def main():
    inp = inputAsList()
    count = 0
    for line in inp:
        sp = re.split(' |-|:',line)
        if(len(sp[4]) >= int(sp[1]) and ((sp[2] == sp[4][int(sp[0])-1]) ^ (sp[2] == sp[4][int(sp[1])-1]))):
            count += 1

    print(count)

def inputAsList():
    f = open('input')
    return f.read().splitlines()

main()