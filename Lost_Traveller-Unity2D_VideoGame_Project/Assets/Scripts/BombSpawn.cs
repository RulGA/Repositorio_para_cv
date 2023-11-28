using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BombSpawn : MonoBehaviour
{
    
    private float waitSecondsToSpawn = 2f;            // Segundos entre spawn y spawn de bomba
    public AudioSource audioSource;                     
    public AudioClip explosionSound, bombAppearSound;
    public GameObject bombPrefab;
    // Start is called before the first frame update
    void Start()
    {
        // Ejecuta la corrutina que spawnea las bombas
        StartCoroutine("SpawnBombs");
    }

    // Update is called once per frame
    void Update()
    {
        audioSource = GetComponent<AudioSource>();
    }

    // De forma permanente se instanciará una bomba cada segundo y medio en la posición del spawn
    IEnumerator SpawnBombs()
    {
        while (true)
        {
            Instantiate(bombPrefab, transform.position, Quaternion.identity);

            yield return new WaitForSeconds(waitSecondsToSpawn);
        }
    }

    // Método que al ser llamado reproducirá el sonido de la explosión
    public void BombExplosion()
    {
        audioSource.PlayOneShot(explosionSound);
    }


}
