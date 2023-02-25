# Задача 4. Есть ли статистически значимые различия в росте
# дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163

import numpy as np
from scipy.stats import ttest_ind

# рост матерей
m_heights = [172, 177, 158, 170, 178, 175, 164, 160, 169, 165]

# рост дочерей
d_heights = [173, 175, 162, 174, 175, 168, 155, 170, 160, 163]

# применяем t-критерий Стьюдента
t, p = ttest_ind(m_heights, d_heights, equal_var=False)

print("t =", t)
print("p-value =", p)

# Задача 4. Есть ли статистически значимые различия в росте
# дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163

import numpy as np
from scipy.stats import ttest_ind

# рост матерей
m_heights = [172, 177, 158, 170, 178, 175, 164, 160, 169, 165]

# рост дочерей
d_heights = [173, 175, 162, 174, 175, 168, 155, 170, 160, 163]

# применяем t-критерий Стьюдента
t, p = ttest_ind(m_heights, d_heights, equal_var=False)

print("t =", t)
print("p-value =", p)

# Ответ
# Значение p-value равно 0.683, что значительно больше выбранного уровня значимости (например, 0.05). 
# Поэтому мы не можем отвергнуть нулевую гипотезу о том, что средние значения 
# двух выборок не различаются. 
# То есть, статистически значимых различий в росте дочерей не обнаружено.
