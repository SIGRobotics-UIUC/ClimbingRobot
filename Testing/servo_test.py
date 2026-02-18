import time
from adafruit_servokit import ServoKit

# Initialize the ServoKit for 16 channels
# By default, the I2C address is 0x40
kit = ServoKit(channels=16)

def test_servo(channel, start_angle=0, end_angle=180):
    kit.servo[channel].angle = start_angle
    time.sleep(1)
    
    kit.servo[channel].angle = end_angle
    time.sleep(1)

try:
    test_servo(15)
except Exception as e:
    print(f"Error: {e}")