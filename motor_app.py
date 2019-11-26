import RPi.GPIO as GPIO

from motor import Motor

#add to app.py


@app.route('/open')
def opendoor():
    Motor.open_door()
    return(''),204
@app.route('/close')
def closedoor():
    Motor.close_door()
    return(''),204
