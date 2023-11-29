using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HealthManger : MonoBehaviour
{
    Rigidbody2D pRB;
    public float BumpX, BumpY;
    [SerializeField] private Transform respawnPoint;

    [SerializeField] private Transform player;
    public int PlayerHealth=5;
    public int enemyDamage=1;
    // Start is called before the first frame update
    void Start()
    {
        pRB = GetComponent<Rigidbody2D>();
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag=="Enemy")
        {
            PlayerHealth -= enemyDamage;

            if (PlayerHealth > 0)
            {
                /*GetComponent<SpriteRenderer>().color = Color.red;*/
                if (other.GetComponent<SpriteRenderer>().flipX == false)
                {
                    pRB.velocity = new Vector2(-BumpX, BumpY);
                }
                else if (other.GetComponent<SpriteRenderer>().flipX == true)
                {
                    pRB.velocity = new Vector2(BumpX, BumpY);
                }
            }
            else if (PlayerHealth<=0)
            {
                player.transform.position = respawnPoint.transform.position;
                PlayerHealth = 5;
            }
        }
    }
    /*private void OnTriggerExit2D(Collider2D col)
    {
        if(col.tag=="Enemy")
        {
            GetComponent<SpriteRenderer>().color = Color.white;
        }
    }*/
}
