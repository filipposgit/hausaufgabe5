import pytest

from single_number import find_single_number


def test_single_number_basic_example():
    numbers = [1, 2, 3, 4, 3, 1, 2]

    result = find_single_number(numbers)

    assert result == 4


def test_single_number_with_one_element():
    numbers = [7]

    result = find_single_number(numbers)

    assert result == 7


def test_single_number_with_negative_numbers():
    numbers = [-1, -2, -1, -3, -2]

    result = find_single_number(numbers)

    assert result == -3


def test_single_number_with_zero():
    numbers = [0, 5, 5, 8, 8]

    result = find_single_number(numbers)

    assert result == 0


def test_single_number_unsorted_longer_list():
    numbers = [10, 3, 5, 10, 3, 8, 5, 9, 9]

    result = find_single_number(numbers)

    assert result == 8


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        find_single_number([])


def test_even_length_list_raises_value_error():
    with pytest.raises(ValueError):
        find_single_number([1, 1, 2, 2])


def test_no_single_number_raises_value_error():
    with pytest.raises(ValueError):
        find_single_number([1, 1, 2, 2, 3, 3])


def test_more_than_one_single_number_raises_value_error():
    with pytest.raises(ValueError):
        find_single_number([1, 2, 3, 1, 2, 4])

def test_required_libraries_are_installed():
    import numpy
    import pandas
    import matplotlib
    import seaborn

    assert numpy is not None
    assert pandas is not None
    assert matplotlib is not None
    assert seaborn is not None
