import sys
from itertools import islice
from collections import namedtuple

from utils import stripped_lines, ints


Chest = namedtuple('Chest', ['number', 'lock', 'contents'])


def solve(starting_keys, chests):
    """Return order of chests to open."""
    chests = [Chest(i, chest[0], chest[1])
              for i, chest in enumerate(chests, start=1)]

    return find_sequence([], starting_keys, chests)


def find_sequence(path, keys, chests):
    """Recursively search for successful sequence of chest unlocks."""
    for key in set(keys):
        openable = (chest for chest in chests if chest.lock == key)

        for chest in openable:
            new_keys = keys[:]
            new_keys.remove(key)
            new_keys += chest.contents
            new_chests = chests[:]
            new_chests.remove(chest)
            new_path = path + [chest.number]
            if not new_chests:
                return new_path
            else:
                result = find_sequence(new_path, new_keys, new_chests)
                if result:
                    return result
    return None


def main():
    lines = stripped_lines(sys.stdin)
    numcases = int(lines.next())

    for i in range(numcases):
        numchests = ints(lines.next())[1]
        starting_keys = ints(lines.next())
        chest_lines = (ints(line) for line in islice(lines, numchests))
        chests = [(chest_line[0], set(chest_line[2:]))
                  for chest_line in chest_lines]

        result = solve(starting_keys, chests)
        output = ' '.join(map(str, result)) if result else 'IMPOSSIBLE'
        print 'Case #%d: %s' % (i + 1, output)

if __name__ == '__main__':
    main()
