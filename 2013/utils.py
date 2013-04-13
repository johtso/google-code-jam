def stripped_lines(lines):
    return (line.rstrip('\n') for line in lines)


def ints(s):
    return [int(num) for num in s.split()]
