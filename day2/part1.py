import re
def main():
    inp = inputAsList()
    count = 0
    for line in inp:
        sp = re.split(' |-|:',line)
        if(sp[4].count(sp[2]) in range(int(sp[0]),int(sp[1])+1)):
            count += 1

    print(count)

def inputAsList():
    f = open('input')
    return f.read().splitlines()

main()