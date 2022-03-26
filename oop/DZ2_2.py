# задача 1
class Knop_tel():
    def __init__(self, zvonok, sms, knopki):
        self.zvonok = zvonok
        self.sms = sms
        self.knopki = knopki
    def zmeika(self,igra_zmeika):
        return f'Игра змейка  {igra_zmeika}'
    def __str__(self):
        return f'Может звонить   -  {self.zvonok}\n'\
               f'Отправка СМС   {self.sms}\n'\
               f'Количество кнопок {self.knopki}'

nokia1100 = Knop_tel(zvonok= True,sms='T9',knopki=10)
print(nokia1100.zmeika('Отличная игра тех лет'))
print(nokia1100)
print('*'*50)

class Sensor_tel(Knop_tel):
    def __init__(self, zvonok, sms, knopki, sensor, kamera):
        super().__init__(zvonok, sms, knopki)
        self.sensor = sensor
        self.kamera = kamera
    def video(self,kachestvo):
        return f'Возможность снимать видео  {kachestvo}'
    def __str__(self):
        return super(Sensor_tel, self).__str__()+ f'Сенсорный экран  {self.sensor}\n'\
                                                  f'Наличие камеры   {self.kamera}\n'
lumia = Sensor_tel(zvonok=True,sms='sensornyi vvod',knopki=10,sensor='2 kasaniya',kamera='2MP')
print(lumia.video('не очень'))
print(lumia)
print('*'*50)


class Android(Sensor_tel):
    def __init__(self,zvonok, sms, knopki, sensor, kamera, internet,):
        super(Android, self).__init__(zvonok, sms, knopki, sensor, kamera)
        self.internet = internet
    def instagram(self):
        return f'Переписка в инстаграмме  {nokia1100}'
    def __str__(self):
        return super(Android, self).__str__() +f'Интернет 4G  {self.internet}'
xiaomi = Android(zvonok= True,sms='golosovoi vvod',knopki=3,sensor='do 5 kasanii',kamera='12MP',internet='WIFI')
print(xiaomi.instagram())
print(xiaomi)
