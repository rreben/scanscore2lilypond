# purgelily.py
# Copyright (c) 2022 Dr. Rupert Rebentisch
# Licensed under the MIT license

import re


def remove_global_staff_and_layout(content: list[str]) -> list[str]:
    """Removes global staff size, paper size,
    and layout instructions from the content.

    Args:
        content (list): The content of the file.

    Returns:
        list: The content of the file without the specified instructions.
    """
    new_content = []
    skip_block = False
    brace_count = 0

    for line in content:
        # Check for lines that should be removed or skipped
        # This line removes the global staff size directive
        if re.match(r'#\(set-global-staff-size', line):
            continue
        # These lines detect the start of a \paper or \layout block
        # and initiate skipping of those blocks
        elif re.match(r'\\paper', line) or re.match(r'\\layout', line):
            skip_block = True
            # Initialize brace count based on the current line
            brace_count = line.count('{') - line.count('}')
            continue

        if skip_block:
            # Update the brace count to track the depth of the block
            brace_count += line.count('{') - line.count('}')
            # Check if we have exited the block
            if brace_count <= 0:
                skip_block = False
            continue

        # Add the line to the new content
        # if it's not in a block that should be skipped
        if not skip_block:
            new_content.append(line)

    return new_content


def replace_point_and_click(content: list[str]) -> list[str]:
    """Replaces \\pointAndClickOff with \\pointAndClickOn in the content.

    Args:
        content (list): The content of the file.

    Returns:
        list: The content of the file with the replaced command.
    """
    new_content = []
    for line in content:
        new_line = re.sub(r'\\pointAndClickOff', r'\\pointAndClickOn', line)
        new_content.append(new_line)
    return new_content


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
            # in all other cases we just add the line
            # and any input of condensed line
            # we might have so far
            if condensed_line:
                condensed_line = re.sub(r'\s+', ' ', condensed_line)
                new_content.append(condensed_line)
                condensed_line = ''
            new_content.append(line)
    return new_content
