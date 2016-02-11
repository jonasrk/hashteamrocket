import numpy

"""
:returns (int n_rows, int n_cols, numpy.array data)
"""
def parse_file_numpy(file_name):
    with open(file_name, 'r') as f:
        n_rows, n_cols = [int(x) for x in f.readline().split()]

    # caveat: numpy parses bytes instead of strings!
    converters = dict.fromkeys([x for x in range(n_cols)], lambda s: s == b'#')

    data = numpy.genfromtxt(file_name, dtype=bool, comments=None,
                            delimiter=1,  # column width = 1
                            skip_header=1, converters=converters)
    return (n_rows, n_cols, data)


"""
:returns (int n_rows, int n_cols, numpy.array data)
"""
def parse_file_manual(file_name):
    with open(file_name, 'r') as f:
        n_rows, n_cols = [int(x) for x in f.readline().split()]
        data = numpy.empty((n_rows, n_cols), dtype=bool)
        for i in range(n_rows):
            row = [x == '#' for x in f.readline().strip()]
            data[i] = row
    return (n_rows, n_cols, data)


def print_bool_array(array):
    numpy.set_printoptions(threshold=numpy.nan, formatter={'bool': lambda b: '#' if b else '.'}, linewidth=numpy.nan)
    print(array)


"""
:return array of command strings
"""
def simple_squares(data):
    commands = []
    for ((r, c), field) in numpy.ndenumerate(data):
        if field:
            commands.append('PAINT_SQUARE %d %d 0' % (r, c))
    return commands

def write_commands(commands, file_name):
    with open(file_name, 'w') as f:
        f.write('%d\n' % len(commands))
        for c in commands:
            f.write(c + '\n')


if __name__ == '__main__':
    n_rows, n_cols, data = parse_file_manual('data/logo.in')
    # print_bool_array(data)
    commands = simple_squares(data)
    write_commands(commands, 'output')