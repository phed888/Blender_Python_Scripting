import bpy

bl_info = {
    "name": "Example Add-on",
    "author": "Brian",
    "version": (0, 0, 1),
    "blender": (4, 4, 1),
    "category": "Generic",
    "location": "View3D",
}

# Add your Blender classes here after importing them
# classes = ()
# register, unregister = bpy.utils.register_classes_factory(classes)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
# if __name__ == "__main__":
#     register()

def register():
    print("Hello World")
def unregister():
    print("Goodbye World")

