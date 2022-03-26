class Vypusknic:
    def __init__(self, shkola, bally_ort, gender):
        self.sh =   shkola
        self._bally = bally_ort
        self.__gender = gender
    def name(self,name):
        return f'Имя    {name}'
    def __str__(self):
        return f'Школа №:  {self.sh}\n'\
               f'Баллы ОРТ:  {self._bally}\n'\
               f'Пол:   {self.__gender}'
student1 =Vypusknic(shkola=52,bally_ort=180,gender=True)

print(student1.name('Вася'))
print('*' *50)
print(student1.bally)
print('*' *50)
print(student1.__gender)