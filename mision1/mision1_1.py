#!/usr/bin/env python

import nxt.bluesock
import nxt.locator
from nxt.motor import *
import math
import time

def connect(mode, mac):
    if(mode=="Usb"):
        return nxt.locator.find_one_brick()
    else:
        return nxt.bluesock.BlueSock(mac).connect()


class Robot:

    def __init__(self, brick, tam_encoder=360, wheel_diameter=5.6):
        
        self.brick_= brick
        self.separationBetweenWheels_= 13
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
        self.cuenta_= ((wheel_diameter*math.pi)/tam_encoder)

        # 1. Calculamos las cuentas que tendra que pasar para girar hacia un stolado.
        # Si suponemos que un giro sobre si mismo es de de radio separationBewteenWheels, un giro solo ocupara una
        # cuarta parte del perimetro de la circunferencia.
        turn_perimeter = (math.pi * 2.0 * self.separationBetweenWheels_) / 4.0
        self.cuentasGiro_ = turn_perimeter / self.cuenta_

    def moveTurnTime(self,t, power):

        current_time = time.time()
        self.syncMotor_.run(80*power)
        while (time.time() - current_time < t):
            pass;      
        self.syncMotor_.brake()

    def mision(self):


        # 1.Mover robot hacia delante 3 segundos
        self.moveTurnTime(3.0,1)
        time.sleep(1)
         
        # 2.Girar a la derecha
        self.syncMotor_.leader.weak_turn(80, self.cuentasGiro_)
        time.sleep(1)

        # 3.Mover robot hacia delante 2 segundos
        self.moveTurnTime(2.0,1)
        time.sleep(1)

        # 4. Girar a la izquierda
        self.syncMotor_.follower.weak_turn(80, self.cuentasGiro_)
        time.sleep(1)

        # 5. Moverse hacia delante 3 segundos
        self.moveTurnTime(3.0,1)
        time.sleep(1)

        self.syncMotor_.follower.weak_turn(80, self.cuentasGiro_)
        time.sleep(1)

        self.moveTurnTime(3.0,1)
        time.sleep(1)

        # 6. Dessincrnizacion motores
        self.syncMotor_.idle()

        # 7. Emitir sonido de finalizacion
        self.brick_.play_tone_and_wait(659, 500)

    def optional(self):

        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)

        self.moveTurnTime(1.0, -1)
        time.sleep(1)

        self.syncMotor_.follower.weak_turn(-80, self.cuentasGiro_)
        time.sleep(1)

        self.moveTurnTime(3.0,-1)
        time.sleep(1)

        self.syncMotor_.follower.weak_turn(-80, self.cuentasGiro_)
        time.sleep(1)

        self.moveTurnTime(2.0,-1)
        time.sleep(1)

        self.syncMotor_.leader.weak_turn(-80, self.cuentasGiro_)
        time.sleep(1)

        self.moveTurnTime(3.0,-1)
        time.sleep(1)



