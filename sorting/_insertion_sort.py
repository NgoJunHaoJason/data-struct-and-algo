def insertion_sort(array: list[int]) -> None:
    for unsorted_index in reversed(range(len(array) - 1)):
        value_to_insert = array[unsorted_index]

        for sorted_index in range(unsorted_index + 1, len(array)):

            if value_to_insert <= array[sorted_index]:
                break

            array[sorted_index - 1] = array[sorted_index]
            array[sorted_index] = value_to_insert
