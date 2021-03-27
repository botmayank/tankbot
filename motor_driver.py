"""
 Motor driver class for RPi GPIO control talking to L298 driver similar to:
 https://components101.com/modules/l293n-motor-driver-module
 
 Motor Driver pin + Wire color + RPi Board GPIO Pin
    M1            |  Gray      |    Pin 7
    M2            |  Purple    |    Pin 11
    M3            |  Yellow    |    Pin 13
    M4            |  Green     |    Pin 15
    5V            |  Red       |    Pin 4 (5V)
    GND           |  Black     |    Pin 6 (GND)

    M1, M2 control left motor
    M3, M4 control right motor

 Mayank Joneja (botmayank@gmail.com)

"""

MOTOR_PINS = [7, 11, 13, 15]

import RPi.GPIO as GPIO
import os
from time import sleep

class MotorDriver():
    def __init__(self, motor_pins):
        self.motor_pins = motor_pins

        GPIO.setmode(GPIO.BOARD)
        print("Setting up motor controller pins...")
        GPIO.setup(self.motor_pins[0], GPIO.OUT)
        GPIO.setup(self.motor_pins[1], GPIO.OUT)
        GPIO.setup(self.motor_pins[2], GPIO.OUT)
        GPIO.setup(self.motor_pins[3], GPIO.OUT)

    def turn_left(self):
        print("Turning Left")
        GPIO.output(self.motor_pins[0], False)
        GPIO.output(self.motor_pins[1], True)
        GPIO.output(self.motor_pins[2], False)        
        GPIO.output(self.motor_pins[3], True)

    def turn_right(self):
        print("Turning Right")
        GPIO.output(self.motor_pins[0], True)
        GPIO.output(self.motor_pins[1], False)
        GPIO.output(self.motor_pins[2], True)        
        GPIO.output(self.motor_pins[3], False)

    def go_back(self):
        print("Going back")
        GPIO.output(self.motor_pins[0], True)
        GPIO.output(self.motor_pins[1], False)
        GPIO.output(self.motor_pins[2], False)        
        GPIO.output(self.motor_pins[3], True)

    def go_forward(self):
        print("Going forward")
        GPIO.output(self.motor_pins[0], False)
        GPIO.output(self.motor_pins[1], True)
        GPIO.output(self.motor_pins[2], True)        
        GPIO.output(self.motor_pins[3], False)

    def halt(self):
        print("Halting!")
        GPIO.output(self.motor_pins[0], False)
        GPIO.output(self.motor_pins[1], False)
        GPIO.output(self.motor_pins[2], False)        
        GPIO.output(self.motor_pins[3], False)



def main():
    m = MotorDriver(MOTOR_PINS)
    KEEP_DRIVING = True

    try:
        while KEEP_DRIVING:
            m.go_forward()
            sleep(1)
            m.go_back()
            sleep(1)
            m.turn_left()
            sleep(1)
            m.turn_right()
            sleep(1)
        m.halt()

    except KeyboardInterrupt as e:
        KEEP_DRIVING = False
        m.halt()
        print("Exiting...")
        GPIO.cleanup()

if __name__ == '__main__':
    main()
