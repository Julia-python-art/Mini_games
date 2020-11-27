from random import *
word_list = ['сода', 'времяпровождение', 'тюлень', 'попугай', 'решетка', 'улитка', 'раковина', 'воспоминание', 'свитер', 'фантазер', 'мята', 'возвышенность', 'напряженность', 'парашютист', 'барбекю', 'перпендикуляр', 'скоросшиватель', 'блокнот', 'анимация']
def get_word():
    word = choice(word_list).upper()
    return word
def display_hangman(tries):
    stages = [  # финальное состояние: голова, туловище, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, туловище, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, туловище, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, туловище и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и туловище
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давай играть в виселицу!')
    print(display_hangman(tries))
    print('Загаданное слово', word_completion)
    print('Количество букв равно', len(word))
    while True:
        print('Введи букву или слово')
        letter = input().upper()
        if not letter.isalpha():
            print('Ты ошибся, введи букву или слово')
            continue
        else:    
            if letter in guessed_letters or letter in guessed_words:
                print('Уже было, попробуй еще')
                continue
            else:
                if len(letter) > 1 and letter == word:
                    guessed_words += letter
                    print('Ураааа, ты угадал!')
                    print('Хочешь сыграть еще раз?')
                    answer = input().lower()
                    if answer == 'да':
                        play(get_word()).upper()
                    else:
                        print('Еще увидимся!')
                        break
                elif len(letter) > 1 and letter != word:
                    guessed_words += letter
                    tries -= 1
                    print('Не верно, осталось попыток: {}'.format(tries))
                    print(display_hangman(tries))
                    print(word_completion)
                    if tries == 0:
                        print('Ты програл, попыток: 0. Загаданное слово:', word)
                        break
            if len(letter) == 1:    
                if letter in word and letter not in guessed_letters:
                    print('Ты угадал букву!')
                    word1 = word
                    for _ in range(len(word)):
                        ind = word.find(letter)
                        word_completion = word_completion[:ind] + letter + word_completion[ind + 1:]
                    print(word_completion)
                    guessed_letters += letter
                else:
                    guessed_letters += letter
                    tries -= 1
                    print('Не верно, осталось попыток: {}'.format(tries))
                    print(display_hangman(tries))
                    print(word_completion)
                    if tries == 2:
                        print('Хочешь дам подсказку?')
                        answer1 = input().lower()
                        if answer1 == 'да' and word_completion[0] == '_':
                            print('Первая буква:', word[0])
                    if tries == 0:
                        print('Ты програл, попыток: 0. Загаданное слово:', word)
                        break
                continue

play(get_word().upper())