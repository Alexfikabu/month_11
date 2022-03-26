univer = []
tehnikum = []
army = []
zamuj = []
abiturient = [
    {'name': 'Radomir', 'ORT':110, 'gender': 'male'},
    {'name': 'Alex', 'ORT':110, 'gender': 'male'},
    {'name': 'denis', 'ORT':90, 'gender': 'male'},
    {'name': 'islam', 'ORT':80, 'gender': 'male'},
    {'name': 'victoria', 'ORT':110, 'gender': 'female'},
    {'name': 'masha', 'ORT':150, 'gender': 'female'},
    {'name': 'Angelina', 'ORT':140, 'gender': 'female'},
    {'name': 'alexei', 'ORT':0, 'gender': 'male'},
    {'name': 'Vlad', 'ORT':0, 'gender': 'male'},
    {'name': 'olga', 'ORT':0, 'gender': 'female'}
]

def all_abit(lst):
    for i in lst:
        for k, v in i.items():
            print(f'{k}-{v}')
            print('')

all_abit(abiturient)

def selection(lst,univer:list, tehnikum:list,army:list,zamuj:list):
    for i in lst:
        if i['ORT'] >=110:
            univer.append(i)
        elif i['ORT']<=100 and i['ORT']>=45:
            tehnikum.append(i)
        elif i['ORT'] <=45 and i['gender'] == 'male':
            army.append(i)
        elif i['ORT'] <45 and i['gender'] == 'female':
            zamuj.append(i)
selection(abiturient,univer,tehnikum,army,zamuj)
print(f'VUNIVER {univer}')
print(f'TEHNIKUM{tehnikum}')
print(f'Armiu{army}')
print(f'ZAMUJ{zamuj}')