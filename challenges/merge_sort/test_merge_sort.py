import pytest
from merge_sort import merge_sort, merge

# - sort empty list
# - list of one, two, and then more elements

def test_empty_list():
    array = []
    merge_sort([])
    expected = []
    assert array == expected