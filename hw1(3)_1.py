class Employee:
    def __init__(self, name, salary, on_vacation):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation

    def get_info(self):
        return f'У {self.name} зарплата в месяц {self.salary} рублей. В отпуске? - {self.on_vacation}'


empoyees = [Employee(name=input('Как зовут работника?'), salary=int(input('Какая у него зарплата?')),
                     on_vacation=input('Работник в отпуске?')),
            Employee(name=input('Как зовут работника?'), salary=int(input('Какая у него зарплата?')),
                     on_vacation=input('Работник в отпуске?')),
            Employee(name=input('Как зовут работника?'), salary=int(input('Какая у него зарплата?')),
                     on_vacation=input('Работник в отпуске?'))]

for empoyee in empoyees:
    print(empoyee.get_info())
