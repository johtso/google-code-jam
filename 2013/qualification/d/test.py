import pytest

import d


@pytest.mark.parametrize(('starting_keys', 'chests', 'expected'), [
    ([1], [(1, []),
           (1, [1, 3]),
           (2, []),
           (3, [2])], [2, 1, 4, 3]),
    ([1, 1, 1], [(1, []),
                 (1, []),
                 (1, [])], [1, 2, 3]),
    ([2], [(1, [1])], None)
])
def test_solve(starting_keys, chests, expected):
    result = d.solve(starting_keys, chests)
    assert result == expected
