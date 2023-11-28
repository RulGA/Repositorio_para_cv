using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OctopusController : MonoBehaviour
{

    public Transform target;                // Posición objetivo que alternará con la original del objeto para que el enemigo haga un movimiento de ida y de venida.
    public bool isHurt = false;             // Indica si el enemigo ha sido dañado.
    private float speed = 4f;               // Velocidad de movimiento del enemigo.
    private Vector3 start, end;             // Variables que nos ayudarán a alternar la posición del target con la inicial del objeto.
    private SpriteRenderer spriteRenderer;  // Usaremos el componente SpriteRenderer para activar su opción flip, para volvear al enemigo.

    // Start is called before the first frame update
    void Start()
    {
        start = transform.position;
        end = target.position;
        spriteRenderer = GetComponent<SpriteRenderer>();
    }

    // Update is called once per frame
    void Update()
    {
        // Movimiento del enemigo. El enemigo se moverá hacia la posición objetivo. Cuando llegue, la posición objetivo cambiará de lugar y
        // se situará en la situación de partida haciendo que la plataforma regrese. Cuando llegue, volverá a cambiar a la posición objetivo, y
        // así sucesivamente.
        transform.position = Vector3.MoveTowards(transform.position, target.position, speed * Time.deltaTime);

        if (transform.position == target.position)
        {

            if (target.position == end)
            {
                target.position = start;
                spriteRenderer.flipX = true;    // Volteamos en la X el sprite.
            }
            else
            {
                target.position = end;
                spriteRenderer.flipX = false;

            }
        }
    }
}

