# Se imprime la selección actual (comentado para desactivar)
# print(cmds.ls(sl=True))

'''
Este código crea articulaciones (joints) y transformaciones (transforms) en Maya basándose en una lista de nombres de folículos. 
Utiliza nodos 'plusMinusAverage' para realizar operaciones matemáticas en las posiciones de los folículos y conectarlas a las transformaciones 
de las articulaciones. La jerarquía se organiza adecuadamente parentando los nodos.
'''

# Lista de nombres de los folículos
fols_list = ['upLip09_r_fol', 'upLip08_r_fol', 'upLip07_r_fol', 'upLip06_r_fol', 'upLip05_r_fol', 'upLip04_r_fol', 'upLip03_r_fol', 'upLip02_r_fol', 'upLip01_r_fol', 'upLip_c_fol', 'upLip01_l_fol', 'upLip02_l_fol', 'upLip03_l_fol', 'upLip04_l_fol', 'upLip05_l_fol', 'upLip06_l_fol', 'upLip07_l_fol', 'upLip08_l_fol', 'upLip09_l_fol', 'dwLip09_r_fol', 'dwLip08_r_fol', 'dwLip07_r_fol', 'dwLip06_r_fol', 'dwLip05_r_fol', 'dwLip04_r_fol', 'dwLip03_r_fol', 'dwLip02_r_fol', 'dwLip01_r_fol', 'dwLip_c_fol', 'dwLip01_l_fol', 'dwLip02_l_fol', 'dwLip03_l_fol', 'dwLip04_l_fol', 'dwLip05_l_fol', 'dwLip06_l_fol', 'dwLip07_l_fol', 'dwLip08_l_fol', 'dwLip09_l_fol']

# Iteración a través de la lista de folículos
for fol in fols_list:
    # Crear nombres para las articulaciones y transformaciones relacionadas
    jnt_name = '{}_{}_skn'.format(fol.split('_')[0], fol.split('_')[1])
    jnt_zero_name = '{}Skn_{}_zero'.format(fol.split('_')[0], fol.split('_')[1])
    jnt_position_name = '{}Skn_{}_position'.format(fol.split('_')[0], fol.split('_')[1])
    
    # Crear una articulación y dos transformaciones
    jnt = cmds.createNode('joint', name=jnt_name)
    jnt_zero = cmds.createNode('transform', name=jnt_zero_name)
    jnt_position = cmds.createNode('transform', name=jnt_position_name)
    
    # Organizar la jerarquía parentando las nodos creados
    jnt = cmds.parent(jnt, jnt_position)[0]
    jnt_position = cmds.parent(jnt_position, jnt_zero)[0]
    
    # Obtener la posición del folículo y aplicarla al nodo de transformación cero
    fol_translation = cmds.xform(fol, query=True, translation=True, worldSpace=True)
    cmds.xform(jnt_zero, translation=fol_translation, worldSpace=True)
    
    # Crear un nodo 'plusMinusAverage' para realizar operaciones matemáticas en las posiciones del folículo
    fol_subs_name = '{}Fol_{}_subs'.format(fol.split('_')[0], fol.split('_')[1])
    fol_subs = cmds.createNode('plusMinusAverage', name=fol_subs_name)
    cmds.setAttr('{}.operation'.format(fol_subs), 2)
    
    # Conectar las posiciones del folículo al nodo 'plusMinusAverage' y al nodo de transformación de la articulación
    for axis in 'xyz':
        cmds.connectAttr('{}.t{}'.format(fol, axis), '{}.input3D[0].input3D{}'.format(fol_subs, axis))
        get_value = cmds.getAttr('{}.input3D[0].input3D{}'.format(fol_subs, axis))
        cmds.setAttr('{}.input3D[1].input3D{}'.format(fol_subs, axis), get_value)
        cmds.connectAttr('{}.output3D.output3D{}'.format(fol_subs, axis), '{}.t{}'.format(jnt_position, axis))
