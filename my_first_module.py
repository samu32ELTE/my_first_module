def print_sum(a, b, *args):
    if args is None:
        print ('sum:',a+b)
    else:
        x = a + b
        for arg in args:
            x+= arg
        print ('sum:',x)