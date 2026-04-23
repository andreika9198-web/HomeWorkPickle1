
def test_01_01_picle_data_wb(pickler_obj):
    assert pickler_obj.picle_data_wb('10') == b'\x80\x05\x95\x06\x00\x00\x00\x00\x00\x00\x00\x8c\x0210\x94.'

