class Mlecopitaushie():
    def __init__(self,razmer,kolvo_nog,strana_obitaniya):
        self.razmer = razmer
        self.kolvo = kolvo_nog
        self.strana = strana_obitaniya
    def __str__(self):
        return f'Размеры животного -- {self.razmer}\n\'' \
               f'Количество лап/ног -- {self.kolvo}\n'\
               f'Страна обитания -- {self.strana}\n'


slon = Mlecopitaushie(razmer='большой',kolvo_nog=4,strana_obitaniya='africa')
kenguru = Mlecopitaushie(razmer='средний',kolvo_nog=2,strana_obitaniya='Australia')
ej = Mlecopitaushie(razmer='маленький',kolvo_nog=4,strana_obitaniya='europe')

class Polzaushie():
    def __init__(self,kryliya,hhvost,sshupalcy):
        self.krliya = bool(kryliya)
        self.hvost = hhvost
        self.sh = sshupalcy
    def __str__(self):
        return f'Наличие крыльев --  {self.krliya}\n'\
               f'Наличие хвоста  --  {self.hvost}\n'\
               f'Наличие щупальцев  --  {self.sh}\n'

rak = Polzaushie(kryliya= 0,hhvost= 'нет',sshupalcy= 2 )
ulitka = Polzaushie(kryliya=0,hhvost='есть',sshupalcy='нет')
pchela = Polzaushie(kryliya=1,hhvost='есть',sshupalcy='нет')


class Animal(Mlecopitaushie):
    def __init__(self,razmer,kolvo_nog,strana_obitaniya,show,cena):
         super().__init__(razmer, show, cena)
         self.show = show
         self.cena = cena
    def __str__(self):
         return super(Animal, self).__str__() + f'Что умеет -- {self.show}\n'\
                                                f'Цена  -- {self.cena}\n'

slon_show = Animal(razmer='big',kolvo_nog=4,strana_obitaniya='Bishkek',show='POLET',cena=100)
print(slon_show)





# class Animal(Mlecopitaushie,Polzaushie):
#     def __init__(self:Mlecopitaushie(razmer,kolvo_nog,strana_obitaniya)Polzaushie(kryliya,hhvost,sshupalcy,show,cena):
#          super().__init__(razmer,kryliya, show,cena)
#          self.show = show
#          self.cena = cena
#     def __str__(self):
#          return super(Animal, self).__str__() + f'Цена билета -- {self.show}\n'\
#                                                 f'Что умеют  -- {self.cena}\n'
#
# slon_show = Animal(razmer='BIG',kolvo_nog=4,strana_obitaniya='Afrika',kryliya=0,hhvost='YES',sshupalcy='NET',show='LETAET',cena=100)
# print(slon_show)


