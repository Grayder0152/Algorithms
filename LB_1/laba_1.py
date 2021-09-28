import datetime
import random

import faker

fake = faker.Faker()


class Employee:
    GENDER = ('Male', 'Female')

    def __init__(self, full_name: str = None, birth_day: datetime.date = None, gender: str = None):
        self.full_name: str = full_name
        self.__birth_day: datetime.date = birth_day
        self.gender: str = gender

    def __repr__(self):
        return f'{self.full_name}'

    @property
    def birth_day(self):
        if self.__birth_day is not None:
            return self.__birth_day.strftime('%d:%m:%Y')

    @birth_day.setter
    def birth_day(self, bd: datetime.date):
        self.__birth_day: datetime.date = bd

    def generate_fake_employee(self):
        self.gender = random.choice(self.GENDER)
        self.full_name = fake.name_male() if self.gender == 'Male' else fake.name_female()
        self.birth_day = fake.date_of_birth()

    def input_employee(self):
        self.full_name = input("Type full name: ")
        self.gender = input(f"Type gender({'/'.join(self.GENDER)}): ")
        bd = input("Type birth_day(day:month:year): ").split(':')
        self.birth_day = datetime.date(*map(int, bd[::-1]))

    def print_all_info(self):
        print(
            f"Full name: {self.full_name}\n"
            f"Birth day: {self.birth_day}\n"
            f"Gender: {self.gender}\n"
        )


if __name__ == '__main__':
    employees = []
    for i in range(1, 3):
        print(f"-------Generate {i} employee-------")
        employee = Employee()
        employee.input_employee()
        employees.append(employee)
        employee.print_all_info()
    male_employees = list(filter(lambda empl: empl.gender == 'Male', employees))

    print(male_employees)
