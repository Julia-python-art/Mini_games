""" Автокорректор ошибок
На основе блокнота Яна Пиле, который перевел блокнот Питера Норвига, Google \ https://norvig.com/spell-correct.html """

import re #регулярные выражения
import math
from collections import Counter
import requests
from matplotlib import pyplot as plt

TEXT = requests.get('https://norvig.com/big.txt').text
print(len(TEXT))
print(TEXT[:90])
# 6488666
# The Project Gutenberg EBook of The Adventures of Sherlock Holmes by Sir Arthur Conan Doyle

# разбиваем текст на слова (токены) не учитываются слова с дефисами, цифры, слова повторяются
def tokens(text):
    return re.findall(r'[a-z]+',text.lower())

"""
проверяем работу функции
tokens('This is: A test, 1, 2, 3, this is.')
"""

WORDS = tokens(TEXT)
print(len(WORDS))
print(WORDS[:10])
# 1105285
# ['the', 'project', 'gutenberg', 'ebook', 'of', 'the', 'adventures', 'of', 'sherlock', 'holmes']

"""
Мешок слов (Bag of words)
В модели мешка слов полностью игнорируется порядок слов, зато соблюдается их частота. 
Смысл мешка слов: все слова текста сбрасываются в мешок и перемешиваются. 
Если достать случайные слова, предложение из них будет некорректным. 
Зато наиболее частые слова действительно будут встречаться наиболее часто, а редкие - реже. 
Реализация:
"""
import random
def sample(bag, n=10):
    return ' '.join(random.choice(bag) for _ in range(n))

sample(WORDS)
# 'which of father during the at in an his qui'

"""
Другое представление мешка слов - Counter. 
Это похож на словарь, состоящий из пар {'слово': кол-во вхождений слова в текст} 
Но у него есть много своих методов. Пример:
"""
COUNTS = Counter(WORDS)
print(COUNTS.most_common(10))

# [('the', 80030), ('of', 40025), ('and', 38313), ('to', 28766), ('in', 22050), ('a', 21155), ('that', 12512), ('he', 12401), ('was', 11410), ('it', 10681)]

# насколько часто встречаются слова из этого преложения в тексте?
for w in tokens('the rare and neverrbeforeseen words'):
    print(COUNTS[w], w)
    
print(len(COUNTS))

# 80030 the
# 83 rare
# 38313 and
# 0 neverrbeforeseen
# 460 words
# 29157

"""
В 1935, лингвист Джордж Ципф отметил, что в любом большом тексте n-тое наиболее часто встречающееся слово 
появляется с частотой ~(пропорционально) 1/n от частоты наиболее встречающегося слова. 
Это наблюдение называется Закон Ципфа. 
Если нарисовать частоты слов, начиная от самого часто встречающегося, на log-log-графике, 
они должны приблизительно следовать прямой линии.
"""

# логарифмируем обе части выражения
M = COUNTS['the']
plt.yscale('log')
plt.xscale('log')
plt.title('Частота n-того наиболее частого сллва и линия 1/n.')
plt.plot([c for(w,c) in COUNTS.most_common()])
plt.plot([M/i for i in range(1,len(COUNTS))])

"""
Задача проверки правописания
Letter insertion - вставка лишней буквы 
Letter omission - пропуск буквы 
Letter substitution - замена буквы 
Transposition - переставление букв местами 
Compounding - склеивание слов 
Apostrophe - неверная постановка апострофа

Задача: для данного слова нужно найти наиболее вероятную правку c = correct(w) 
Применим наивный подход: всегда будем брать более близкое слово, если проверки на близость недостаточно, 
берем слово с максимальной частотой из WORDS. 
Близость можно измерить с помощью Расстояния Левенштейна: минимального необходимого количества удалений, 
перестановок, вставок и замен символов, необходимых чтобы одно слово превратилось в другое. 
Методом проб и ошибок можно понять, что поиск слов в пределах расстояния 2 уже даст достойные результаты. 
Остается определить функцию c = correct(w) :
"""
def correct(word):
    #предрассчитать edit_distance==0, затем 1, затем 2, иначе: оставить слово "как есть"
    candidates = (known(edits0(word)) or
                  known(edits1(word)) or
                  known(edits2(word)) or
                   [word])
    return max(candidates, key=COUNTS.get)
    
# Функция edits1(word) должна возвращать множество слов, находящихся на расстоянии edit_distance==1.

def edits1(word):
    pairs      = splits(word)
    deletes    = [a+b[1:]            for (a,b) in pairs if b]
    transposes = [a+b[1]+b[0]+b[2:]  for (a,b) in pairs if len(b)>1]
    replaces   = [a+c+b[1:]          for (a,b) in pairs for c in alphabet if b]
    inserts    = [a+c+b              for (a,b) in pairs for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def splits(word):
    return [(word[:i], word[i:])
            for i in range (len(word)+1)]

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def known(words):
    # Вернуть подмножество слов, которое есть в нашем словаре
    return {w for w in words if w in COUNTS}

def edits0(word):
    # Вернуть все строки, которые находятся на edit_distance== 0 от word (т.е само слово)
    return {word}

def edits2(word):
    # Врнуть все строки, которые находятся на edit_distance== 2 от word
    return {e2 for e1 in edits1(word) for e2 in edits1(e1)}
    
splits('pencil')
# [('', 'pencil'),
# ('p', 'encil'),
# ('pe', 'ncil'),
# ('pen', 'cil'),
# ('penc', 'il'),
# ('penci', 'l'),
# ('pencil', '')]

print(edits1('wird'))
print(len(edits1('wird')))
print(len(edits2('wird')))

tokens('Speling errurs in somethink. Whutever; ususuel misteakes everyware?)')
list(map(correct, tokens('Speling errurs in somethink. Whutever; ususuel misteakes everyware?)')))

# давайте возвращать слово в регистре в котором оно встретилось
def correct_text(text):
    return re.sub('[a-zA-Z]+', correct_match, text)

def correct_match(match):
    word = match.group()
    return case_of(word)(correct(word.lower()))

# возвращает функцию, преобразовывающую слово в определенный регистр
def case_of(text):
    return (str.upper if text.isupper() else
            str.lower if text.islower() else
            str.title if text.istitle() else
            str)
            
list(map(case_of,['UPPER','lower','Title','CamelCase']))
correct_text('Speling Errurs IN somethink. Whutever; ususuel misteakes?')

"""
Теория: От счетчика слов к вероятностям последовательностей слов
Нам нужно научиться подсчитывать вероятности слов,P(w). 
Делать это будем с помощью функции pdist, которая на вход принимает Counter(мешок слов) и возвращает функцию, 
выполняющую роль вероятностного распределения на множестве всех возможных слов.
"""

def pdist(counter):
    "Превращает частоты из Counter в вероятностное распределение"
    N = sum(list(counter.values()))
    return lambda x: counter[x]/N

P=pdist(COUNTS)

for w in tokens('"The" is the most common word in English'):
    print(P(w),w)

"""
Модель мешка слов подразумевает, что каждое слово из мешка достается независимо от других. 
Чтобы посчитать вероятности P(w_1...w_n), обозначим его Pwords.
"""

def Pwords(words): 
    #вероятности слов при условии что они независимы
    return product(P(w) for w in words)

def product(nums):
    #перемножим числа
    result = 1
    for x in nums:
        result*=x
    return result
    
tests = ['this is a test',
         'this is an unusual test',
         'this is a neverbeforeseen test']

for test in tests:
    print(Pwords(tokens(test)),test)
 
""" 
Задача Разбиения слов на сегменты
Разбить полученную последовательность символов без пробелов на последовательность слов
1. Перенумеруем все возможные разбиения и выберем то, у которого максимальная Pwords Как выбрать кол-во сегментов для строки длины n?
2. Делаем одно разбиение: на первое слов и все остальное. 
Если предположить, что слова независимы, то можно максимизировать вероятность первого слова + лучшего разбиения оставшихся букв.
assert segment('choosespain') == ['choose', 'spain'] segment('choosespain') == max(Pwords(['c'] + segment('hoosespain')), 
Pwords(['ch'] + segment('oosespain')), Pwords(['cho'] + segment('osespain')), Pwords(['choo'] + segment('sespain')), ... Pwords(['choosespain'] + segment('')))

Чтобы это было эффективным, нужно избежать избыточного пересчета оставшейся части слова. 
Это можно сделать с помощью динамического программирования или мемоизации (кэширования). 
Кроме того, можно установить максимальную длины и не брать все возможные варианты разбиений для первого слова. 
Максимальная длина должна быть чуть больше, чем длина самого длинного слова, которое мы видели.
"""
def memo(f):
    """ Запомнить результаты исполнения функции f, чьи аргументы args должны быть хешируемыми """
    cache = {}
    def fmemo(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    fmemo.cache = cache
    return fmemo

max(len(w) for w in COUNTS)

def splits(text, start=0, L=20):
    "Вернуть список всех пар (a, b); start <= len(a) <= L"
    return [(text[:i], text[i:])
           for i in range(start, min(len(text), L) + 1)]
           
print(splits('word'))
print(splits('reallylongtext', 1, 4))

@memo
def segment(text):
    """ Вернуть список слов, который является наиболее вероятной сегментацией нашего текста """
    if not text:
        return []
    else:
        candidates = ([first] + segment(rest)
                     for (first, rest) in splits(text, 1))
        return max(candidates, key=Pwords)        
        
segment('choosespain')
# ['choose', 'spain']

segment('speedofart')
# ['speed', 'of', 'art']

decl = ('wheninthecourseofhumaneventsitbecomesneccesaryforpeople' +
        'todissolvethepoliticalbandswhichhaveconnectedthemwithoneanother' +
        'andtoassumeamongthepowersoftheearththeseparateandequalstation' +
       'towhichthelawsofnatureandofnaturesgodentitlethem')
print(segment(decl))

Pwords(segment(decl))
# 5.013917503097498e-163

Pwords(segment(decl * 2)) 
""" Возникла проблема переполнения разрядности числа """
# 0.0

segment('smallandinsignificant')
# ['small', 'and', 'insignificant']

segment('largeandinsignificant')
# ['large', 'and', 'insignificant']

print(Pwords(['small', 'and', 'insignificant']))
# 4.485957977672864e-10

print(Pwords(['large', 'and', 'insignificant']))
# 4.111418791681202e-10

print(Pwords(['large', 'and', 'in', 'significant']))
# 1.0662753919897733e-11