from itertools import product

n = 4
print(list(product(['+', '-', '*', '/'], repeat=(n-1))))