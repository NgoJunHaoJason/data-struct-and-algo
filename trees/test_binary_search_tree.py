from ._binary_search_tree import BinarySearchTree


def test_traverse_binary_search_tree_in_order_is_sorted() -> None:
    expected_result = ["A", "B", "C", "D", "E", "F", "G"]

    bst = BinarySearchTree(*expected_result)
    actual_result = bst.to_list()

    assert len(actual_result) == len(expected_result)

    for actual_key, expected_key in zip(actual_result, expected_result):
        assert actual_key == expected_key


def test_insert_in_binary_search_tree_remains_sorted() -> None:
    bst = BinarySearchTree("A", "B", "C", "D", "E", "F", "G")

    bst.insert("D")
    bst.insert("H")
    bst.insert("A")

    expected_result = ["A", "A", "B", "C", "D", "D", "E", "F", "G", "H"]

    actual_result = bst.to_list()

    assert len(actual_result) == len(expected_result)

    for actual_key, expected_key in zip(actual_result, expected_result):
        assert actual_key == expected_key


def test_binary_search_tree_minimum() -> None:
    bst = BinarySearchTree("A", "B", "C", "D", "E", "F", "G")

    assert bst.min() == "A"


def test_empty_binary_search_tree_minimum_is_none() -> None:
    bst = BinarySearchTree()

    assert bst.min() is None


def test_binary_search_tree_maximum() -> None:
    bst = BinarySearchTree("A", "B", "C", "D", "E", "F", "G")

    assert bst.max() == "G"


def test_empty_binary_search_tree_maximum_is_none() -> None:
    bst = BinarySearchTree()

    assert bst.max() is None


# TODO: pop?
