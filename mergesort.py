def merge_sort(numbers):
    """
    Sortiert eine Liste von Zahlen mit dem Merge-Sort-Algorithmus.

    Der Algorithmus teilt die Liste rekursiv in kleinere Listen auf,
    sortiert diese und fügt sie anschließend wieder geordnet zusammen.
    """
    if len(numbers) <= 1:
        return numbers

    middle_index = len(numbers) // 2
    left_half = numbers[:middle_index]
    right_half = numbers[middle_index:]

    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)

    return merge(sorted_left_half, sorted_right_half)


def merge(left_half, right_half):
    """
    Fügt zwei bereits sortierte Listen zu einer sortierten Liste zusammen.
    """
    sorted_numbers = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            sorted_numbers.append(left_half[left_index])
            left_index += 1
        else:
            sorted_numbers.append(right_half[right_index])
            right_index += 1

    sorted_numbers.extend(left_half[left_index:])
    sorted_numbers.extend(right_half[right_index:])

    return sorted_numbers


if __name__ == "__main__":
    example_numbers = [5, 3, 8, 4, 2, 7, 1, 6]
    sorted_numbers = merge_sort(example_numbers)

    print("Unsorted list:", example_numbers)
    print("Sorted list:", sorted_numbers)
