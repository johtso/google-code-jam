import sys
from itertools import islice, izip

from utils import stripped_lines, ints


def possible(pattern):
    """Return whether grass pattern is possible."""
    rows = pattern
    columns = izip(*pattern)

    impossible = set()

    for swathes, is_vertical in [(rows, False), (columns, True)]:
        for swathe_number, swathe in enumerate(swathes):
            tallest = max(swathe)
            for patch_number, height in enumerate(swathe):
                if height < tallest:
                    if is_vertical:
                        location = (patch_number, swathe_number)
                    else:
                        location = (swathe_number, patch_number)

                    if location in impossible:
                        return False
                    else:
                        impossible.add(location)

    return True


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
