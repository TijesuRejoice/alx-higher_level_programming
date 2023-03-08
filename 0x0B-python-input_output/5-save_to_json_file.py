#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_pbj, filename):
    """Write an object to the text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
