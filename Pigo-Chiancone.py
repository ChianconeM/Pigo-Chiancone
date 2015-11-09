from gopigo import *
import time

#Global variqavle on how close to something before stop
STOP_DIST = 50


class Pigo:

    #####
    #####  Basic status and methods
    #####

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 175,
              'rightspeed': 175, 'dist': 100}

    def __init__(self):
        print "I'm such a pigo."
        self.checkDist()

    def stop(self):
        self.status["isMoving"] = False
        print "Whoaa there."
        for x in range(3):
            stop()

    def fwd(self):
        self.status['isMoving'] = True
        print "lets roll"
        for x in range(3):
            fwd()

    def bwd(self):
        self.status['isMoving'] = True
        print "back it up"
        for x in range(3):
            bwd()

    def keepGoinng(self):
        if self.status['dist'] < STOP_DIST:
            return False
        else:
            return True

    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "I see something " + str(self.status['dist']) + "mm away"
        if not self.keepGoing():
            print "Emergency stop from check distance method"
            self.stop()

    #####
    #####  advanced methods
    #####

    def dance(self):
        print "I just want to dance"
        if self.keepGoinng():
            self.circleRight()
            self.circleLeft()
            self.shuffle()
            self.servoShake()
            self.blink()

#####
#####  main app starts here
#####

tina = Pigo()
while tina.keepGoing():
    tina.fwd()
    tina.sleep(2)
    tina.stop()

tina.stop()
