using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    
    public string creditos;
    public string controls;
    public string menu; 

    public void PlayGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }


    public void Credits()
    {
        SceneManager.LoadScene(creditos);
    }

    public void Controls()
    {
        SceneManager.LoadScene(controls);
    }
    public void Menu()
    {
        SceneManager.LoadScene(menu);
    }
    public void QuitGame()
    {
        Debug.Log("QUIT");
        Application.Quit();
    }
}
