{"filter":false,"title":"mision4.py","tooltip":"/mision4/mision4.py","ace":{"folds":[],"scrolltop":240,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":23,"state":"start","mode":"ace/mode/python"}},"hash":"925e9c477c86a1d9a3b593820ca32d941a1ae880","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":46,"column":0},"action":"remove","lines":["#!/usr/bin/env python","","import nxt.bluesock","import nxt.locator","from nxt.sensor import *","from nxt.motor import *","import time","","class Robot:","","    def __init__(self, brick, tam_encoder=360, wheel_diameter=5.6):","","        self.brick_= brick","        #self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)","        #self.arm_ = Motor(self.brick_, PORT_A)","        self.sensorUltraSound_= Ultrasonic(self.brick_, PORT_4)","","      #  self.separationBetweenWheels_= 14","       # self.cuenta_= ((encoder_*math.pi)/wheelDiameter_)","        #turn_perimeter = (math.pi * self.wheelDiameter_) / 4","        #self.cuentasGiro_ = turn_perimeter / self.cuenta_","","    def mision(self):","","        #1.Probar que mierdas devuelve cada funcion, falta probar los setters","        while True:","            print \"Distance: \", self.sensorUltraSound_.get_distance()","            print \"Measurament units: \", self.sensorUltraSound_.get_measurement_units()","            print \"Interval: \", self.sensorUltraSound_.get_interval()","            print \"All measuraments: \", self.sensorUltraSound_.get_all_measurements()","            time.sleep(1)","","","        # 3. Parar motores","       # self.syncMotor_.idle()","","        # 4. Opcional. Emitir sonido como finalizacion","        self.brick_.play_tone_and_wait(659, 500)","","","if __name__=='__main__':","    robot= Robot(nxt.locator.find_one_brick())","    #robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())","    robot.mision()","","",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":71,"column":0},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","import nxt.locator","from nxt.sensor import *","from nxt.motor import *","import time","import math","","class Robot:","","    def __init__(self, brick, tam_encoder=360, wheel_diameter=5.6):","","        self.brick_= brick","        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)","        self.arm_ = Motor(self.brick_, PORT_A)","        self.sensorUltraSound_= Ultrasonic(self.brick_, PORT_4)","","        self.separationBetweenWheels_= 14","        self.cuenta_= ((tam_encoder*math.pi)/wheel_diameter)","        turn_perimeter = (math.pi * 2.0 * self.separationBetweenWheels_) / 4.0","        self.cuentasGiro_ = turn_perimeter / self.cuenta_","","    def mision(self):","","        #1.Probar que mierdas devuelve cada funcion, falta probar los setters","        self.syncMotor_.leader.run(65)","        self.syncMotor_.follower.run(-65)","        minus= 255","        tm= time.time()","","        while time.time() - tm <=5.0:","            x= self.sensorUltraSound_.get_distance()","            if(x<minus):","                minus= x","        print \"vuelta dada\"","        print \"Min distance: \", minus","        self.syncMotor_.brake()","        ","        self.syncMotor_.leader.run(65)","        self.syncMotor_.follower.run(-65)","       ","        while self.sensorUltraSound_.get_distance()>=(minus+5):","            # print \"sensor:\", self.sensorUltraSound_.get_distance()","            pass;","        print \"Stop\"","        self.syncMotor_.brake()","","        print \"Arranco motores\"","        self.syncMotor_.run(70)","        # self.syncMotor_.leader.run(65)","        # self.syncMotor_.follower.run(65)","","        # self.syncMotor_.run(65)","        while self.sensorUltraSound_.get_distance()<=18:","            print \"ir al objeto\"","            pass;","        self.syncMotor_.brake()","","","","        # 4. Opcional. Emitir sonido como finalizacion","        self.brick_.play_tone_and_wait(659, 500)","","","if __name__=='__main__':","    robot= Robot(nxt.locator.find_one_brick())","    #robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())","    robot.mision()","","",""]}]]},"timestamp":1430984220000}