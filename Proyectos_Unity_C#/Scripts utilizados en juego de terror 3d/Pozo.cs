using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Pozo : MonoBehaviour
{
    
    public bool open;
    public bool close;
    public bool inTrigger;

    void OnTriggerEnter(Collider other)
    {
        inTrigger = true;
    }

    void OnTriggerExit(Collider other)
    {
        inTrigger = false;
    }

    void Update()
    {
        if (inTrigger)
        {
            if (close)
            {
               
                
                    if (Input.GetKeyDown(KeyCode.E))
                    {
                        open = true;
                        close = false;
                    }
                
            }
            else
            {
                if (Input.GetKeyDown(KeyCode.E))
                {
                    close = true;
                    open = false;
                }
            }
        }

        if (open)
        {
            SceneManager.LoadScene("Nivel 3");
        }
        else
        {

        }
    }

    void OnGUI()
    {
        if (inTrigger)
        {
            if (open)
            {
                GUI.Box(new Rect(0, 0, 200, 25), "Presiona la tecla E para asomarte");
            }
            else
            {
                
                
                    GUI.Box(new Rect(0, 0, 200, 25), "Presiona la tecla E para asomarte");
                
               
            }
        }
    }
}
