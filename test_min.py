def test_min(lst):
    """
    Find and return the minimum value in a list of integers.

    Parameters:
    lst (list): A list of integers.

    Returns:
    int: The minimum value in the list.

    Raises:
    ValueError: If the list is empty.
    """
    if not lst:
        raise ValueError("List is empty")
    
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    
    return min_val

def test_find_min():
    # Test an empty list
    try:
        test_min([])
    except ValueError as e:
        assert str(e) == "List is empty"
    else:
        assert False, "Expected ValueError for empty list was not raised"

    # Test a list with one item
    assert test_min([5]) == 5

    # Test a list with multiple items
    assert test_min([3, 5, 2, 8, 1]) == 1
