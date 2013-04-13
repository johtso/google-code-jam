import pytest

import a


@pytest.mark.parametrize(('line', 'expected'), [
    ('....', None),
    ('.XXX', None),
    ('XXXX', 'X'),
    ('OOOO', 'O'),
    ('TXXX', 'X'),
])
def test_winning(line, expected):
    assert a.winning(line) == expected


def test_lines_of_four():
    grid = ['1234',
            '5678',
            '9ABC',
            'DEFG']

    expected = set(
        grid +    # Rows
        ['159D',  # Columns
         '26AE',
         '37BF',
         '48CG'] +
        ['16BG',  # Diagonals
         '47AD']
    )

    result = a.lines_of_four(grid)
    lines = [''.join(line) for line in result]

    assert set(lines) == expected


@pytest.mark.parametrize(('grid', 'expected'), [
    (['XXXT',
      '....',
      'OO..',
      '....'], 'X won'),
    (['XOXT',
      'XXOO',
      'OXOX',
      'XXOO'], 'Draw'),
    (['XOX.',
      'OX..',
      '....',
      '....'], 'Game has not completed'),
    (['OOXX',
      'OXXX',
      'OX.T',
      'O..O'], 'O won'),
    (['XXXO',
      '..O.',
      '.O..',
      'T...'], 'O won'),
    (['OXXX',
      'XO..',
      '..O.',
      '...O'], 'O won'),
])
def test_solve(grid, expected):
    assert a.solve(grid) == expected
