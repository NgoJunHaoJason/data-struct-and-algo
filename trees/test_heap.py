import pytest

from ._binary_tree import TreeNode, Traversal
from ._heap import _is_leaf, MaxHeap


def test_leaf_node() -> None:
    leaf_node = TreeNode(0)

    assert _is_leaf(leaf_node)


def test_node_has_left_subheap() -> None:
    leaf_node = TreeNode(0, left=TreeNode(1))

    assert not _is_leaf(leaf_node)


def test_node_has_right_subheap() -> None:
    leaf_node = TreeNode(0, right=TreeNode(1))

    assert not _is_leaf(leaf_node)


def test_node_has_left_and_right_subheap() -> None:
    leaf_node = TreeNode(0, left=TreeNode(1), right=TreeNode(2))

    assert not _is_leaf(leaf_node)


@pytest.fixture
def heap() -> MaxHeap:
    return MaxHeap(2, 3, 5, 7, 11, 13, 17)


def test_traverse_heap_in_order(heap: MaxHeap) -> None:
    expected_result = [7, 11, 3, 17, 2, 13, 5]
    actual_result = heap.to_list()

    assert len(actual_result) == len(expected_result)

    for actual_value, expected_value in zip(actual_result, expected_result):
        assert actual_value == expected_value


def test_traverse_heap_pre_order(heap: MaxHeap) -> None:
    expected_result = [17, 11, 7, 3, 13, 2, 5]
    actual_result = heap.to_list(Traversal.PRE_ORDER)

    assert len(actual_result) == len(expected_result)

    for actual_value, expected_value in zip(actual_result, expected_result):
        assert actual_value == expected_value


def test_traverse_max_heap_post_order(heap: MaxHeap) -> None:
    expected_result = [7, 3, 11, 2, 5, 13, 17]
    actual_result = heap.to_list(Traversal.POST_ORDER)

    assert len(actual_result) == len(expected_result)

    for actual_value, expected_value in zip(actual_result, expected_result):
        assert actual_value == expected_value


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
