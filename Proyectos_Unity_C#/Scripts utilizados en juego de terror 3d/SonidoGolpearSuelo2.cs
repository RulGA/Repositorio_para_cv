using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SonidoGolpearSuelo2 : MonoBehaviour
{
  
        //El Clip de audio se tiene que introducir en el script NO EN EL AUDIO SOURCE.
        public AudioClip clip;

    void OnCollisionEnter(Collision col)
    {
        //Aseguraos de que el jugador tenga el tag player.
        if (col.gameObject.tag == "estanteria")
        {
            GetComponent<AudioSource>().PlayOneShot(clip);
        }
    }
}


