kolvo = 45
horoshee = 0
plohoe = 0
print(f'Рассортируйте яблоки {kolvo} шт.\n Наберите 1 если яблоко хорошее\n Наберите 2 если яблоко плохое\n')
# a = int(input())
while kolvo != 0:
    a = int(input())
    kolvo -= 1
    if a == 1:
        horoshee += 1
        print(f'Осталось яблок {kolvo} шт.\n Плохих яблок {plohoe} шт.\n Хороших яблок {horoshee}\n')
    elif a == 2:
        plohoe += 1
        print(f'Осталось яблок {kolvo} шт.\n Плохих яблок {plohoe} шт.\n Хороших яблок {horoshee}\n')
    else:
        # a = int(input(f'Повторите ввод 1 - Хороше, 2- Плохое\n'))?????
        print('jhgsdhgd')
        continue