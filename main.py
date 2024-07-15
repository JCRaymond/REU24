import gen_data
from sys import argv

if len(argv) < 2:
    print('Must provide file to write data to as argument')
    exit()

fname = argv[1]

gen_data.gen_data(list(range(3, 50)), 10000, 5000, 100,
                  [i * 0.05 for i in range(16)], fname)
