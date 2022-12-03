# purge.py
# Copyright (c) 2022 Dr. Rupert Rebentisch
# Licensed under the MIT license

import re

def file_content(filename) -> list[str]:
    content = []
    with open(filename, 'r') as afile:
        content = afile.readlines()
    return content

def remove_layout_instructions(content: list[str]) -> list[str]:
    """Removes layout instructions from the content.

    Args:
        content (list): The content of the file.

    Returns:
        list: The content of the file without layout instructions.
    """
    new_content = []
    for line in content:
        new_line = re.sub(r'\\once \\override Stem\.color', '', line)
        new_line = re.sub(r' \= \#\(rgb-color 0\.0 0\.0 0\.0\)', '', new_line)
        new_line = re.sub(r' \= \#\(rgb-color( 0\.0)*', '', new_line)
        new_line = re.sub(r'^\w*(0\.0)* *0\.0+\)', '', new_line)
        new_line = re.sub(r'\\stemUp', '', new_line)
        new_line = re.sub(r'\\stemDown', '', new_line)
        new_line = re.sub(r'\\break', '', new_line)
        new_line = re.sub(r'\\pageBreak', '', new_line)
        new_line = re.sub(r'\\bar \"\|\"', '|', new_line)
        new_line = re.sub(r'\| \% \d+', '|', new_line)
        new_line = re.sub(r'\n$', '', new_line)
        new_content.append(new_line)
        
    return new_content