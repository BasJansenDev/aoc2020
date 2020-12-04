import re
def main():
    input = inputAsList()
    count = 0
    for passport in input:
        if('hcl' in passport and 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'ecl' in passport and 'pid' in passport):
           count +=1
    print(count)



def inputAsList():
    f = open('input')
    return f.read().split('\n\n')


main()