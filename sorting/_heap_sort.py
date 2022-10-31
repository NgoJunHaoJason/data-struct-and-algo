from trees import MaxHeap


def heap_sort(array: list[str]) -> None:
    max_heap = MaxHeap(*array)

    for index in reversed(range(len(array))):
        array[index] = max_heap.find_max()
        max_heap.delete_max()
