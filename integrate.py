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
    fr = [float(a) for a in range(1, len(p) + 1)]
    ip = [0] + [x/i for x, i in zip(fp, fr)]
    return ip

def tests():
    p1 = [1, 2, 4, 6]
    ip1 = int_poly(p1)
    print 'Integrating polynomial: {}'.format(rep_poly(p1))
    print 'Integrated to: {}'.format(rep_poly(ip1))
    assert ip1 == [0, 1, 1, 4.0/3, 6.0/4]
    print "Passed tests!!"

if __name__ == '__main__':
    tests()
