import pytest

from timeit import timeit

from .linked_list import LinkedList


def test_create_empty_linked_list():
    linked_list = LinkedList()

    assert linked_list is not None
    assert linked_list.head_node is None


def test_create_linked_list_from_given_array():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    assert linked_list is not None

    current_node = linked_list.head_node

    for value in array:
        assert current_node is not None
        assert current_node.value == value

        current_node = current_node.next_node

    assert current_node is None  # reached the end


def test_get_value_from_empty_linked_list_raises_error():
    linked_list = LinkedList()

    with pytest.raises(IndexError):
        linked_list[0]


def test_get_value_from_linked_list_with_index_beyond_range():
    linked_list = LinkedList(0)

    with pytest.raises(IndexError):
        linked_list[1]


def test_get_value_from_linked_list_with_invalid_index_type():
    linked_list = LinkedList(0)

    with pytest.raises(TypeError):
        linked_list["A"]


def test_get_value_from_linked_list_by_positive_indices():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    for index in range(len(array)):
        assert linked_list[index] == array[index]


def test_get_value_from_linked_list_by_negative_indices():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    for index in range(-1, -len(array) - 1, -1):
        assert linked_list[index] == array[index]


def test_get_length_of_linked_list():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    assert len(linked_list) == len(array)


def test_get_length_of_linked_list_in_constant_time():
    small_linked_list = LinkedList(i for i in range(10))
    big_linked_list = LinkedList(i for i in range(1000))

    time_taken_for_small = timeit(lambda: len(small_linked_list))
    time_taken_for_big = timeit(lambda: len(big_linked_list))

    assert time_taken_for_small == pytest.approx(time_taken_for_big, 0.1)


def test_iterate_over_empty_linked_list():
    linked_list = LinkedList()
    array = [value for value in linked_list]

    assert not array


def test_iterate_over_linked_list():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    for linked_list_value, array_value in zip(linked_list, array):
        assert linked_list_value == array_value


def test_reverse_linked_list():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    for linked_list_value, array_value in zip(reversed(linked_list), reversed(array)):
        assert linked_list_value == array_value


def test_slice_linked_list():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    subarray = array[1:3]
    sublist = linked_list[1:3]

    assert len(sublist) == len(subarray)

    for linked_list_value, array_value in zip(sublist, subarray):
        assert linked_list_value == array_value


# TODO
# __doc__()
# __contains__()
# __eq__(), le, ge, lt, gt, ne
# slice step more than 1
# negative slice step
# __setitem__()
# __add__(), sub, mul
# __repr__()
# __str__()


def test_insert_value_at_start_of_linked_list_by_index():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    value = 1
    linked_list.insert(0, value)

    assert len(linked_list) == len(array) + 1

    for linked_list_value, array_value in zip(linked_list, [value] + array):
        assert linked_list_value == array_value


def test_insert_value_in_middle_of_linked_list_by_index():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    value = 1
    linked_list.insert(2, value)

    assert len(linked_list) == len(array) + 1

    for linked_list_value, array_value in zip(linked_list, [2, 3, 1, 5, 7, 11]):
        assert linked_list_value == array_value


def test_insert_value_at_end_of_linked_list_by_index():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    value = 1
    linked_list.insert(len(array), value)

    assert len(linked_list) == len(array) + 1

    for linked_list_value, array_value in zip(linked_list, array + [value]):
        assert linked_list_value == array_value


def test_insert_value_into_linked_list_by_invalid_index():
    linked_list = LinkedList(2)

    with pytest.raises(IndexError):
        linked_list.insert(2, 1)


def test_pop_value_from_start_of_linked_list_by_index():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    value = linked_list.pop(0)

    assert value == 2
    assert len(linked_list) == len(array) - 1

    for linked_list_value, array_value in zip(linked_list, array[1:]):
        assert linked_list_value == array_value


def test_pop_value_from_middle_of_linked_list_by_index():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    value = linked_list.pop(2)

    assert value == 5
    assert len(linked_list) == len(array) - 1

    for linked_list_value, array_value in zip(linked_list, [2, 3, 7, 11]):
        assert linked_list_value == array_value


def test_pop_value_from_end_of_linked_list_by_index():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    value = linked_list.pop(4)

    assert value == 11
    assert len(linked_list) == len(array) - 1

    for linked_list_value, array_value in zip(linked_list, array[:-1]):
        assert linked_list_value == array_value


def test_pop_value_from_linked_list_by_invalid_index():
    linked_list = LinkedList(2)

    with pytest.raises(IndexError):
        linked_list.pop(1)


def test_remove_value_from_start_of_linked_list():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    linked_list.remove(2)

    assert len(linked_list) == len(array) - 1

    for linked_list_value, array_value in zip(linked_list, array[1:]):
        assert linked_list_value == array_value


def test_remove_value_from_middle_of_linked_list():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    linked_list.remove(5)

    assert len(linked_list) == len(array) - 1

    for linked_list_value, array_value in zip(linked_list, [2, 3, 7, 11]):
        assert linked_list_value == array_value


def test_remove_value_from_end_of_linked_list():
    array = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*array)

    linked_list.remove(11)

    assert len(linked_list) == len(array) - 1

    for linked_list_value, array_value in zip(linked_list, array[:-1]):
        assert linked_list_value == array_value


def test_remove_value_not_in_linked_list():
    linked_list = LinkedList(2)

    with pytest.raises(ValueError):
        linked_list.remove(3)
