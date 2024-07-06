import gen_genome

import numpy as np


def gen_genomes(n, l, s, rtbfs, a):

    parent, bfs = rtbfs

    genomes = np.empty((n, l, s), dtype=np.uint8)
    rng_buf = np.empty((l, s), dtype=float)

    bfs_iter = iter(bfs)
    genomes[next(bfs_iter)] = gen_genome.gen_genome_unif(l, s)

    for v in bfs_iter:
        gen_genome.gen_mutation(genomes[parent[v]],
                                a,
                                rng_buf=rng_buf,
                                out=genomes[v])

    return genomes


if __name__ == '__main__':
    import gen_tree
    n = 3
    l = 10
    s = 10
    a = 0.1
    rtbfs = gen_tree.gen_rooted_tree_bfs(n)
    print(rtbfs[0])
    print(gen_genomes(n, l, s, rtbfs, a))
