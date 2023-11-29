'''
Este código realiza la función de mirror en el eje X para controles y articulaciones seleccionados. 
La función mirror_control_joint toma una lista de controles como argumento y realiza los siguientes pasos para cada control en la lista:

1. Obtiene información sobre el nombre y la orientación del control.
2. Crea un nodo de transformación cero para el control.
3. Obtiene la articulación conectada al control y crea un nodo de transformación cero para la articulación.
4. Duplica y renombra los nodos de control y articulación para el lado opuesto.
5. Crea un nodo de transformación temporal para facilitar la inversión en el eje X.
6. Restaura la jerarquía original de los nodos duplicados.
7. Elimina el nodo de transformación temporal.
8. Conecta las transformaciones reflejadas entre el control y la articulación en el eje X.

Para utilizar el código, se llama a la función mirror_control_joint con la selección actual como la lista de controles. Por ejemplo, mirror_control_joint(ctr_list=cmds.ls(sl=True)).

'''

def mirror_control_joint(ctr_list=None):
    # Iterar a través de la lista de controles
    for ctr in ctr_list:
        # Obtener información del nombre del control
        ctr_descriptor = ctr.split('_')[0]
        ctr_side = ctr.split('_')[1]
        ctr_usage = ctr.split('_')[2]
        
        # Crear el nombre del nodo de transformación cero del control
        ctr_zero = '{}{}_{}_zero'.format(ctr_descriptor, ctr_usage.capitalize(), ctr_side)
        
        # Obtener información del nombre de la articulación conectada al control
        jnt = [x for x in cmds.listConnections('{}.tx'.format(ctr)) if cmds.nodeType(x) == 'joint'][0]
        jnt_descriptor = jnt.split('_')[0]
        jnt_side = jnt.split('_')[1]
        jnt_usage = jnt.split('_')[2]
        
        # Crear el nombre del nodo de transformación cero de la articulación conectada
        jnt_zero = '{}{}_{}_zero'.format(jnt_descriptor, jnt_usage.capitalize(), jnt_side)
        
        # Duplicar y renombrar los nodos de control y articulación para el lado opuesto
        mirror_ctr_zero_dup = cmds.duplicate(ctr_zero)
        if ctr_side == 'l':
            mirror_ctr_zero_name = '{}{}_r_zero'.format(ctr_descriptor, ctr_usage.capitalize())
            mirror_ctr_name = '{}_r_{}'.format(ctr_descriptor, ctr_usage)
        elif ctr_side == 'r':
            mirror_ctr_zero_name = '{}{}_l_zero'.format(ctr_descriptor, ctr_usage.capitalize())
            mirror_ctr_name = '{}_l_{}'.format(ctr_descriptor, ctr_usage)
        mirror_ctr_zero = cmds.rename(mirror_ctr_zero_dup[0], mirror_ctr_zero_name)
        mirror_ctr = cmds.listRelatives(mirror_ctr_zero, children=True, fullPath=True)[0]
        mirror_ctr = cmds.rename(mirror_ctr, mirror_ctr_name)
        
        mirror_jnt_zero_dup = cmds.duplicate(jnt_zero)
        if jnt_side == 'l':
            mirror_jnt_zero_name = '{}{}_r_zero'.format(jnt_descriptor, jnt_usage.capitalize())
            mirror_jnt_name = '{}_r_{}'.format(jnt_descriptor, jnt_usage)
        elif jnt_side == 'r':
            mirror_jnt_zero_name = '{}{}_l_zero'.format(jnt_descriptor, jnt_usage.capitalize())
            mirror_jnt_name = '{}_l_{}'.format(jnt_descriptor, jnt_usage)
        mirror_jnt_zero = cmds.rename(mirror_jnt_zero_dup[0], mirror_jnt_zero_name)
        mirror_jnt = cmds.listRelatives(mirror_jnt_zero, children=True, fullPath=True)[0]
        mirror_jnt = cmds.rename(mirror_jnt, mirror_jnt_name)
        
        # Crear un nodo de transformación temporal para facilitar la inversión en el eje X
        mirror_grp = cmds.createNode('transform', name='temp_mirror_grp')
        mirror_ctr_zero = cmds.parent(mirror_ctr_zero, mirror_grp)[0]
        mirror_jnt_zero = cmds.parent(mirror_jnt_zero, mirror_grp)[0]
        cmds.setAttr('{}.sx'.format(mirror_grp), -1)
        
        # Restaurar la jerarquía original de los nodos duplicados
        ctr_zero_father = cmds.listRelatives(ctr_zero, parent=True)
        if ctr_zero_father:
            mirror_ctr_zero = cmds.parent(mirror_ctr_zero, ctr_zero_father)[0]
        else:
            mirror_ctr_zero = cmds.parent(mirror_ctr_zero, w=True)[0]
        jnt_zero_father = cmds.listRelatives(jnt_zero, parent=True)
        if jnt_zero_father:
            mirror_jnt_zero = cmds.parent(mirror_jnt_zero, jnt_zero_father)[0]
        else:
            mirror_jnt_zero = cmds.parent(mirror_jnt_zero, w=True)[0]
        
        # Eliminar el nodo de transformación temporal
        cmds.delete(mirror_grp)
        
        # Conectar las transformaciones reflejadas entre el control y la articulación
        for attr in 'trs':
            for axis in 'xyz':
                cmds.connectAttr('{}.{}{}'.format(mirror_ctr, attr, axis), '{}.{}{}'.format(mirror_jnt, attr, axis))

# Llamar a la función con la selección actual como lista de controles
mirror_control_joint(ctr_list=cmds.ls(sl=True))
