using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraSoundController : MonoBehaviour
{
    private AudioSource audioSourceCamera;
    private GameObject heart1, heart2, heart3;
    private int totalLifes;
    private PlayerController scriptPlayer;
    public AudioClip damageSound, deathSound, gameOverSound;

    void Start()
    {
        audioSourceCamera = GetComponent<AudioSource>();
        scriptPlayer = FindObjectOfType<PlayerController>();
        heart1 = GameObject.Find("Heart1");
        heart2 = GameObject.Find("Heart2");
        heart3 = GameObject.Find("Heart3");
        
        
    }

    
    void Update()
    {
        totalLifes = scriptPlayer.totalLifes;
        // Nos muestra las vidas en pantalla
        switch (totalLifes)
        {
            case 0:
                heart1.SetActive(false);
                heart2.SetActive(false);
                heart3.SetActive(false);
                break;
            case 1:
                heart1.SetActive(true);
                heart2.SetActive(false);
                heart3.SetActive(false);
                break;
            case 2:
                heart1.SetActive(true);
                heart2.SetActive(true);
                heart3.SetActive(false);
                break;
            case 3:
                heart1.SetActive(true);
                heart2.SetActive(true);
                heart3.SetActive(true);
                
                break;
            default:
                break;
        }

    }

    // Decidimos que este sonido lo ejecutara la cámara ya que si el player muere, se destruye el objeto.

    // Sonido de daño
    public void DamageSound()
    {
        audioSourceCamera.PlayOneShot(damageSound);
    }

    // Sonido de muerte
    public void DeathSound()
    {
        audioSourceCamera.PlayOneShot(deathSound);
    }

    // Sonido de Game Over
    public void GameOverSound()
    {
        audioSourceCamera.PlayOneShot(gameOverSound);
    }

    
}
