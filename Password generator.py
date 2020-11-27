# Заголовок программы
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
symbols = 'il1Lo0O'
chars = ''

# Считываем данные

print('Укажите количество паролей для генерации')
n = int(input())
print('Укажите длину одного пароля')
length = int(input())
print('Включать ли цифры 0123456789? да или нет')
check1 = input()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да или нет')
check2 = input()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да или нет')
check3 = input()
print('Включать ли символы !#$%&*+-=?@^_? да или нет')
check4 = input()
print('Включать ли неоднозначные символы il1Lo0O? да или нет')
check5 = input()

# Создаем строку, где находятся все разрешенные символы

if check1.lower() == 'да':
    chars += digits
if check2.lower() == 'да':
    chars += lowercase_letters
if check3.lower() == 'да':
    chars += uppercase_letters
if check4.lower() == 'да':
    chars += punctuation
if check5.lower() == 'нет':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

# Создаем функцию для генерации безопасного пароля
def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password


# Запускаем функцию
for i in range(n):
    print(*generate_password(length, chars), sep='')