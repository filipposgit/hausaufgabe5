def find_single_number(numbers):
    if len(numbers) == 0:
        raise ValueError("The list must not be empty.")

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    single_numbers = []

    for number, count in counts.items():
        if count == 1:
            single_numbers.append(number)
        elif count != 2:
            raise ValueError("All numbers must appear exactly twice except one.")

    if len(single_numbers) != 1:
        raise ValueError("There must be exactly one single number.")

    return single_numbers[0]
