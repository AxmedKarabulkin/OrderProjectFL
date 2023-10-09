class Temperature:
    def c_to_f(self, c):        # перевод Цельсий в Фаренгейт
        f = (c * 9 / 5) + 32
        return f

    def f_to_c(self, f):        # перевод Фаренгейт в Цельсии
        c = (f - 32) * 5 / 9
        return c
