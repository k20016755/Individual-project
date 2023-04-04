import random
import pytest

@pytest.fixture
def lst():
    return [random.randint(1,100) for _ in range(random.randint(1,10))]
def test_min(lst):
    if not lst:
        raise ValueError("List is empty")
    
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    
    return min_val
@pytest.mark.benchmark
def test_lst():
    try:
        test_min([])
    except ValueError as e:
        assert str(e) == "List is empty"
    else:
        assert False, "Expected ValueError for empty list was not raised"

   
    assert test_min([5]) == 5

    
    assert test_min([3, 5, 2, 8, 1]) == 1
