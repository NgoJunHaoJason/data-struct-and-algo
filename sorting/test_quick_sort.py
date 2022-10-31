import random

from ._quick_sort import quick_sort


def test_quick_sort_on_empty_array():
    expected_array = []
    actual_array = expected_array[:]

    random.shuffle(actual_array)

    quick_sort(actual_array)

    assert len(actual_array) == len(expected_array)

    for actual_value, expected_value in zip(actual_array, expected_array):
        assert actual_value == expected_value


def test_quick_sort_on_small_array():
    expected_array = [number for number in range(2**3)]
    actual_array = expected_array[:]

    random.shuffle(actual_array)

    quick_sort(actual_array)

    assert len(actual_array) == len(expected_array)

    for actual_value, expected_value in zip(actual_array, expected_array):
        assert actual_value == expected_value
