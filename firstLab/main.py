import numpy as np


sum = (((0 + 999999) * (999999 + 1)) / 2)
print ("Сумма ряда:", sum)

avg = sum / (999999 + 1)
print ("Среднее ряда:",avg)

medaina = np.median(np.random.rand(1000000))
print ("Медиана случайных чисел:", medaina)

multiplication = np.prod(np.random.rand(1000000))
print ("Произведение:" , multiplication)