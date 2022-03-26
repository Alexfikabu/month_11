class Knopka1:
    def __init__(self,test):
        self.test = test
    def pusk(self):
        return f'Нажимает кнопку старт \n'
class Knopka2:
    def __init__(self,test):
        self.test2 = test
    def pusk(self):
        return f'Нажимает прыжок\n'
class Knopka3:
    def __init__(self, test):
        self.test3 = test
    def pusk(self):
        return f'Показывает счет\n'
enter = Knopka1(test='СТАРТ')
space = Knopka2(test='ПРЫЖОК')
esq = Knopka3(test='СЧЕТ')
print(enter.pusk(),space.pusk(),esq.pusk())
