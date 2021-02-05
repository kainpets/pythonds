def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    
    def __mul__(self, other):
        topfactor = self.num * other.num
        bottomfactor = self.den * other.den
        common = gcd(topfactor, bottomfactor)

        return Fraction(topfactor // common, bottomfactor // common)

    def __truediv__(self, other):
        topdiv = self.num * other.den
        bottomdiv = self.den * other.num
        common = gcd(topdiv, bottomdiv)

        return Fraction(topdiv // common, bottomdiv // common)

    def __gt__(self, other):
        

x = Fraction(4,6)
y = Fraction(2,3)
print(x+y)
print(x == y)
print(x * y)
print(x / y)
print(x > y)
