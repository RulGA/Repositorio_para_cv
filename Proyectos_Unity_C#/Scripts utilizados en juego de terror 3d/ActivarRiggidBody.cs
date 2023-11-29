using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ActivarRiggidBody : MonoBehaviour
{
    public Collider estanteria1;
    public Collider estanteria2;
    void Start()
    {
        estanteria1.enabled = true;
        estanteria2.enabled = true;
    }
    private void Update()
    {
        
    }
    private void OnAnimatorIK(int layerIndex)
    {
      
    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            Destroy(estanteria1);
            Destroy(estanteria2);
        }
    }

 




}
