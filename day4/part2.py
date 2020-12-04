import re

def oneliner():
    return len(list(filter(lambda passport:
                           (passport[passport.index("hcl") + 1].startswith('#') and len(passport[passport.index("hcl") + 1]) == 7)
                           and
                           1920 <= int(passport[passport.index("byr") + 1]) <= 2002
                           and
                           2010 <= int(passport[passport.index("iyr") + 1]) <= 2020
                           and
                           2020 <= int(passport[passport.index("eyr") + 1]) <= 2030
                           and
                           (59 <= int(re.search(r'\d+', passport[passport.index("hgt") + 1]).group()) <= 76 if (
                                       'in' in passport[passport.index("hgt") + 1]) else
                            (150 <= int(re.search(r'\d+', passport[passport.index("hgt") + 1]).group()) <= 193 if (
                                        'cm' in passport[passport.index("hgt") + 1]) else False))
                           and
                           (passport[passport.index("ecl") + 1] in ['amb','blu','brn','gry','hzl','oth','grn'])
                           and
                           len(str(re.search(r'\d+', passport[passport.index("pid") + 1]).group())) == 9
                           , list(re.split("[ :\n]", passport) for passport in (list(filter(
            lambda passport: all(field in passport for field in ['hcl', 'byr', 'iyr', 'eyr', 'hgt', 'ecl', 'pid']),
            inputAsList())))))))

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
    return count

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


print("Part 2 : " + str(main()))
print("Part 2 : " + str(oneliner()))