# purgexml.py
# Copyright (c) 2022 Dr. Rupert Rebentisch
# Licensed under the MIT license

import xml.etree.ElementTree as ET

def remove_layout_instructions_from_xml(content) -> str:
    
    new_content = []
   # Parse the MusicXML file
    tree = ET.fromstring(content)
    note_elements = []

    # Find the layout element
    layout_element = tree.find('.//layout')

    # If the layout element exists, remove it
    if layout_element is not None:
        layout_element.clear()

    # Find all note elements
    note_elements = tree.findall('.//note')
    print ('number of notes: ', len(note_elements))

    # Remove stem and color information from each note element
    for note_element in note_elements:
        stem_element = note_element.find('stem')
        if stem_element is not None:
            stem_element.clear()
        color_element = note_element.find('color')
        if color_element is not None:
            color_element.clear()
        note_element.attrib.pop('color', None)

# Write the modified MusicXML file
    new_content = ET.tostring(tree)
    return new_content