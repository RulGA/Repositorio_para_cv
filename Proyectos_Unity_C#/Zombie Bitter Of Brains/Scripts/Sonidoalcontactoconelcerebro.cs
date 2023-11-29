using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sonidoalcontactoconelcerebro : MonoBehaviour
{
    public GameObject Mordiscocerebro;
   
    void Start()
    {
        
    }

    void OnTriggerEnter2D(Collider2D col)
    {
            Instantiate(Mordiscocerebro);
    }
    void Update()
    {
        
    }
}
