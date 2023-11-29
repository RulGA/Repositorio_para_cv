using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class DoorScript : MonoBehaviour
{
    public static bool doorLintern;
    public static bool doorKey;
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
                if (doorKey)
                {
                    if (Input.GetKeyDown(KeyCode.E))
                    {
                        open = true;
                        close = false;
                    }
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
            SceneManager.LoadScene("Nivel 2");
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
                GUI.Box(new Rect(0, 0, 200, 25), "Presiona la tecla E para cerrar");
            }
            else
            {
                if (doorKey)
                {
                    GUI.Box(new Rect(0, 0, 200, 25), "Presiona la tecla E para abrir");
                }
                else
                {
                    GUI.Box(new Rect(0, 0, 200, 25), "¡Necesitas la llave de la puerta!");
                }
            }
        }
    }
}