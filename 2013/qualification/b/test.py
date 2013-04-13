import pytest

import b


@pytest.mark.parametrize(('pattern', 'expected'), [
    ([[2, 1, 2],
      [1, 1, 1],
      [2, 1, 2]], True),

    ([[2, 2, 2, 2, 2],
      [2, 1, 1, 1, 2],
      [2, 1, 2, 1, 2],
      [2, 1, 1, 1, 2],
      [2, 2, 2, 2, 2]], False),

    ([[1, 2, 1]], True),
])
def test_possible(pattern, expected):
    assert b.possible(pattern) == expected
