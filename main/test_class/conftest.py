import pytest
from main.Class.my_class import Dict,Pickler

@pytest.fixture()
def pickler_obj():
    """
    Создал объект класса Pickler
    """
    return Pickler()

@pytest.fixture()
def dict_obj():
    """
    Создал объект класса Dict с пустым словарем
    """
    my_dict = {}
    dict_test = Dict(my_dict )
    return dict_test

@pytest.fixture()
def dict_obj_filled():
    """
    Создал объект класса Dict с наполненным словарем
    """
    my_dict = {
        'test_key_1': 'test_value_1',
        'test_key_2': 'test_value_2',
        'test_key_3': 'test_value_3'
    }
    dict_test = Dict(my_dict)
    return dict_test