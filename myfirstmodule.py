__version__ = '1.0.0'

import numpy
import networkx
from community import best_partition as Louvain
print('Numpy succesfully loaded.')

def print_sum(a, b, *args):
    if args is None:
        print ('sum:',a+b)
        G = nx.barabasi_albert_graph(10,2)
        print (G.nodes(), Louvain(G))
    else:
        x = a + b
        for arg in args:
            x+= arg
        print ('sum:',x)
        G = nx.barabasi_albert_graph(10,2)
        print (G.nodes(), Louvain(G))