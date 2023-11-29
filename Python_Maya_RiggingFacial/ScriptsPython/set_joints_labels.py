'''
Este código asigna valores a los atributos 'side', 'type', y 'otherType' de los nodos de articulación 
en la escena en función de sus nombres y lados. La articulación se etiqueta como 'Other' (18) y se utiliza el nombre como 'otherType'.
'''

# Obtener todos los nodos de tipo 'joint' en la escena
all_jnts = cmds.ls(type='joint')

# Iterar a través de cada articulación
for jnt in all_jnts:
    # Crear un nombre para la etiqueta basado en el nombre y uso de la articulación
    label_name = '{}{}'.format(jnt.split('_')[0],
                               jnt.split('_')[2].capitalize())
    label_side = jnt.split('_')[1]
    
    # Establecer el atributo 'side' basado en el lado de la articulación
    if label_side == 'c':
        cmds.setAttr('{}.side'.format(jnt), 0)
    elif label_side == 'l':
        cmds.setAttr('{}.side'.format(jnt), 1)
    elif label_side == 'r':
        cmds.setAttr('{}.side'.format(jnt), 2)
    
    # Configurar el tipo de la articulación como 'Other' (18) y asignar el nombre como 'otherType'
    cmds.setAttr('{}.type'.format(jnt), 18)
    cmds.setAttr('{}.otherType'.format(jnt), label_name, type='string')
