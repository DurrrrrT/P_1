# Подсчитать сумму цифр в вещественном числе.

def summ(V):
    print(f"Входящее число V = {V}")
    summel = 0
    for i in str(V):
        if i.isdigit():
            summel += int(i)
    return summel

print(f"Сумма всех = {summ(23.141)}")
