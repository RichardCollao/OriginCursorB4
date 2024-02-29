import bpy

class OBJECT_ORIGIN_SETTER(bpy.types.Operator):
    bl_idname = "object.vertex_cursor_operator"
    bl_label = "Move Cursor to Selected Vertex"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.obj = bpy.context.active_object
        
        # Verifica si hay un objeto activo y si es de tipo malla
        if self.obj and self.obj.type == 'MESH':
            # Cambia a modo objeto si está en modo de edición
            bpy.ops.object.mode_set(mode='OBJECT')

            # Verifica si hay al menos un vértice seleccionado
            if any(v.select for v in self.obj.data.vertices):
                # Encuentra el primer vértice seleccionado
                selected_vertex = next(v for v in self.obj.data.vertices if v.select)

                # Establece la posición del cursor 3D en el vértice seleccionado
                bpy.context.scene.cursor.location = self.obj.matrix_world @ selected_vertex.co
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
                bpy.ops.object.mode_set(mode='EDIT')

        return {'FINISHED'}

hotkey = None
        
def register():
    bpy.utils.register_class(OBJECT_ORIGIN_SETTER)
    
    global hotkey
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc and not hotkey:
        km = wm.keyconfigs.addon.keymaps.new(name="3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new(OBJECT_ORIGIN_SETTER.bl_idname, type='C', value='PRESS', ctrl=True, shift=True)

        hotkey = (km, kmi)

def unregister():
    bpy.utils.unregister_class(OBJECT_ORIGIN_SETTER)
    
    global hotkey
    if hotkey:
        km, kmi = hotkey
        km.keymap_items.remove(kmi)
        hotkey = None

if __name__ == "__main__":
    register()
