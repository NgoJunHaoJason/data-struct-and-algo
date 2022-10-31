import pytest

from ._binary_tree import BinaryTree, Traversal


@pytest.fixture
def binary_tree() -> BinaryTree:
    return BinaryTree("A", "B", "C", "D", "E", "F", "G")


def test_traverse_binary_tree_in_order(binary_tree: BinaryTree) -> None:
    expected_result = ["D", "B", "E", "A", "F", "C", "G"]
    actual_result = binary_tree.to_list()

    assert len(actual_result) == len(expected_result)

    for actual_key, expected_key in zip(actual_result, expected_result):
        assert actual_key == expected_key


def test_traverse_binary_tree_pre_order(binary_tree: BinaryTree) -> None:
    expected_result = ["A", "B", "D", "E", "C", "F", "G"]
    actual_result = binary_tree.to_list(Traversal.PRE_ORDER)

    assert len(actual_result) == len(expected_result)

    for actual_key, expected_key in zip(actual_result, expected_result):
        assert actual_key == expected_key


def test_traverse_binary_tree_post_order(binary_tree: BinaryTree) -> None:
    expected_result = ["D", "E", "B", "F", "G", "C", "A"]
    actual_result = binary_tree.to_list(Traversal.POST_ORDER)

    assert len(actual_result) == len(expected_result)

    for actual_key, expected_key in zip(actual_result, expected_result):
        assert actual_key == expected_key
