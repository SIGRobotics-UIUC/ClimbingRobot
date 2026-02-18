import RPi.GPIO as GPIO
from time import sleep

# Format: [Pin1, Pin2, PWM_Pin]
MOTORS = {
    1: [17, 27, 12], # Motor 1 (Front Left)
    2: [22, 23, 12], # Motor 2 (Front Right)
    3: [24, 25, 13], # Motor 3 (Rear Left)
    4: [26, 16, 13]  # Motor 4 (Rear Right)
}

class RobotDrive:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.pwms = {}
        
        for m_id, pins in MOTORS.items():
            GPIO.setup(pins[0], GPIO.OUT)
            GPIO.setup(pins[1], GPIO.OUT)
            GPIO.setup(pins[2], GPIO.OUT)
            
            if pins[2] not in self.pwms:
                p = GPIO.PWM(pins[2], 1000)
                p.start(0)
                self.pwms[pins[2]] = p

    def move_motor(self, motor_id, direction, speed):
        pins = MOTORS[motor_id]
        pwm = self.pwms[pins[2]]
        
        pwm.ChangeDutyCycle(speed)
        
        if direction == 'f':
            GPIO.output(pins[0], GPIO.LOW)
            GPIO.output(pins[1], GPIO.HIGH)
        elif direction == 'b':
            GPIO.output(pins[0], GPIO.HIGH)
            GPIO.output(pins[1], GPIO.LOW)
        else: # stop
            GPIO.output(pins[0], GPIO.LOW)
            GPIO.output(pins[1], GPIO.LOW)
            pwm.ChangeDutyCycle(0)

    def cleanup(self):
        GPIO.cleanup()

bot = RobotDrive()

try:
    print("Testing each motor individually for 2 seconds...")
    for i in range(1, 5):
        print(f"Testing Motor {i}")
        bot.move_motor(i, 'f', 50)
        sleep(2)
        bot.move_motor(i, 's', 0)
        sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    bot.cleanup()