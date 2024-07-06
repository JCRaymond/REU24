import numpy as np

rng = np.random.default_rng()


def gen_genome_unif(l, s=1):
    return rng.integers(4, size=(l, s), dtype=np.uint8)


def gen_mutation(genome, a, rng_buf=None, out=None):
    if rng_buf is None:
        rng_buf = np.empty(genome.shape, dtype=float)
    if out is None:
        out = np.empty_like(genome)

    l, s = genome.shape

    rng.random(out=rng_buf[:l, :s])

    left = a / 3
    middle = 2 * a / 3
    right = a

    out[:l, :s] = (rng_buf[:l, :s] <= left)
    out[:l, :s] += (rng_buf[:l, :s] <= middle)
    out[:l, :s] += (rng_buf[:l, :s] <= right)
    out[:l, :s] += genome
    out[:l, :s] &= 3

    return out


if __name__ == '__main__':
    a = 0.001
    g1 = gen_genome_unif(10, s=20)
    print(g1)
    print()
    g2 = gen_mutation(g1, a)
    print()
    print(g2)
