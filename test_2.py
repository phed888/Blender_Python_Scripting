from setuptools.command.build_ext import if_dl

import bpy
import os

from bl_i18n_utils.settings import CHECK_PRINTF_FORMAT
from helper_functions import *

# Clear the system terminal
os.system('cls' if os.name == 'nt' else 'clear')


# Call all functions created below this function in this script here
def main():
    select(types = ['LIGHT'])


# Functions for this file
def select(*object_names, **kwargs):
    """
    This function is designed to select multiple
    objects by their name and type.

    Named objects can be listed first in the parenthesis (comma-separated)
    after names, then list types as array preceded by 'types ='

    select() will deselect all objects
    select(types='ALL') will select all objects
    select(types=['MESH', 'EMPTY']) will select all the types in the list
    select('Name') will select all objects by their name.
    """

    types = kwargs.get('types')

    # Check if objects exist
    number_of_objects = len(all_objects())
    if number_of_objects == 0:
        print('No objects in scene')

    else:
        match types:

            case None:
                for obj in all_objects():
                    obj.select_set(False)

            case 'ALL':
                for obj in all_objects():
                    obj.select_set(True)

            case _:
                for obj in all_objects():
                    if obj.type in types:
                        obj.select_set(True)
                    else:
                        obj.select_set(False)

        # # Deselect ALL
        # if types is None or types == []:
        #     for obj in all_objects():
        #         obj.select_set(False)
        #
        # # Select ALL
        # elif types == 'ALL':
        #     for obj in all_objects():
        #         obj.select_set(True)
        #
        # # Select by type
        # else:
        #     for obj in all_objects():
        #         if obj.type in types:
        #             obj.select_set(True)
        #         else:
        #             obj.select_set(False)

        # Select objects by name
        if object_names is not None:
            for obj in object_names:
                all_objects()[obj].select_set(True)

    # Invert current selection


# Prevent conflicts with other add-ons
if __name__ == '__main__':
    main()
