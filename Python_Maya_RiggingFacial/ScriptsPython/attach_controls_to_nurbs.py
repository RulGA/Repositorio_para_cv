def attach_control_to_nurbs(ctr=None,
                            nurbs=None,
                            rotation=False):
    """
    Función para conectar un control (ctr) a una superficie NURBS (nurbs).

    Parametros:
    ctr (str): Nombre del control a conectar.
    nurbs (str): Nombre de la superficie NURBS a la que se conectará el control.
    rotation (bool): Indica si se debe conectar también la rotación del control.

    Returns:
    None
    """

    # 1. Crear folículo
    fol_shape_name = '{}{}_{}_folShape'.format(ctr.split('_')[0], ctr.split('_')[2].capitalize(), ctr.split('_')[1])
    fol_shape = cmds.createNode('follicle', name=fol_shape_name)
    fol = cmds.listRelatives(fol_shape, parent=True)[0]

    # 2. Conectar folículo a la NURBS
    nurbs_shape = cmds.listRelatives(nurbs, shapes=True)[0]
    cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(fol_shape))
    cmds.connectAttr('{}.worldMatrix[0]'.format(nurbs_shape), '{}.inputWorldMatrix'.format(fol_shape))
    cmds.connectAttr('{}.outTranslate'.format(fol_shape), '{}.translate'.format(fol))
    if rotation:
        cmds.connectAttr('{}.outRotate'.format(fol_shape), '{}.rotate'.format(fol))

    # 3. Colocar folículo en la posición más cercana
    ctr_matrix = cmds.xform(ctr, query=True, matrix=True, worldSpace=True)
    temp_transform = cmds.createNode('transform', name='wip_element')
    cmds.xform(temp_transform, matrix=ctr_matrix, worldSpace=True)
    cpos_node = cmds.createNode('closestPointOnSurface', name='wip_cpos')
    cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(cpos_node))
    cmds.connectAttr('{}.t'.format(temp_transform), '{}.inPosition'.format(cpos_node))
    parameter_u = cmds.getAttr('{}.parameterU'.format(cpos_node))
    parameter_v = cmds.getAttr('{}.parameterV'.format(cpos_node))
    cmds.delete(temp_transform, cpos_node)
    cmds.setAttr('{}.parameterU'.format(fol_shape), parameter_u)
    cmds.setAttr('{}.parameterV'.format(fol_shape), parameter_v)

    # 4. Crear control position offset
    ctr_pos_offset_name = '{}{}_{}_pos'.format(ctr.split('_')[0], ctr.split('_')[2].capitalize(), ctr.split('_')[1])
    ctr_pos_offset_zero_name = '{}{}Pos_{}_zero'.format(ctr.split('_')[0], ctr.split('_')[2].capitalize(), ctr.split('_')[1])
    ctr_pos_offset = cmds.createNode('transform', name=ctr_pos_offset_name)
    ctr_pos_offset_zero = cmds.createNode('transform', name=ctr_pos_offset_zero_name)
    ctr_pos_offset = cmds.parent(ctr_pos_offset, ctr_pos_offset_zero)[0]
    ctr_zero = '{}{}_{}_zero'.format(ctr.split('_')[0], ctr.split('_')[2].capitalize(), ctr.split('_')[1])
    ctr_zero_father = cmds.listRelatives(ctr_zero, parent=True)[0]
    ctr_pos_offset_zero = cmds.parent(ctr_pos_offset_zero, ctr_zero_father)[0]
    fol_matrix = cmds.xform(fol, query=True, matrix=True, worldSpace=True)
    cmds.xform(ctr_pos_offset_zero, matrix=fol_matrix, worldSpace=True)
    ctr_zero = cmds.parent(ctr_zero, ctr_pos_offset)[0]

    # 5. Obtener transformación local del folículo y conectar a offset position
    fol_subs_node_name = '{}{}_{}_subs'.format(fol.split('_')[0], fol.split('_')[2].capitalize(), fol.split('_')[1])
    fol_subs_node = cmds.createNode('plusMinusAverage', name=fol_subs_node_name)
    cmds.setAttr('{}.operation'.format(fol_subs_node), 2)
    cmds.connectAttr('{}.t'.format(fol), '{}.input3D[0]'.format(fol_subs_node))
    subs_value = cmds.getAttr('{}.input3D[0]'.format(fol_subs_node))[0]
    cmds.setAttr('{}.input3D[1]'.format(fol_subs_node), *subs_value)
    cmds.connectAttr('{}.output3D'.format(fol_subs_node), '{}.t'.format(ctr_pos_offset))

    # 6. Invertir las propias translaciones del control
    ctr_rev_offset_name = '{}{}_{}_rev'.format(ctr.split('_')[0], ctr.split('_')[2].capitalize(), ctr.split('_')[1])
    ctr_rev_offset = cmds.createNode('transform', name=ctr_rev_offset_name)
    ctr_rev_offset = cmds.parent(ctr_rev_offset, ctr_zero)[0]
    cmds.xform(ctr_rev_offset, matrix=ctr_matrix, worldSpace=True)
    ctr = cmds.parent(ctr, ctr_rev_offset)[0]
    reverse_mult_name = '{}{}Reverse_{}_mult'.format(ctr.split('_')[0], ctr.split('_')[2].capitalize(), ctr.split('_')[1])
    reverse_mult = cmds.createNode('multiplyDivide', name=reverse_mult_name)
    cmds.connectAttr('{}.t'.format(ctr), '{}.input1'.format(reverse_mult))
    for axis in 'XYZ':
        cmds.setAttr('{}.input2{}'.format(reverse_mult, axis), -1)
    cmds.connectAttr('{}.output'.format(reverse_mult), '{}.t'.format(ctr_rev_offset))

# Lista de controles a conectar a la NURBS (todos excepto el último de la selección)
ctrs_list = cmds.ls(sl=True)[:-1]
# NURBS a la que se conectarán los controles (último de la selección)
nurbs = cmds.ls(sl=True)[-1]

# Iterar sobre cada control y conectarlo a la NURBS
for ctr in ctrs_list:
    attach_control_to_nurbs(ctr=ctr, nurbs=nurbs, rotation=False)
