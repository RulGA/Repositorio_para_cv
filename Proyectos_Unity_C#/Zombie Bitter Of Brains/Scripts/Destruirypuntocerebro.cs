﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Destruirypuntocerebro : MonoBehaviour
{
   

    void Start()
    {

    }
    void OnTriggerEnter2D(Collider2D col)
    {
        if (col.tag == "Player")
        {

            Destroy(gameObject);


        }
    }
    void Update()
    {

    }
}
