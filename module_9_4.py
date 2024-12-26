# Создание функций на лету#module_9_4.py
##Задача "Функциональное разнообразие":
#import random
from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'

rez1=list(map(lambda x,y: x==y, first, second))
print(rez1)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='utf-8')
        for i in range(len(data_set)):
            if isinstance(data_set[i],str):
                file.write(data_set[i])
                file.write('\n')
            else:
                file.write(str(data_set[i]))
                file.write('\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__( *words):

        self= words
    def __call__(self):
        return choice(self)
#2 дня пытался этот__find__отработать/ без него работет в лёт
xx=('Да', 'Нет', 'Наверное')
print(choice(xx))
#
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
