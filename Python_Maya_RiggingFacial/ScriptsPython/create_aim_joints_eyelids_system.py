##### CREACIÓN HUESOS DEFORMACIÓN NURBS DE LOS EYELIDS #####

# Obtiene la lista de selección actual (puede ser útil para depurar)
#print(cmds.ls(sl=True))

# Lista de nombres de articulaciones para los párpados
jnt_list = ['intEyelidSpecific_r_jnt', 'extEyelidSpecific_r_jnt', 'upEyelidSpecific01_r_jnt', 'upEyelidSpecific02_r_jnt', 'upEyelidSpecific03_r_jnt', 'dwEyelidSpecific01_r_jnt', 'dwEyelidSpecific02_r_jnt', 'dwEyelidSpecific03_r_jnt']
center_eye_locator = 'centerEye_r_loc'

# Itera sobre cada articulación en la lista
for jnt in jnt_list:
    # Crea nombres para los nodos skinCluster y zero y aim transform asociados a la articulación
    nskn_name = '{}_{}_nskn'.format(jnt.split('_')[0], jnt.split('_')[1])
    nskn_zero_name = '{}Nskn_{}_zero'.format(jnt.split('_')[0], jnt.split('_')[1])
    nskn_aim_name = '{}Nskn_{}_aim'.format(jnt.split('_')[0], jnt.split('_')[1])
    
    # Crea los nodos joint, transform zero y transform aim
    nskn = cmds.createNode('joint', name=nskn_name)
    nskn_zero = cmds.createNode('transform', name=nskn_zero_name)
    nskn_aim = cmds.createNode('transform', name=nskn_aim_name)
    
    # Establece la jerarquía de nodos parentando los joints y transforms adecuadamente
    nskn = cmds.parent(nskn, nskn_aim)[0]
    nskn_aim = cmds.parent(nskn_aim, nskn_zero)[0]
    
    # Obtiene la posición del locator del ojo y aplica esa posición al nodo zero
    center_eye_position = cmds.xform(center_eye_locator, query=True, translation=True, worldSpace=True)
    cmds.xform(nskn_zero, translation=center_eye_position, worldSpace=True)
    
    # Aplica un constraint de aim entre la articulación original y el nodo aim
    cmds.aimConstraint(jnt, nskn_aim,
                       offset=(0,0,0), w=1,
                       aimVector=(0,0,1),
                       upVector=(1,0,0),
                       worldUpType='objectrotation',
                       worldUpVector=(1,0,0),
                       worldUpObject=jnt)

##### CREACIÓN HUESOS DEFORMACIÓN GEO DE LOS EYELIDS #####

# Obtiene la lista de selección actual (puede ser útil para depurar)
#print(cmds.ls(sl=True))

# Lista de nombres de folículos para los párpados
fols_list = ['upEyelid01_r_fol', 'upEyelid02_r_fol', 'upEyelid03_r_fol', 'upEyelid04_r_fol', 'upEyelid05_r_fol', 'upEyelid06_r_fol', 'upEyelid07_r_fol', 'upEyelid08_r_fol', 'upEyelid09_r_fol', 'upEyelid10_r_fol', 'upEyelid11_r_fol', 'upEyelid12_r_fol', 'upEyelid13_r_fol', 'upEyelid14_r_fol', 'upEyelid15_r_fol', 'dwEyelid01_r_fol', 'dwEyelid02_r_fol', 'dwEyelid03_r_fol', 'dwEyelid04_r_fol', 'dwEyelid05_r_fol', 'dwEyelid06_r_fol', 'dwEyelid07_r_fol', 'dwEyelid08_r_fol', 'dwEyelid09_r_fol', 'dwEyelid10_r_fol', 'dwEyelid11_r_fol', 'dwEyelid12_r_fol', 'dwEyelid13_r_fol', 'dwEyelid14_r_fol', 'dwEyelid15_r_fol']
center_eye_locator = 'centerEye_r_loc'

# Itera sobre cada folículo en la lista
for fol in fols_list:
    # Crea nombres para los nodos joint, transform zero y transform aim asociados al folículo
    skn_name = '{}_{}_skn'.format(fol.split('_')[0], fol.split('_')[1])
    skn_zero_name = '{}Skn_{}_zero'.format(fol.split('_')[0], fol.split('_')[1])
    skn_aim_name = '{}Skn_{}_aim'.format(fol.split('_')[0], fol.split('_')[1])
    
    # Crea los nodos joint, transform zero y transform aim
    skn = cmds.createNode('joint', name=skn_name)
    skn_zero = cmds.createNode('transform', name=skn_zero_name)
    skn_aim = cmds.createNode('transform', name=skn_aim_name)
    
    # Establece la jerarquía de nodos parentando los joints y transforms adecuadamente
    skn = cmds.parent(skn, skn_aim)[0]
    skn_aim = cmds.parent(skn_aim, skn_zero)[0]
    
    # Obtiene la posición del locator del ojo y aplica esa posición al nodo zero
    center_eye_position = cmds.xform(center_eye_locator, query=True, translation=True, worldSpace=True)
    cmds.xform(skn_zero, translation=center_eye_position, worldSpace=True)
    
    # Aplica un constraint de aim entre el folículo original y el nodo aim
    cmds.aimConstraint(fol, skn_aim,
                       offset=(0,0,0), w=1,
                       aimVector=(0,0,1),
                       upVector=(0,1,0),
                       worldUpType='scene')
