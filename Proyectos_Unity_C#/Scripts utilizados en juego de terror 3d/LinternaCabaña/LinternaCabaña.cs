using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LinternaCabaña : MonoBehaviour
{
    public float bateria;
    public GameObject luz;



    void Update()
    {
        if (luz.activeSelf)
            /* bateria -= Time.deltaTime;*/
            if (bateria <= 0)
                luz.SetActive(false);

        if (Input.GetKeyDown(KeyCode.F) && bateria > 0)
        {
            luz.SetActive(!luz.activeSelf);
            GetComponent<AudioSource>().Play();
        }


    }
}
