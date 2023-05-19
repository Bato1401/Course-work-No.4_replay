from src.classes_api import APIHeadHunter, APISuperJob
from src.menu import main_menu
from src.utils import SaveJson, load_data, choice_website


def main():
    while True:
        main_choice = main_menu()

        if main_choice == 1:  # Head Hunter
            print('Вы выбрали сайт Head Hunter')
            keyword_hh = input('Введите ключевое слово: ').title()
            hh = APIHeadHunter(keyword_hh).get_vacancies()
            SaveJson(hh).save_json()
            choice_website()

        elif main_choice == 2:  # Super Job
            print('Вы выбрали сайт Super Job')
            keyword_sj = input('Введите ключевое слово: ').title()
            hh = APISuperJob(keyword_sj).get_vacancies()
            SaveJson(hh).save_json()
            choice_website()

        elif main_choice == 3:  # selected_vacancies
            print(f'ИЗБАННОЕ: выбрано вакансий - {len(load_data())}')
            print(end=f'{"-" * 100}\n')
            n = 0
            for i in load_data():
                n += 1
                print(f'{n} Вакансия\n{i}')

        elif main_choice == 4:
            break

        else:
            print('Некорректный ввод. Повторите выбор.')
            continue


if __name__ == '__main__':
    main()
