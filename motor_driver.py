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

class Motor():
    def __init__(self, motor_pins, motor_type="left"):
        self.motor_pins = motor_pins
        self.motor_type = motor_type
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motor_pins[0], GPIO.OUT)
        GPIO.setup(self.motor_pins[1], GPIO.OUT)

    def forward(self):
        if self.motor_type == "left":
            GPIO.output(self.motor_pins[0], True)
            GPIO.output(self.motor_pins[1], False)
        elif self.motor_type == "right":
            GPIO.output(self.motor_pins[0], False)
            GPIO.output(self.motor_pins[1], True)

    def reverse(self):
        if self.motor_type == "left":
            GPIO.output(self.motor_pins[0], False)
            GPIO.output(self.motor_pins[1], True)
        elif self.motor_type == "right":
            GPIO.output(self.motor_pins[0], True)
            GPIO.output(self.motor_pins[1], False)

    def brake(self):        
        GPIO.output(self.motor_pins[0], False)
        GPIO.output(self.motor_pins[1], False)

    def hardbrake(self):
        GPIO.output(self.motor_pins[0], True)
        GPIO.output(self.motor_pins[1], True)

class MotorDriver():
    def __init__(self, motor_pins=MOTOR_PINS):
        self.motor_pins = motor_pins
        self.left_motor = Motor(motor_pins[2:4], motor_type="left")
        self.right_motor = Motor(motor_pins[:2], motor_type="right")
        print("Setting up motor controller pins...")

    def __del__(self):
        GPIO.cleanup()

    def turn_left(self):
        print("Turning Left")
        self.left_motor.reverse()
        self.right_motor.forward()

    def turn_1pt_forward_left(self):
        print("Turning 1pt fwd left")
        self.left_motor.brake()
        self.right_motor.forward()

    def turn_1pt_back_left(self):
        print("Turning 1pt back left")
        self.left_motor.brake()
        self.right_motor.reverse()
        
    def turn_right(self):
        print("Turning Right")
        self.left_motor.forward()
        self.right_motor.reverse()

    def turn_1pt_forward_right(self):
        print("Turning 1pt fwd right")
        self.right_motor.brake()
        self.left_motor.forward()

    def turn_1pt_back_right(self):
        print("Turning 1pt back right")
        self.right_motor.brake()
        self.left_motor.reverse()

    def go_back(self):
        print("Going back")
        self.left_motor.reverse()
        self.right_motor.reverse()

    def go_forward(self):
        print("Going forward")
        self.left_motor.forward()
        self.right_motor.forward()

    def halt(self):
        print("Halting!")
        self.left_motor.brake()
        self.right_motor.brake()

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
