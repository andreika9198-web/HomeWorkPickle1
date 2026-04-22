import pickle

class Pickler:
    def __init__(self, protocol = pickle.DEFAULT_PROTOCOL):
        self.protocol = protocol

    def picle_data_wb(self,data):
        pickled_data = pickle.dumps(data, self.protocol)
        return pickled_data

    def picle_data_to_file_wb(self, filename, data):
        with open(filename, 'wb') as file:
            pickle.dump(data, file, self.protocol)
        print(f'Данные были записаны {filename}')
        return True

    @classmethod
    def picle_data_rb(cls, pickle_data):
        pickle_data_rb = pickle.loads(pickle_data)
        return pickle_data_rb

    @classmethod
    def picle_data_to_file_rb(cls,filename):
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
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def add_dict(self, data_key, data_value):
        if not data_key in self.my_dict:
            self.my_dict.setdefault(data_key, data_value)
            print('Данные успешно добавлены')
        else:
            print('Данные с таким значением уже есть')

    def remove_from_dict(self, data_key):
        remove_dict = self.my_dict.pop(data_key)
        if remove_dict :
            print(f'Данные {data_key} : {remove_dict} были успешно удалены')
            return remove_dict
        else:
            print('Данные не были найдены')
            return None

    def rename_value(self, data_key, data_value):
        if data_key in self.my_dict:
            my_get = self.my_dict.get()
            self.my_dict[data_key] = data_value
            print(f'Данные были изменены : {my_get}  на {data_value} ')
        else:
            print('Данные не найдены')

    def rename_key(self, data_key, data_new_key):
        if not data_new_key in self.my_dict:
            remove_dict = self.my_dict.pop(data_key)
            if remove_dict :
                self.add_dict(data_new_key, remove_dict)
                print(f'Данные были изменены : {data_key}  на {data_new_key}')
            else:
                print('Данные не были найдены')
        else:
            print('Нельзя изменить на существующие данные')
