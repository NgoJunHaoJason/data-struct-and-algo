from .linked_list import LinkedList


def test_create_linked_list_from_empty_array():
    linked_list = LinkedList([])

    assert linked_list is not None
    assert linked_list.head_node is None


def test_create_linked_list_from_array_with_one_value():
    value = 0

    linked_list = LinkedList([value])

    assert linked_list is not None
    assert linked_list.head_node is not None
    assert linked_list.head_node.value == value


def test_create_linked_list_from_array_with_multiple_values():
    array = [0, 1, 2, 3, 4]

    linked_list = LinkedList(array)

    assert linked_list is not None

    current_node = linked_list.head_node

    for value in array:
        assert current_node is not None
        assert current_node.value == value

        current_node = current_node.next_node

    assert current_node is None  # reached the end


def test_iterate_over_linked_list():
    array = [0, 1, 2, 3, 4]

    linked_list = LinkedList(array)

    for linked_list_value, array_value in zip(linked_list, array):
        assert linked_list_value == array_value
