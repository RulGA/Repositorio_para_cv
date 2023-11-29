##### ORDENAR VÉRTICES #####

def order_vertex_list(vertex_list=None, direction='rl'):
    """
    Ordena una lista de vértices en función de su posición en una dirección determinada.

    Parameters:
    vertex_list (list): Lista de vértices a ordenar.
    direction (str): Dirección en la que se realizará el orden ('rl' para de derecha a izquierda, 'lr' para lo contrario).

    Returns:
    list: Lista ordenada de vértices.
    """

    # 1. Encontrar los vértices que son extremos, que solo tienen otro vértice adyacente.
    tips_vertex = []
    for vtx in vertex_list:
        vtx_to_edges = cmds.polyListComponentConversion(vtx, toEdge=True)
        edges_to_vtx = cmds.polyListComponentConversion(vtx_to_edges, toVertex=True)
        edges_to_vtx = cmds.ls(edges_to_vtx, fl=True)
        common_vtx = [x for x in edges_to_vtx if x in vertex_list]
        if len(common_vtx) == 2:
            tips_vertex.append(vtx)
    
    # 2. Determinar cuál es el primer y el último vértice
    tips_vertex_positions = []
    first_tip_vertex_position = cmds.xform(tips_vertex[0], query=True, translation=True, worldSpace=True)[0]
    second_tip_vertex_position = cmds.xform(tips_vertex[1], query=True, translation=True, worldSpace=True)[0]
    
    if first_tip_vertex_position < second_tip_vertex_position:
        if direction == 'rl':
            first_vertex =  tips_vertex[0]
            end_vertex = tips_vertex[1]
        else:
            first_vertex =  tips_vertex[1]
            end_vertex = tips_vertex[0]
    else:
        if direction == 'rl':
            first_vertex =  tips_vertex[1]
            end_vertex = tips_vertex[0]
        else:
            first_vertex =  tips_vertex[0]
            end_vertex = tips_vertex[1]
    
    # 3. Ordenar lista de vértices
    copy_vertex_list = vertex_list.copy()
    ordered_vertex_list = [None] * len(vertex_list)
    
    ordered_vertex_list[0] = first_vertex
    copy_vertex_list.remove(first_vertex)
    ordered_vertex_list[-1] = end_vertex
    copy_vertex_list.remove(end_vertex)
    
    i=1
    while copy_vertex_list:
        for vtx in copy_vertex_list:
            vtx_to_edges = cmds.polyListComponentConversion(vtx, toEdge=True)
            edges_to_vtx = cmds.polyListComponentConversion(vtx_to_edges, toVertex=True)
            edges_to_vtx = cmds.ls(edges_to_vtx, fl=True)
            common_vtx = [x for x in edges_to_vtx if x in vertex_list]
            if ordered_vertex_list[(i-1)] in common_vtx:
                ordered_vertex_list[i] = vtx
                copy_vertex_list.remove(vtx)
                i = i+1
                break
    
    return ordered_vertex_list

# Crear fóliculo en la posición de un vértice
def create_follicle_on_nurbs_by_vtx(vtx=None,
                                    nurbs=None,
                                    follicle_descriptor=None,
                                    follicle_side=None,
                                    rotation=False):
    """
    Crea un fóliculo en la posición de un vértice de una superficie NURBS.

    Parameters:
    vtx (str): Vértice en el que se creará el fóliculo.
    nurbs (str): Superficie NURBS a la que estará asociado el fóliculo.
    follicle_descriptor (str): Descriptor para el nombre del fóliculo.
    follicle_side (str): Lado del fóliculo ('l' para izquierda, 'r' para derecha, 'c' para centro).
    rotation (bool): Indica si se debe conectar también la rotación del fóliculo.

    Returns:
    str: Nombre del fóliculo creado.
    """

    # 1. Crear fóliculo
    fol_shape = cmds.createNode('follicle', name='{}_{}_folShape'.format(follicle_descriptor, follicle_side))
    fol = cmds.listRelatives(fol_shape, parent=True)[0]
    
    # 2. Conectar fóliculo a la NURBS
    nurbs_shape = cmds.listRelatives(nurbs, shapes=True)[0]
    cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(fol_shape))
    cmds.connectAttr('{}.worldMatrix[0]'.format(nurbs_shape), '{}.inputWorldMatrix'.format(fol_shape))
    cmds.connectAttr('{}.outTranslate'.format(fol_shape), '{}.translate'.format(fol))
    if rotation:
        cmds.connectAttr('{}.outRotate'.format(fol_shape), '{}.rotate'.format(fol))
    
    # 3. Colocar fóliculo en la posición más cercana
    vtx_position = cmds.xform(vtx, query=True, translation=True, worldSpace=True)
    temp_transform = cmds.createNode('transform', name='wip_element')
    cmds.xform(temp_transform, translation=vtx_position, worldSpace=True)
    cpos_node = cmds.createNode('closestPointOnSurface', name='wip_cpos')
    cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(cpos_node))
    cmds.connectAttr('{}.t'.format(temp_transform), '{}.inPosition'.format(cpos_node))
    parameter_u = cmds.getAttr('{}.parameterU'.format(cpos_node))
    parameter_v = cmds.getAttr('{}.parameterV'.format(cpos_node))
    cmds.delete(temp_transform, cpos_node)
    cmds.setAttr('{}.parameterU'.format(fol_shape),
