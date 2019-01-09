import longest_substring as ls
import pytest

tests = [
    (None, 0),
    ('', 0),
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3)
]


@pytest.mark.parametrize('s,expected', tests)
def test_longest_substring_1(s, expected):
    assert ls.longest_substring_1(s) == expected


@pytest.mark.parametrize('s,expected', tests)
def test_longest_substring_2(s, expected):
    assert ls.longest_substring_2(s) == expected


@pytest.mark.parametrize('s,expected', tests)
def test_longest_substring_3(s, expected):
    assert ls.longest_substring_3(s) == expected
