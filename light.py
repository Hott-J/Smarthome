import RPi.GPIO as GPIO

class Light(object):

    #pin number
    light_pin = 23
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(light_pin,GPIO.OUT,initial=GPIO.LOW)

    def light_on():
        GPIO.output(Light.light_pin,GPIO.HIGH)
        GPIO.cleanup()

    def light_off():
        GPIO.output(Light.light_pin,GPIO.LOW)
        GPIO.cleanup()
