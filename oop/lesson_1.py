# class Person:
#     def __init__(self, name, age, gender,height, hobby):
#         if isinstance(name,str):
#             self.name = name
#         else:
#             raise ValueError('name shoudle be str')
#
#
#         if isinstance(age,int):
#             self.age =age
#         else: ValueError('age should be int')
#
#
#         if isinstance(age,int):
#             self.gender = gender
#         else:
#             raise ValueError('age shoudle be str')
#
#         if isinstance(height,float):
#             self.height = height
#         else:
#             raise ValueError('name shoudle be float')
#
#         if isinstance(hobby,bool):
#             self.hobby = hobby
#         else:
#             raise ValueError('hobby shoudle be bool')
#
#     def 123(self):
#         return f'my name is {self.name()}'
#     def age_yu(self):
#         return f'i am {self.age}'
#
#
#
#     def __str__(self):
#         return f'Name:{self.name}\n' \
#                f'Age:{self.age}\n' \
#                f'Gender:{self.gender}\n' \
#                f'Height:{self.height}\n' \
#                f'Hobby:{self.hobby}\n'
#
# human1 = Person(name='Alexandr', age=32, gender='male', height=193.2, hobby=True)
# print(f'{human1}')
#
# human2 = Person(name='Vasya', age=25, gender= 'male', height =255.21, hobby=False)
# print(human2)
# print(human1.123())

# создать класс whotch
class  Whatch:
    def __init__(self,color, type, size,):
     if isinstance(color, str):
         self.color = color
     else:
         raise ValueError('color must be str')
     if isinstance(type,bool):
         self.type =type
     else:
         raise ValueError('type must be bool')
     if isinstance(size,int):
         self.size = size
     else:
         raise ValueError('type must be int')

    def __str__(self):
        return f'color{self.color}\n' \
                f'type{self.type}\n' \
                f'size{self.size}'

whatch1 = Whatch(color='red',type=True,size=25)
print(whatch1)