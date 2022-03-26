import time
myself = {
    'my adress': 'Toktogula',
    'my_hobby': ['Android', 'Python', 'Frontend'],
    'bag': {'fails', 'errors','stack'},
}
del myself['bag']
myself['my adress'] = 'Ahunbaev str.'
myself['email'] = 'alex@gmail.com'
myself['phone'] = 559139770
myself['my_hobby'] += ['job', 'painting', 'disain']
myself['my_hobby'] = tuple(myself['my_hobby'])
for i,j in myself.items():
    time.sleep(1)
    print (f'{i}-{j}')
