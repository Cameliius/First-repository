# class Year:
#     def __init__(self, days, season):
#         self.__days = days  # кол-во дней
#         self.__season = season
#
#     @property
#     def days(self):
#         return self.__days
#
#     @property
#     def season(self):
#         return self.__season
#
#     @days.setter
#     def days(self, days):
#         if days not in [365, 366]:
#             raise ValueError('В году не может быть столько дней.')
#
#         self.__days = days
#
#     @season.setter
#     def season(self, season):
#         if season not in ['весна', 'осень', 'зима', 'лето']:
#             raise ValueError('Такого времени года не существует')
#
#         self.__season = season
#
#
# year = Year(366, 'весна')
#
# year.days = 365
# year.season = 'лето'
# print(year.season)
# print(year.days)

# year2 = Year2(364, 'весна')
#
# year2.days = 366
# year2.season = 'лето'
# print(year2.season)
# print(year2.days)


#     def get_days(self):
#         return self.__days
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Некорректное значение')
#
# year = Year(365, 'весна')
#
# year.set_days(366)
#
# print(year.get_days())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError('Вы ещё не родились')

    @name.deleter
    def name(self):
        del self.__name

    @age.deleter
    def age(self):
        del self.__age

person = Person('Иван', 5)
print(person.name)
print(person.age)
person.name = 'Данил'
person.age = 6
print(person.name)
print(person.age)

del person.age
del person.name

print(person.age)
print(person.name)
