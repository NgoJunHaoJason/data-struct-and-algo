import pytest

from ._binary_tree import BinaryTree, Traversal


def test_create_empty_binary_tree():
    with pytest.raises(ValueError):
        BinaryTree()


def test_traverse_binary_tree_in_order():
    expected_result = [7, 3, 11, 2, 13, 5, 17]

    binary_tree = BinaryTree(2, 3, 5, 7, 11, 13, 17)
    actual_result = binary_tree.to_list()

    assert len(actual_result) == len(expected_result)

    for actual_value, expected_value in zip(actual_result, expected_result):
        assert actual_value == expected_value


def test_traverse_binary_tree_pre_order():
    expected_result = [2, 3, 7, 11, 5, 13, 17]

    binary_tree = BinaryTree(2, 3, 5, 7, 11, 13, 17)
    actual_result = binary_tree.to_list(Traversal.PRE_ORDER)

    assert len(actual_result) == len(expected_result)

    for actual_value, expected_value in zip(actual_result, expected_result):
        assert actual_value == expected_value


def test_traverse_binary_tree_post_order():
    expected_result = [7, 11, 3, 13, 17, 5, 2]

    binary_tree = BinaryTree(2, 3, 5, 7, 11, 13, 17)
    actual_result = binary_tree.to_list(Traversal.POST_ORDER)

    assert len(actual_result) == len(expected_result)

    for actual_value, expected_value in zip(actual_result, expected_result):
        assert actual_value == expected_value
