from array_binary_search import binary_search

def test_binary_search_null():
    input_arr = []
    input_target = 5

    actual = binary_search(input_arr, input_target)
    expected = -1
    assert expected == actual

def test_binary_search_even():
    input_arr = [4,8,15,16,23,42]
    input_target = 15

    actual = binary_search(input_arr, input_target)
    expected = 2
    assert expected == actual

def test_binary_search_odd():
    input_arr = [4,8,15,16,23,42]
    input_target = 15

    actual = binary_search(input_arr, input_target)
    expected = 2
    assert expected == actual

def test_binary_search_not_found():
    input_arr = [11,22,33,44,55,66,77]
    input_target = 90

    actual = binary_search(input_arr, input_target)
    expected = -1
    assert expected == actual
