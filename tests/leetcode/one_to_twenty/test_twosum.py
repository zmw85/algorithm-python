from src.leetcode.one_to_twenty import twosum
import pytest

twosum_tests = [
    ([], 1, []),
    ([1, 8], None, []),
    ([1], 1, []),
    ([1, 8, 10, 20], 9, [0, 1]),
    ([2, 9, 11, 15], 26, [2, 3])
]


@pytest.mark.parametrize('arr,sum,expected', twosum_tests)
def test_twosum_1(arr, sum, expected):
    assert twosum.twosum_1(arr, sum) == expected


@pytest.mark.parametrize('arr,sum,expected', twosum_tests)
def test_twosum_2(arr, sum, expected):
    assert twosum.twosum_2(arr, sum) == expected
