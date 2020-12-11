r = open('input.txt','r').read()
input = r.splitlines()

#Part 1
def occupied(state,row,col):
    if 0 <= row < len(state) and 0 <= col < len(state[row]):
        return state[row][col]
    return 'X'

def update(state):
    next = []
    delta = False
    counter = 0
    for row in range(len(state)):
        strip = ''
        for col in range(len(state[row])):
            adj = 0
            for x in [1,0,-1]:
                for y in [1,0,-1]:
                    if not x==y==0 and occupied(state,row+x,col+y) == '#':
                        adj = adj + 1
            pointer = state[row][col]
            new = pointer
            if pointer == '#' and adj >= 4:
                new = 'L'
                delta = True
            if pointer == 'L' and adj == 0:
                new = '#'
                delta = True
            if new == '#':
                counter = counter + 1
            strip = strip + new
        next.append(strip)
    if delta:
        return next
    return counter

state = input

while isinstance(state,list):
    state = update(state)

print(state)

#Part 2
def update(state):
    next = []
    delta = False
    counter = 0
    for row in range(len(state)):
        strip = ''
        for col in range(len(state[row])):
            adj = 0
            pointer = state[row][col]
            new = pointer
            if new != '.': #Optimization
                for x in [1,0,-1]:
                    for y in [1,0,-1]:
                        if x==y==0:
                            continue
                        a = 0
                        empty = True
                        while(empty):
                            a = a + 1
                            query = occupied(state,row+a*x,col+a*y)
                            if query != '.':
                                empty = False
                                if query == '#':
                                    adj = adj + 1
            if pointer == '#' and adj >= 5:
                new = 'L'
                delta = True
            if pointer == 'L' and adj == 0:
                new = '#'
                delta = True
            if new == '#':
                counter = counter + 1
            strip = strip + new
        next.append(strip)
    if delta:
        return next
    return counter

state = input

while isinstance(state,list):
    state = update(state)

print(state)
