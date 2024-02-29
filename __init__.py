bl_info = {
    "name" : "OriginCursor",
    "author" : "Richard Collao",
    "description" : "",
    "blender" : (4, 0, 3),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . origin_cursor import OBJECT_ORIGIN_SETTER 

def register():
    origin_cursor.register()

def unregister():
    origin_cursor.unregister()