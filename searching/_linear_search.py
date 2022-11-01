def linear_search(array: list[int], target_value: int) -> int:
    """Search for the target value in an array of size n, in sequence

    Analysis
    --------
    - worst case: value is not in array, or is last element of array
    - time complexity: O(n)
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
        the index of the first occurrence of the value if found (-1 if not found)
    """
    for index, value in enumerate(array):
        if value == target_value:
            return index
    return -1
