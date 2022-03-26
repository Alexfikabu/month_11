italia =[]
russia = []
france = []
japon = []
sport =[]
auto = [
    {'marka':'BMW', 'country': 'ge', 'type_car': 'old'},
    {'marka': 'Toyota', 'country': 'jp', 'type_car': 'modern'},
    {'marka': 'Toyota', 'country': 'jp', 'type_car': 'sport'},
    {'marka': 'Lexus', 'country': 'us', 'type_car': 'modern'},
    {'marka': 'Ferrary', 'country': 'it', 'type_car': 'sport'},
    {'marka': ' Lada ', 'country': 'rus', 'type_car': 'old'},
    {'marka': 'Peugeot', 'country': 'fr', 'type_car': 'old'},
    {'marka': 'Subaru', 'country': 'jp', 'type_car': 'sport'},
]


def vybor(lst, italia: list, russia: list, france: list, japon:list, sport:list):
    for i in lst:
        if i['country'] == 'it':
            italia.append(i)
        elif i['country'] == 'rus':
            russia.append(i)
        elif i['country'] == 'fr':
            france.append(i)
        elif i == 'jp':
            japon.append(i)
        elif i['type_car'] == 'sport':
            sport.append(i)
vybor(auto,italia,russia,france,japon,sport)
print(f'Итальянские машины - {italia}')
print(f'Российские машины - {russia}')
print(f'Французские машины - {france}')
print(f'Японские машины - {japon}')
print(f'SPORT_CAR - {sport}')