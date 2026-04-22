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
            user_country = input('Введите название страны: ').strip().capitalize()
            user_capital = input('Введите название столицы: ').strip().capitalize()
            my_dict.add_dict(user_country,user_capital)
            print(capitals)
        elif navigation == '2':
            user_country = input('Введите название страны: ').strip().capitalize()
            my_dict.remove_from_dict(user_country)
        elif navigation == '3':
            user_country = input('Введите название страны: ').strip().capitalize()
            my_search = my_dict.search_dict(user_country)
            if my_search:
                print(f"Страна {user_country} - Столица {my_search}")
        elif navigation == '4':
            user_capital = input('Введите название столицы: ').strip().capitalize()
            my_search = my_dict.search_dict(user_capital, False)
            print(f"Страна {my_search } - Столица {user_capital}")
        elif navigation == '5':
            user_country = input('Введите название страны: ').strip().capitalize()
            user_new_capital = input('Введите название  новой столицы: ').strip().capitalize()
            my_dict.rename_value(user_country,user_new_capital)
        elif navigation == '6':
            user_country = input('Введите название страны: ').strip().capitalize()
            user_new_country = input('Введите название новой страны: ').strip().capitalize()
            my_dict.rename_key(user_country,user_new_country)
            print(capitals)


