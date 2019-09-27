# Имеется класс Гражданин, у которого определены следующие свойства: Имя,
# Фамилия, Отчество, год рождения; и функции: ввода данных (можно использовать
# конструктор), вывода (ФИО, возраст). Создать дочерний класс Студент, для
# которого помимо указанных данных родительского класса запрашиваются данные:
# место учебы, номер группы. Предусмотреть вывод (ФИО, возраст, Место учебы,
# номер группы).

from dataclasses import dataclass


@dataclass
class Citizen():
    name: str
    surname: str
    patronymic: str
    year_of_birth: int

    def __repr__(self):
        return "Name: {} {} {}\nAge: {}".format(
            self.name, self.surname,
            self.patronymic, 2019 - self.year_of_birth
        )


@dataclass
class Student(Citizen):
    place_of_study: str
    group_num: int

    def __repr__(self):
        return super().__repr__() + "\nStudy: {}\nGroup: {}".format(
            self.place_of_study, self.group_num)


student = Student(
    name="Kotori",
    surname="Minami",
    patronymic="-",
    year_of_birth=1994,
    place_of_study="Otonokizaka High School",
    group_num=1
)

print(student)
