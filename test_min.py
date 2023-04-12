import random
import pytest

def lst():
    return [random.randint(1,100) for _ in range(random.randint(1,10))]

def specify_min(lst):
    if not lst:
        raise ValueError("List does not contain anything")
    
    minimum_value = lst[0]
    for num in lst:
        if num < minimum_value:
            minimum_value = num
    
    return minimum_value
def test_lst():
    try:
        specify_min([])
    except ValueError as e:
        assert str(e) == "List does not contain anything"
    else:
        assert False, "Value Error not raised"

   
    assert specify_min([5]) == 5

    assert specify_min([2,2,1,3,10,1]) == 1
    assert specify_min([3,4,6,9,1]) == 1
