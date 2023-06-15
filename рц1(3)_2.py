class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        if is_good_employee.lower() == 'false':
            is_good_employee = False
        elif is_good_employee.lower() == 'true':
            is_good_employee = True
        else:
            is_good_employee = None
        self.is_good_employee = is_good_employee

    def get_info(self):
        return f'У {self.name} зарплата в месяц {self.salary} рублей. В отпуске? - {self.on_vacation}'


empoyees = [Employee('Антон', 20000, 'да', is_good_employee=input('Хороший работник?')),
            Employee('Анастасия', 20000, 'да', is_good_employee=input('Хороший работник?')),
            Employee('Вика', 20000, 'да', is_good_employee=input('Хороший работник?')),
            Employee('Ольга', 20000, 'да', is_good_employee=input('Хороший работник?')),
            Employee('Иван', 20000, 'да', is_good_employee=input('Хороший работник?'))]

for i in empoyees:
    if i.is_good_employee == False:
        empoyees.remove(i)
        print(f'Yeah!!! {i.name} уволен!!!')
    else:
        print(i.get_info())
