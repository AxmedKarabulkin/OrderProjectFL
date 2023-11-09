class Convertor:
    @staticmethod
    def km_to_miles(kilometers):   # перевод километры в мили
        miles = kilometers * 0.621371
        return miles

    @staticmethod
    def miles_to_km(miles):        # перевод милли в километры
        kilometers = miles * 1.60934
        return kilometers

    @staticmethod
    def gallons_to_liters(gallons):   # перевод галлоны в литры
        liters = gallons * 3.78541
        return liters

    @staticmethod
    def liters_to_gallons(liters):    # перевод литры в галлоны
        gallons = liters / 3.78541
        return gallons
