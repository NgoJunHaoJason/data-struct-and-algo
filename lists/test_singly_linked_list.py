import pytest

from ._singly_linked_list import SinglyLinkedList


@pytest.fixture
def keys() -> SinglyLinkedList:
    return ["A", "B", "C", "D", "E", "F", "G"]


def test_create_empty_linked_list() -> None:
    linked_list = SinglyLinkedList()

    assert linked_list is not None
    assert linked_list.sentinel_node.next_node is None


def test_create_linked_list_from_given_keys(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    assert linked_list is not None

    current_node = linked_list.sentinel_node.next_node

    for key in keys:
        assert current_node is not None
        assert current_node.key == key

        current_node = current_node.next_node

    assert current_node is None  # reached the end


def test_index_into_linked_list_with_invalid_types() -> None:
    linked_list = SinglyLinkedList("A")

    with pytest.raises(TypeError):
        linked_list["A"]

    with pytest.raises(TypeError):
        linked_list[:]


def test_get_length_of_linked_list(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    assert len(linked_list) == len(keys)


def test_iterate_over_empty_linked_list() -> None:
    linked_list = SinglyLinkedList()
    keys = [key for key in linked_list]

    assert not keys


def test_iterate_over_linked_list(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    for linked_list_key, expected_key in zip(linked_list, keys):
        assert linked_list_key == expected_key


def test_string_representation_of_linked_list():
    linked_list = SinglyLinkedList(2, 3, 5, 7, 11)

    assert str(linked_list) == "LinkedList(2, 3, 5, 7, 11)"


def test_insert_key_at_start_of_linked_list_by_index(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    key = "H"
    linked_list.insert(0, key)

    assert len(linked_list) == len(keys) + 1

    for linked_list_key, expected_key in zip(linked_list, [key] + keys):
        assert linked_list_key == expected_key


def test_insert_key_in_middle_of_linked_list_by_index(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    middle_index = len(keys) // 2
    key = "H"

    linked_list.insert(middle_index, key)

    assert len(linked_list) == len(keys) + 1

    expected_keys = keys[:middle_index] + [key] + keys[middle_index:]
    for linked_list_key, expected_key in zip(linked_list, expected_keys):
        assert linked_list_key == expected_key


def test_insert_key_at_end_of_linked_list_by_index(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    key = "H"
    linked_list.insert(len(keys), key)

    assert len(linked_list) == len(keys) + 1

    for linked_list_key, expected_key in zip(linked_list, keys + [key]):
        assert linked_list_key == expected_key


def test_insert_key_into_linked_list_by_invalid_index() -> None:
    linked_list = SinglyLinkedList("A")

    with pytest.raises(IndexError):
        linked_list.insert(2, "B")


def test_pop_key_from_start_of_linked_list_by_index(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    key = linked_list.pop(0)

    assert key == keys[0]
    assert len(linked_list) == len(keys) - 1

    for linked_list_key, expected_key in zip(linked_list, keys[1:]):
        assert linked_list_key == expected_key


def test_pop_key_from_middle_of_linked_list_by_index(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    middle_index = len(keys) // 2
    key = linked_list.pop(middle_index)

    assert key == keys[middle_index]
    assert len(linked_list) == len(keys) - 1

    expected_keys = keys[:middle_index] + keys[middle_index + 1 :]
    for linked_list_key, expected_key in zip(linked_list, expected_keys):
        assert linked_list_key == expected_key


def test_pop_key_from_end_of_linked_list_by_index(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    key = linked_list.pop(len(keys) - 1)

    assert key == keys[-1]
    assert len(linked_list) == len(keys) - 1

    for linked_list_key, expected_key in zip(linked_list, keys[:-1]):
        assert linked_list_key == expected_key


def test_pop_key_from_linked_list_by_invalid_index() -> None:
    linked_list = SinglyLinkedList("A")

    with pytest.raises(IndexError):
        linked_list.pop(1)


def test_remove_key_from_start_of_linked_list(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    linked_list.remove(keys[0])

    assert len(linked_list) == len(keys) - 1

    for linked_list_key, expected_key in zip(linked_list, keys[1:]):
        assert linked_list_key == expected_key


def test_remove_key_from_middle_of_linked_list(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    middle_index = len(keys) // 2
    linked_list.remove(keys[middle_index])

    assert len(linked_list) == len(keys) - 1

    expected_keys = keys[:middle_index] + keys[middle_index + 1 :]
    for linked_list_key, expected_key in zip(linked_list, expected_keys):
        assert linked_list_key == expected_key


def test_remove_key_from_end_of_linked_list(keys: list[str]) -> None:
    linked_list = SinglyLinkedList(*keys)

    linked_list.remove(keys[-1])

    assert len(linked_list) == len(keys) - 1

    for linked_list_key, expected_key in zip(linked_list, keys[:-1]):
        assert linked_list_key == expected_key


def test_remove_key_not_in_linked_list() -> None:
    linked_list = SinglyLinkedList(2)

    with pytest.raises(ValueError):
        linked_list.remove(3)
