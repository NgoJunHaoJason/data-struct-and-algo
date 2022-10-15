import pytest

from .linked_list import LinkedList


def test_create_linked_list_from_empty_array():
    linked_list = LinkedList([])

    assert linked_list is not None
    assert linked_list.head_node is None


def test_create_linked_list_from_array_with_one_value():
    value = 2

    linked_list = LinkedList([value])

    assert linked_list is not None
    assert linked_list.head_node is not None
    assert linked_list.head_node.value == value


def test_create_linked_list_from_array_with_multiple_values():
    array = [2, 3, 5, 7, 11]

    linked_list = LinkedList(array)

    assert linked_list is not None

    current_node = linked_list.head_node

    for value in array:
        assert current_node is not None
        assert current_node.value == value

        current_node = current_node.next_node

    assert current_node is None  # reached the end


def test_get_item_from_empty_linked_list_raises_error():
    linked_list = LinkedList([])

    with pytest.raises(IndexError):
        linked_list[0]


def test_get_item_from_linked_list_with_one_value_by_index():
    value = 2

    linked_list = LinkedList([value])

    assert linked_list[0] == value


def test_get_item_from_linked_list_with_multiple_values_by_positive_indices():
    array = [2, 3, 5, 7, 11]

    linked_list = LinkedList(array)

    for index in range(len(array)):
        assert linked_list[index] == array[index]


def test_iterate_over_empty_linked_list():
    linked_list = LinkedList([])

    array = [value for value in linked_list]

    assert not array


def test_iterate_over_linked_list_with_multiple_values():
    array = [2, 3, 5, 7, 11]

    linked_list = LinkedList(array)

    for linked_list_value, array_value in zip(linked_list, array):
        assert linked_list_value == array_value
