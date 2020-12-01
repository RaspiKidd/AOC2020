expenses = list(map(int, open("input.txt", "r").read().split()))

# Part 1
#for num1 in expenses:
#    for num2 in expenses:
#        if num1+num2==2020:
#            print(num1*num2)

# Part 2
for num1 in expenses:
    for num2 in expenses:
        for num3 in expenses:
            if num1+num2+num3==2020:
                print(num1*num2*num3)
