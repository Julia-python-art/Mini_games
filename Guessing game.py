# Проверяем число это или текст
def is_valid(s, y):
    if 1 <= int(s) <= y:
        return True
    False 

# Функция для угадывания числа     
from random import *
def guess():
    print('Добро пожаловать в числовую угадайку')
    print('Введите границу для загаданного числа')
    # Вводим границу и загадываем число
    borders = int(input())
    num = randint(1, borders)
    
    # Вводим число и проверяем его
    print('Введите число от 1 до {}'.format(borders))
    x = input()
    result = is_valid(x, borders)
    if result:
        x = int(x)
    else:
        print('А может быть все-таки введем целое число от 1 до {}?'.format(borders))
    
    # Пробуем угадать загаданное число и считаем количество попыток
    attempts = 1
    while True:
        if x < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            x = int(input())
            attempts += 1
        elif x > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            x = int(input())
            attempts += 1
        else:
            break
    print('Вы угадали, поздравляем!')
    print(num)
    print('Количество попыток =', attempts)
    print('Хотите сыграть еще раз? (Да или Нет)')
    answer = input()
    if answer.lower() == 'да':
        numbers = guess()
    else:    
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

# Запускаем игру
number = guess()