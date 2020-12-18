def read_input(fname):
    with open(fname, "r") as handle:
        return [x.strip() for x in handle.readlines()]


def build_world(inp, dims):
    world = set()
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == "#":
                world.add(tuple([x, y] + ([0] * (dims - 2))))
    return world


def get_neighbours(cell, dims):
    if dims == 3:
        return get_neighbours_3(cell)
    else:
        return get_neighbours_4(cell)

    # NOTE: This could be simplified to the following, however this
    # runs too slowly
    # for coord in itertools.product(*([[-1, 0, 1]] * dims)):
    #     if not all([True if x == 0 else False for x in coord]):
    #         yield tuple([off + cell for off, cell in zip(coord, cell)])


def get_neighbours_3(cell):
    for z in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if not (x == y == z == 0):
                    yield (cell[0] + x, cell[1] + y, cell[2] + z)


def get_neighbours_4(cell):
    for w in [-1, 0, 1]:
        for z in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if not (x == y == z == w == 0):
                        yield (cell[0] + x, cell[1] + y, cell[2] + z, cell[3] + w)


def run_step(world, dims):
    new = set()
    for cell in world:
        # Inactive cells become active if 3 neighbours are active
        new.update([
            neighbour for neighbour in
            [x for x in get_neighbours(cell, dims) if x not in world]
            if len([x for x in get_neighbours(neighbour, dims) if x in world]) == 3
        ])

        # Active cells remain active if they have 2 or 3 active
        # neighbours
        if 2 <= len([x for x in get_neighbours(cell, dims) if x in world]) <= 3:
            new.add(cell)

    return new


def run_simulation(inp, seq_len, dims=3):
    world = build_world(inp, dims)
    yield world
    for i in range(seq_len):
        world = run_step(world, dims)
        yield world
    return world


def solve_p1(inp):
    w = None
    for world in run_simulation(inp, 6, 3):
        w = world
    return len(w)


def solve_p2(inp):
    w = None
    for world in run_simulation(inp, 6, 4):
        w = world
    return len(w)


def main():
    inp = read_input("input.txt")
    sln1 = solve_p1(inp)
    print("The solution to part 1 is: {}".format(sln1))
    sln2 = solve_p2(inp)
    print("The solution to part 2 is: {}".format(sln2))


def test_main():
    inp = read_input("input.txt")
    assert solve_p1(inp) == "<hidden>"
    assert solve_p2(inp) == "<hidden>"


def test_ex():
    inp = read_input("input_ex.txt")
    assert solve_p1(inp) == 112
    assert solve_p2(inp) == 848


if __name__ == "__main__":
    main()
