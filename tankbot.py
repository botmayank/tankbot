"""
 Main script to drive tankbot by wiring modules

 Mayank Joneja (botmayank@gmail.com)
"""

from controller import Joystick
from motor_driver import MotorDriver

EPSILON_FWD = 0.05

def main():
    js = Joystick()
    md = MotorDriver()

    KEEP_DRIVING = True

    try:
        while KEEP_DRIVING:
            x, y = js.get_left_x_y()
            if y > EPSILON_FWD:
                md.go_forward()
            elif y < -EPSILON_FWD:
                md.go_back()
            else:
                md.halt()

            if x > EPSILON_FWD:
                md.turn_right()
            elif x < -EPSILON_FWD:
                md.turn_left()
            else:
                md.halt()

    except KeyboardInterrupt as e:
        KEEP_DRIVING = False
        md.halt()
        print("\nExiting...")


if __name__ == '__main__':
    main()