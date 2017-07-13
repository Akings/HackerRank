class Complex(object):

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        new_real = self.real + no.real
        new_imaginary = self.imaginary + no.imaginary
        return Complex(new_real, new_imaginary)

    def __sub__(self, no):
        new_real = self.real - no.real
        new_imaginary = self.imaginary - no.imaginary
        return Complex(new_real, new_imaginary)

    def __mul__(self, no):
        new_real = self.real * no.real - self.imaginary * no.imaginary
        new_imaginary = self.imaginary * no.real + self.real * no.imaginary
        return Complex(new_real, new_imaginary)

    def __truediv__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        new_real = (a * c + b * d) / (c ** 2 + d ** 2)
        new_imaginary = (b * c - a * d) / (c ** 2 + d ** 2)
        return Complex(new_real, new_imaginary)

    def mod(self):
        new_real = pow(self.real ** 2 + self.imaginary ** 2, 0.5)
        return Complex(new_real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
