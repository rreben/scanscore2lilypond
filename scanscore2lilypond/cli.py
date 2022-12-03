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

@click.command(help='purges input file')
@click.argument('filename')
def purge(filename):
    content = file_content(filename)
    for line in condense_lines(remove_layout_instructions( content)):
        print(line)
