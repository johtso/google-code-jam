import pytest

import c


@pytest.mark.parametrize(('start', 'stop', 'expected'), [
    (1, 4, 2),
    (10, 120, 0),
    (100, 1000, 2),
])
def test_solve(start, stop, expected):
    assert c.solve(start, stop) == expected


@pytest.mark.parametrize(('iterable', 'expected'), [
    ('1', True),
    ('10', False),
    ('101', True),
    ('110', False),
])
def test_palindrome(iterable, expected):
    assert c.palindrome(iterable) == expected
