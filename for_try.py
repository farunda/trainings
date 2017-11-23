'''
Цикл
    Создать список из десяти целых чисел.
    Вывести на экран каждое число, увеличенное на 1.
'''

ten_digits_list = [3, 14, 15, 926, 535, 89, 79, 32, 38, 46]
for digit in ten_digits_list:
    print(digit + 1)

'''
Цикл
    Ввести с клавиатуры строку.
    Вывести эту же строку вертикально: по одному символу на строку консоли.
'''

string_1 = input("Please, enter some text here: ")
for character in string_1:
    print(character)

'''
Оценки
    Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
    Посчитать и вывести средний балл по всей школе.
    Посчитать и вывести средний балл по каждому классу.
'''

classes_list = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '8b', 'scores': [5,4,4,5,4]},
                {'school_class': '6c', 'scores': [2,4,3,5,5]},
                {'school_class': '5a', 'scores': [4,4,4,4,3]},
                {'school_class': '7b', 'scores': [2,2,3,5,4]},
               ]

total = []

for clas in classes_list:
    clas_total = clas.get('scores')
    total = total + clas_total

scores_qty = len(total)
scores_sum = sum(total)
print('The average score in school is', scores_sum / scores_qty)

for clas in classes_list:
    clas_total = clas.get('scores')
    class_scores_qty = len(clas_total)
    class_scores_sum = sum(clas_total)
    avg_score = class_scores_sum / class_scores_qty
    print('The average score in the class', clas.get('school_class'), 'is', avg_score)

'''
изящное решение от Саши Телкова
for clas in classes_list:
    total += clas['scores']
    print(total)
'''