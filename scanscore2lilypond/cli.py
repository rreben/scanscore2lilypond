# cli.py

# Copyright (c) 2021 Rupert Rebentisch
# Licensed under the MIT license

"""The command line interface.

Click is used as backbone for the cli.
An excellent tutorial is found at "https://zetcode.com/python/click".
"""

import click
from . import __version__
from .purge import remove_layout_instructions, condense_lines

def file_content(filename) -> list[str]:
    content = []
    with open(filename, 'r') as afile:
        content = afile.readlines()
    return content


def write_file_content(filename, content):
    with open(filename, 'w') as afile:
        for line in content:
            afile.write(line + '\n')


@click.command(help='purges input file')
@click.argument('filename')
@click.option('--output', '-o', 'output_file', default=None, help='output file')
def purge(filename, output_file):
    content = file_content(filename)
    content_without_layout_instructions = remove_layout_instructions(content)
    purged_content = condense_lines(content_without_layout_instructions)
    if output_file:
        write_file_content(output_file, content_without_layout_instructions)
    else:
        for line in purged_content:
            print(line)
