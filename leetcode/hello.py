' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# if __name__=='__main__':
# #     test()
# #
# # li = [lambda :x for x in range(10)]
# # print(type(li))
# # print(type(li[0]))

def createCounter():
    x = [0]
    def counter():
        x[0] += 1
        return x[0]
    return counter

def createCounter():
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n
    return counter
createCounter()