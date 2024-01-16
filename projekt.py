class Quadratic_poly:
    """Class Quadratic_poly implements quadratic polynomial a ∗ x^2 + b ∗ x + c:
    Attributes:
        elements: tuple - polynomial coefficients
        """
    def __init__(self,elements):
        self.elements = elements

    def __repr__(self):
        return f'coefficient: {self.elements}'

    def delta(self):

        return ((self.elements[1])**2) - (4 * self.elements[0] * self.elements[2])

    def solve(self):
        if self.elements[0] == 0:
            raise ValueError('"a" cannot be zero')
        if  == 0:
            x = self.elements[0]*2






