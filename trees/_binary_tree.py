from __future__ import annotations
from enum import Enum


class Traversal(Enum):
    IN_ORDER = 0
    PRE_ORDER = 1
    POST_ORDER = 2


class BinaryTree:
    def __init__(self, *keys) -> None:
        self.root = TreeNode(keys[0]) if keys else None

        node_queue = [self.root]

        for key in keys[1:]:
            new_node = TreeNode(key)

            root_node = node_queue.pop(0)

            if root_node.left is None:
                root_node.left = new_node
                node_queue.insert(0, root_node)

            elif root_node.right is None:
                root_node.right = new_node

            else:
                raise ValueError

            node_queue.append(new_node)

    def to_list(self, traversal: Traversal = Traversal.IN_ORDER) -> list[str]:
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

    def _traverse_in_order(self, tree_node: TreeNode, result: list[str]) -> list[str]:
        if tree_node is None:
            return result

        result = self._traverse_in_order(tree_node.left, result)
        result.append(tree_node.key)
        result = self._traverse_in_order(tree_node.right, result)

        return result

    def _traverse_pre_order(self, tree_node: TreeNode, result: list[str]) -> list[str]:
        if tree_node is None:
            return result

        result.append(tree_node.key)
        result = self._traverse_pre_order(tree_node.left, result)
        result = self._traverse_pre_order(tree_node.right, result)

        return result

    def _traverse_post_order(self, tree_node: TreeNode, result: list[str]) -> list[str]:
        if tree_node is None:
            return result

        result = self._traverse_post_order(tree_node.left, result)
        result = self._traverse_post_order(tree_node.right, result)
        result.append(tree_node.key)

        return result


class TreeNode:
    def __init__(
        self,
        key: str,
        left: TreeNode = None,
        right: TreeNode = None,
    ) -> None:
        self.key = key
        self.left = left
        self.right = right
