import pickle
from abc import ABC, abstractmethod


class WorkingVac(ABC):
    """Абстрактный класс для работы с вакансиями"""

    @abstractmethod
    def add_vacancies_to_file(self):
        pass

    @abstractmethod
    def get_data_by_criteria(self):
        pass


class WorkingWithVacancy(WorkingVac):
    """Класс для работы с вакансиями"""

    def __init__(self, vac):
        self.vac = vac  # список объектов класса Vacancy

    def add_vacancies_to_file(self):
        """Метод добавления данных в файл"""
        with open('selected_vacancies.dat', 'wb') as output_file:
            pickle.dump(self.vac, output_file)

    def get_data_by_criteria(self):
        """Метод получения данных из файла"""
        with open('selected_vacancies.dat', 'rb') as input_file:
            contact_dct = pickle.load(input_file)
        return contact_dct


class Vacancy:
    """Класс для создания объектов Вакансий"""
    __slots__ = ('name', 'firm', 'salary_from', 'salary_to', 'url', 'area')

    def __init__(self, name, firm, salary_from, salary_to, url, area):
        self.name = name
        self.firm = firm
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.area = area

    def __str__(self):
        self.salary_to = 'не указана' if self.salary_to == 0 else self.salary_to
        self.salary_from = 'не указана' if self.salary_from == 0 else self.salary_from
        return f'Название: {self.name}\n' \
               f'Фирма: {self.firm}\n' \
               f'Зарплата: от - {self.salary_from}, до - {self.salary_to}\n' \
               f'Город: {self.area}\n' \
               f'Эл. адрес: {self.url}\n'

    def __gt__(self, other):
        """Возвращает True если self больше"""
        return self.salary_from > other.salary_from


def constructor_vac(load_j):
    """Создает список экземпляров класса Vacancy"""
    vacancies = [Vacancy(line["name"], line["firm"], line["salary_from"],
                         line["salary_to"], line["url"], line["area"]) for line in load_j]

    return vacancies


def show_vac(const):
    select = []
    n = 0
    for i in const:
        n += 1
        print(f'{n} Вакансия\n{i}')
        if (n % 10) == 0:
            print('----------------------------')
            print('Выберите понравившиеся вакансии.\n'
                  'Что бы добавить в избранное, наберите их номера (через пробел).\n'
                  '"q" - закончить выбор, возврат в предыдущее меню.')
            choice = input('Ввод: ')
            choice_spl = choice.split()
            if choice == 'q':
                break
            else:
                print('----------------------------')
                for row in choice_spl:
                    select.append(const[int(row) - 1])
    return select
