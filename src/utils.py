import json
import pickle

from src.menu import menu_website
from src.vacancy import WorkingWithVacancy, show_vac, constructor_vac


class ParsingError(Exception):
    """Класс для вывода ошибки"""

    def __str__(self):
        return 'Ошибка получения данных'


class SaveJson:
    """Сохраняет данные по вакансиям в json файл и считывает"""
    def __init__(self, file):
        self.file = file

    def save_json(self):
        with open('all_vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(self.file, f, indent=2, ensure_ascii=False)


def load_json():
    """Выгружает json файл в работу"""
    with open('all_vacancies.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def load_data():
    with open('selected_vacancies.dat', 'rb') as input_file:
        contact_dct = pickle.load(input_file)
    return contact_dct


def choice_website():
    while True:
        choice_hh = menu_website()
        if choice_hh == 1:
            vac = constructor_vac(load_json())
            selected_vac = show_vac(vac)
            WorkingWithVacancy(selected_vac).add_vacancies_to_file()
        elif choice_hh == 2:
            print(f'ИЗБАННОЕ: выбрано вакансий - {len(load_data())}')
            print(end=f'{"-" * 100}\n')
            n = 0
            for i in load_data():
                n += 1
                print(f'{n} Вакансия\n{i}')
        elif choice_hh == 3:
            break
        elif choice_hh == 4:
            exit()
        else:
            print('Неверное значение. Повторите набор.')
            continue