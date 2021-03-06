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
        
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

        
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    
    def __mul__(self, other):
        topfactor = self.num * other.num
        bottomfactor = self.den * other.den
        
        return Fraction(topfactor, bottomfactor)

    def __truediv__(self, other):
        topdiv = self.num * other.den
        bottomdiv = self.den * other.num

        return Fraction(topdiv, bottomdiv)

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum
    
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den
        
x = Fraction(1,3)
y = Fraction(2,3)

print(x.getDen())
print(x * y)
print(x + y)
print(y - x)
print(x > y)
print(y > x)

