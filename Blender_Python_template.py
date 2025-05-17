import bpy
import os

# Clear the system terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Clear all objects from the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Call all functions created below this function in this script here
def main():
    pass

# Functions for this file


# Prevent conflicts with other add-ons
if __name__ == '__main__':
    main()