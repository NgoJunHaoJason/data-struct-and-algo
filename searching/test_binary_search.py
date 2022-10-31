import random


from ._binary_search import binary_search


def test_binary_search_target_value_in_array():
    array = [number for number in range(8)]
    target_value = random.randrange(0, 8)

    expected_index = array.index(target_value)
    actual_index = binary_search(array, target_value)

    assert actual_index == expected_index


def test_binary_search_target_value_not_in_array():
    array = [number for number in range(8)]

    actual_index = binary_search(array, 8)

    assert actual_index == -1


def test_binary_search_empty_array():
    actual_index = binary_search([], 8)

    assert actual_index == -1
