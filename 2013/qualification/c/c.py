import sys
import math
from itertools import ifilter


from utils import stripped_lines, ints


def solve(start, stop):
    """Return whether grass pattern is possible."""

    def root_predicate(n):
        return palindrome(str(n))

    return sum(1 for candidate in perfect_squares(start, stop, root_predicate)
               if palindrome(str(candidate)))


def palindrome(iterable):
    """Returns whether the iterable is a palindrome."""
    return iterable == iterable[::-1]


def perfect_squares(start, stop, root_predicate):
    lowest = int(math.ceil(math.sqrt(start)))
    heighest = int(math.sqrt(stop))
    roots = ifilter(root_predicate, xrange(lowest, heighest + 1))
    return (square(n) for n in roots)


def square(n):
    return n**2


def main():
    lines = stripped_lines(sys.stdin)
    numcases = int(lines.next())

    for i in range(numcases):
        start, stop = ints(lines.next())

        total = solve(start, stop)

        print 'Case #%d: %s' % (i + 1, total)

if __name__ == '__main__':
    main()
