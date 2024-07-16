# cli.py

# Copyright (c) 2021 Rupert Rebentisch
# Licensed under the MIT license

"""The command line interface.

Click is used as backbone for the cli.
An excellent tutorial is found at "https://zetcode.com/python/click".
"""

import click
import os
from . import __version__
from .purgelily import (
    remove_layout_instructions,
    condense_lines,
    correct_tuplets
)
from .purgexml import remove_layout_instructions_from_xml
from pyfiglet import Figlet


def file_content(filename) -> str:
    content = []
    with open(filename, 'r') as afile:
        content = afile.read()
    return content


def file_content_line_by_line(filename) -> list[str]:
    try:
        with open(filename, 'r') as afile:
            content = afile.readlines()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)


def concat_lines(content: list[str]) -> str:
    return ''.join(content)


def append_step_to_filename(filepath, step_name):
    # Zerlegen des Pfades in Verzeichnis, Basisnamen und Erweiterung
    directory, filename = os.path.split(filepath)
    basename, extension = os.path.splitext(filename)
    # "_step1" an den Basisnamen anhängen
    new_basename = basename + step_name
    # Neuen Dateinamen im gleichen Verzeichnis zusammensetzen
    new_filepath = os.path.join(directory, new_basename + extension)
    return new_filepath


def write_file_content(filename, content):
    try:
        with open(filename, 'x') as afile:
            afile.write(content)
    except FileExistsError:
        print(f"Error: File '{filename}' already exists.")
        exit(1)
    except Exception as e:
        print(f"Error: Failed to write file '{filename}'.")
        print(f"Reason: {str(e)}")
        exit(1)


def purge_process(input_file):
    content = file_content(input_file)
    purged_content = remove_layout_instructions_from_xml(content)
    purged_content = purged_content.decode('utf-8')
    output_file = append_step_to_filename(input_file, '_step1')
    write_file_content(output_file, purged_content)
    exit(2)


def show_banner():
    f = Figlet(font='slant')
    print(f.renderText('scanscore2lilypond'))
    print("Copyright (c) 2021 Rupert Rebentisch, Version: ", __version__)


@click.command(help='purges input file')
@click.argument('filename')
@click.option(
    '-f',
    '--full',
    'mode',
    flag_value='full',
    default=False,
    help=(
        'runs the full process of purging a musicsxml file' +
        'assertand transforming it to a lylipond file which' +
        'will furthter be cleaned.'))
@click.option('-x',
              '--xml',
              'mode',
              flag_value='xml',
              default=False,
              help='input file is xml')
@click.option(
    '--output',
    '-o',
    'output_file',
    default=None,
    help='output file'
)
def purge(filename, output_file, mode):
    show_banner()
    if mode == 'full':
        purge_process(filename)
    elif mode == 'xml':
        content = file_content(filename)
        purged_content = remove_layout_instructions_from_xml(content)
        purged_content = purged_content.decode('utf-8')
    else:
        content = file_content_line_by_line(filename)
        content_without_layout_instructions = (
            remove_layout_instructions(content))
        content_with_corrected_tuplets = (
            correct_tuplets(content_without_layout_instructions))
        purged_content = condense_lines(content_with_corrected_tuplets)
        purged_content = concat_lines(
            content_with_corrected_tuplets
        )

    if output_file:
        print(f'writing to {output_file}')
        write_file_content(output_file, purged_content)
    else:
        print(purged_content)
