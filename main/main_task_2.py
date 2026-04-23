from Class.my_class import  Dict,Pickler
if __name__ == "__main__":
    capitals = {
        'Россия': 'Москва',
        'Франция': 'Париж',
        'Германия': 'Берлин',
        'Италия': 'Рим',
        'Испания': 'Мадрид',
        'Великобритания': 'Лондон',
        'Сша': 'Вашингтон',
        'Китай': 'Пекин',
        'Япония': 'Токио',
        'Турция': 'Анкара'
    }
    my_dict = Dict(capitals)
    pickle_5 = Pickler()
    save = ['save_1.txt','save_2.txt','save_3.txt','save_4.txt','save_5.txt',]
    print('Добро пожаловать')
    while True:
        print()
        navigation = input("""Выберите вариант действий:
0.Выход
1.Добавить данные в словарь
2.Удалить данные 
3.Поиск данных (найти название столице по имени страны)
4.Поиск данных (найти название страны по имени столицы)
5.Изменить данные(изменить название  столицы)
6.Изменить данные(изменить  название  страны)
7.Сохранить данные 
8.Загрузить данные
9.Отобразить список данных
Ваш вариант: """).strip()
        print()
        if navigation == '0':
            break

        elif navigation == '1':
            user_country = input('Введите название группы: ').strip().capitalize()
            user_capital = input('Введите название альбома: ').strip().capitalize()
            my_dict.add_dict(user_country,user_capital)
            print(capitals)

        elif navigation == '2':
            user_country = input('Введите название группы: ').strip().capitalize()
            capitals = my_dict.remove_from_dict(user_country)

        elif navigation == '3':
            user_country = input('Введите название группы: ').strip().capitalize()
            my_search = my_dict.search_dict(user_country)
            if my_search:
                print(f"Группа {user_country} - Альбом {my_search}")

        elif navigation == '4':
            user_capital = input('Введите название Группы: ').strip().capitalize()
            my_search = my_dict.search_dict(user_capital, False)
            print(f"Группа {my_search } - Альбом {user_capital}")

        elif navigation == '5':
            user_country = input('Введите название группы: ').strip().capitalize()
            user_new_capital = input('Введите название  нового альбома: ').strip().capitalize()
            my_dict.rename_value(user_country,user_new_capital)

        elif navigation == '6':
            user_country = input('Введите название группы: ').strip().capitalize()
            user_new_country = input('Введите название новой группы: ').strip().capitalize()
            my_dict.rename_key(user_country,user_new_country)
            print(capitals)

        elif navigation == '7':
            my_save_input = input('Выбери слот для сохранения(1-5): ').strip()
            if f'save_{my_save_input}.txt' in save:
                my_file = fr'my_save_2/save_{my_save_input}.txt'
                if  pickle_5.has_feli(my_file):
                    pickle_5.picle_data_to_file_wb(my_file, capitals)
                else:
                    my_new_save = input("Вы хотите перезаписать данные, старые данные будут потерянны (да/нет): ").strip().lower()
                    if my_new_save == 'да':
                        pickle_5.picle_data_to_file_wb(my_file, capitals)
                    else:
                        print("Данные не были сохранены: ")
            else:
                print('Вы выбрали не существующий слот')

        elif navigation == '8':
            download = input('Выбери слот для загрузки(1-5): ').strip()
            if f'save_{download}.txt' in save:
                my_file = fr'my_save_2/save_{download}.txt'
                if  pickle_5.has_feli(my_file):
                    print(f"В слоте {download} нету сохраненных данных")
                else:
                    my_download = input("Вы уверены, что хотите загрузить?, текущий прогресс будет потерян(да/нет): ").strip().lower()
                    if my_download == 'да':
                        capitals = pickle_5.picle_data_to_file_rb(my_file)
                        print(capitals)
                    else:
                        print('Данные не были загружены')
            else:
                print('Вы выбрали не существующий слот')

        elif navigation == '9':
            print('Группа - Альбом')
            print('________________')
            my_dict.print_dict()
