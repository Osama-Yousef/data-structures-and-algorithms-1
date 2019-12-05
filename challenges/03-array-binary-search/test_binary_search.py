from array_binary_search import binary_search

def test_binary_search_null():
    input_arr = []
    input_target = 5

    actual = binary_search(input_arr, input_target)
    expected = -1
    assert expected == actual

