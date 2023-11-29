using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine.UI;

public class Jugador : MonoBehaviour
{
    public bool regenrarVida, regenerarEnergia;

    public Transform camara, linterna;
    public GameObject enemigo;

    public float vidaMaxima, energiaMaxima, tiempoParaRecuperarse;
    float vida, energia;
    public CharacterController cc;

    public Text texto;

    private void Start()
    {
        energia = Mathf.Abs(energiaMaxima);
        vida = Mathf.Abs(vidaMaxima);
 
    }

    void Update()
    {
        texto.text = "Vida: " + vida.ToString("0") + "\nEnergia: " + energia.ToString("0");
        if (Input.GetKeyDown(KeyCode.E))
        {
            RaycastHit raycast;
            if (Physics.Raycast(camara.position, camara.forward, out raycast, 5f))
            {
                if (raycast.collider.gameObject.CompareTag("Objetivo"))
                {
                 
                    Destroy(raycast.collider.gameObject);

                
                }
                else if (raycast.collider.gameObject.CompareTag("Bateria"))
                {
                    float total = raycast.collider.gameObject.GetComponent<Propiedad>().total;
         
                    Destroy(raycast.collider.gameObject);
                }
                else if (raycast.collider.gameObject.CompareTag("Curar"))
                {
                    float total = raycast.collider.gameObject.GetComponent<Propiedad>().total;
                    Curar(total);
                    Destroy(raycast.collider.gameObject);
                }
                else if (raycast.collider.gameObject.CompareTag("Energia"))
                {
                    float total = raycast.collider.gameObject.GetComponent<Propiedad>().total;
                    RecuperarEnergia(total);
                    Destroy(raycast.collider.gameObject);
                }
            }
        }

        if (regenrarVida && vida < Mathf.Abs(vidaMaxima))
            vida += Time.deltaTime;

        if (Input.GetKey(KeyCode.LeftShift) && cc.velocity.magnitude >= 1f && energia >= 0)
        {
            Vector3 xyz = new Vector3(30, 0, 0);
            linterna.localEulerAngles = Vector3.Lerp(linterna.localEulerAngles, xyz, Time.deltaTime * 2.5f);

            energia -= Time.deltaTime;

            if (energia <= 0)
            {
                energia = -Mathf.Abs(tiempoParaRecuperarse);
          
            }
        }
        else
        {
            Vector3 xyz = new Vector3(0, 0, 0);
            linterna.localEulerAngles = Vector3.Lerp(linterna.localEulerAngles, xyz, Time.deltaTime * 2.5f);

            if (energia < Mathf.Abs(energiaMaxima) && regenerarEnergia)
            {
                energia += Time.deltaTime;
              
            }
        }
    }

    public void RecibirDaño (float daño)
    {
        vida -= daño;
        if (vida <= 0)
            UnityEngine.SceneManagement.SceneManager.LoadScene(UnityEngine.SceneManagement.SceneManager.GetActiveScene().buildIndex);
    }

    public void Curar(float vidaRegenerada)
    {
        vida += vidaRegenerada;
        if (vida >= Mathf.Abs(vidaMaxima))
            vida = Mathf.Abs(vidaMaxima);
    }

    public void RecuperarEnergia(float energiaRegenerada)
    {
        energia += energiaRegenerada;
        if (energia >= Mathf.Abs(energiaMaxima))
            energia = Mathf.Abs(energiaMaxima);
    }
}
