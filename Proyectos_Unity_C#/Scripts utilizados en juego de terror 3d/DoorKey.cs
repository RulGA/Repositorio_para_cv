using UnityEngine;
using System.Collections;

public class DoorKey : MonoBehaviour
{

    public bool inTrigger;
    public Collider blabla;

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
           
            if (Input.GetKeyDown(KeyCode.E))
            {
                
                DoorScript.doorKey = true;
               
       
            }
        }
    }

    void OnGUI()
    {
        if (inTrigger)
        {
            GUI.Box(new Rect(0, 60, 200, 25), "Pulsa E para cojer la llave");
        }
    }
}