from setuptools.command.build_ext import if_dl

import bpy
import os

from bl_i18n_utils.settings import CHECK_PRINTF_FORMAT
from helper_functions import *

# Clear the system terminal
os.system('cls' if os.name == 'nt' else 'clear')


# Call all functions created below this function in this script here
def main():
    select(object_types = 'MESH')


# Functions for this file
def select(*object_names, object_types = None):
    """
    This function is designed to select multiple
    objects by their name and type.

    select() will deselect all objects
    select(type='ALL') will select all objects
    """
    # Check if objects exist
    number_of_objects = len(all_objects())
    if number_of_objects == 0:
        print('No objects')
    else:
        # Select ALL
        if object_types is None or object_types == []:
            for obj in all_objects():
                obj.select_set(False)

        elif object_types == 'ALL':
            for obj in all_objects():
                obj.select_set(True)

        elif object_types == 'MESH':
            for obj in all_objects():
                if obj.type == 'MESH':
                    obj.select_set(True)
                else:
                    obj.select_set(False)

        # Select ALL by type
        # Select objects by name
        # Invert current selection
        print(number_of_objects)


    for item in object_names:
        all_objects()[item].select_set(True)

# Prevent conflicts with other add-ons
if __name__ == '__main__':
    main()
