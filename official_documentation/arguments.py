"""
Example command:

    python official_documentation/arguments.py\
        string\                            # string
        123\                               # int
        1.23\                              # float
        yes\                               # bool
        official_documentation/\           # path
        official_documentation/test_file\  # file
        2                                  # choice (1 or 2)
        5                                  # int in range (0 to 10)

Custom arguments:

    http://click.pocoo.org/6/parameters/#implementing-custom-types
"""

import click


@click.command()
@click.argument('string', type=click.STRING)
@click.argument('num_int', type=click.INT)
@click.argument('num_float', type=click.FLOAT)
@click.argument('boolean', type=click.BOOL)
@click.argument('path', type=click.Path(exists=True))
@click.argument('file', type=click.File(mode='r'))
@click.argument('choice', type=click.Choice(['1', '2']))
@click.argument('int_range', type=click.IntRange(min=0, max=10))
def cli(string, num_int, num_float, boolean, path, file, choice, int_range):
    print(string, type(string))
    print(num_int, type(num_int))
    print(num_float, type(num_float))
    print(boolean, type(boolean))
    print(path, type(path))
    print(file.readlines(), type(file))
    print(choice, type(choice))
    print(int_range, type(int_range))

if __name__ == '__main__':
    cli()
