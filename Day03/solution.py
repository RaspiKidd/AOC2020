grid = open("input.txt").read().split()
width = len(grid[0])

# part 1
def angle(h, w):
    return sum(row[i *w % width] == "#" for i, row in enumerate(grid[::h]))

# Part 2
part2 = 1
for trees in [angle(h, w) for h, w in [(1, 3), (1, 5), (1, 7), (1, 1), (2, 1)]]:
    part2 *= trees

print(angle(1, 3), part2)
