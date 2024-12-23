# Генераторные сборки#module_9_3.py
##Задача "":
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result= (len(x)-len(y) for x,y in zip(first,second) if len(x) != len(y))
print(list(first_result))
second_result= (len(x) == len(y) for x in first for y in second if x != y )
print(list(second_result))
