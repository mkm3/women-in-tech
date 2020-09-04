from fractions import Fraction
from math import degrees

memo = {}

def ab(n):
    if n in memo:
        return memo[n]
    assert isinstance(n, int) and n > 0, n
    if n%2 == 0:
        return Fraction()
    nterms = (n-1) // 2
    arg = nterms + 1
    sum = Fraction(-1,2) * Fraction(2*arg-1, 2*arg+1)
    for i in range(nterms):
        degree = 2*i + 1
        v = term(degree, arg)
        sum += ab(degree) * v
    res = -sum
    memo[n] = res
    return res

def term(degree, n):
    num = 1
    den = 1
    for i in range(degree):
        num *= 2*n -i
        den *= 2 + i
    return Fraction(num,den)

cipher = {}
for b in [65, 97]:
    for i in range(26):
        cipher[b+i] = b + (i+13)%26

def caesar(s):
    return s.translate(cipher)

def main():
    for n in range(1, 37):
        a = ab(n)
        print("AB[%2s] == %21s / %s" % (n, a.numerator, a.denominator))
    print(caesar("uggcf://jjj.sbhezvyno.pu/onoontr/fxrgpu.ugzy"))

if __name__ == '__main__':
    main()

