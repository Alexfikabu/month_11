borsh = {'мясо', 'капуста', 'свекла', 'картошка', 'специи',
         'лук', 'сметана'}
lagman = {'мясо','лапша', 'специи', 'лук', 'редька', 'джусай'}

# находит похожее значение
print(lagman.intersection(borsh))
print(lagman&borsh)

# вывод микс значений
print(lagman.union(borsh))
print((lagman|borsh))

# Различия
print(lagman.difference(borsh))
print(lagman-borsh)
#  по одиночке не одинаковых
print(lagman.symmetric_difference(borsh))
print(lagman^borsh)

list1 = [1,2,2,2,3,4,8,5,6,5,4,78,89,5,6,2]
list_set = set(list1)
print(list_set)
















# nominal = [1, 3, 5, 10, 20, 50, 100, 200, 500, '1k', '2k','5k' ]
# person = ['nothing', 'nothing','nothing','nothing','Togolok','Datka',
#           'satylganov', 'osmonov', 'karalaev', 'balasagyn', 'chokmorov', 'burana' ]
# banknots =dict(zip(nominal, person))
#
# del banknots[1]
# del banknots[3]
# del banknots[5]
# del banknots[10]
# for i,j in banknots.items():
#     print(f'{i}-{j}')