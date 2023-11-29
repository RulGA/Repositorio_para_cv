using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ReproducirSonido : MonoBehaviour
{

        // Start is called before the first frame update
        public AudioClip clip;
    bool encendido = false;

    bool solounavez = true;
        AudioSource fuenteaudio;



        void Start()
        {
        encendido = false;
            fuenteaudio = GetComponent<AudioSource>();
        fuenteaudio.clip = clip;
      
    }

    // Update is called once per frame
    void Update()
    {
        if (encendido == true)
        {
            if (Input.GetKeyDown(KeyCode.E)&&solounavez==true)
            {
      
                GetComponent<AudioSource>().PlayOneShot(clip);
                encendido = false;
                solounavez = false;
             

            }
         
            


        }
        
    }

    private void OnTriggerStay(Collider col)
    {
        if (col.gameObject.tag == "Player")
        {
            encendido = true;
        }

    }
}
