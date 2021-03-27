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
            x_r, y_r = js.get_right_x_y()

            # Halt if Lstick in center
            if y < EPSILON_FWD and y > -EPSILON_FWD\
                  and x < EPSILON_FWD and x > -EPSILON_FWD:
                md.halt()

            # Back/forward
            if y > EPSILON_FWD: # y is positive when pushed down
                md.go_back()
                if x_r > EPSILON_FWD:
                    md.turn_1pt_back_right()
                elif x_r < -EPSILON_FWD:
                    md.turn_1pt_back_left()

            elif y < -EPSILON_FWD:
                md.go_forward()
                # 1 point Left/Right
                if x_r > EPSILON_FWD:
<<<<<<< HEAD
                    md.turn_1pt_back_left()
=======
                    md.turn_1pt_forward_right()
>>>>>>> ab1d7300045b77ada2c897eb62a5058ff87f8fb8
                elif x_r < -EPSILON_FWD:
                    md.turn_1pt_forward_left()

            # Spot Left/Spot Right
            if x > EPSILON_FWD:
                md.turn_right()
            elif x < -EPSILON_FWD:
                md.turn_left()


    except KeyboardInterrupt as e:
        KEEP_DRIVING = False
        md.halt()
        print("\nExiting...")


if __name__ == '__main__':
    main()
