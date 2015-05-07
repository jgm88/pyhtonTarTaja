{"filter":false,"title":"gui_mision1_2.py","tooltip":"/mision1/gui_mision1_2.py","undoManager":{"stack":[[{"start":{"row":0,"column":0},"end":{"row":43,"column":16},"action":"remove","lines":["#!/usr/bin/env python","","from Tkinter import *","import mision1_2","","class Application:","","\tdef __init__(self, root):","","\t\tself.root= root","\t\tself.root.title= 'Mision 2'","\t\troot.resizable(width=FALSE, height=FALSE)","","\t\tself.panel = PanedWindow(self.root, orient=VERTICAL)","\t\tself.var= StringVar()","\t\tself.mac= StringVar()","\t\tself.radio= DoubleVar()","\t\tself.var.set(\"Usb\")","\t\tself.panel.add(Radiobutton(root, text=\"Usb\", variable=self.var, value=\"Usb\"))","\t\tself.panel.add(Radiobutton(root, text=\"Bluetooth\", variable=self.var, value=\"Bluetooth\"))","\t\t","\t\tself.panel.add(Label(self.root, justify=LEFT, text=\"Mac address, obligatoria si desea conexion Bluetooth\", font=\"Arial 12 bold\"))","\t\tself.panel.add(Entry(self.root, textvariable=self.mac))","","\t\tself.panel.add(Label(self.root, justify=LEFT, text=\"Especificar radio del circulo\", font=\"Arial 12 bold\"))","\t\tself.panel.add(Entry(self.root, textvariable=self.radio))","\t\t","\t\tself.panel.add(Button(root, text=\"Run mision\", command=self.mision))","\t\tself.panel.pack()","","\tdef mision(self):","\t\tif self.var.get()==\"Bluetooth\" and self.mac.get()==\"\":","\t\t\treturn","","\t\tif self.radio.get()==0.0:","\t\t\treturn","","\t\trobot= Robot(connect(self.var.get(), self.mac.get()))","\t\trobot.mision(self.radio.get())","","if __name__=='__main__':","\troot= Tk()","\tApplication(root)","\troot.mainloop()"],"id":2},{"start":{"row":0,"column":0},"end":{"row":51,"column":16},"action":"insert","lines":["#!/usr/bin/env python","","from Tkinter import *","from mision1_2 import *","","class Application:","","\tdef __init__(self, root):","","\t\tself.root= root","\t\tself.root.title= 'Mision 2'","\t\troot.resizable(width=FALSE, height=FALSE)","","\t\tself.panel = PanedWindow(self.root, orient=VERTICAL)","\t\tself.var= StringVar()","\t\tself.mac= StringVar()","\t\tself.radio= DoubleVar()","\t\tself.connect= IntVar()","\t\tself.var.set(\"Usb\")","\t\tself.connect.set(0)","\t\tself.panel.add(Radiobutton(root, text=\"Usb\", variable=self.var, value=\"Usb\"))","\t\tself.panel.add(Radiobutton(root, text=\"Bluetooth\", variable=self.var, value=\"Bluetooth\"))","\t\t","\t\tself.panel.add(Label(self.root, justify=LEFT, text=\"Mac address, obligatoria si desea conexion Bluetooth\", font=\"Arial 12 bold\"))","\t\tself.panel.add(Entry(self.root, textvariable=self.mac))","","\t\tself.panel.add(Label(self.root, justify=LEFT, text=\"Especificar radio del circulo\", font=\"Arial 12 bold\"))","\t\tself.panel.add(Entry(self.root, textvariable=self.radio))","\t\t","\t\tself.panel.add(Button(root, text=\"Run mision\", command=self.mision))","\t\tself.panel.pack()","","\tdef mision(self):","\t\tif self.var.get()==\"Bluetooth\" and self.mac.get()==\"\":","\t\t\treturn","","\t\tif self.radio.get()==0.0:","\t\t\treturn","","\t\ttry :","\t\t\tif self.connect.get()==0:","\t\t\t\tself.robot= Robot(connect(self.var.get(), self.mac.get()))","\t\t\t\tself.connect.set(1)","\t\t\telse:","\t\t\t\tself.robot.mision(self.radio.get())","\t\texcept ValueError:","\t\t\tprint \"Cannot connect to robot\"","","if __name__=='__main__':","\troot= Tk()","\tApplication(root)","\troot.mainloop()"]}],[{"start":{"row":0,"column":0},"end":{"row":51,"column":16},"action":"remove","lines":["#!/usr/bin/env python","","from Tkinter import *","from mision1_2 import *","","class Application:","","\tdef __init__(self, root):","","\t\tself.root= root","\t\tself.root.title= 'Mision 2'","\t\troot.resizable(width=FALSE, height=FALSE)","","\t\tself.panel = PanedWindow(self.root, orient=VERTICAL)","\t\tself.var= StringVar()","\t\tself.mac= StringVar()","\t\tself.radio= DoubleVar()","\t\tself.connect= IntVar()","\t\tself.var.set(\"Usb\")","\t\tself.connect.set(0)","\t\tself.panel.add(Radiobutton(root, text=\"Usb\", variable=self.var, value=\"Usb\"))","\t\tself.panel.add(Radiobutton(root, text=\"Bluetooth\", variable=self.var, value=\"Bluetooth\"))","\t\t","\t\tself.panel.add(Label(self.root, justify=LEFT, text=\"Mac address, obligatoria si desea conexion Bluetooth\", font=\"Arial 12 bold\"))","\t\tself.panel.add(Entry(self.root, textvariable=self.mac))","","\t\tself.panel.add(Label(self.root, justify=LEFT, text=\"Especificar radio del circulo\", font=\"Arial 12 bold\"))","\t\tself.panel.add(Entry(self.root, textvariable=self.radio))","\t\t","\t\tself.panel.add(Button(root, text=\"Run mision\", command=self.mision))","\t\tself.panel.pack()","","\tdef mision(self):","\t\tif self.var.get()==\"Bluetooth\" and self.mac.get()==\"\":","\t\t\treturn","","\t\tif self.radio.get()==0.0:","\t\t\treturn","","\t\ttry :","\t\t\tif self.connect.get()==0:","\t\t\t\tself.robot= Robot(connect(self.var.get(), self.mac.get()))","\t\t\t\tself.connect.set(1)","\t\t\telse:","\t\t\t\tself.robot.mision(self.radio.get())","\t\texcept ValueError:","\t\t\tprint \"Cannot connect to robot\"","","if __name__=='__main__':","\troot= Tk()","\tApplication(root)","\troot.mainloop()"],"id":3},{"start":{"row":0,"column":0},"end":{"row":51,"column":16},"action":"insert","lines":["#!/usr/bin/env python","","from Tkinter import *","from mision1_2 import *","","class Application:","","\tdef __init__(self, root):","","\t\tself.root= root","\t\tself.root.title= 'Mision 2'","\t\troot.resizable(width=FALSE, height=FALSE)","","\t\tself.panel = PanedWindow(self.root, orient=VERTICAL)","\t\tself.var= StringVar()","\t\tself.mac= StringVar()","\t\tself.radio= DoubleVar()","\t\tself.connect= IntVar()","\t\tself.var.set(\"Usb\")","\t\tself.connect.set(0)","\t\tself.panel.add(Radiobutton(root, text=\"Usb\", variable=self.var, value=\"Usb\"))","\t\tself.panel.add(Radiobutton(root, text=\"Bluetooth\", variable=self.var, value=\"Bluetooth\"))","\t\t","\t\tself.panel.add(Label(self.root, justify=LEFT, text=\"Mac address, obligatoria si desea conexion Bluetooth\", font=\"Arial 12 bold\"))","\t\tself.panel.add(Entry(self.root, textvariable=self.mac))","","\t\tself.panel.add(Label(self.root, justify=LEFT, text=\"Especificar radio del circulo\", font=\"Arial 12 bold\"))","\t\tself.panel.add(Entry(self.root, textvariable=self.radio))","\t\t","\t\tself.panel.add(Button(root, text=\"Run mision\", command=self.mision))","\t\tself.panel.pack()","","\tdef mision(self):","\t\tif self.var.get()==\"Bluetooth\" and self.mac.get()==\"\":","\t\t\treturn","","\t\tif self.radio.get()==0.0:","\t\t\treturn","","\t\ttry :","\t\t\tif self.connect.get()==0:","\t\t\t\tself.robot= Robot(connect(self.var.get(), self.mac.get()))","\t\t\t\tself.connect.set(1)","\t\t\telse:","\t\t\t\tself.robot.mision(self.radio.get())","\t\texcept ValueError:","\t\t\tprint \"Cannot connect to robot\"","","if __name__=='__main__':","\troot= Tk()","\tApplication(root)","\troot.mainloop()"]}]],"mark":1,"position":1},"ace":{"folds":[],"scrolltop":367,"scrollleft":0,"selection":{"start":{"row":39,"column":2},"end":{"row":46,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":25,"state":"start","mode":"ace/mode/python"}},"timestamp":1430984350077,"hash":"2e79a74825bcf7ee40199e3dc5218348c3406fb9"}