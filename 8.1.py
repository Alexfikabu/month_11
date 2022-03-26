from random import randint
from datetime import datetime
cash = 1000
    while cash > 0:
    start = datetime.now()
        try:
        bet =int(input(f'Доступно {cash}\n какую сумму хотите поставить? или нажмите 0 для выхода'))
         if bet ==0:
            print (f'Doswidaniya vash schet {cash}')
            break
    except:
        print('не пиши буквы пиши цифры!!!!')
        continue
    if bet>cash, or bet < 1:
        print(f'Ставка > 0 b меньше кэша')
        continue
    computer = randint(1,6)
    user = randint(1,6)

    elif computer>user
        print('ВЫ проиграли')
        cash -= bet
        with open('bone.txt','a',encoding='UTF-8')as game:
            game.write(f'V  K:{computer}, U:{user, ставка{bet}, Game ower остаток {cash}')

    else:
    computer < user
    print('ВЫ проиграли')
    cash = bet
    with open('bone.txt', 'a', encoding='UTF-8') as game:
        game.write(f'V  K:{computer}, U:{user, ставка{bet},DRAW остаток {cash}')

with open('bone.txt', 'a' enc)





# # чтение файла
# with open('file2.txt','r', encoding='UTF8') as text:
#
# # # добавление
# # with open('file2.txt','a') as text:
# #     name = input(f'name')
# #     text.write(f'{name},\n')
#
#









# # sozdanie
# with open('file2.txt','w') as text:
#     text.write(
#         input('what is you name')
#         )
#






# # zapis faila
# file = open('gymn.txt','r', encoding='UTF-8')
# print(file.read())
# file.close()