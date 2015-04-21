{"filter":false,"title":"mision3_1.py","tooltip":"/mision3/mision3_1.py","undoManager":{"mark":12,"position":12,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.sensor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","def run(brick):","","    # 1.Encedemos sensor de luz","    sensor= Light(brick, PORT_3)","","    # 2.Encender Motor B y Motor C, sentido hacia adelante","    sync = SynchronizedMotors(Motor(brick, PORT_B),Motor(brick, PORT_C))","    sync.run(100, True)","","    # 3.Avanzar hasta encontrar linea negra","    while sensor.get_sample()>15:","        pass","    sync.brake()","","    # 4. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","def __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","","","",""]}]}],[{"group":"doc","deltas":[{"start":{"row":32,"column":0},"end":{"row":32,"column":3},"action":"remove","lines":["def"]},{"start":{"row":32,"column":0},"end":{"row":32,"column":1},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":32,"column":1},"end":{"row":32,"column":2},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":0},"end":{"row":37,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":35,"column":0},"end":{"row":36,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":34,"column":14},"end":{"row":35,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":0},"end":{"row":8,"column":47},"action":"insert","lines":["Programa una función en Matlab (mision3_1.m) en la que el robot avance","indefinidamente hasta que alcance una línea negra. Si encuentra algún","obstáculo, debe parar y cambiar de trayectoria."]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":9},"end":{"row":6,"column":45},"action":"remove","lines":["una función en Matlab (mision3_1.m) "]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["#"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":1},"end":{"row":8,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1429566798940,"hash":"4a8bac5d8b7ce2794052240ef67a8b5ed00e8f0d"}