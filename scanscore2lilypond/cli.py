# cli.py

# Copyright (c) 2021 Rupert Rebentisch
# Licensed under the MIT license

"""The command line interface.

Click is used as backbone for the cli.
An excellent tutorial is found at "https://zetcode.com/python/click".
"""

import click
from . import __version__
from .purgelily import remove_layout_instructions, condense_lines, correct_tuplets
from .purgexml import remove_layout_instructions_from_xml


def file_content(filename) -> str:
    content = []
    with open(filename, 'r') as afile:
        content = afile.read()
    return content


def file_content_line_by_line(filename) -> list[str]:
    content = []
    with open(filename, 'r') as afile:
        content = afile.readlines()
    return content


def concat_lines(content: list[str]) -> str:
    return ''.join(content)


def write_file_content(filename, content):
    with open(filename, 'w') as afile:
            afile.write(content)


@click.command(help='purges input file')
@click.argument('filename')
@click.option('-x', '--xml', 'mode', flag_value='xml', default=False, help='input file is xml')
@click.option('--output', '-o', 'output_file', default=None, help='output file')
def purge(filename, output_file, mode):
    if mode == 'xml':
        content = file_content(filename)
        purged_content = remove_layout_instructions_from_xml(content)
        purged_content = purged_content.decode('utf-8')
    else:
        content = file_content_line_by_line(filename)
        content_without_layout_instructions = remove_layout_instructions(content)
        content_with_corrected_tuplets = correct_tuplets(content_without_layout_instructions)
        purged_content = condense_lines(content_with_corrected_tuplets)
        purged_content = concat_lines(content_with_corrected_tuplets)

    if output_file:
        print(f'writing to {output_file}')
        write_file_content(output_file, purged_content)
    else:
        print(purged_content)
