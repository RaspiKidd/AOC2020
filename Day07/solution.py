lines = open('input.txt').read().replace(' bags','').replace(' bag','').replace('.','').splitlines()

empties = ['base']
dictionary = {}
for line in lines:
    r = line.split(' contain ')
    if 'no other' in line:
        dictionary[r[0]] = {}
        empties.append(r[0])
    else:
        dictionary[r[0]] = {y[1]: int(y[0]) for x in r[1].split(', ') if (y := x.split(' ',1))}


# Part 1
def g(li):
    for u in li:
        if u == 'shiny gold':
            return True
        else:
            if g(dictionary[u]) == True:
                return True

d = {x:g(dictionary[x]) for x in dictionary}

print(len({x for x in d if (d[x] == True)}))

# Part 2
def f(li,count):
    for u in li:
        k = li[u]
        if u not in empties:
            tmp = {x:y*k for x in dictionary[u] if (y := dictionary[u][x])}
            tmp.update({'base':k})
            count = f(tmp,count)
        else:
            count += k
    return count

print( f(dictionary['shiny gold'],0) )
