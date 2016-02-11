import numpy

"""
:returns (int n_rows, int n_cols, numpy.array data)
"""
def parse_file(file_name):
    with open(file_name, 'r') as f:
        n_rows, n_cols, n_drones, deadline, max_load = [int(x) for x in f.readline().split()]
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