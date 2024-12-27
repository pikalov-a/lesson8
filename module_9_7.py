# Декораторы#module_9_7.py
##Задача "":
def is_prime(func):
    def wrapper(x1, x2, x3):
        n=func(x1, x2, x3)
        i=2
        xrez="Простое"
        while i<= n // 2:
            if n % i == 0:
                xrez='Составное'
                break
            else:
                i += 1
                continue
        print(xrez)
        return n
    return wrapper
@is_prime
def sum_three(x1,x2,x3):
    return x1+x2+x3
result = sum_three(2, 3, 6)
print(result)
