import bpy
import os
from helper_functions import *

# Clear the system terminal
os.system('cls' if os.name == 'nt' else 'clear')


# Call all functions created below this function in this script here
def main():
    # list_of_items = ['Cube', 'Camera']
    select_by_name('Cube', 'Camera', 'Light')


# Functions for this file
def select_by_name(*object_names):
    for item in object_names:
        all_objects()[item].select_set(True)

# Prevent conflicts with other add-ons
if __name__ == '__main__':
    main()
