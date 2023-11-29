using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RespawnCaida : MonoBehaviour
{
    [SerializeField] private Transform player;
    [SerializeField] private Transform respawnPoint;
    void OnTriggerEnter2D(Collider2D col)
    {
        if (col.tag == "Player")
        {

            player.transform.position = respawnPoint.transform.position;

        }
    }
}
