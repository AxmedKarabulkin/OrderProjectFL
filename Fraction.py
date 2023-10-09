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

