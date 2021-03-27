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
            js.get_event()
            x, y = js.get_left_x_y()
            if y < EPSILON_FWD and y > -EPSILON_FWD\
                  and x < EPSILON_FWD and x > -EPSILON_FWD:
                md.halt()
            # Forward/back
            if y > EPSILON_FWD:
                md.go_back()
            elif y < -EPSILON_FWD:
                md.go_forward()

            # Spot Left/Spot Right
            if x > EPSILON_FWD:
                md.turn_right()
            elif x < -EPSILON_FWD:
                md.turn_left()

            x_r, y_r = js.get_right_x_y()

            # 1 point Left/Right
            if x_r > EPSILON_FWD:
                md.turn_1pt_right()
            elif x_r < -EPSILON_FWD:
                md.turn_1pt_left()

    except KeyboardInterrupt as e:
        KEEP_DRIVING = False
        md.halt()
        print("\nExiting...")


if __name__ == '__main__':
    main()
