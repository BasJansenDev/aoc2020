def main():
    list = inputAsList()
    for i in list:
        for j in list:
            for k in list:
                if(i != j != k and i+j+k == 2020):
                    print(i*j*k)
                    return

def inputAsList():
    f = open('day1/input')
    return list(map(int, f.read().splitlines()))

main()