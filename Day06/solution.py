# turn input into a list of lists of lists of characters
# [
#   [['a, 'b', 'c'], ['z']] # first group has 2 persons, who voted abc, and z
#   [['x']] # second group has a single person, who voted x
# ]
groups = [list()]
with open('input.txt', 'r') as f:
    for line in f:
        if line == "\n":
            groups.append(list())
        else:
            groups[-1].append([c for c in line.strip()])

# Part 1 - For each group, count the number of questions to which
# **anyone** answered "yes". What is the sum of those counts?
print("Part 1:", sum([len(set().union(*g)) for g in groups]))

# Part 2 - For each group, count the number of questions to which
# **everyone** answered "yes". What is the sum of those counts?
print("Part 2:", sum([len(set(g[0]).intersection(*g[1:])) for g in groups]))
