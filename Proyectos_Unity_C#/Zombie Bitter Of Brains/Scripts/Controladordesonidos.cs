using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Controladordesonidos : MonoBehaviour
{
    public GameObject sonidoSeleccionar;
    public GameObject sonidoClick;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void BotonSonSelect()
    {
        Instantiate(sonidoSeleccionar);
    }
    public void BotonSonidoclick()
    {
        Instantiate(sonidoClick);
    }
}
