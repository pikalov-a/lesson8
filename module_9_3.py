# Генераторные сборки#module_9_2.py
##Задача "":
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result= (len(x)-len(y) for x,y in zip(first,second) if len(x) != len(y))
print(list(first_result))
second_result= (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i==j )
print(list(second_result))
