using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class PlayerController : MonoBehaviour
{
    public int contador;
    public float maxSpeed = 1f;
    public float speed = 2f;
    public bool grounded;
    public float jumpPower = 6.5f;
    public Text puntuacion;
    public Text win;
    public Text salirjuego;

    public GameObject SonidoSalto;
    public GameObject SonidoCaida;
    public GameObject Chicazombieattack;
   

    private Rigidbody2D rb2d;
    private Animator anim;
    private bool jump;
    private bool doubleJump;
    CircleCollider2D attackCollider;

    public void Awake()
    {
        contador = 0;
        Actualizarmarcador();
        win.gameObject.SetActive(false);
        salirjuego.gameObject.SetActive(false);
    }
   
    void OnTriggerEnter2D(Collider2D col)
    {
        if (col.tag == "Cerebro")
        {

            contador = contador + 1;
            Actualizarmarcador();
           
            if (contador >= 5)
            {
                win.gameObject.SetActive(true);
                salirjuego.gameObject.SetActive(true);
                

                /*Destroy(gameObject);*/
            }

        }
    }

    private void Actualizarmarcador()
    {
        puntuacion.text = "puntuacion: " + contador;
    }

    void Start()
    {
        rb2d = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
        attackCollider = transform.GetChild(0).GetComponent<CircleCollider2D>();
        attackCollider.enabled = false;
     
    }


    void Update()
    {
        anim.SetFloat("Speed", Mathf.Abs(rb2d.velocity.x));
        anim.SetBool("Grounded", grounded);

        if (grounded)
        {
            doubleJump = true;
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (grounded)
            {
                Instantiate(SonidoSalto);
                jump = true;
                doubleJump = true;

            } else if (doubleJump)
            {
                jump = true;
                doubleJump = false;
                Instantiate(SonidoSalto);
            }
        }
        AnimatorStateInfo stateInfo = anim.GetCurrentAnimatorStateInfo(0);
        bool attacking = stateInfo.IsName("Player_Attack");
if (Input.GetKeyDown("r")&&!attacking)
        {
            anim.SetTrigger("attacking");
            attackCollider.enabled = true;
            Instantiate(Chicazombieattack);
        }
        else if (Input.GetKeyUp("r"))

        {
            attackCollider.enabled = false;
        
        }

        if (Input.GetKeyDown(KeyCode.Escape))
        {
            SceneManager.LoadScene("MENU");
        }

    

    }
    void FixedUpdate()
    {
       
        Vector3 fixedVelocity = rb2d.velocity;
        fixedVelocity.x *= 0.75f;

        if (grounded)
        {
            rb2d.velocity = fixedVelocity;
        }


        float h = Input.GetAxis("Horizontal");
        rb2d.AddForce(Vector2.right * speed * h);
        float limitedSpeed = Mathf.Clamp(rb2d.velocity.x, -maxSpeed, maxSpeed);
        rb2d.velocity = new Vector2(limitedSpeed, rb2d.velocity.y);
        if (h>0.1f)
        {
            transform.localScale = new Vector3(1f, 1f, 1f);
        }
        if (h<-0.1f)
        {
            transform.localScale = new Vector3(-1f, 1f, 1f);
        }
        if (jump)
        {
            rb2d.velocity = new Vector2(rb2d.velocity.x, 0);
            rb2d.AddForce(Vector2.up * jumpPower,ForceMode2D.Impulse);
            jump = false;
        }
;
        Debug.Log(rb2d.velocity.x);


    }
    public void EnemyJump()
    {
        jump = true;
    }
}
