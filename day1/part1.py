def main():
    list = inputAsList()
    for i in list:
        for j in list:
            if(i != j and i+j == 2020):
                print(i*j)
                return

def inputAsList():
    f = open('day1/input')
    return list(map(int, f.read().splitlines()))

main()