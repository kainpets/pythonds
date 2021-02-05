"""Implement the simple methods getNum and
getDen that will return the numerator and denominator of a fraction."""

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top / gcd(top, bottom)
        self.den = bottom / gcd(top, bottom)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    
    def __mul__(self, other):
        topfactor = self.num * other.num
        bottomfactor = self.den * other.den
        common = gcd(topfactor, bottomfactor)

        return Fraction(topfactor, bottomfactor)

    def __truediv__(self, other):
        topdiv = self.num * other.den
        bottomdiv = self.den * other.num
       

        return Fraction(topdiv, bottomdiv)

    #TODO def __gt__(self, other):

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den
        
x = Fraction(5,6)
y = Fraction(2,3)

print(x.getDen())
print(x * y)
