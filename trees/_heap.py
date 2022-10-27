from ._binary_tree import BinaryTree, TreeNode


def _is_leaf(node: TreeNode) -> bool:
    return node is not None and node.left is None and node.right is None


class MaxHeap(BinaryTree):
    def __init__(self, *values) -> None:
        super().__init__(*values)

        if self.root is not None:
            self._heapify(self.root)

        self.size = len(values)

    def _heapify(self, root: TreeNode) -> None:
        if not _is_leaf(root):
            if root.left is not None:
                self._heapify(root.left)

            if root.right is not None:
                self._heapify(root.right)

            self._fix_heap(root, root.value)

    def _fix_heap(self, root: TreeNode, value: int) -> None:
        if _is_leaf(root):
            root.value = value
        else:
            larger_subheap = (
                root.right
                if root.right is not None and root.right.value > root.left.value
                else root.left
            )

            if value >= larger_subheap.value:
                root.value = value
            else:
                root.value = larger_subheap.value
                self._fix_heap(larger_subheap, value)

    def _find_parent_of_last(self) -> TreeNode:
        if self.size <= 1:
            return None

        size_in_binary = bin(self.size)[2:]

        last_node = self.root
        for digit in size_in_binary[1:-1]:
            last_node = last_node.left if digit == "0" else last_node.right

        return last_node

    def __repr__(self) -> str:
        return str(self.to_list())

    def find_max(self) -> int:
        return self.root.value

    def delete_max(self) -> None:
        if self.size > 1:
            parent_of_last = self._find_parent_of_last()

            if parent_of_last.right is None:
                last_node_value = parent_of_last.left.value
                parent_of_last.left = None
            else:
                last_node_value = parent_of_last.right.value
                parent_of_last.right = None

            self.size -= 1

            self._fix_heap(self.root, last_node_value)

        elif self.size > 0:
            self.root = None
            self.size -= 1
