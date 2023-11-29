def create_control_joint(name=None,
                         side=None,
                         jnt_usage=None):
    """
    Función para crear un control y un joint asociado.

    Parameters:
    name (str): Nombre base para el control y el joint.
    side (str): Lado del cuerpo al que pertenece ('l' para izquierda, 'r' para derecha).
    jnt_usage (str): Uso del joint ('skn' para deformación, 'nskn' para no deformación).

    Returns:
    None
    """

    # Construir nombres para el control y el joint
    ctr_name = '{}_{}_ctr'.format(name, side)
    ctr_zero_name = '{}Ctr_{}_zero'.format(name, side)
    jnt_name = '{}_{}_{}'.format(name, side, jnt_usage)
    jnt_zero_name = '{}{}_{}_zero'.format(name, jnt_usage.capitalize(), side)

    # Crear el control
    ctr = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=0, name=ctr_name)
    ctr_zero = cmds.createNode('transform', name=ctr_zero_name)
    ctr = cmds.parent(ctr, ctr_zero)[0]

    # Crear el joint
    jnt = cmds.createNode('joint', name=jnt_name)
    jnt_zero = cmds.createNode('transform', name=jnt_zero_name)
    jnt = cmds.parent(jnt, jnt_zero)[0]

    # Conectar las transformaciones del control al joint
    for attr in 'trs':
        for axis in 'xyz':
            cmds.connectAttr('{}.{}{}'.format(ctr, attr, axis), '{}.{}{}'.format(jnt, attr, axis))

# Ejemplo de uso
create_control_joint(name='ear', side='l', jnt_usage='skn')
