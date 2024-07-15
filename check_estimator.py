import numpy as np


def check_estimator(genomes, rtbfs):
    n, l, s = genomes.shape
    parent, bfs = rtbfs

    bfs_iter = iter(bfs)
    root = next(bfs_iter)

    errors = np.zeros((l, s), dtype=np.int32)
    mask = np.zeros(n, dtype=bool)

    actual_dist_max = np.max(np.cumsum(genomes[parent] != genomes, axis=1),
                             axis=0)
    for i, v in enumerate(bfs_iter):
        mask[bfs[i]] = True
        mask[parent[v]] = False
        errors += np.sum(
            np.cumsum(genomes[mask] != genomes[v], axis=1) <= actual_dist_max,
            axis=0)
        mask[parent[v]] = True

    return errors


if __name__ == '__main__':
    import gen_genomes
    import gen_tree

    n = 20
    l = 1000
    s = 5
    a = 0.2
    rtbfs = gen_tree.gen_rooted_tree_bfs(n)
    genomes = gen_genomes.gen_genomes(n, l, s, rtbfs, a)

    print(check_estimator(genomes, rtbfs))
