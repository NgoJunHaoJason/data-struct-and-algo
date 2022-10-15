import pytest

from timeit import timeit

from .linked_list import LinkedList


def test_create_linked_list_from_empty_array():
    linked_list = LinkedList()

    assert linked_list is not None
    assert linked_list.head_node is None


def test_create_linked_list_from_one_value():
    value = 2
    linked_list = LinkedList(value)

    assert linked_list is not None
    assert linked_list.head_node is not None
    assert linked_list.head_node.value == value


def test_create_linked_list_from_multiple_values():
    values = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*values)

    assert linked_list is not None

    current_node = linked_list.head_node

    for value in values:
        assert current_node is not None
        assert current_node.value == value

        current_node = current_node.next_node

    assert current_node is None  # reached the end


def test_get_item_from_empty_linked_list_raises_error():
    linked_list = LinkedList()

    with pytest.raises(IndexError):
        linked_list[0]


def test_get_item_from_linked_list_with_one_value_by_index():
    value = 2
    linked_list = LinkedList(value)

    assert linked_list[0] == value


def test_get_item_from_linked_list_with_multiple_values_by_positive_indices():
    values = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*values)

    for index in range(len(values)):
        assert linked_list[index] == values[index]


def test_get_length_of_linked_list():
    values = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*values)

    assert len(linked_list) == len(values)


def test_get_length_of_linked_list_in_constant_time():
    small_linked_list = LinkedList(i for i in range(10))
    big_linked_list = LinkedList(i for i in range(1000))

    time_taken_for_small = timeit(lambda: len(small_linked_list))
    time_taken_for_big = timeit(lambda: len(big_linked_list))

    assert time_taken_for_small == pytest.approx(time_taken_for_big, 0.01)


def test_iterate_over_empty_linked_list():
    linked_list = LinkedList()
    values = [value for value in linked_list]

    assert not values


def test_iterate_over_linked_list_with_multiple_values():
    values = [2, 3, 5, 7, 11]
    linked_list = LinkedList(*values)

    for linked_list_value, array_value in zip(linked_list, values):
        assert linked_list_value == array_value
