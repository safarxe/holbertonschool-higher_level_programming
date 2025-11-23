#!/usr/bin/python3
"""
Module for serializing and deserializing with XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to a file.

    Args:
        dictionary: A Python dictionary to serialize
        filename: The filename to save the XML data to
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file and returns a Python dictionary.

    Args:
        filename: The filename to load the XML data from

    Returns:
        dict: A Python dictionary with the deserialized data
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary

