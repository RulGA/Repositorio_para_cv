using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CogerLlave : MonoBehaviour
{
    public AudioClip clip;
    public Renderer Llave;
    public AudioSource fuenteaudio;
    bool encendido = false;
    public Collider collave;
    public Collider ActivarEstanterias;
   
   

    void Start()
    {
        fuenteaudio.Pause();
        fuenteaudio = GetComponent<AudioSource>();
        fuenteaudio.clip = clip;
        ActivarEstanterias.enabled = false;
    }

    void Update()
    {
        if (encendido == true && Input.GetKeyDown(KeyCode.E))
        { 
            Destroy(Llave);
            if(collave.enabled==true)
            {
                GetComponent<AudioSource>().PlayOneShot(clip);
                fuenteaudio.UnPause();
                ActivarEstanterias.enabled = true;

            }
            Destroy(collave);
           
        }
    

      
   
    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Player")
        {
            encendido = true;
           
        }
      
    }
   
}
