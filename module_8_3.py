##Создание исключений#module_8_3.py
##Задача "Некорректность":
class Car:
    def __init__(self, model, vin, number ):
        self.model=model
        self.__vin= vin
        self.__numbers = number
        if self.__is_valid_numbers(number):
            self.__numbers = number
        if self.__is_valid_vin(vin):
            self.__vin = vin

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999 :
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        if len(numbers) != 6 :
            raise IncorrectVinNumber('Неверная длина номера')
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message=message
        super().__init__(self.message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print("!!!1")
    print(exc.message)
except IncorrectCarNumbers as exc:
    print("!!!1.1")
    print(exc.message)
else:
    print(f'{first.model} успешно создан')
try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')
try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
