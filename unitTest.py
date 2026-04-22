import pytest
from merge_of_two_lists import merge_lists

MERGE_LISTS_TEST_CASES = [

    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),  # Caso normal
    ([1, 2, 3], [], [1, 2, 3]),                  # Una lista vacía
    ([], [4, 5, 6], [4, 5, 6]),                  # La otra vacía
]  

@pytest.mark.parametrize("arr1, arr2, expected", MERGE_LISTS_TEST_CASES)
def test_merge_lists(arr1, arr2, expected):
    assert merge_lists(arr1.copy(), arr2.copy()) == expected