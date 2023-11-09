class Temperature:
    @staticmethod
    def c_to_f(c):        # перевод Цельсий в Фаренгейт
        F = (c * 9 / 5) + 32
        return F

    @staticmethod
    def f_to_c(f):        # перевод Фаренгейт в Цельсии
        C = (f - 32) * 5 / 9
        return C


