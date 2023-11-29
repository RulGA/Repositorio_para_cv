using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Destroyable : MonoBehaviour
{
    

    

    void Start()
    {

    }
    void OnTriggerEnter2D(Collider2D col)
    {
        if(col.tag=="Attack")
        {

            Destroy(gameObject);
           

        }
    }
    void Update()
    {
        
    }
}
