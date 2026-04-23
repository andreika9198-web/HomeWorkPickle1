#Тестировали класс Pickler
def test_01_01_picle_data_wb(pickler_obj):
    """
    Тестируем сохранения данных в байт
    """
    assert pickler_obj.picle_data_wb('10') == b'\x80\x05\x95\x06\x00\x00\x00\x00\x00\x00\x00\x8c\x0210\x94.'

def test_02_01_picle_data_to_file_wb(pickler_obj):
    """
    Тестируем сохранения данных в байт, и записываем в файл
    """
    filename = r'test_save\save_1.txt'
    my_dict = {
        'test_key_1': 'test_value_1',
        'test_key_2': 'test_value_2',
        'test_key_3': 'test_value_3'
    }
    assert pickler_obj.picle_data_to_file_wb(filename ,my_dict) == True

def test_03_01_picle_data_to_file_rb(pickler_obj):
    """
    Тестируем загрузку данных из файла
    """
    filename = r'test_save\save_1.txt'
    assert pickler_obj.picle_data_to_file_rb(filename) == {'test_key_1': 'test_value_1',
    'test_key_2': 'test_value_2',
    'test_key_3': 'test_value_3'}
    filename_2 = r'test_save\save_6.txt'
    assert pickler_obj.picle_data_to_file_rb(filename_2) is None
    filename_3 = r'test_save\save_2.txt'
    assert pickler_obj.picle_data_to_file_rb(filename_3) is None

def test_04_01_picle_picle_data_rb(pickler_obj):
    """
    Тестируем загрузку данных из байта
    """
    test_b = b'\x80\x05\x95\x06\x00\x00\x00\x00\x00\x00\x00\x8c\x0210\x94.'
    assert pickler_obj.picle_data_rb(test_b) == '10'

def test_05_01_has_feli(pickler_obj):
    """
    Тестируем на наличие пустого файла
    """
    filename = r'test_save\save_1.txt'
    assert pickler_obj.has_feli(filename) == False
    filename_1 = r'test_save\save_3.txt'
    assert pickler_obj.has_feli(filename_1) == True

#Тестировали класс Dict
def test_06_01_add_dict(dict_obj_filled):
    """
    Тестируем добавления новых в словарь
    """
    assert dict_obj_filled.add_dict("test_key_4","test_value_4") == True
    assert "test_key_4" in dict_obj_filled.my_dict
    assert  dict_obj_filled.add_dict("test_key_4", "test_value_4") == False

def test_07_01_remove_from_dict(dict_obj_filled):
    """
    Тестируем удаление данных из словаря
    """
    assert dict_obj_filled.remove_from_dict("test_key_3") == {'test_key_1': 'test_value_1', 'test_key_2': 'test_value_2'}
    assert dict_obj_filled.remove_from_dict("test_key_4") is None

def test_08_01_rename_value(dict_obj_filled):
    """
    Тестируем изменения данных по ключу
    """
    assert dict_obj_filled.rename_value("test_key_3","my_test") == True
    assert "my_test" in dict_obj_filled.my_dict["test_key_3"]
    assert dict_obj_filled.rename_value("test_key_4","my_test") == False

def test_09_01_rename_key(dict_obj_filled):
    """
    Тестируем изменения имени ключа
    """
    assert dict_obj_filled.rename_key("test_key_3","test_key_5") == True
    assert "test_key_5"  in dict_obj_filled.my_dict
    assert "test_key_3" not in dict_obj_filled.my_dict
    assert dict_obj_filled.rename_key("test_key_2","test_key_1") == False
    assert dict_obj_filled.rename_key("test_key_4", "test_key_6") == False

def test_09_01_search_dict(dict_obj_filled):
    """
    Тестируем поиск данных ключа или самого ключа по содержимому(находит первое вхождение)
    """
    assert dict_obj_filled.search_dict("test_key_2") == 'test_value_2'
    assert dict_obj_filled.search_dict("test_key_5") == 'Данные не найдены'
    assert dict_obj_filled.search_dict('test_value_2', False) == "test_key_2"
    assert dict_obj_filled.search_dict('test_value_5', False) == False