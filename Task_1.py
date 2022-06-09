# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
def number(N):
    rezult = []
    for i in range(0, N):
        rezult.append((-3)**i)
    return(rezult)
print(number(5))