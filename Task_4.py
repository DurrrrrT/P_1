# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [1, 2, 6, 24]

def f(n):
    return 1 if n == 0 else n * f(n - 1)
print(f(4))

