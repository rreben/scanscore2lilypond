# purge.py
# Copyright (c) 2022 Dr. Rupert Rebentisch
# Licensed under the MIT license

import re

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

def condense_lines(content: list[str]) -> list[str]:
    """Condenses lines with multiple notes into one line per bar.

    Args:
        content (list): The content of the file.

    Returns:
        list: The content of the file with condensed lines.
    """
    new_content = []
    condensed_line = ''
    for line in content:
        if re.search(r'^\s*[rsabcdefg](es)*(is)*[\,\']*[12345678]\.*', line):
            # line starts with a note or a rest or a silent note
            condensed_line += line
        elif re.search(r'^\s*\|', line):
            # line starts with a bar so we can add the condensed line
            condensed_line += line
            condensed_line = re.sub(r'\s+', ' ', condensed_line)
            new_content.append(condensed_line)
            condensed_line = ''
        else:
            # in all other cases we just add the line and any input of condensed line
            # we might have so far
            if condensed_line:
                condensed_line = re.sub(r'\s+', ' ', condensed_line)
                new_content.append(condensed_line)
                condensed_line = ''
            new_content.append(line)
    return new_content
