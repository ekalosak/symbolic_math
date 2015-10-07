import sys
import os

def rep_poly(p):
    ''' vector representation of the polynomial '''
    s = ''
    x_tothe = lambda x: 'x^{}'.format(x)
    for i in range(len(p)):
        s = s + str(p[i]) + '*' + x_tothe(i)
        if i != len(p) - 1:
            s = s + ' + '
    return s

def int_poly(p):
    ''' integrate vector representation of the polynomial'''
    fp = [float(a) for a in p]
    ip = [0] + [x/i for x, i in zip(


def tests():
    p1 = [1, 2, 4, 6]
    print 'Integrating polynomial: {}'.format(rep_poly(p1))
    assert int_poly(p1) == [0, 1, 
if __name__ == '__main__':
    tests()
