using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Linterna : MonoBehaviour
{
    public Light l;
    public float bateria;
    public GameObject luz;
    public Renderer fanttassma;
    bool activarfantasma = false;
    public GameObject ffantassmaGameO;


    private void Start()
    {
        ffantassmaGameO.SetActive(true);
        fanttassma.enabled = true;
    }
    void Update()
    {
        if (luz.activeSelf)
            /* bateria -= Time.deltaTime;*/
            if (bateria <= 0)
                luz.SetActive(false);

        if (Input.GetKeyDown(KeyCode.F) && l.enabled == true)
        {
            activarfantasma = !activarfantasma;

            luz.SetActive(!luz.activeSelf);
            GetComponent<AudioSource>().Play();
            if (activarfantasma == true)
            {
                ffantassmaGameO.SetActive(false);
                fanttassma.enabled = false;
            }
            else if (activarfantasma == false)
            {
                ffantassmaGameO.SetActive(true);
                fanttassma.enabled = true;
            }

        }



    }


}
