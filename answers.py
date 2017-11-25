#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

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