def binary_search(array: list[int], target_value: int) -> int:
    return (
        -1
        if len(array) == 0
        else _binary_search(array, target_value, 0, len(array) - 1)
    )


def _binary_search(array: list[int], target_value: int, start: int, end: int) -> int:
    if start >= end:
        return start if array[start] == target_value else -1

    middle = (start + end) // 2
    middle_value = array[middle]

    if middle_value > target_value:
        return _binary_search(array, target_value, start, middle - 1)
    elif middle_value < target_value:
        return _binary_search(array, target_value, middle + 1, end)
    else:
        return middle_value
