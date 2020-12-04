inp = open("input.txt", "r")
rawPassports = []
for line in inp:
    rawPassports.append(line.strip())

passports = []
x = 0
for i in range(len(rawPassports)):
    if rawPassports[i] == '':
        data = ' '.join(rawPassports[x:i])
        passports.append(data)
        x = i+1

firstHalfCounter = 0
secondHalfCounter = 0
for line in passports:
    if "byr" in line and "iyr" in line and "eyr" in line and "hgt" in line\
            and "hcl" in line and "ecl" in line and "pid" in line:
                firstHalfCounter += 1
                dic = dict(data.split(':') for data in line.split(' '))
                if\
                    1920 <= int(dic['byr']) <= 2002 and\
                    2010 <= int(dic['iyr']) <= 2020 and\
                    2020 <= int(dic['eyr']) <= 2030 and\
                    dic['hcl'].startswith('#') and len(dic['hcl']) == 7 and\
                    dic['ecl'] in 'amb blu brn gry grn hzl oth' and\
                    len(dic['pid']) == 9:
                        if dic['hgt'].endswith('in'):
                            if 59 <= int(dic['hgt'][:-2]) <= 76:
                                secondHalfCounter += 1
                        elif dic['hgt'].endswith('cm'):
                            if 150 <= int(dic['hgt'][:-2]) <= 193:
                                secondHalfCounter += 1

print(firstHalfCounter)
print(secondHalfCounter)
