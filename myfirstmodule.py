__version__ = '1.0.0'

import numpy
import networkx
import community

print('Numpy succesfully loaded.')

def print_sum(a, b, *args):
    if args is None:
        print ('sum:',a+b)
    else:
        x = a + b
        for arg in args:
            x+= arg
        print ('sum:',x)