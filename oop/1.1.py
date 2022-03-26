class Car:
    def __init__(self, brand, speed, color, cost, transmission):
        self.brand = brand
        self.speed = speed
        self.color = color
        self.cost = cost
        self.t = transmission
    def tuning(self,cost_tuning):
            self.cooost = cost_tuning+self.cost
            return f'tsena{self.cooost}'

    def __str__(self):
        return f'Brand:{self.brand}\n'\
                f'speed{self.speed}\n'\
                f'color{self.color}\n'\
                f'cost{self.cost}$\n'\
                f'korobka{self.t}\n'

car1 = Car(brand='BMW',speed= 220,color='red',cost=2200,transmission='automat')
print(car1)

class Electric(Car):
        def __init__(self, brand, speed, color, cost, transmission,fuel, date):
            super().__init__(brand, speed, color, cost, transmission)
            self.fuel = fuel
            self.date =date
        def __str__(self):
            return super(Electric, self).__str__()+ f'toplivo:{self.fuel}\n' \
                                                    f'god{self.date}'
electric1 = Electric(brand='tesla',speed=400, color='grey',cost=10000,transmission='robot',fuel='electric', date= 2222)
print(electric1)
electric2 = Electric('tesla', 300, 'red', 5500, 'robot','benzin', 3030)
print('+'*30)
print(electric2)