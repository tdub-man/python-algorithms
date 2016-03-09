class rational():
    """Represent rational numbers with fractions"""
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def clone(self):
        return rational(self.numerator,self.denominator)
    def add(self,rational2):
        n = (self.numerator*rational2.denominator)+(self.denominator*rational2.numerator)
        d = self.denominator*rational2.denominator
        return rational(n,d)
    def negate(self):
        return rational(-1*self.numerator,self.denominator)
    def subtract(self,rational2):
        return self.add(rational2.negate())
    def multiply(self,rational2):
        n = self.numerator * rational2.numerator
        d = self.denominator * rational2.denominator
        return rational(n,d)
    def divide(self,rational2):
        return multiply(rational2.reciprocal())
    def reciprocal(self):
        return rational(self.denominator,self.numerator)
    def power(self,exp):
        b = self.clone()
        if exp < 0:
            return rational(pow(b.denominator,-exp),pow(b.numerator,-exp))
        else:
            return rational(pow(b.numerator,exp),pow(b.denominator,exp))
    def value(self):
        return self.numerator / self.denominator
