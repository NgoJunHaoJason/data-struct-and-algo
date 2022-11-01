def binary_search(sorted_array: list[int], target_value: int) -> int:
    """Search for the target value in a sorted array of size n,
    checking only half of the array in subsequent invocations

    Analysis
    --------
    - worst case: value is not in array, or is last element of array
    - time complexity: O(log n)
    - additional data structures used: None
    - space complexity: O(1)

    Parameters
    ----------
    array : list[int]
        The array to search in
    target_value : int
        The value to search for

    Returns
    -------
    int
        the index of the value if found (-1 if not found)
    """
    return (
        -1
        if len(sorted_array) == 0
        else _binary_search(sorted_array, target_value, 0, len(sorted_array) - 1)
    )


def _binary_search(
    sorted_array: list[int],
    target_value: int,
    start: int,
    end: int,
) -> int:
    if start >= end:
        return start if sorted_array[start] == target_value else -1

    middle = (start + end) // 2
    middle_value = sorted_array[middle]

    if middle_value > target_value:
        return _binary_search(sorted_array, target_value, start, middle - 1)
    elif middle_value < target_value:
        return _binary_search(sorted_array, target_value, middle + 1, end)
    else:
        return middle_value
