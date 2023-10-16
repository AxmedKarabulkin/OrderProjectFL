class Fraction:
    def __init__(self, numerator, denominator):     # Конструктор класса Fraction
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):    # Геттер числителя
        return self.numerator

    def get_denominator(self):  # Геттер знаменателя
        return self.denominator

    def set_numerator(self, numerator):     # Сеттер числителя
        self.numerator = numerator

    def set_denominator(self, denominator):     # Сеттер знаменателя
        self.denominator = denominator

    def division(self, fraction):
        numerator = self.numerator / fraction.denominator   #деление
        denominator = self.denominator / fraction.numerator
        return Fraction(numerator, denominator)

    def multiply(self, fraction):
        numerator = self.numerator * fraction.numerator     #умножение
        denominator = self.denominator * fraction.denominator
        return Fraction(numerator, denominator)

    def add(self, fraction):
        numerator = self.numerator * fraction.denominator + self.denominator * fraction.numerator   #сложение
        denominator = self.denominator * fraction.numerator + self.denominator * fraction.numerator
        return Fraction(numerator, denominator)

    def subtraction(self, fraction):
        numerator = self.numerator * fraction.denominator - self.denominator * fraction.numerator   #вычитание
        denominator = self.denominator * fraction.numerator - self.denominator * fraction.numerator
        return Fraction(numerator, denominator)

