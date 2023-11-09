from Fraction import Fraction  # Импортируем класс Fraction из файла Fraction.py
from Temperature import (
    Temperature,  # Импортируем класс TemperatureConverter из файла TemperatureConverter.py
)
from Conventor import (
    Convertor,  # Импортируем класс UnitConverter из файла UnitConverter.py
)

if __name__ == "__main__":
    print("Добро пожаловать в программу для работы с дробями, конвертацией температуры и метрическими единицами!")

    while True:
        print("\nВыберите опцию:")
        print("1. Работа с дробями")
        print("2. Конвертация температуры")
        print("3. Конвертация метрических единиц")
        print("4. Выход")

        choice = input("Введите номер опции: ")

        if choice == "1":
            numerator1 = int(input("Введите числитель первой дроби: "))
            denominator1 = int(input("Введите знаменатель первой дроби: "))
            fraction1 = Fraction(numerator1, denominator1)

            numerator2 = int(input("Введите числитель второй дроби: "))
            denominator2 = int(input("Введите знаменатель второй дроби: "))
            fraction2 = Fraction(numerator2, denominator2)

            print("Выберите операцию:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")

            operation = input("Введите номер операции: ")

            if operation == "1":
                result = fraction1.add(fraction2)
            elif operation == "2":
                result = fraction1.subtraction(fraction2)
            elif operation == "3":
                result = fraction1.multiply(fraction2)
            elif operation == "4":
                result = fraction1.division(fraction2)
            else:
                print("Неверная операция")
                continue

            print("Результат:")
            result.display()

        elif choice == "2":
            temp_choice = input("Выберите опцию (1 - Цельсий в Фаренгейт, 2 - Фаренгейт в Цельсий): ")

            if temp_choice == "1":
                celsius_temp = float(input("Введите температуру в градусах Цельсия: "))
                fahrenheit_temp = Temperature.c_to_f(celsius_temp)
                print(f"{celsius_temp} градусов Цельсия равно {fahrenheit_temp} градусов Фаренгейта")

            elif temp_choice == "2":
                fahrenheit_temp = float(input("Введите температуру в градусах Фаренгейта: "))
                celsius_temp = Temperature.f_to_c(fahrenheit_temp)
                print(f"{fahrenheit_temp} градусов Фаренгейта равно {celsius_temp} градусов Цельсия")

            else:
                print("Неверная опция")

        elif choice == "3":
            unit_choice = input(
                "Выберите опцию (1 - километры в мили, 2 - мили в километры, 3 - галлоны в литры, 4 - литры в галлоны): ")

            if unit_choice == "1":
                km = float(input("Введите количество километров: "))
                miles = Convertor.km_to_miles(km)
                print(f"{km} километров равно {miles} миль")

            elif unit_choice == "2":
                miles = float(input("Введите количество миль: "))
                km = Convertor.miles_to_km(miles)
                print(f"{miles} миль равно {km} километров")

            elif unit_choice == "3":
                gallons = float(input("Введите количество галлонов: "))
                liters = Convertor.gallons_to_liters(gallons)
                print(f"{gallons} галлонов равно {liters} литров")

            elif unit_choice == "4":
                liters = float(input("Введите количество литров: "))
                gallons = Convertor.liters_to_gallons(liters)
                print(f"{liters} литров равно {gallons} галлонов")

            else:
                print("Неверная опция")

        elif choice == "4":
            print("Спасибо за использование программы!")
            break

        else:
            print("Неверная опция. Пожалуйста, выберите существующую опцию.")


