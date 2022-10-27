from __future__ import annotations
from enum import Enum


class Traversal(Enum):
    IN_ORDER = 0
    PRE_ORDER = 1
    POST_ORDER = 2


class BinaryTree:
    def __init__(self, *values) -> None:
        self.root = TreeNode(values[0]) if values else None

        node_queue = [self.root]

        for value in values[1:]:
            new_node = TreeNode(value)

            root_node = node_queue.pop(0)

            if root_node.left is None:
                root_node.left = new_node
                node_queue.insert(0, root_node)

            elif root_node.right is None:
                root_node.right = new_node

            else:
                raise ValueError

            node_queue.append(new_node)

    def to_list(self, traversal: Traversal = Traversal.IN_ORDER) -> list[int]:
        result = []

        if traversal == Traversal.IN_ORDER:
            result = self._traverse_in_order(self.root, result)

        elif traversal == Traversal.PRE_ORDER:
            result = self._traverse_pre_order(self.root, result)

        elif traversal == Traversal.POST_ORDER:
            result = self._traverse_post_order(self.root, result)

        else:
            raise ValueError

        return result

    def _traverse_in_order(self, tree_node: TreeNode, result: list[int]) -> list[int]:
        if tree_node is None:
            return result

        result = self._traverse_in_order(tree_node.left, result)
        result.append(tree_node.value)
        result = self._traverse_in_order(tree_node.right, result)

        return result

    def _traverse_pre_order(self, tree_node: TreeNode, result: list[int]) -> list[int]:
        if tree_node is None:
            return result

        result.append(tree_node.value)
        result = self._traverse_pre_order(tree_node.left, result)
        result = self._traverse_pre_order(tree_node.right, result)

        return result

    def _traverse_post_order(self, tree_node: TreeNode, result: list[int]) -> list[int]:
        if tree_node is None:
            return result

        result = self._traverse_post_order(tree_node.left, result)
        result = self._traverse_post_order(tree_node.right, result)
        result.append(tree_node.value)

        return result


class TreeNode:
    def __init__(
        self,
        value: int,
        left: TreeNode = None,
        right: TreeNode = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right
