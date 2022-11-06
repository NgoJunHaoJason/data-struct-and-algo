import pytest

from ._binary_tree import TreeNode, Traversal
from ._heap import _is_leaf, MaxHeap


def test_leaf_node() -> None:
    leaf_node = TreeNode("A")

    assert _is_leaf(leaf_node)


def test_node_has_left_subheap() -> None:
    leaf_node = TreeNode("A", left=TreeNode("B"))

    assert not _is_leaf(leaf_node)


def test_node_has_right_subheap() -> None:
    leaf_node = TreeNode("A", right=TreeNode("B"))

    assert not _is_leaf(leaf_node)


def test_node_has_left_and_right_subheap() -> None:
    leaf_node = TreeNode("A", left=TreeNode("B"), right=TreeNode("C"))

    assert not _is_leaf(leaf_node)


@pytest.fixture
def heap() -> MaxHeap:
    return MaxHeap("A", "B", "C", "D", "E", "F", "G")


def test_traverse_heap_in_order(heap: MaxHeap) -> None:
    expected_result = ["D", "E", "B", "G", "A", "F", "C"]
    actual_result = heap.to_list()

    assert len(actual_result) == len(expected_result)

    for actual_key, expected_key in zip(actual_result, expected_result):
        assert actual_key == expected_key


def test_traverse_heap_pre_order(heap: MaxHeap) -> None:
    expected_result = ["G", "E", "D", "B", "F", "A", "C"]
    actual_result = heap.to_list(Traversal.PRE_ORDER)

    assert len(actual_result) == len(expected_result)

    for actual_key, expected_key in zip(actual_result, expected_result):
        assert actual_key == expected_key


def test_traverse_max_heap_post_order(heap: MaxHeap) -> None:
    expected_result = ["D", "B", "E", "A", "C", "F", "G"]
    actual_result = heap.to_list(Traversal.POST_ORDER)

    assert len(actual_result) == len(expected_result)

    for actual_key, expected_key in zip(actual_result, expected_result):
        assert actual_key == expected_key


def test_find_max(heap: MaxHeap) -> None:
    expected_max = max(heap.to_list())

    assert heap.find_max() == expected_max


def test_delete_max(heap: MaxHeap) -> None:
    heap_as_list = heap.to_list()
    heap_as_list.remove(max(heap_as_list))

    expected_max = max(heap_as_list)

    heap.delete_max()

    assert heap.find_max() == expected_max


# TODO: more heap operations
