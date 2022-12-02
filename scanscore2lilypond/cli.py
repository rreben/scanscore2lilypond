# cli.py

# Copyright (c) 2021 Rupert Rebentisch
# Licensed under the MIT license

"""The command line interface.

Click is used as backbone for the cli.
An excellent tutorial is found at "https://zetcode.com/python/click".
"""

import click
from . import __version__


@click.command(help='purges input file')
@click.argument('filename')
def purge(filename):
    """Print FILENAME."""
    click.echo(filename)

