############## app.py 파일에 추가해 주세요.........

import RPi.GPIO as GPIO

from light import Light

app.route('/lighton')
def lightup():
    Light.light_on()
    return(''),204

app.route('/lightoff')
def lightoff():
    Light.light_off()
    return('').204
