'''
Задание
    Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()
    Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
    Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
    При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”
'''

valera_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
'''
# первое, что пришло в голову:

while True:
    current_name = list.pop(valera_list)
    #Проверяем все имена
    print(current_name)
    if current_name == 'Валера':
        print('Валера нашёлся!')
        break

# по подсказке от Саши работать через длину списка, чтобы не было ошибки,
# если заданного элемента нет в списке:

while len(valera_list) > 0:
    current_name = list.pop(valera_list)
    #Проверяем все имена
    print(current_name)
    if current_name == 'Валера':
        print('Валера нашёлся!')
        break
'''

def find_person(name, a_list):
    while len(a_list) > 0:
        current_name = list.pop(a_list)
        print(current_name)
        if current_name == name:
            print(name + ' тут!')
            break
# немножко творчества
print(valera_list)
name_request = input('^^^^^ Введите имя, кого ищем в списке выше ^^^^^ ? ').capitalize()
find_person(name_request, valera_list)

def ask_user():
    answer = input("Как дела? ").capitalize()
    return answer

def get_answer():
    while True:
        answer = ask_user()
        if answer == 'Плохо':
            print("Не расстраивайся")
        elif answer == 'Хорошо':
            print("Уже лучше!")
        elif answer == 'Отлично':
            print("Это не может не радовать!")
        elif answer == 'Пока':
            print("Ну, до скорого")
            break
        else:
            print("Не понимаю, повторите еще раз")

get_answer()




















