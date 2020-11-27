# Заголовок
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Считываем данные

print('Шифрование или дешифрование?')
way = input()
print('Русский или английский?')
language = input()
print('Какой сдвиг?')
k = int(input())
print('Введите текст')
text = input()
new_text = ''

# Если шифрование и язык русский
if way.lower() == 'шифрование' and language.lower() == 'русский':
    for i in range(len(text)):
        if text[i].isalpha() and text[i].islower():
            new_text += rus_lower_alphabet[(rus_lower_alphabet.index(text[i]) + k) % len(rus_lower_alphabet)]
        elif text[i].isupper() and text[i].isalpha():
            new_text += rus_upper_alphabet[(rus_upper_alphabet.index(text[i]) + k) % len(rus_upper_alphabet)]
        else:
            new_text += text[i]
    print(new_text)
    
# Если дешифрование и русский язык
elif way.lower() == 'дешифрование' and language.lower() == 'русский':
    for j in range(len(text)):
        if text[j].isalpha() and text[j].islower():
            new_text += rus_lower_alphabet[(rus_lower_alphabet.index(text[j]) - k) % len(rus_lower_alphabet)]
        elif text[j].isupper() and text[j].isalpha():
            new_text += rus_upper_alphabet[(rus_upper_alphabet.index(text[j]) - k) % len(rus_upper_alphabet)]
        else:
            new_text += text[j]
    print(new_text)
    
# Если шифрование и английский язык
elif way.lower() == 'шифрование' and language.lower() == 'английский':
    for n in range(len(text)):
        if text[n].isalpha() and text[n].islower():
            new_text += eng_lower_alphabet[(eng_lower_alphabet.index(text[n]) + k) % len(eng_lower_alphabet)]
        elif text[n].isupper() and text[n].isalpha():
            new_text += eng_upper_alphabet[(eng_upper_alphabet.index(text[n]) + k) % len(eng_upper_alphabet)]
        else:
            new_text += text[n]
    print(new_text)
    
    # Если дешифрование и английский язык
elif way.lower() == 'дешифрование' and language.lower() == 'английский':
    for m in range(len(text)):
        if text[m].isalpha() and text[m].islower():
            new_text += eng_lower_alphabet[(eng_lower_alphabet.index(text[m]) - k) % len(eng_lower_alphabet)]
        elif text[m].isupper() and text[m].isalpha():
            new_text += eng_upper_alphabet[(eng_upper_alphabet.index(text[m]) - k) % len(eng_upper_alphabet)]
        else:
            new_text += text[m]
    print(new_text)











# Заголовок
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Считываем данные
text = input().split(' ')
new_text = ''
count = 0
    
for i in range(len(text)):
    word = text[i]
    for letter in range(len(word)):
        if word[letter].isalpha():
            count += 1
        k = count
        if letter == len(word) - 1:
            for j in range(len(word)):
                if word[j].isalpha() and word[j].islower():
                    new_text += eng_lower_alphabet[(eng_lower_alphabet.index(word[j]) + k) % len(eng_lower_alphabet)]
                elif word[j].isupper() and word[j].isalpha():
                    new_text += eng_upper_alphabet[(eng_upper_alphabet.index(word[j]) + k) % len(eng_upper_alphabet)]
                else:
                    new_text += word[j]
            count = 0
            new_text += ' '
print(new_text)