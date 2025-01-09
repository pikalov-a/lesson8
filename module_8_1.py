##Try и Except#module_8_1.py
##Задача "Программистам всё можно":
def add_everything_up(a, b):
    try:
        return a + b
    except:
        if type(a) != str:
            a = str(a)
        if type(b) != str:
            b = str(b)
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
