from random import randint
import datetime
name = str(input('kak zvat'))
attempts = 0
attempts = int(input('сколько попыток?')
start = datetime.datetime.now()

while 1:
    num1 = randint(1,9)
    num2 = randint(1,9)
    action = num1*num2
    print(f'Сколько будет{num1}*{num2} = ?',)
    result =int (input())
    attempts-= 1

    if attempts == 0:
        print(f'ИМЯ{name}\n'
            f'Время{datetime.datetime.now()-start}\n'
            f'Количество попыток{attempts}')
        break

