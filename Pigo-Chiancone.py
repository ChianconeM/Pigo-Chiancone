from gopigo import *
import time

__author__ = 'Matt'


class Pigo:

    #####
    #####  Basic status and methods
    #####

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 175,
              'rightspeed': 175}

    def __init__(self):
        print "I'm such a pigo."

    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "I'm having trouble stopping"

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(.1)
            print "I can't seem to get going"

    #####
    #####  advanced methods
    #####

#####
#####  main app starts here
#####

bruh = Pigo()
bruh.fwd()
bruh.sleep(2)
bruh.stop()
