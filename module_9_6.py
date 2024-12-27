# Генераторы#module_9_6.py
##Задача "":
def all_variants(text):
    i = 0
    while i < len(text):
        j = 0
        while len(text) - j > 0:
            if i + j < len(text):
                yield text[j:j + i + 1]
            j += 1
        i += 1
a = all_variants("abc")
for i in a:
    print(i)
