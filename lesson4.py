

auto = dict(brand = 'BMV', model = 'e34', color= 'black', volume=3.0)
print(auto)

# Добовление 2
auto.update(year = 1995)
print(auto)
# for key,value in auto.items():
#     print(f'{key}-{value }')
auto2 =auto.copy()
print(auto2)
# auto2.update(crash = True)
# print(auto2)
print(auto.keys)
print(auto.values())
# Получение значений через гет функцию
print(auto.get('brand'))
#
#
#
#
#
#
#
#
#
#
#
#
#
# # student = {
# #     'name' : 'John',
# #     'age' : 24,
# #     1997: 'Cow Year',
# #     'height': 1.80,
# #     'education': True,
# #     'hobby':['Guitar', 'Programing', 'Sleep']
# #
# # }
# # # Удаление из словаря
# # del  student [1997]
# # print(student)
# # print(student['hobby'][1])
# # # изменение значений в словаре
# # student['age'] = 25
# # print(student)
# #
# #
# #
# #
# # # # расширение словаря
# # # student['zp'] = 20000
# # # print(student)
