import os

filename = os.path.join("/Users/brianspeight/Dev/Python/Blender", "test_1.py")
exec(compile(open(filename).read(), filename, 'exec'))