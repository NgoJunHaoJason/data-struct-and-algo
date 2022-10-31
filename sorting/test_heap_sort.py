import random

from ._heap_sort import heap_sort


def test_heap_sort_on_empty_array():
    expected_array = []
    actual_array = expected_array[:]

    random.shuffle(actual_array)

    heap_sort(actual_array)

    assert len(actual_array) == len(expected_array)

    for actual_value, expected_value in zip(actual_array, expected_array):
        assert actual_value == expected_value


def test_heap_sort_on_small_array():
    expected_array = [chr(unicode) for unicode in range(ord("A"), ord("H"))]
    actual_array = expected_array[:]

    random.shuffle(actual_array)

    heap_sort(actual_array)

    assert len(actual_array) == len(expected_array)
    assert actual_array == expected_array

    for actual_value, expected_value in zip(actual_array, expected_array):
        assert actual_value == expected_value
