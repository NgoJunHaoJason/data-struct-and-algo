from typing import Optional

from ._binary_tree import BinaryTree, TreeNode


class BinarySearchTree(BinaryTree):
    def __init__(self, *keys) -> None:
        self.root = TreeNode(keys[0]) if keys else None

        for key in keys[1:]:
            self._insert(self.root, key)

    def insert(self, key: str) -> None:
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node: TreeNode, key: str) -> None:
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def min(self) -> Optional[str]:
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left

        return current.key

    def max(self) -> Optional[str]:
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right

        return current.key
