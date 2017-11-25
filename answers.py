'''
Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”,
пока он не ответит “Хорошо”
При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), 
пока он не скажет “Пока!”

плюс добавлена обработка keyboard interrupt в функции ask_user()
'''

answers = {'hi':'and you too!', 
           'how are you':'i\'m fine!',
           'bye':'bye-bye!'
          }

def get_answer(question, answers):
    answer = answers.get(question, 'try to ask me again!')
    return answer
    
def ask_user():
    while True:
        try:
            print('\n hi, i\'m bot, you can talk with me with next words: hi, how are you and bye. Any other words coming soon!')
            question = input().lower()
            print(get_answer(question, answers))
        except:
            KeyboardInterrupt
            print('\nYou pressed the Ctrl+C combination. See you later!')
            break

ask_user()