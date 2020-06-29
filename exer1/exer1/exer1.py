import math

class Rational:
    def __init__(self,p,q=1):

        if q==0:
            raise ValueError('Denominator must not be zero')
        if not isinstance(p, int):
            raise TypeError('Numerador must be an integer')
        if not isinstance(q,int):
            raise TypeError('Denominator must be an Integer')

        g = math.gcd(p, q)

        self.p = p // g
        self.q = q // g

#method to convert rational to float

def _float_(self):
    return float(self.p) /float(self.q)

#method to convert rational  to string for printing

def _str_(self):
    return '%d /%d ' % (self.p, self.q)

#method to add txo rationals - interprets seft + other

def _add_(self, other):
    if isinstance(other, Rational):
        return Rational (self.p * other.q + other.p * self.q, self.q * other.q)
        #--if it's an integer...
    elif isinstance(other, int):
         return Rational(self.p + other * self.q, self.q)
    #--otherwise, we assume it wil be a float 
    return float(self) + float(other)

def _radd_(self, other): #interprete other + self
    return self + other 