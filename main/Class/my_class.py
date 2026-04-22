import pickle

class Pickler:
    """
    Класс для сохранения и загрузки данных
    """
    def __init__(self, protocol = pickle.DEFAULT_PROTOCOL):
        self.protocol = protocol

    def picle_data_wb(self,data):
        """
        Метод для сохранения дынных в байты
        :param data:
            данные для сохранения
        :return:
            данные в байтах
        """
        pickled_data = pickle.dumps(data, self.protocol)
        return pickled_data

    def picle_data_to_file_wb(self, filename, data):
        """
        Метод для сохранения дынных в файл
        :param filename:
            ссылка на файл
        :param data:
            данные для сохранения
        :return:
        """
        with open(filename, 'wb') as file:
            pickle.dump(data, file, self.protocol)
        print(f'Данные были записаны {filename}')
        return True

    @classmethod
    def picle_data_rb(cls, pickle_data):
        """
        Метод для загрузки байтовых дынных
        :return:
            возвращает загруженные данные
        """
        pickle_data_rb = pickle.loads(pickle_data)
        return pickle_data_rb

    @classmethod
    def picle_data_to_file_rb(cls,filename):
        """
        Метод для загрузки дынных из файла
        :param filename:
            ссылка на файл
        :return:
        """
        try:
            with open(filename, 'rb') as file:
                picle_data_to_file =  pickle.load(file)
                return picle_data_to_file
        except FileNotFoundError:
            print('Файл не найден')
            return None
        except Exception as ex:
            print(ex)
            return None

class Dict:
    """
    Класс для работы со словарем, использует такие методы как
    добавить в словарь, удалить, изменить содержимое ключа, изменить ключ
    """
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def add_dict(self, data_key, data_value):
        """
        Метод для добавления в данных словарь
        :param data_key:
            название ключа
        :param data_value:
            данные ключа
        """
        if not data_key in self.my_dict:
            self.my_dict.setdefault(data_key, data_value)
            print('Данные успешно добавлены')
        else:
            print('Данные с таким значением уже есть')

    def remove_from_dict(self, data_key):
        """
        Метод для удаления ключа из словаря
        :param data_key:
            данные ключа для удаления из словаря
        :return:
            удаленные данные или None
        """
        if data_key in self.my_dict :
            remove_dict = self.my_dict.pop(data_key)
            print(f'Данные {data_key} : {remove_dict} были успешно удалены')
            return remove_dict
        else:
            print('Данные не были найдены')
            return None

    def rename_value(self, data_key, data_new_value):
        """
        Метод для изменения данных по ключу
        :param data_key:
            название ключа
        :param data_new_value:
            новое данные для ключа
        """
        if data_key in self.my_dict:
            my_get = self.my_dict.get()
            self.my_dict[data_key] = data_new_value
            print(f'Данные были изменены : {my_get}  на {data_new_value} ')
        else:
            print('Данные не найдены')

    def rename_key(self, data_key, data_new_key):
        """
        Метод для изменения имени ключа
        :param data_key:
            название старого ключа
        :param data_new_key:
            названия нового ключа
        """
        if not data_new_key in self.my_dict:
            remove_dict = self.my_dict.pop(data_key)
            if remove_dict :
                self.add_dict(data_new_key, remove_dict)
                print(f'Данные были изменены : {data_key}  на {data_new_key}')
            else:
                print('Данные не были найдены')
        else:
            print('Нельзя изменить на существующие данные')


    def search_dict(self, data, data_key = True):
        """
        Метод для поиска данных ключа или самого ключа по содержимому(находит первое вхождение)
        :param data:
            Данные для поиска
        :param data_key:
            поиск по ключу или данным ключа
        :return:
        """
        if data_key:
            return self.my_dict.get(data, "Данные не найдены")
        else:
            for k,v in self.my_dict.items():
                if v == data:
                    return k
            print('"Данные не найдены"')
            return False

    def print_dict(self):
        """"
        Метод для отображения содержимого словаря
        """
        if self.my_dict:
            for k,v in self.my_dict:
                print(f'{k} - {v}')
        else:
            print('Список пуст')