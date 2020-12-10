# Part 1
from functools import reduce
from operator import mul

input = sorted(map(int, open("input.txt").read().splitlines()))

# Part 1
#diff = list()
#for c in range(1, len(input)):
#    diff.append(input[c] - input[c-1])

#print(diff.count(3)+1, diff.count(1)+1, 'part1:', (diff.count(3)+1) * (diff.count(1)+1))

# Part 2
count = ''.join([str(max(1, c-input[i-1])) for i, c in enumerate(input)]).split('3')
permutations = [max(1, 2**(len(c)-1)) if len(c)<4 else (2**(len(c)-1))-1 for c in count]
print("part2:", reduce(mul, permutations))
