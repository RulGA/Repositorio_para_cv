
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextoTrigger : MonoBehaviour
{

        public Renderer m;


        private void Start()
        {
            m = GetComponent<Renderer>();

            m.enabled = false;


        }

        private void OnTriggerStay(Collider co)
        {
            if (co.gameObject.tag == "Player")
            {
                m.enabled = true;
            }

        }
        private void OnTriggerExit(Collider co)
        {
            m.enabled = false;

        }
    }