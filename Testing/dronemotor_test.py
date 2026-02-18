import pigpio
import time

ESC_PIN = 17
pi = pigpio.pi()

def arm_esc():
    # 1000 is the standard "Zero Throttle" pulse width
    pi.set_servo_pulsewidth(ESC_PIN, 0)
    time.sleep(2)
    print("ESC Armed and Ready.")

def test_drone_motor():
    try:
        arm_esc()
        pi.set_servo_pulsewidth(ESC_PIN, 1000)
        time.sleep(2)
        pi.set_servo_pulsewidth(ESC_PIN, 1250)
        time.sleep(2)
    except KeyboardInterrupt:
        pi.set_servo_pulsewidth(ESC_PIN, 0)

test_drone_motor()
pi.set_servo_pulsewidth(ESC_PIN, 0)
pi.stop()