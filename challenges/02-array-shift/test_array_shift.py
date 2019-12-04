from array_shift import insert_shift_array

def test_even_array():
    old_arr = [1,2,3,4]
    old_val = 3

    actual = insert_shift_array(old_arr, old_val)
    expected = [1,2,3,3,4]
    assert expected == actual

def test_odd_array():
    pass

def test_empty_array():
    pass

def test_other_array():
    # use other types of data
    pass
