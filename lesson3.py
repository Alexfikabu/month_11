data_types =['name', 1, 2, 5.5,34.55, 'Hellow', 'world', True, False ]
print(f'Our list - {data_types}')
# metod peremesheniya mejdu spiskami
data_types2 =[]
data_types2.append(data_types.pop(0))
data_types2.append(data_types.pop(5))
data_types2.append(data_types.pop(6))
print(f'1spis{data_types}')
print(f'2spis{data_types2}')

# Merod obnovleniya
data_types[2] = 3.0
data_types[3] = 4.0
data_types[4] = 5.0
print(data_types)

# рачсширение списка списком
data_types.extend(data_types2)

# metod vyvoda cherez index
print(data_types[5])




#
# data_types =['name', 1, 2, 5.5,34.55, 'Hellow', 'world', True, False ]
# print(f'Our list - {data_types}')
#
# data_types.append('good morning')
# data_types.insert(6,'Alexanndr')
#
# print(f'dobavili{data_types}')
# # udalenie
# # data_types.clear()
# print(f'data clear {data_types}')
# data_types.remove('Hellow')
# del data_types[0]
# print(f'index delete{data_types}')
#
