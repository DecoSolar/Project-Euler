summa = 23
for i in range(10, 1000):
    if i % 3 == 0 or i % 5 ==0:
        summa += i
print("Сумма чисел меньше 1000 равна:", summa)
