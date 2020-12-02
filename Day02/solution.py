with open("input.txt","r") as file:
    data = [i.rstrip().split() for i in file.readlines()]

def check(row):
    _min, _max = row[0].split("-")
    letter = row[1][0]
    password = row[2]

    return int(_max) >= len([i for i in password if i == letter]) >= int(_min)

def check2(row):
    paswrd = row[2]
    l1, l2 = paswrd[int(row[0].split("-")[0]) - 1], paswrd[int(row[0].split("-")[1]) -1]
    letter = row[1][0]

    return l1 != l2 and letter in (l1, l2)

# Part 1 output
#print(len([1 for i in data if check(i) is True]))

# Part 2 output
print (len([1 for i in data if check2(i) is True]))
