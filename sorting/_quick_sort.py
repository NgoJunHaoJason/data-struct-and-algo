def quick_sort(array: list[int]) -> None:
    _quick_sort(array, start=0, end=len(array) - 1)


def _quick_sort(array: list[int], start: int, end: int) -> None:
    if start >= end:
        return

    pivot_index = _partition(array, start, end)

    _quick_sort(array, start=start, end=pivot_index - 1)
    _quick_sort(array, start=pivot_index + 1, end=end)


def _partition(array: list[int], start: int, end: int) -> int:
    pivot_index, pivot_value = start, array[start]

    for index in range(start + 1, end + 1):
        if array[index] < pivot_value:
            pivot_index += 1
            _swap(array, pivot_index, index)

    _swap(array, start, pivot_index)
    return pivot_index


def _swap(array: list[int], index1: int, index2: int) -> None:
    array[index1], array[index2] = array[index2], array[index1]
