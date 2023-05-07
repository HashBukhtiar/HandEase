import time
from gpiozero import Motor, Button
from sensor_library import *
import matplotlib.pyplot as plt

def change_state(state):
    if state == "Open":
        return "Closed"
    else:
        return "Open"

def motor_activation(state, max_spin_duration):
    motor = Motor(forward=16,backward=12)
    start_time = time.time()
    
    if state == "Closed":
        motor.forward(speed=0.2)
        print("Motor Uncoiling")
    else:
        motor.backward(speed=0.2)
        print("Motor Recoiling")

    while True:
        if time.time() - start_time >= max_spin_duration:
            print("Motor Activated")
            break
            
    motor.stop()
    return change_state(state)

def check_button():
    button = Button(17)
    while True:
        if button.is_pressed:
            print("\nButton Pressed")
            break
    

def main():
    glove_state = "Closed"
    max_spin_time = 1

    while True:
        try:
            check_button()
            glove_state = motor_activation(glove_state, max_spin_time)
            print(f"Glove State: {glove_state}")
            time.sleep(1)
            glove_state = motor_activation(glove_state, max_spin_time*0.9)
            print(f"Glove State: {glove_state}")

        except KeyboardInterrupt:
            print("\nThank you")
            break

if __name__ == "__main__":  
    main()
    
    
    
