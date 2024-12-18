##Сложные моменты и исключения в стеке вызовов функции#module_8_2.py
##Задача "План перехват":
def personal_sum(numbers):
    xsum=0
    xlen=0
    for i in range(len(numbers)):
        try:
            xsum += numbers[i]
            xlen += 1
        except:
            print(f'Некорректный тип данных для подсчёта суммы {numbers[i]}')
    return xsum, xlen

def calculate_average(numbers):
    try:
        xmid=personal_sum(numbers)[0] / personal_sum(numbers)[1]
    except:
        print('В numbers записан некорректный тип данных ')
        return None
    return xmid


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
##TypeError 'str' object is not callable
##от меня ждут ответ 2.0=4/2  а не 1.0=4/4
#№ из-за этого мне приходится считать складываемые числа и вводить для этого переменную
## в результате все ошибки ВЫВОДЯТСЯ ДВАЖДЫ. Никак не могу избавиться
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
##TypeError: 'list' object is not callable
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
##TypeError: object of type 'int' has no len()
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
