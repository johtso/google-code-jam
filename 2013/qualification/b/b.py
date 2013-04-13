import sys
from itertools import islice, izip, imap

from utils import stripped_lines, ints


def possible(pattern):
    """Return whether grass pattern is possible."""
    rows = pattern
    columns = izip(*pattern)

    horizontal_impossible = []
    vertical_impossible = []

    for x, row in enumerate(rows):
        tallest = max(row)
        for y, height in enumerate(row):
            if height < tallest:
                horizontal_impossible.append((x, y))

    for y, column in enumerate(columns):
        tallest = max(column)
        for x, height in enumerate(column):
            if height < tallest:
                vertical_impossible.append((x, y))

    return not lists_overlap(horizontal_impossible, vertical_impossible)


def lists_overlap(a, b):
    sb = set(b)
    return any(imap(sb.__contains__, a))


def main():
    lines = stripped_lines(sys.stdin)
    numcases = int(lines.next())

    for i in range(numcases):
        size = ints(lines.next())[0]
        pattern = [ints(line) for line in islice(lines, size)]

        result = 'YES' if possible(pattern) else 'NO'

        print 'Case #%d: %s' % (i + 1, result)

if __name__ == '__main__':
    main()
