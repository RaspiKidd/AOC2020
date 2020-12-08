input = open("input.txt", "r")
data = []

for line in input:
    data += [line.strip().split()]

# Part 1
#visited = [False for i in range(len(data))]
#accumulator = 0
#index = 0
#while not visited[index]:
#    visited[index] = True
#    if data[index][0] == 'acc':
#        accumulator += int(data[index][1])
#        index+=1
#    elif data[index][0] == 'jmp':
#        index += int(data[index][1])
#    elif data[index][0] == 'nop':
#        index += 1
#print(accumulator)

# Part 2
visited = [False for i in range(len(data))]

def traverse(accumulator, index, visited, changed):
    if index == len(data):
        print(accumulator)
        raise SystemExit
    if visited[index]:
        return 0
    visited[index] = True
    if data[index][0] == 'acc':
        return traverse(accumulator + int(data[index][1]), index+1, visited[:], changed)
    elif data[index][0] == 'jmp':
        if changed or not traverse(accumulator, index+1, visited[:], True):
            return traverse(accumulator, index + int(data[index][1]), visited[:], changed)
    elif data[index][0] == 'nop':
        if changed or not traverse(accumulator, index+ int(data[index][1]), visited[:], True):
            return traverse(accumulator, index +1 , visited[:], changed)

traverse(0,0,visited[:], False)
