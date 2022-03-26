def pluse (x,y):
    return x*y
print(2,3)

plus_lmb = lambda x,y: x*y
print(plus_lmb(2,3))
print(plus_lmb(4,6))


words = ['aplle', 'banana', 'telefone', 'name', 'hello','world']
a = list(filter(lambda  word:(word )==5, words))
print(a)
b = list(map(lambda  word: word.upper(), words))
print(b)

# example
numbers = [1,2,3,4,5,6,7,8,9,10]
ne4etnye_4isla = list(filter (lambda  x: x%2 ==1, numbers))
v_5_stepen = list(map(lambda  y: y**5, ne4etnye_4isla))
print(v_5_stepen)