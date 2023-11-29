using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SimplePatrol : MonoBehaviour
{
    public GameObject startPoint;
    public GameObject endPoint;

    public float enemySpeed;

    private bool isGoingRight;
    // Start is called before the first frame update
    void Start()
    {
        if(!isGoingRight)
        {
            transform.position = startPoint.transform.position;
        }
        else
        {
            transform.position = endPoint.transform.position;           
        }
    }

    // Update is called once per frame
    void Update()
    {
       
        if(!isGoingRight)
        {
            transform.position = Vector3.MoveTowards(transform.position, endPoint.transform.position, enemySpeed * Time.deltaTime);
            if (transform.position == endPoint.transform.position)
            {
                isGoingRight = true;
                GetComponent<SpriteRenderer>().flipX = true;
            }
        }
        if (isGoingRight)
        {
            transform.position = Vector3.MoveTowards(transform.position, startPoint.transform.position, enemySpeed * Time.deltaTime);
            if (transform.position == startPoint.transform.position)
            {
                isGoingRight = false;
                GetComponent<SpriteRenderer>().flipX = false;
            }
        }
    }
    
}
