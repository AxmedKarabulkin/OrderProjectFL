class Convertor:
    def km_to_miles(self, kilometers):   # перевод километры в мили
        miles = kilometers * 0.621371
        return miles

    def miles_to_km(self, miles):        # перевод милли в километры
        kilometers = miles * 1.60934
        return kilometers

    def gallons_to_liters(self, gallons):   # перевод галлоны в литры
        liters = gallons * 3.78541
        return liters

    def liters_to_gallons(self, liters):    # перевод литры в галлоны
        gallons = liters / 3.78541
        return gallons
