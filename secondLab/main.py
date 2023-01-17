from Calculate import Calculate
import json
import os.path

res = 0

def save(): # Объявление функции сохранения
    with open('result.json', 'w') as file:
        to_json = {'result': res}
        json.dump(to_json, file)

if os.path.exists('result.json') == False: # Создание файла, если его не существует
    save()

with open('result.json') as file: # Загрузка результата прошлых вычислений
    obj = json.load(file)
    res = obj["result"]

c = Calculate(res)

print(f'Последний результат - {res}')
while True:
    string = input('Введите операцию, либо save для сохранения результата: ')
    if string == 'save': # Сохранение результата работы
        save()
        print('Результат сохранен')
        continue
    lst = string.split(' ')
    if lst[0] in ['+', '-', '*', '/']: # Работа в предыдущим результатом вычислений
        if lst[0] == '+':
            res = c.plus(b=float(lst[1]))
            print(res)
        elif lst[0] == '-':
            res = c.minus(b=float(lst[1]))
            print(res)
        elif lst[0] == '*':
            res = c.multiply(b=float(lst[1]))
            print(res)
        elif lst[0] == '/':
            res = c.divide(b=float(lst[1]))
            print(res)
        else: print('Некоректный ввод')
    else: # Работа с двумя заданными числами
        if lst[1] == '+':
            res = c.plus(float(lst[0]), float(lst[2]))
            print(res)
        elif lst[1] == '-':
            res = c.minus(float(lst[0]), float(lst[2]))
            print(res)
        elif lst[1] == '*':
            res = c.multiply(float(lst[0]), float(lst[2]))
            print(res)
        elif lst[1] == '/':
            res = c.divide(float(lst[0]), float(lst[2]))
            print(res)
        else: print('Некоректный ввод')