import re

def main():
    input = inputAsList()
    count = 0
    for passport in input:
        if('hcl' in passport and 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'ecl' in passport and 'pid' in passport):
            passport = re.split("[ :\n]",passport)
            if(
            hclCheck(passport[passport.index("hcl")+1])
                and
            byrCheck(passport[passport.index("byr")+1])
                and
            iyrCheck(passport[passport.index("iyr")+1])
                and
            eyrCheck(passport[passport.index("eyr")+1])
                and
            hgtCheck(passport[passport.index("hgt")+1])
                and
            eclCheck(passport[passport.index("ecl")+1])
                and
            pidCheck(passport[passport.index("pid")+1])
            ):
                count +=1
    print(count)

def hclCheck(param):
    return param.startswith('#') and len(param.strip('#')) == 6


def byrCheck(param):
    return 1920 <= int(param) <= 2002


def iyrCheck(param):
    return 2010 <= int(param) <= 2020


def eyrCheck(param):
    return 2020 <= int(param) <= 2030


def hgtCheck(param):
    num = int(re.search(r'\d+', param).group())
    if('in' in param):
        return 59 <= num <= 76
    elif('cm' in param):
        return 150 <= num <= 193
    else:
        return False


def eclCheck(param):
    return (('amb' in param) ^ ('blu' in param) ^ ('brn' in param) ^ ('gry' in param) ^ ('hzl' in param) ^ ('oth' in param) ^ ('grn' in param))


def pidCheck(param):
    return len(str(re.search(r'\d+', param).group())) == 9


def inputAsList():
    f = open('input')
    return f.read().split('\n\n')


main()