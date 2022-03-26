data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3,'e', 1,'g')
letters = []
numbers = []
for i in data_tuple:
    if type (i) == str:
        letters.append(i)
    else:
        numbers.append(i)
numbers.remove(6.13)
numbers.pop(0)
numbers.insert(3, True)
numbers.insert(1, 2)
del numbers[3]
numbers.reverse()
letters.reverse()
letters.insert(0,True)
letters[1] = 'G'
letters[-2] = 'c'
letters_tup = tuple(letters)
numbers_tup = tuple(numbers)
print(letters_tup)
print(numbers_tup)
# не разобрался как G большую сделать
numbers 