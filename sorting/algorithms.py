def insertion_sort(array: list[int]) -> None:
    for unsorted_index in reversed(range(len(array) - 1)):
        value_to_insert = array[unsorted_index]

        for sorted_index in range(unsorted_index + 1, len(array)):

            if value_to_insert <= array[sorted_index]:
                break

            array[sorted_index - 1] = array[sorted_index]
            array[sorted_index] = value_to_insert


def merge_sort(array: list[int]) -> None:
    _merge_sort(array, 0, len(array) - 1)


def _merge_sort(array: list[int], start: int, end: int) -> None:
    if start >= end:
        return

    middle = (start + end) // 2

    _merge_sort(array, start, middle)
    _merge_sort(array, middle + 1, end)

    _merge(
        array,
        start1=start,
        end1=middle,
        start2=middle + 1,
        end2=end,
    )


def _merge(
    array: list[int],
    start1: int,
    end1: int,
    start2: int,
    end2: int,
) -> None:
    subarray1 = array[start1 : end1 + 1]
    subarray2 = array[start2 : end2 + 1]

    length1, length2 = len(subarray1), len(subarray2)

    from_index1, from_index2 = 0, 0
    insert_index = start1

    while from_index1 < length1 and from_index2 < length2:
        if subarray1[from_index1] > subarray2[from_index2]:
            array[insert_index] = subarray2[from_index2]
            from_index2 += 1

        else:
            array[insert_index] = subarray1[from_index1]
            from_index1 += 1

        insert_index += 1

    if from_index1 < length1:
        array[insert_index : end2 + 1] = subarray1[from_index1:length1]

    elif from_index2 < length2:
        array[insert_index : end2 + 1] = subarray2[from_index2:length2]

    else:
        raise RuntimeError
