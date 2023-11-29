def create_joint_by_follicles(fols_list=None, jnts_usage=None):
    """
    Crea articulaciones conectadas a fóliculos.

    Parameters:
    fols_list (list): Lista de fóliculos a los que se conectarán las articulaciones.
    jnts_usage (str): Uso de las articulaciones (por ejemplo, 'skn' para skinning).

    Returns:
    None
    """

    for fol in fols_list:
        jnt_name = '{}_{}_{}'.format(fol.split('_')[0], fol.split('_')[1], jnts_usage)
        jnt_zero_name = '{}{}_{}_zero'.format(fol.split('_')[0], jnts_usage.capitalize(), fol.split('_')[1])
        jnt = cmds.createNode('joint', name=jnt_name)
        jnt_zero = cmds.createNode('transform', name=jnt_zero_name)
        jnt = cmds.parent(jnt, jnt_zero)[0]
        for attr in 'trs':
            for axis in 'xyz':
                cmds.connectAttr('{}.{}{}'.format(fol, attr, axis), '{}.{}{}'.format(jnt_zero, attr, axis))

# Crear articulaciones conectadas a fóliculos
create_joint_by_follicles(fols_list=cmds.ls('brow*_fol'), jnts_usage='skn')
