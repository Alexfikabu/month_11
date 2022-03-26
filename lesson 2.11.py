coca_cola =25
cola_05l = 0
cola_1l = 0
cola_15l =0
while coca_cola != 0:
    coca_cola -=1
    answer =int( input('Какой литр 1-05'))
    if answer  == 1:
        cola_05l +=1
    elif answer ==2:
        cola_1l +=1
    elif answer ==3:
        cola_15l +=1
    else:
        break























# enter_number = int(input('Zagadaite chislo ot1 do 100'))
# left = 0
# right = 101
# attemps = 0
# while 1:
#     result =(right + left)//2
#     attemps +=1
#     print (f'POPYTKI {attemps}')
#     print(f'компьютер сказал число {result}')
#     if result == enter_number:
#         print('Uraa ')
#         break
#     elif result > enter_number:
#         right = result
#     elif result < enter_number:
#         left = result
# print (f'Количество всех попыток {attemps}')