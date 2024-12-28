from random import randrange

class Zx:
    def __init__(self, coeffs):
        """
        Initialize the polynomial with a list of coefficients.
        """
        self.coeffs = coeffs

    def coefficient(self, n):
        """
        Get the coefficient of x^n.
        """
        if n < 0:
            raise ValueError("Coefficient index must be non-negative.")
        if n >= len(self.coeffs):
            return 0
        return self.coeffs[n]

    def degree(self):
        """
        Return the degree of the polynomial.
        """
        return len(self.coeffs) - 1

    def eval(self, x):
        """
        Evaluate the polynomial at a given value of x.
        """
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x ** i)
        return result

    def add(self, other):
        """
        Add two polynomials and return the result.
        """
        max_degree = max(self.degree(), other.degree())
        result_coeffs = [self.coefficient(i) + other.coefficient(i) for i in range(max_degree + 1)]
        return Zx(result_coeffs)

    def multiply_single_term(self, coefficient, degree):
        """
        Multiply the polynomial by a single term (coefficient * x^degree).
        """
        result_coeffs = [0] * degree + [c * coefficient for c in self.coeffs]
        return Zx(result_coeffs)

    def multiply(self, other):
        """
        Multiply two polynomials and return the result.
        """
        result = Zx([0])
        for i in range(len(other.coeffs)):
            term = self.multiply_single_term(other.coefficient(i), i)
            result = result.add(term)
        return result

    def reduce_mod_xn(self, N):
        """
        Reduce the polynomial modulo x^N - 1.
        """
        result_coeffs = [0] * N
        for i, coeff in enumerate(self.coeffs):
            result_coeffs[i % N] += coeff
        return Zx(result_coeffs)

    def mod_coeffs(self, q):
        """
        Reduce the coefficients modulo q.
        """
        self.coeffs = [c % q for c in self.coeffs]
        return self

    def balanced_mod(self, q):
        """
        Reduce the coefficients modulo q to the range [-q/2, q/2].
        """
        self.coeffs = [((c + q // 2) % q) - q // 2 for c in self.coeffs]
        return self

    def random_poly(self, d, N):
        """
        Generate a random polynomial with exactly d coefficients set to ±1, and the rest set to 0.
        """
        self.coeffs = [0] * N
        for _ in range(d):
            while True:
                index = randrange(N)
                if self.coeffs[index] == 0:
                    self.coeffs[index] = 1 if randrange(2) == 0 else -1
                    break
        return self

    def print_polynomial(self):
        """
        Return a string representation of the polynomial.
        """
        terms = []
        for i, coeff in enumerate(self.coeffs):
            if coeff != 0:
                term = f"{coeff}"
                if i > 0:
                    term += f"x^{i}" if i > 1 else "x"
                terms.append(term)
        return " + ".join(terms[::-1]) if terms else "0"
