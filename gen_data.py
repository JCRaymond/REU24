import gen_tree
import gen_genomes
import check_estimator

import numpy as np


def gen_data(ns, num_trees, max_l, s, aas, fname):
    with open(fname, 'w') as f:
        for n in ns:
            for a in aas:
                print(n, a)
                for t in range(num_trees):
                    if t % 100 == 99:
                        print(f'\t{t+1}')
                    rtbfs = gen_tree.gen_rooted_tree_bfs(n)
                    genomes = gen_genomes.gen_genomes(n, max_l, s, rtbfs, a)
                    errors = check_estimator.check_estimator(genomes, rtbfs)
                    avg_error = np.average(errors, axis=1)
                    f.write(f'{n} {max_l} {a} {s}\n')
                    f.write(f'{",".join(map(str, rtbfs[0]))}\n')
                    f.writelines(f'{",".join(map(str, avg_error))}\n')


if __name__ == '__main__':
    gen_data(list(range(3, 50)), 10000, 5000, 100,
             [i * 0.05 for i in range(16)], 'data.txt')
