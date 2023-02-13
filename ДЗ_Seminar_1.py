from math import factorial

    # Из колоды в 52 карты извлекаются случайным образом 4 карты. 
    # a) Найти вероятность того, что все карты – крести. 
    # 

    # Решение а)

# считаем благоприятное сочетание крестей. 52 / 4 = 13

# n = 13
# k = 4
# def combination(n,k):
#     return float(factorial(n) / (factorial(k) * factorial(n-k)))

# resultA = combination(n,k)
# print('благоприятных исходов =',resultA)

# # считаем общее сочетание для крестей
# n1 = 52
# k1 = 4
# def combination_1(n1,k1):
#     return factorial(n1) / (factorial(k1) * factorial(n1-k1))

# resultB = combination_1(n1,k1)
# print('общее число исходов =',resultB)

# P = resultA / resultB
# print('вероятность того, что все карты – крести =', round(P,5), 'или',round(P,5)*100,'%')

    # б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
    # Решение б)

# считаем благоприятное сочетание без тузов. 52 - 4 = 48
# n = 48
# k = 4
# def combination(n,k):
#     return float(factorial(n) / (factorial(k) * factorial(n-k)))

# resultA = combination(n,k)
# print('благоприятных исходов =',resultA)

# # считаем общее сочетание
# n1 = 52
# k1 = 4
# def combination_1(n1,k1):
#     return factorial(n1) / (factorial(k1) * factorial(n1-k1))

# resultB = combination_1(n1,k1)
# print('общее число исходов =',resultB)

# P = 1 - (resultA / resultB)
# print('вероятность, что среди 4-х карт окажется хотя бы один туз =', round(P,2), 'или',round(P,2)*100,'%')



    # На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
    # Код содержит три цифры, которые нужно нажать одновременно. 
    # Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

# считаем благоприятное сочетание.
# n = 10
# k = 3
# def combination(n,k):
#     return float(factorial(n) / (factorial(k) * factorial(n-k)))

# resultA = combination(n,k)
# print('благоприятных исходов =',resultA)

# P = ( 1/ resultA )
# print('вероятность того, что человек, не знающий код, откроет дверь с первой попытки =', round(P,3), 'или',round(P,4)*100,'%')

    # В ящике имеется 15 деталей, из которых 9 окрашены. 
    # Рабочий случайным образом извлекает 3 детали. 
    # Какова вероятность того, что все извлеченные детали окрашены?
# считаем благоприятное сочетание.
# n = 9
# k = 3
# def combination(n,k):
#     return float(factorial(n) / (factorial(k) * factorial(n-k)))

# resultA = combination(n,k)
# print('благоприятных исходов =',resultA)

# # считаем общее сочетание
# n1 = 15
# k1 = 3
# def combination_1(n1,k1):
#     return factorial(n1) / (factorial(k1) * factorial(n1-k1))

# resultB = combination_1(n1,k1)
# print('общее число исходов =',resultB)

# P = (resultA / resultB)
# print('вероятность того, что все извлеченные детали окрашены =', round(P,3), 'или',round(P,3)*100,'%')

    # В лотерее 100 билетов. Из них 2 выигрышных. 
    # Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

# считаем благоприятное сочетание.
# n = 100
# k = 2
# def combination(n,k):
#     return float(factorial(n) / (factorial(k) * factorial(n-k)))

# resultA = combination(n,k)
# print('благоприятных исходов =',resultA)

# P = ( 1 / resultA )

# print('вероятность того, что 2 приобретенных билета окажутся выигрышными =', round(P,4), 'или',round(P,4)*100,'%')