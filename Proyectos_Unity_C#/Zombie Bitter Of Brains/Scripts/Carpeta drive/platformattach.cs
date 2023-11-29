using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class platformattach : MonoBehaviour
{
    public GameObject Player;

    // Start is called before the first frame update
    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.gameObject == Player)
        {
            Player.transform.parent = transform;
        }
    }
    private void OnTriggerExit2D(Collider2D other)
    {
        if (other.gameObject == Player)
        {
            Player.transform.parent = null;
        }
    }

}
