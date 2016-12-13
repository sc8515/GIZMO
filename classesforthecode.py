from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
from Tkinter import *
import RPi.GPIO as GPIO

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class StepperMotor:
    # recommended for auto-disabling motors on shutdown!
    def TurnOffMotors(self):
        # create a default object, no changes to I2C address or frequency
        mh = Adafruit_MotorHAT()
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    #def forward. to move the motor forwards by the amount of steps required to travel an interval.
    def Forwards(self):
        # create a default object, no changes to I2C address or frequency
        mh = Adafruit_MotorHAT()
        # 200 steps/rev, motor port #1
        myStepper = mh.getStepper(200, 1)
        # step velocity to a fixed number.
        myStepper.setSpeed(100) #even though the real speed is 30 rpm aprox.
        myStepper.step(170, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
    #def backward. to move the motor backwards by the amount of steps required to travel an interval.
    def Backwards(self):
        mh = Adafruit_MotorHAT()
        myStepper = mh.getStepper(200, 1)
        myStepper.setSpeed(100)
        myStepper.step(170, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

class ServoMotor:
    def Hit(self):
        GPIO.setmode(GPIO.BCM)
        servoPIN18 = 18
        move1 = 11
        move2 = 4
        GPIO.setup(servoPIN18, GPIO.OUT)

        # GPIO 18 als PWM mit 50Hz
        p18 = GPIO.PWM(servoPIN18, 50)
        # initial position
        p18.start(4)
        time.sleep(0.2)
        p18.ChangeDutyCycle(move1)
        time.sleep(0.2)
        p18.ChangeDutyCycle(move2)
        time.sleep(1)
    def TurnOff(self):
        GPIO.setmode(GPIO.BCM)
        servoPIN18 = 18
        GPIO.setup(servoPIN18, GPIO.OUT)
        # GPIO 18 als PWM mit 50Hz
        p18 = GPIO.PWM(servoPIN18, 50)
        p18.stop()
        GPIO.cleanup()