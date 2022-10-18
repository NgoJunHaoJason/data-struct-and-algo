import random


from .algorithms import linear_search


def test_linear_search_target_value_in_array():
    array = [number for number in range(8)]
    target_value = random.randrange(0, 8)

    random.shuffle(array)

    expected_index = array.index(target_value)
    actual_index = linear_search(array, target_value)

    assert actual_index == expected_index


def test_linear_search_target_value_not_in_array():
    array = [number for number in range(8)]
    target_value = 8

    random.shuffle(array)

    actual_index = linear_search(array, target_value)

    assert actual_index == -1
