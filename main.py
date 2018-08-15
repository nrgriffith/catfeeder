import wiringpi
import time

# Number of rations to dispense
rations = 3

# Pin for servo data
pin = 18

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

wiringpi.pwmWrite(pin,50)

for x in range(rations):

    print "ration ", x

    for pulse in range(50, 250, 1):
        wiringpi.pwmWrite(18, pulse)
        time.sleep(0.01)
    for pulse in range(50, 250, -1):
        wiringpi.pwmWrite(pin, pulse)
        time.sleep(0.01)