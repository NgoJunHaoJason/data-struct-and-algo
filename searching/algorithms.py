def linear_search(array: list[int], target_value: int) -> int:
    for index, value in enumerate(array):
        if value == target_value:
            return index
    return -1
