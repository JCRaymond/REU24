from random import randrange


def code_to_tree(code):
    n = len(code) + 2
    counts = [0] * n
    for c in code:
        counts[c] += 1

    currvert = 0
    for c in code:
        while counts[currvert] != 0:
            currvert += 1
        counts[currvert] = -1
        counts[c] -= 1
        yield (currvert, c)
        if c < currvert and counts[c] == 0:
            currvert = c

    while counts[currvert] != 0:
        currvert += 1
    start = currvert
    currvert += 1
    while counts[currvert] != 0:
        currvert += 1
    yield (start, currvert)


def gen_tree(n):
    code = [randrange(n) for _ in range(n - 2)]
    yield from code_to_tree(code)


def gen_rooted_tree_bfs(n):
    rooted_tree = [None] * n
    bfs = [None] * n

    root = randrange(n)

    rooted_tree[root] = root
    bfs[0] = root
    bfs_back = 1

    tree = {i: set() for i in range(n)}
    for s, e in gen_tree(n):
        tree[s].add(e)
        tree[e].add(s)

    for i in range(n):
        curr = bfs[i]
        for j in tree[curr]:
            if rooted_tree[j] is None:
                rooted_tree[j] = curr
                bfs[bfs_back] = j
                bfs_back += 1

    return rooted_tree, bfs


def gen_rooted_tree(n):
    tree, _ = gen_rooted_tree_bfs(n)
    return tree


if __name__ == '__main__':
    print(gen_rooted_tree(10))
