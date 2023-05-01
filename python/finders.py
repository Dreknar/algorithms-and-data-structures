def find_max(numbers: list) -> float:
    """
    Find the biggest value on the list. It works similar to max().
    Arguments:
        numbers (list): list of numbers
    Returns:
        (float): the biggest value from the list
    """
    result = numbers[0]
    for value in numbers:
        if result < value:
            result = value

    return result


def find_min(numbers: list) -> float:
    """
    Find the smallest value on the list. It works like min().
    Arguments:
        numbers (list): list of numbers
    Returns:
        (float): the smallest value from the list
    """
    result = numbers[0]
    for value in numbers:
        if result > value:
            result = value

    return result


def find_longest_series(numbers: list, asc=True) -> list:
    """
    Find the longest ascending/descending series in list. Including equal values!
    Arguments:
        numbers (list): list of numbers
        asc (bool): find ascending series (default). Set False for descending order.

    Returns:
        (list): the longest ascending/descending series
    """
    longest_series = 0
    current_series = 1
    last_item = 0
    first_item = 0

    if asc:
        for i in range(1, len(numbers)):
            if numbers[i] > numbers[i - 1]:
                current_series += 1
            elif current_series > longest_series:
                longest_series = current_series
                current_series = 1
                last_item = i
                first_item = i - longest_series
            else:
                current_series = 1

        if current_series > longest_series:
            longest_series = current_series
            last_item = len(numbers)
            first_item = last_item - longest_series
    else:
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i - 1]:
                current_series += 1
            elif current_series > longest_series:
                longest_series = current_series
                current_series = 1
                last_item = i
                first_item = i - longest_series
            else:
                current_series = 1

        if current_series > longest_series:
            longest_series = current_series
            last_item = len(numbers)
            first_item = last_item - longest_series

    return numbers[first_item:last_item]
