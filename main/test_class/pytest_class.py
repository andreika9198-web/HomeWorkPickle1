
def test_01_01_picle_data_wb(pickler_obj):
    assert pickler_obj.picle_data_wb('10') == b'\x80\x05\x95\x06\x00\x00\x00\x00\x00\x00\x00\x8c\x0210\x94.'

def test_02_01_picle_data_to_file_wb(pickler_obj):
    filename = r'test_save\save_1.txt'
    my_dict = {
        'test_key_1': 'test_value_1',
        'test_key_2': 'test_value_2',
        'test_key_3': 'test_value_3'
    }
    assert pickler_obj.picle_data_to_file_wb(filename,my_dict) == True
