using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ActivarHingeJoint : MonoBehaviour
{
    public AudioClip clip;
    AudioSource fuenteaudio;
    HingeJoint hinge;

    void Start()
    {
        // Disable the spring on the HingeJoint component.
        hinge = GetComponent<HingeJoint>();
        JointMotor motor = hinge.motor;
        motor.force = 0;
        motor.targetVelocity = 0;
        motor.freeSpin = false;
        hinge.motor = motor;
    }
    public void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Player")
        {
            JointMotor motor = hinge.motor;
            motor.force = 20;
            motor.targetVelocity = 50;
            motor.freeSpin = true;
            hinge.motor = motor;
            fuenteaudio = GetComponent<AudioSource>();
            fuenteaudio.clip = clip;
            GetComponent<AudioSource>().PlayOneShot(clip);
        }


    }
}
