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

	def mision(self,radio):

		# 1.Calculamos cuantes cuentas del encoder debe pasar para recorrer el radio
		num_cuentas_radio= radio/self.cuenta_

		# 2.Movemos los motores sincronamete las cuentas necesarias
		self.syncMotor_.turn(80, num_cuentas_radio)
		time.sleep(1)

		# 3.Giramos hacia la izquierda
		self.syncMotor_.leader.weak_turn(80, self.cuentasGiro_)
		time.sleep(1)
		
		# 4.Desincronizamos motores y volvemos a syncronizarlos con un desfase de la rueda interior (que funcione mas lenta)
		self.syncMotor_.idle()
		self.syncMotor_= SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 10)

		# 5.Calculamos las cuentas necesarias del perimetro del circulo
		perimeter_circle= 2 * math.pi * radio
		num_cuentas_circle= perimeter_circle / self.cuenta_

		self.syncMotor_.turn(80, num_cuentas_circle*4)
		time.sleep(2)
		
		

		# 6. Hemos llegado al punto de inicio del circulo, por lo que desactivamos motores
		self.syncMotor_.idle()
		self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
		self.syncMotor_.leader.weak_turn(80, self.cuentasGiro_)
		time.sleep(1)
		self.syncMotor_.turn(80, num_cuentas_radio)
		time.sleep(1)

        # 7. Emitir sonido de finalizacion
		self.brick_.play_tone_and_wait(659, 500)

