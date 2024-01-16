import math


class Quadratic_poly:
    """Class Quadratic_poly implements quadratic polynomial a ∗ x^2 + b ∗ x + c:
    Attributes:
        elements: tuple - polynomial coefficients
    """
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f' Coefficients: {self.elements}'

    def delta(self):
        """Finding delta"""
        return ((self.elements[1]) ** 2) - (4 * self.elements[0] * self.elements[2])

    def __mul__(self, scalar):
        """Multiplication of quadratic polynomial by a scalar"""
        elements = [coefficient * scalar for coefficient in self.elements]
        return elements

    def __rmul__(self, scalar):
        """Right multiplication of quadratic polynomial by a scalar"""
        return self.__mul__(scalar)

    def solve(self):
        if self.elements[0] == 0:
            raise ValueError('"a" cannot be zero')
        if self.delta() == 0:
            x = - self.elements[1] / (2*self.elements[0])
            return x
        if self.delta() > 0:
            x1 = (- self.elements[1] - math.sqrt(self.delta())) / (2 * self.elements[0])
            x2 = (- self.elements[1] + math.sqrt(self.delta())) / (2 * self.elements[0])
            return x1, x2
        if self.delta() < 0:
            x1 = (- self.elements[1] + 1j * math.sqrt(abs(self.delta()))) / (2 * self.elements[0])
            x2 = (- self.elements[1] + 1j * math.sqrt(abs(self.delta()))) / (2 * self.elements[0])
            return x1, x2

    def __str__(self):
        if self.elements[0] > 0:
            first_co = str(self.elements[0]) + 'x^2'
        elif self.elements[0] == 0:
            raise ValueError('"a" cannot be zero')
        else:
            first_co = str(abs(self.elements[0])) + 'x^2'
        if self.elements[1] > 0:
            second_co = '+' + str(self.elements[1]) + 'x'
        elif self.elements[1] < 0:
            second_co = '-' + str(abs(self.elements[1])) + 'x'
        else:
            second_co = ''
        if self.elements[2] > 0:
            third_co = '+' + str(self.elements[2])
        elif self.elements[2] < 0:
            third_co = '-' + str(abs(self.elements[2]))
        else:
            third_co = ''
        return first_co + second_co + third_co
