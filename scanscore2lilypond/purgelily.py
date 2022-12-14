# purgelily.py
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
        new_line = re.sub(r'\\once \\omit TupletBracket', '', line)
        new_line = re.sub(r'\\break', '', new_line)
        new_line = re.sub(r'\\pageBreak', '', new_line)
        new_line = re.sub(r'\\barNumberCheck \#\d+', '', new_line)
        new_line = re.sub(r'\\bar \"\|\"', '|', new_line)
        new_line = re.sub(r'\| \% \d+', '|', new_line)
        new_content.append(new_line)
        
    return new_content

def correct_tuplets(content: list[str]) -> list[str]:
    """Corrects tuplets.

    Args:
        content (list): The content of the file.

    Returns:
        list: The content of the file with corrected tuplets.
    """
    new_content = []
    for line in content:
        new_line = re.sub(r'\\times 2\/3\s+{', r'\\tuplet 3/2 {', line)
        new_line = re.sub(r'\*3/2', '', new_line)
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
        if re.search(r'^\s*[rsabcdefg](es)*(is)*[\,\']*[12345678]+\.*', line):
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
