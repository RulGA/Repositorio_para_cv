using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlatformMov : MonoBehaviour
{
    
    public Transform targetPlatform;    // Posición objetivo que alternará con la original del objeto para que la plataforma haga un movimiento de ida y de venida.
    private float speed = 3f;           // Velocidad a la que se mueve la plataforma.
    private Vector3 start, end;         // Variables que nos ayudarán a alternar la posición del target con la inicial del objeto.



    void Start()
    {
        start = transform.position;
        end = targetPlatform.position;
    }

    
    void Update()
    {
        // Movimiento de la plataforma. La plataforma se moverá hacia la posición objetivo. Cuando llegue, la posición objetivo cambiará de lugar y
        // se situará en la situación de partida haciendo que la plataforma regrese. Cuando llegue, volverá a cambiar a la posición objetivo, y
        // así sucesivamente.
        transform.position = Vector3.MoveTowards(transform.position, targetPlatform.position, speed * Time.deltaTime);

        if(transform.position == targetPlatform.position)
        {

            if (targetPlatform.position == end)
            {
                targetPlatform.position = start;
            }
            else
            {
                targetPlatform.position = end;
            }
        }
    }

    
    // Si un objeto colisiona con la plataforma, pasará a ser hijo de esta (haciendo que siga su movimiento)
    private void OnCollisionEnter2D(Collision2D collision)
    {
        collision.transform.parent = transform;
    }

    // Si un objeto deja la colisión con la plataforma, dejará de ser hijo de esta (haciendo que siga su movimiento)
    private void OnCollisionExit2D(Collision2D collision)
    {
        collision.transform.parent = null;
    }
}
