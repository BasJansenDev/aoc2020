def main():
    input = inputAsList()
    count = 0
    for passport in input:
        if('hcl' in passport and 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'ecl' in passport and 'pid' in passport):
           count +=1
    return count

def oneliner():
     return len(list(filter(lambda passport : all(field in passport for field in ['hcl','byr','iyr','eyr','hgt','ecl','pid']),inputAsList())))

def inputAsList():
    f = open('input')
    return f.read().split('\n\n')


print("Part 1: " + str(main()))
print("Part 1: " + str(oneliner()))