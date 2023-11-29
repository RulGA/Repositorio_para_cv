'''
STICKY LIPS SYSTEM:

Este código establece un sistema de labios pegajosos ("Sticky Lips System") en Maya, creando nodos y conexiones para gestionar 
atributos de control y la funcionalidad Sticky Lips en articulaciones del sistema facial.

'''

# Crear el nodo de transformación para la configuración del control
sticky_control_transform = cmds.createNode('transform', name='stickyLipsConfiguration_c_null')
sticky_control_transform = cmds.parent(sticky_control_transform, 'facialMouthSystem_c_grp')[0]

# Bloquear atributos del nodo de transformación del control
for attr in cmds.listAttr(sticky_control_transform, k=True):
    cmds.setAttr('{}.{}'.format(sticky_control_transform, attr), lock=True, k=False, channelBox=False)

# Definir el número de articulaciones laterales y crear una lista de atributos de labio
side_joints_num = 8
lip_attributes_list = []
for i in range(0, side_joints_num):
    attr_name = 'lip{}_r_sticky'.format(str(side_joints_num - i).zfill(2))
    lip_attributes_list.append(attr_name)
lip_attributes_list.append('lip_c_sticky')
for i in range(0, side_joints_num):
    attr_name = 'lip{}_l_sticky'.format(str(i + 1).zfill(2))
    lip_attributes_list.append(attr_name)

# Agregar atributos a la configuración del control
for attr_name in lip_attributes_list:
    cmds.addAttr(sticky_control_transform,
                 ln=attr_name,
                 at='double',
                 min=0, max=1, dv=0,
                 k=True)
    
    # Crear nodos para la funcionalidad de Sticky Lips
    sticky_div_name = '{}{}_{}_div'.format(attr_name.split('_')[0],
                                           attr_name.split('_')[2].capitalize(),
                                           attr_name.split('_')[1])
    sticky_div = cmds.createNode('multiplyDivide', name=sticky_div_name)
    cmds.setAttr('{}.operation'.format(sticky_div), 2)
    cmds.connectAttr('{}.{}'.format(sticky_control_transform, attr_name), '{}.input1X'.format(sticky_div))
    cmds.setAttr('{}.input2X'.format(sticky_div), 2)
    
    # Crear nodos de referencia y transformación para cada parte del labio (up, dw)
    for part in ['up', 'dw']:
        part_jnt = '{}{}_{}_skn'.format(part,
                                        attr_name.split('_')[0].capitalize(),
                                        attr_name.split('_')[1])
        part_jnt_opposite_ref_name = '{}{}Oposite_{}_ref'.format(part,
                                                                 attr_name.split('_')[0].capitalize(),
                                                                 attr_name.split('_')[1])
        part_jnt_opposite_ref = cmds.createNode('transform', name=part_jnt_opposite_ref_name)
        part_jnt_position = '{}{}Skn_{}_position'.format(part,
                                                         attr_name.split('_')[0].capitalize(),
                                                         attr_name.split('_')[1])
        part_jnt_opposite_ref = cmds.parent(part_jnt_opposite_ref, part_jnt_position)[0]
        if part == 'up':
            part_jnt_position_opposite = 'dw{}Skn_{}_position'.format(attr_name.split('_')[0].capitalize(),
                                                                       attr_name.split('_')[1])
        elif part == 'dw':
            part_jnt_position_opposite = 'up{}Skn_{}_position'.format(attr_name.split('_')[0].capitalize(),
                                                                       attr_name.split('_')[1])
        cmds.pointConstraint(part_jnt_position_opposite, part_jnt_opposite_ref, mo=False)
        
        # Crear nodos de offset y pairBlend para la funcionalidad Sticky Lips
        sticky_offset_name = '{}{}Skn_{}_sticky'.format(part,
                                                        attr_name.split('_')[0].capitalize(),
                                                        attr_name.split('_')[1])
        sticky_offset = cmds.createNode('transform', name=sticky_offset_name)
        sticky_offset = cmds.parent(sticky_offset, part_jnt_position)[0]
        part_jnt_matrix = cmds.xform(part_jnt, query=True, matrix=True, worldSpace=True)
        cmds.xform(sticky_offset, matrix=part_jnt_matrix, worldSpace=True)
        part_jnt = cmds.parent(part_jnt, sticky_offset)[0]
        
        sticky_pair_blend_name = '{}{}Sticky_{}_pairb'.format(part,
                                                              attr_name.split('_')[0].capitalize(),
                                                              attr_name.split('_')[1])
        sticky_pair_blend = cmds.createNode('pairBlend', name=sticky_pair_blend_name)
        cmds.setAttr('{}.inTranslate1'.format(sticky_pair_blend), 0, 0, 0)
        cmds.setAttr('{}.inTranslate2'.format(sticky_pair_blend), 0, 0, 0)
        cmds.connectAttr('{}.t'.format(part_jnt_opposite_ref), '{}.inTranslate2'.format(sticky_pair_blend))
        cmds.connectAttr('{}.outputX'.format(sticky_div), '{}.weight'.format(sticky_pair_blend))
        cmds.connectAttr('{}.outTranslate'.format(sticky_pair_blend), '{}.t'.format(sticky_offset))
